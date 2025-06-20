const darkModeToggle = document.getElementById('darkModeToggle');
        const modeIcon = document.getElementById('modeIcon');
        const body = document.body;

        // Check for saved theme preference or default to light mode
        const currentTheme = localStorage.getItem('theme') || 'light';
        if (currentTheme === 'dark') {
            body.classList.add('dark');
            modeIcon.classList.remove('fa-moon');
            modeIcon.classList.add('fa-sun');
        }

        darkModeToggle.addEventListener('click', () => {
            body.classList.toggle('dark');
            
            // Update icon with animation
            modeIcon.style.transform = 'scale(0)';
            
            setTimeout(() => {
                if (body.classList.contains('dark')) {
                    modeIcon.classList.remove('fa-moon');
                    modeIcon.classList.add('fa-sun');
                    localStorage.setItem('theme', 'dark');
                } else {
                    modeIcon.classList.remove('fa-sun');
                    modeIcon.classList.add('fa-moon');
                    localStorage.setItem('theme', 'light');
                }
                modeIcon.style.transform = 'scale(1)';
            }, 150);
        });

        // Add some interactive feedback
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                link.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    link.style.transform = '';
                }, 150);
            });
        });