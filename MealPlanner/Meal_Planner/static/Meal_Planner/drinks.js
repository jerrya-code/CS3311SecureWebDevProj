document.addEventListener('DOMContentLoaded', () => {
    const carouselSlide = document.querySelector('.carousel-slide');
    if (!carouselSlide) return;
    const carouselContainer = document.querySelector('.carousel-container');

    let cards = document.querySelectorAll('.card');
    if (cards.length === 0) return; // nothing to do

    const leftArrow = document.querySelector('.arrow-left');
    const rightArrow = document.querySelector('.arrow-right');

    // clones for infinite effect
    const firstClone = cards[0].cloneNode(true);
    const lastClone = cards[cards.length - 1].cloneNode(true);
    firstClone.id = 'first-clone';
    lastClone.id = 'last-clone';

    carouselSlide.appendChild(firstClone);
    carouselSlide.insertBefore(lastClone, cards[0]);

    // refresh lists and compute sizes AFTER clones inserted
    let allCards = document.querySelectorAll('.card');
    let currentIndex = 1; // start at first real card
    let gap = 40; // must match CSS gap
    let cardWidth = allCards[1].offsetWidth; // index 1 is first real card (0 is lastClone)

    function computeOffsetForIndex(index) {
        // Robust approach: measure the card and the container in viewport space,
        // compute how far the card must move so its center matches container center.
        const targetCard = allCards[index] || allCards[1];
        if (!carouselContainer || !targetCard) return 0;

        // Temporarily remove transform so we measure the slide/card in their natural positions.
        const prevTransition = carouselSlide.style.transition;
        const prevTransform = carouselSlide.style.transform;
        carouselSlide.style.transition = 'none';
        carouselSlide.style.transform = 'none';

        const containerRect = carouselContainer.getBoundingClientRect();
        const cardRect = targetCard.getBoundingClientRect();

        // desired left coordinate for the card so its center aligns with container center
        const desiredLeft = containerRect.left + (containerRect.width / 2) - (cardRect.width / 2);
        const delta = desiredLeft - cardRect.left; // pixels to move the slide

        // restore previous inline styles (we'll apply the computed transform next)
        carouselSlide.style.transform = prevTransform;
        carouselSlide.style.transition = prevTransition;

        // Return the absolute translateX value (apply as transform: translateX(<px>))
        return delta;
    }

    function updateDimensions() {
        allCards = document.querySelectorAll('.card');
        cardWidth = allCards[1].offsetWidth;
        // reposition to currentIndex without transition
        carouselSlide.style.transition = 'none';
        const offset = computeOffsetForIndex(currentIndex);
        carouselSlide.style.transform = `translateX(${offset}px)`;
        updateActiveCard();
    }

    function updateActiveCard() {
        allCards.forEach(card => card.classList.remove('active'));
        if (allCards[currentIndex]) allCards[currentIndex].classList.add('active');
    }

    function moveTo(index) {
        carouselSlide.style.transition = 'transform 0.5s ease-in-out';
        const offset = computeOffsetForIndex(index);
        carouselSlide.style.transform = `translateX(${offset}px)`;
        updateActiveCard();
    }

    leftArrow.addEventListener('click', () => {
        if (currentIndex <= 0) return;
        currentIndex--;
        moveTo(currentIndex);
    });

    rightArrow.addEventListener('click', () => {
        if (currentIndex >= allCards.length - 1) return;
        currentIndex++;
        moveTo(currentIndex);
    });

    carouselSlide.addEventListener('transitionend', () => {
        if (!allCards[currentIndex]) return;
        if (allCards[currentIndex].id === 'first-clone') {
            carouselSlide.style.transition = 'none';
            currentIndex = 1;
            const offset = computeOffsetForIndex(currentIndex);
            carouselSlide.style.transform = `translateX(${offset}px)`;
        }
        if (allCards[currentIndex].id === 'last-clone') {
            carouselSlide.style.transition = 'none';
            currentIndex = allCards.length - 2; // real last card
            const offset = computeOffsetForIndex(currentIndex);
            carouselSlide.style.transform = `translateX(${offset}px)`;
        }
    });

    // initial setup
    updateDimensions();

    // handle resize
    window.addEventListener('resize', () => {
        updateDimensions();
    });
});
