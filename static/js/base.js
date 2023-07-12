$(function () {
  "use strict";

  var swiper = new Swiper('.lp-short-menu-slider', {
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

  $('[data-fancybox="menu"]').fancybox({
    animationEffect: "zoom-in-out",
    animationDuration: 600,
    transitionDuration: 1200,
  });

  $('.lp-add').on('click', function () {
    if ($(this).prev().val() < 10) {
      $(this).prev().val(+$(this).prev().val() + 1);
    }
  });

  $('.lp-sub').on('click', function () {
    if ($(this).next().val() > 1) {
      if ($(this).next().val() > 1) $(this).next().val(+$(this).next().val() - 1);
    }
  });
});