const currentUrl = window.location.pathname;
const navItems = document.querySelectorAll('.nav_items a');

navItems.forEach(item => {
    if (item.getAttribute('href') === currentUrl) {
        item.classList.add('active');
    }
});

const menuBtn = document.getElementById('menuBtn');
const navItemsMenu = document.getElementById('navItemsMenu');
let menuOpen = false;

menuBtn.addEventListener('click', () => {
    if (!menuOpen) {
        menuBtn.classList.add('open');
        navItemsMenu.style.display = 'block';
        menuOpen = true;
    } else {
        menuBtn.classList.remove('open');
        navItemsMenu.style.display = 'none';
        menuOpen = false;
    }
});
