document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.querySelector('#theme-toggle');
    const body = document.body;

    themeToggle.addEventListener('change', function() {
        if (this.checked) {
            body.classList.add('dark-theme');
            toggleEarthAnimation(true);
        } else {
            body.classList.remove('dark-theme');
            toggleEarthAnimation(false);
        }
    });

    function toggleEarthAnimation(enable) {
        const earth = document.querySelector('.earth');
        if (enable) {
            earth.style.animation = 'rotateEarthDark 10s linear infinite';
        } else {
            earth.style.animation = 'rotateEarth 10s linear infinite';
        }
    }
});
