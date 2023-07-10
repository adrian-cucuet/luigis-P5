$(function () {
  "use strict";

  const swiper = new Swiper('.lp-short-menu-slider', {
    slidesPerView: 4,
    spaceBetween: 30,
    parallax: true,
    speed: 1000,
    navigation: {
      prevEl: '.lp-short-menu-prev',
      nextEl: '.lp-short-menu-next',
    },
    breakpoints: {
      992: {
        slidesPerView: 2,
      },
      768: {
        slidesPerView: 1,
      },
    },
  });
});