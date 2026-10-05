





        // Navbar Scrolled Effect with requestAnimationFrame and passive true
        let isScrolling = false;
        window.addEventListener('scroll', () => {
            if (!isScrolling) {
                window.requestAnimationFrame(() => {
                    const navbar = document.getElementById('navbar');
                    if (window.scrollY > 50) {
                        navbar.classList.add('scrolled');
                    } else {
                        navbar.classList.remove('scrolled');
                    }
                    isScrolling = false;
                });
                isScrolling = true;
            }
        }, { passive: true });

        // Theme Toggle Logic
        const themeToggle = document.getElementById('themeToggle');
        const themeIcon = document.getElementById('themeIcon');
        
        // Check local storage for theme
        const currentTheme = localStorage.getItem('theme') || 'dark';
        document.documentElement.setAttribute('data-theme', currentTheme);

        themeToggle.addEventListener('click', () => {
            let theme = document.documentElement.getAttribute('data-theme');
            let newTheme = theme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            // Dispatch event for dynamic components like Globe
            window.dispatchEvent(new Event('themeChanged'));
        });

        // Initialize AOS
        AOS.init({
            duration: 800,
            once: true
        });

        // Register ScrollTrigger
        gsap.registerPlugin(ScrollTrigger);

        // Vanilla JS Performant Parallax for .parallax-bg
        (function() {
            if (window.innerWidth < 768) return; // Disable on mobile

            const parallaxSections = document.querySelectorAll('.parallax-bg');
            if (parallaxSections.length === 0) return;

            // Setup layers
            parallaxSections.forEach(section => {
                const bgImg = section.style.backgroundImage || window.getComputedStyle(section).backgroundImage;
                if (bgImg && bgImg !== 'none' && bgImg !== '') {
                    section.style.backgroundImage = 'none';
                    section.style.position = 'relative';
                    section.style.overflow = 'hidden';

                    const layer = document.createElement('div');
                    layer.classList.add('parallax-layer');
                    layer.style.backgroundImage = bgImg;
                    layer.style.position = 'absolute';
                    layer.style.top = '-20%';
                    layer.style.left = '0';
                    layer.style.width = '100%';
                    layer.style.height = '140%';
                    layer.style.backgroundSize = 'cover';
                    layer.style.backgroundPosition = 'center';
                    layer.style.zIndex = '0';
                    layer.style.pointerEvents = 'none';
                    
                    Array.from(section.children).forEach(child => {
                        const style = window.getComputedStyle(child);
                        if (style.position === 'static') {
                            child.style.position = 'relative';
                        }
                        if (style.zIndex === 'auto' || style.zIndex === '0') {
                            child.style.zIndex = '1';
                        }
                    });

                    section.insertBefore(layer, section.firstChild);
                }
            });

            // Scroll Logic with requestAnimationFrame and Viewport Check
            let isParallaxScrolling = false;
            
            function updateParallax() {
                const viewportCenter = window.innerHeight / 2;
                
                parallaxSections.forEach(section => {
                    const rect = section.getBoundingClientRect();
                    // if not in viewport, skip calculation to save performance
                    if (rect.bottom < 0 || rect.top > window.innerHeight) {
                        const layer = section.querySelector('.parallax-layer');
                        if (layer) layer.style.willChange = 'auto';
                        return;
                    }
                    
                    const layer = section.querySelector('.parallax-layer');
                    if (layer) {
                        layer.style.willChange = 'transform';
                        const sectionCenter = rect.top + rect.height / 2;
                        // Move background opposite to scroll direction
                        const offset = (sectionCenter - viewportCenter) * 0.2; 
                        layer.style.transform = `translateY(${offset}px)`;
                    }
                });
            }

            window.addEventListener('scroll', () => {
                if (!isParallaxScrolling) {
                    window.requestAnimationFrame(() => {
                        updateParallax();
                        isParallaxScrolling = false;
                    });
                    isParallaxScrolling = true;
                }
            }, { passive: true });

            // Initial calculation so it's correct before any scroll
            updateParallax();
        })();
    

