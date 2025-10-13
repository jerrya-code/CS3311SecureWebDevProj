document.addEventListener('DOMContentLoaded', () => {
    const gallery = document.querySelector('.carousel-slide');
    const leftArrow = document.querySelector('.arrow-left');
    const rightArrow = document.querySelector('.arrow-right');

    leftArrow.addEventListener('click', () => {
        const scrollAmount = gallery.querySelector('img').offsetWidth + 15; //15px margin
        gallery.scrollLeft -= scrollAmount;
    });

    rightArrow.addEventListener('click', () => {
        const scrollAmount = gallery.querySelector('img').offsetWidth + 15; //15px margin
        gallery.scrollLeft += scrollAmount;
    });
});
