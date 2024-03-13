const currentUrl = window.location.pathname;
const navItems = document.querySelectorAll('.nav_items a');

navItems.forEach(item => {
    if (item.getAttribute('href') === currentUrl) {
        item.classList.add('active');
    }
});
