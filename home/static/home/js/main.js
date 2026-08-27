// Initialize Swiper
const swiper = new Swiper(".mySwiper", {
  loop: true, // infinite loop
  autoplay: {
    delay: 4000,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  effect: "slide", // you can also use 'fade', 'cube', etc.
  speed: 600,
});
