document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelector('.slides');
    let index = 0;
    const totalSlides = slides.children.length;

    function showNextSlide() {
        index = (index + 1) % totalSlides;
        slides.style.transform = `translateX(-${index * 70}%)`;
    }

    setInterval(showNextSlide, 2000000); // con esto modificamos el tiempo que se mueve
});
    