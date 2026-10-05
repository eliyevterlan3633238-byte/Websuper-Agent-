document.addEventListener('DOMContentLoaded', function() {
    const wsHelperForm = document.getElementById('wsHelperForm');
    const wsHelperHistory = document.getElementById('wsHelperHistory');
    const chatInput = document.getElementById('wsHelperMessage');
    const submitBtn = document.querySelector('.chat-submit-btn');
    
    const nameScreen = document.getElementById('wsHelperNameScreen');
    const chatArea = document.getElementById('wsHelperChatArea');
    const nameInput = document.getElementById('wsCustomerNameInput');
    const nameError = document.getElementById('wsNameError');
    const startChatBtn = document.getElementById('wsStartChatBtn');

    let customerName = localStorage.getItem('wsCustomerName');

    if (!customerName) {
        if (nameScreen) nameScreen.style.display = 'flex';
        if (chatArea) chatArea.style.display = 'none';
    } else {
        if (nameScreen) nameScreen.style.display = 'none';
        if (chatArea) chatArea.style.display = 'flex';
    }

    if (startChatBtn) {
        startChatBtn.addEventListener('click', function() {
            const val = nameInput.value.trim().replace(/\s+/g, ' ');
            const words = val.split(' ');
            if (val.length < 2 || words.length < 2 || val.length > 60) {
                nameError.style.visibility = 'visible';
                return;
            }
            nameError.style.visibility = 'hidden';
            customerName = val;
            localStorage.setItem('wsCustomerName', val);
            
            if (nameScreen) nameScreen.style.display = 'none';
            if (chatArea) chatArea.style.display = 'flex';
            
            if (chatSocket && chatSocket.readyState === WebSocket.OPEN) {
                chatSocket.send(JSON.stringify({
                    'action': 'start',
                    'name': customerName
                }));
            }
        });
    }

    if (nameInput) {
        nameInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                if (startChatBtn) startChatBtn.click();
            }
        });
    }

    if (!wsHelperForm) return;

    let chatSocket = null;
    let reconnectTimer = null;
    let wsScheme = window.location.protocol === "https:" ? "wss" : "ws";

    // Configuration from json_script
    const configEl = document.getElementById('chat-config');
    const config = configEl ? JSON.parse(configEl.textContent) : {
        initialMsg: 'Salam! Sizə necə kömək edə bilərik?',
        placeholderNormal: 'Mesajınızı yazın...',
        placeholderConnecting: 'Bağlanılır...'
    };

    function addMessageToUI(type, text, messageId = null, animate = false) {
        const msgDiv = document.createElement('div');
        let cssClass = (type === 'customer' || type === 'user') ? 'user' : type;
        msgDiv.className = `ws-helper-message ${cssClass}`;
        if (messageId) {
            msgDiv.dataset.id = messageId;
        }
        
        let html = '';
        if (cssClass === 'bot' || cssClass === 'operator') {
            html += '<div class="avatar"><i class="fas fa-headset"></i></div>';
        }
        
        let bubbleHtml = `<div class="bubble">${text}</div>`;
        
        // Add edit/delete buttons for user
        if (cssClass === 'user') {
            bubbleHtml = `
            <div style="display: flex; align-items: center; justify-content: flex-end; gap: 12px; width: 100%;">
                <div class="msg-actions" style="display: flex; gap: 15px; font-size: 16px; color: #888;">
                    <i class="fas fa-edit" onclick="editCustomerMessage(${messageId}, this)" style="cursor:pointer;" title="Redaktə et"></i>
                    <i class="fas fa-trash" onclick="deleteCustomerMessage(${messageId})" style="cursor:pointer;" title="Sil"></i>
                </div>
                ${bubbleHtml}
            </div>
            `;
            html += bubbleHtml;
        } else {
            html += `<div style="display: flex; flex-direction: column;">${bubbleHtml}</div>`;
        }
        
        msgDiv.innerHTML = html;
        wsHelperHistory.appendChild(msgDiv);
        
        if (animate) {
            msgDiv.style.opacity = '0';
            msgDiv.style.transform = 'translateY(10px)';
            setTimeout(() => {
                msgDiv.style.transition = 'all 0.3s ease';
                msgDiv.style.opacity = '1';
                msgDiv.style.transform = 'translateY(0)';
            }, 10);
        }
        
        wsHelperHistory.scrollTop = wsHelperHistory.scrollHeight;
    }

    function renderHistory() {
        wsHelperHistory.innerHTML = '';
        const historyEl = document.getElementById('chat-history');
        const messages = historyEl ? JSON.parse(historyEl.textContent || '[]') : [];
        
        if (messages.length === 0) {
            addMessageToUI('bot', config.initialMsg);
        } else {
            messages.forEach(msg => {
                addMessageToUI(msg.type, msg.text, msg.id);
            });
        }
    }

    function connectChatSocket() {
        const idEl = document.getElementById('chat-id');
        if (!idEl) return;
        
        const chatId = JSON.parse(idEl.textContent);
        if (!chatId) return;

        chatSocket = new WebSocket(wsScheme + '://' + window.location.host + '/ws/chat/' + chatId + '/?source=widget');

        chatSocket.onopen = function(e) {
            if (chatInput) {
                chatInput.disabled = false;
                chatInput.placeholder = config.placeholderNormal;
            }
            if (submitBtn) submitBtn.disabled = false;
            
            if (reconnectTimer) {
                clearTimeout(reconnectTimer);
                reconnectTimer = null;
            }
            
            if (customerName) {
                chatSocket.send(JSON.stringify({
                    'action': 'start',
                    'name': customerName
                }));
            }
        };

        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            if (data.action === 'message') {
                const popup = document.getElementById('wsHelperPopup');
                if (popup && !popup.classList.contains('active') && data.sender_type !== 'customer') {
                    let btn = document.getElementById('wsHelperBtn');
                    if (btn) {
                        let badge = document.getElementById('wsHelperBadgeUnread');
                        if (!badge) {
                            badge = document.createElement('span');
                            badge.id = 'wsHelperBadgeUnread';
                            badge.style.cssText = 'position: absolute; top: -5px; right: -5px; background: red; color: white; border-radius: 50%; width: 20px; height: 20px; font-size: 12px; display: flex; align-items: center; justify-content: center; font-weight: bold;';
                            badge.textContent = '1';
                            btn.appendChild(badge);
                        } else {
                            badge.textContent = parseInt(badge.textContent) + 1;
                        }
                    }
                }
                
                addMessageToUI(data.sender_type, data.message, data.message_id, true);
            } else if (data.action === 'delete_message') {
                const msgDiv = wsHelperHistory.querySelector(`.ws-helper-message[data-id="${data.message_id}"]`);
                if (msgDiv) {
                    msgDiv.remove();
                }
            } else if (data.action === 'edit_message') {
                const msgDiv = wsHelperHistory.querySelector(`.ws-helper-message[data-id="${data.message_id}"]`);
                if (msgDiv) {
                    const bubble = msgDiv.querySelector('.bubble');
                    if (bubble) bubble.textContent = data.message;
                }
            }
        };

        chatSocket.onclose = function(e) {
            if (chatInput) {
                chatInput.disabled = true;
                chatInput.placeholder = config.placeholderConnecting;
            }
            if (submitBtn) submitBtn.disabled = true;
            
            reconnectTimer = setTimeout(connectChatSocket, 3000);
        };
    }

    renderHistory();
    connectChatSocket();
    
    const supportBtn = document.getElementById('wsHelperBtn');
    if (supportBtn) {
        supportBtn.addEventListener('click', function() {
            let badge = document.getElementById('wsHelperBadgeUnread');
            if (badge) badge.remove();
        });
    }

    wsHelperForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const userText = chatInput.value.trim();
        if (!userText || !chatSocket || chatSocket.readyState !== WebSocket.OPEN) return;
        
        chatSocket.send(JSON.stringify({
            'action': 'message',
            'message': userText
        }));
        
        chatInput.value = '';
    });
    
    window.deleteCustomerMessage = function(msgId) {
        if (!msgId) return;
        if (confirm('Mesajınızı silmək istədiyinizə əminsiniz?')) {
            chatSocket.send(JSON.stringify({
                'action': 'delete_message',
                'message_id': msgId
            }));
        }
    };
    
    window.editCustomerMessage = function(msgId, btnEl) {
        if (!msgId) return;
        const msgDiv = btnEl.closest('.ws-helper-message');
        const bubble = msgDiv.querySelector('.bubble');
        const currentText = bubble.textContent;
        
        const newText = prompt('Mesajınızı redaktə edin:', currentText);
        if (newText !== null && newText.trim() !== '' && newText.trim() !== currentText) {
            chatSocket.send(JSON.stringify({
                'action': 'edit_message',
                'message_id': msgId,
                'message': newText.trim()
            }));
        }
    };

    window.startNewChat = function() {
        if (confirm('Yeni söhbətə başlamaq istədiyinizə əminsiniz? Köhnə mesajlar bu ekrandan silinəcək.')) {
            localStorage.removeItem('wsCustomerName');
            fetch('/admin/chat/reset/', {
                method: 'GET'
            }).then(() => {
                window.location.reload();
            }).catch(() => {
                window.location.reload();
            });
        }
    };
});
