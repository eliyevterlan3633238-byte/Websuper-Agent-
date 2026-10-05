


    // globe.gl Real World Wireframe Globe
    const globeContainer = document.getElementById('globe-container');
    
    // CSS Variables handler
    const rootStyles = getComputedStyle(document.documentElement);
    const getThemeVar = (name, fallback) => {
        const val = rootStyles.getPropertyValue(name).trim();
        return val ? val.replace(/^"|"$/g, '') : fallback;
    };

    if (globeContainer) {
        // Force square dimensions for perfect sphere
        let width = globeContainer.clientWidth;
        let height = globeContainer.clientHeight;
        if (width === 0) width = 500;
        if (height === 0) height = 500;

        let globeColor = getThemeVar('--globe-color', '#124a26');
        let globeOutline = getThemeVar('--globe-outline', '#1c7541');

        const myGlobe = Globe({ animateIn: true })(globeContainer)
            .backgroundColor('rgba(0,0,0,0)') // Transparent background
            .showAtmosphere(true)
            .atmosphereColor(globeColor)
            .atmosphereAltitude(0.2)
            .width(width)
            .height(height);

        // Make the base globe a wireframe grid
        const globeMaterial = myGlobe.globeMaterial();
        if (globeMaterial && globeMaterial.color) {
            globeMaterial.color.set(globeColor); 
            globeMaterial.wireframe = true;
            globeMaterial.transparent = true;
            globeMaterial.opacity = 0.2;
        }

        // Fetch and draw real continent outlines
        fetch('https://raw.githubusercontent.com/vasturiano/globe.gl/master/example/datasets/ne_110m_admin_0_countries.geojson')
            .then(res => res.json())
            .then(countries => {
                myGlobe
                    .polygonsData(countries.features)
                    .polygonAltitude(0.01)
                    .polygonCapColor(() => 'rgba(0, 0, 0, 0)') // Transparent body
                    .polygonSideColor(() => 'rgba(0, 0, 0, 0)') // Transparent sides
                    .polygonStrokeColor(() => getThemeVar('--globe-outline', '#EFF25A'));
            });
// Auto-rotation & control settings
        myGlobe.controls().autoRotate = true;
        myGlobe.controls().autoRotateSpeed = 1.0;
        myGlobe.controls().enableZoom = false; // Prevent zooming

        // Handle resize to keep it perfectly spherical
        window.addEventListener('resize', () => {
            if (globeContainer) {
                const newSize = globeContainer.clientWidth;
                myGlobe.width(newSize);
                myGlobe.height(newSize);
            }
        });
// Listen for theme changes to update dynamic globe properties
        window.addEventListener('themeChanged', () => {
            const newGlobeColor = getThemeVar('--globe-color', '#124a26');
            const newGlobeOutline = getThemeVar('--globe-outline', '#1c7541');
            
            if (globeMaterial && globeMaterial.color) {
                globeMaterial.color.set(newGlobeColor);
            }
            myGlobe.atmosphereColor(newGlobeColor);
            myGlobe.polygonStrokeColor(() => newGlobeOutline);
        });
    }


    // Sub Hero Slider Initialize
    const subHeroSwiper = new Swiper('.subHeroSwiper', {
        slidesPerView: 3,
        spaceBetween: 0,
        loop: true,
        autoplay: {
            delay: 8000,
            disableOnInteraction: false,
        },
        effect: 'slide',
        navigation: {
            nextEl: '.sub-hero-next',
            prevEl: '.sub-hero-prev',
        },
        pagination: {
            el: '.sub-hero-pagination',
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
            },
            768: {
                slidesPerView: 2,
            },
            1024: {
                slidesPerView: 3,
            }
        }
    });
// Typewriter for Sub Hero
    let typedInstancesStarted = false;
    const typeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !typedInstancesStarted) {
                typedInstancesStarted = true;
                document.querySelectorAll('.sub-hero-content').forEach(content => {
                    const titleEl = content.querySelector('.typed-title');
                    const strings = JSON.parse(titleEl.getAttribute('data-strings'));
                    
                    new Typed(titleEl, {
                        strings: strings,
                        typeSpeed: 50,
                        backSpeed: 30,
                        backDelay: 2000,
                        loop: true,
                        cursorChar: '|'
                    });
const descEl = content.querySelector('.typed-desc');
                    const descStrings = JSON.parse(descEl.getAttribute('data-strings'));
                    
                    setTimeout(() => {
                        new Typed(descEl, {
                            strings: descStrings,
                            typeSpeed: 30,
                            backSpeed: 20,
                            backDelay: 2000,
                            loop: true,
                            cursorChar: ''
                        });
                        content.querySelector('.action-btn').style.opacity = '1';
                    }, 500);
                });
            }
        });
    }, { threshold: 0.3 });
    const subHeroSec = document.querySelector('.sub-hero-slider-section');
    if(subHeroSec) typeObserver.observe(subHeroSec);

    // Hero Swiper Init
    var heroSwiper = new Swiper('.heroSwiper', {
        effect: 'fade',
        fadeEffect: { crossFade: true },
        autoplay: {
            delay: 6000,
            disableOnInteraction: false,
        },
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
    });
// Particles.js (Digital Stars/Network)
    function initParticles() {
        if(typeof particlesJS !== 'undefined') {
            const pColor = getThemeVar('--particles-color', '#EFF25A');
            const pLineColor = getThemeVar('--particles-line-color', '#33B36B');
            const pOpacity = parseFloat(getThemeVar('--particles-opacity', '0.5'));
            const pLineOpacity = parseFloat(getThemeVar('--particles-line-opacity', '0.4'));

            // Destroy existing if re-initializing
            if (window.pJSDom && window.pJSDom.length > 0) {
                window.pJSDom[0].pJS.fn.vendors.destroypJS();
                window.pJSDom = [];
            }

            particlesJS("particles-js", {
                "particles": {
                    "number": { "value": 100, "density": { "enable": true, "value_area": 800 } },
                    "color": { "value": pColor },
                    "shape": { "type": "circle" },
                    "opacity": { "value": pOpacity, "random": true, "anim": { "enable": true, "speed": 1, "opacity_min": 0.1, "sync": false } },
                    "size": { "value": 3, "random": true },
                    "line_linked": { "enable": true, "distance": 150, "color": pLineColor, "opacity": pLineOpacity, "width": 1 },
                    "move": { "enable": true, "speed": 4, "direction": "none", "random": true, "straight": false, "out_mode": "out", "bounce": false }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": { "onhover": { "enable": true, "mode": "repulse" }, "onclick": { "enable": true, "mode": "push" }, "resize": true },
                    "modes": { "repulse": { "distance": 100, "duration": 0.4 }, "push": { "particles_nb": 4 } }
                },
                "retina_detect": true
            });
        }
    }
    initParticles();
    window.addEventListener('themeChanged', initParticles);
// Counter Animation
    const counters = document.querySelectorAll('.counter');
    const speed = 200; 

    ScrollTrigger.create({
        trigger: '#stats',
        start: 'top 80%',
        onEnter: () => {
            counters.forEach(counter => {
                const animate = () => {
                    const target = +counter.getAttribute('data-target');
                    const count = +counter.innerText;
                    const increment = target / speed;
                    if (count < target) {
                        counter.innerText = Math.ceil(count + increment);
                        setTimeout(animate, 10);
                    } else {
                        counter.innerText = target;
                    }
                }
                animate();
            });
        },
        once: true
    });


