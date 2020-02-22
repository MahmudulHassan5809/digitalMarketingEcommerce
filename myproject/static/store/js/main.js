$(document).ready(function() {
  $(function() {
    $(".category_card").hover(
      function() {
        $(this.children[1]).addClass("category_card__hover");
      },
      function() {
        // on mouseout, reset the background colour
        $(this.children[1]).removeClass("category_card__hover");
      }
    );
  });
});
