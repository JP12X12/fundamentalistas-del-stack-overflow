document.addEventListener('DOMContentLoaded', function() {
    const carouselImages = document.querySelector('.carousel-images');
    const images = document.querySelectorAll('.carousel-images img');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    let currentIndex = 0;

    function showImage(index) {
        if (index >= images.length) {
            currentIndex = 0;
        } else if (index < 0) {
            currentIndex = images.length - 1;
        } else {
            currentIndex = index;
        }
        carouselImages.style.transform = `translateX(-${currentIndex * 100}%)`;
    }

    function nextImage() {
        showImage(currentIndex + 1);
    }

    function prevImage() {
        showImage(currentIndex - 1);
    }

    nextButton.addEventListener('click', nextImage);
    prevButton.addEventListener('click', prevImage);


});
