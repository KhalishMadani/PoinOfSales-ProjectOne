$(".menu > ul > li").click(function (e) {
  //remove active from already active
  $(this).siblings().removeClass("active");

  // add active to clicked
  $(this).toggleClass("active");

  // if has sub menu open it
  $(this).find("ul").slideToggle();
});