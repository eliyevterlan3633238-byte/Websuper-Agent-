/**
 * ==========================================================================
 * WebSuper Agency - High-Performance Multi-App Parallax Engine
 * ==========================================================================
 */

(function () {
    'use strict';

    // Check prefers-reduced-motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) return;

    // Wait until DOM is ready
    function initParallax() {
        const isMobile = window.innerWidth < 768;

        // ==================================================================
        // 1. DYNAMIC BACKGROUND PARALLAX FOR SECTIONS & HEADERS
        // ==================================================================
        const parallaxSections = document.querySelectorAll('.parallax-bg:not(.final-cta), .page-header:not(.final-cta)');
        const bgLayerList = [];

        parallaxSections.forEach(section => {
            if (section.classList.contains('final-cta')) return;
            // Avoid double init
            if (section.querySelector('.parallax-bg-layer-inner')) {
                const existingLayer = section.querySelector('.parallax-bg-layer-inner');
                const speed = parseFloat(section.getAttribute('data-parallax-speed')) || 0.35;
                bgLayerList.push({ section, layer: existingLayer, speed });
                return;
            }

            // Get background image from inline style or computed style
            const style = window.getComputedStyle(section);
            let bgImg = section.style.backgroundImage || style.backgroundImage;

            if (bgImg && bgImg !== 'none' && bgImg !== '') {
                // Ensure section is positioned relative and overflow hidden
                section.classList.add('parallax-bg');
                section.style.position = 'relative';
                section.style.overflow = 'hidden';
                section.style.backgroundImage = 'none';

                // Create dedicated inner layer for hardware-accelerated movement
                const layer = document.createElement('div');
                layer.className = 'parallax-bg-layer-inner';
                layer.style.backgroundImage = bgImg;

                // Ensure sibling content elements stay above the layer
                Array.from(section.children).forEach(child => {
                    if (child.classList.contains('header-overlay') || 
                        child.classList.contains('cta-overlay') || 
                        child.classList.contains('sub-hero-overlay') ||
                        child.classList.contains('parallax-bg-layer-inner')) {
                        return;
                    }
                    const childStyle = window.getComputedStyle(child);
                    if (childStyle.position === 'static') {
                        child.style.position = 'relative';
                    }
                    if (childStyle.zIndex === 'auto' || childStyle.zIndex === '0') {
                        child.style.zIndex = '2';
                    }
                });

                section.insertBefore(layer, section.firstChild);

                const speed = parseFloat(section.getAttribute('data-parallax-speed')) || 0.35;
                bgLayerList.push({ section, layer, speed });
            }
        });

        // ==================================================================
        // 2. SUB-HERO SLIDER PARALLAX (Home page cards)
        // ==================================================================
        const subHeroLayers = document.querySelectorAll('.parallax-bg-layer');

        // ==================================================================
        // 3. FLOATING CONTENT & CARD PARALLAX
        // ==================================================================
        const floatElements = document.querySelectorAll('.parallax-float, .gsap-parallax, [data-depth]');
        const floatList = [];

        floatElements.forEach(el => {
            const depth = parseFloat(el.getAttribute('data-depth')) || 0.12;
            floatList.push({ el, depth });
        });

        // ==================================================================
        // 4. MAIN SCROLL RENDER LOOP (60FPS via requestAnimationFrame)
        // ==================================================================
        let ticking = false;

        function updateAllParallax() {
            const windowHeight = window.innerHeight;
            const viewportCenter = windowHeight / 2;

            // A) Background Layers
            for (let i = 0; i < bgLayerList.length; i++) {
                const item = bgLayerList[i];
                const rect = item.section.getBoundingClientRect();

                // Viewport culling
                if (rect.bottom >= -50 && rect.top <= windowHeight + 50) {
                    let scrollProgress = (windowHeight - rect.top) / (windowHeight + rect.height);
                    scrollProgress = Math.max(0, Math.min(1, scrollProgress));
                    const maxTranslate = 15; // Safe margin for height:160% top:-30%
                    const yPos = -maxTranslate + (scrollProgress * (maxTranslate * 2));
                    item.layer.style.transform = `translate3d(0, ${yPos.toFixed(2)}%, 0)`;
                }
            }

            // B) Sub-hero Cards (on Home page)
            const currentSubHeroLayers = document.querySelectorAll('.parallax-bg-layer');
            if (currentSubHeroLayers.length > 0 && !isMobile) {
                for (let i = 0; i < currentSubHeroLayers.length; i++) {
                    const layer = currentSubHeroLayers[i];
                    const parent = layer.parentElement;
                    const rect = parent.getBoundingClientRect();

                    if (rect.bottom >= -50 && rect.top <= windowHeight + 50) {
                        let scrollProgress = (windowHeight - rect.top) / (windowHeight + rect.height);
                        scrollProgress = Math.max(0, Math.min(1, scrollProgress));
                        const maxTranslate = 15; // 15% visible movement (safe for 160% height)
                        const yPos = -maxTranslate + (scrollProgress * (maxTranslate * 2));
                        layer.style.transform = `translate3d(0, ${yPos.toFixed(2)}%, 0)`;
                    }
                }
            }

            // C) Floating Elements & Cards
            if (!isMobile) {
                for (let i = 0; i < floatList.length; i++) {
                    const item = floatList[i];
                    const rect = item.el.getBoundingClientRect();

                    if (rect.bottom >= -100 && rect.top <= windowHeight + 100) {
                        const elemCenter = rect.top + rect.height / 2;
                        // Move element according to depth
                        const offset = (elemCenter - viewportCenter) * item.depth;
                        item.el.style.transform = `translate3d(0, ${offset.toFixed(1)}px, 0)`;
                    }
                }
            }

            ticking = false;
        }

        function requestTick() {
            if (!ticking) {
                window.requestAnimationFrame(updateAllParallax);
                ticking = true;
            }
        }

        // Attach scroll & resize listeners
        window.addEventListener('scroll', requestTick, { passive: true });
        window.addEventListener('resize', () => {
            requestTick();
        }, { passive: true });

        // Initial setup
        updateAllParallax();

        // ==================================================================
        // 5. INTERACTIVE 3D TILT EFFECT ON CARDS
        // ==================================================================
        if (!isMobile) {
            const tiltCards = document.querySelectorAll(
                '.tilt-card, .portfolio-item, .blog-card, .contact-info-card, .value-card, .service-card, .pricing-card, .team-card, .sub-hero-card'
            );

            tiltCards.forEach(card => {
                let bounds = null;
                let rafId = null;

                card.addEventListener('mouseenter', () => {
                    if (card.classList.contains('map-interactive-mode')) return;
                    bounds = card.getBoundingClientRect();
                    card.style.transition = 'transform 0.08s ease-out, box-shadow 0.3s ease';
                });

                card.addEventListener('mousemove', (e) => {
                    if (card.classList.contains('map-interactive-mode')) return;
                    if (!bounds) bounds = card.getBoundingClientRect();
                    const mouseX = e.clientX - bounds.left;
                    const mouseY = e.clientY - bounds.top;
                    
                    const xPct = Math.max(-1, Math.min(1, (mouseX / bounds.width - 0.5) * 2));
                    const yPct = Math.max(-1, Math.min(1, (mouseY / bounds.height - 0.5) * 2));

                    const rotateX = (-yPct * 7).toFixed(2); // Max 7 deg
                    const rotateY = (xPct * 7).toFixed(2);

                    if (rafId) cancelAnimationFrame(rafId);
                    rafId = requestAnimationFrame(() => {
                        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.015, 1.015, 1.015)`;
                    });
                });

                card.addEventListener('mouseleave', () => {
                    if (rafId) cancelAnimationFrame(rafId);
                    card.style.transition = 'transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.4s ease';
                    card.style.transform = ''; /* Clear inline transform to restore CSS default */
                    bounds = null;
                });
            });
        }

        // ==================================================================
        // 6. REVEAL-ON-SCROLL OBSERVER
        // ==================================================================
        const revealElements = document.querySelectorAll('.reveal-on-scroll');
        if (revealElements.length > 0) {
            const revealObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const target = entry.target;
                        const delay = parseInt(target.getAttribute('data-delay')) || 0;
                        setTimeout(() => {
                            target.classList.add('is-revealed');
                        }, delay);
                        observer.unobserve(target);
                    }
                });
            }, { threshold: 0.15 });

            revealElements.forEach(el => revealObserver.observe(el));
        }
    }

    // Initialize as soon as DOM is interactive, and re-check after images load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initParallax);
    } else {
        initParallax();
    }

    window.addEventListener('load', initParallax);
})();
