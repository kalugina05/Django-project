document.addEventListener("DOMContentLoaded", function() {
    const menuLinks = document.querySelectorAll('.menu_link');
    const currentPath = window.location.pathname;

    menuLinks.forEach(link => {
        const linkPath = link.getAttribute('href');

        if (linkPath === currentPath) {
            link.classList.add('active');
        }
    });
});

document.querySelectorAll('.toggle-header').forEach(header => {
    header.addEventListener('click', () => {
        const list = header.nextElementSibling;
        list.classList.toggle('toggle-list');
        header.classList.toggle('active');
        if (list.style.display === "block") {
            list.style.display = "none";
        } else {
            list.style.display = "block";
        }
    });
});