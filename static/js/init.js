(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.slider').slider({
      indicators: false,
      duration: 250
    });

    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);

    $('.scroll-top').hide();
    
    $(window).scroll(function() {
      if ($(this).scrollTop() > 300) {
        $('.scroll-top').fadeIn('slow');    
      } else {
        $('.scroll-top').fadeOut('slow');
      }
    });
    $('.scroll-top').click(function(event) {
        event.preventDefault();
        $('html, body').animate({scrollTop: 0}, 600);
    });

    $(window).on('beforeunload', function() {
        window.setTimeout(function() {
        $(window).scrollTop(0); 
      }, 0);
    });

    $("#sorry_msg").hide();

    $("#confirmed").on("change", () => {
      if ($("#confirmed").find(":selected").val() === "false") {
        $("#sorry_msg").show();
        $("#confirmed_adults").attr("min", "0");
        $("#confirmed_adults").val("0");
        $("#adults_section").hide();
        $("#children_section").hide();
      } else {
        $("#sorry_msg").hide();
        $("#adults_section").show();
        $("#confirmed_adults").attr("min", "1");
        $("#children_section").show();
      }
    });

  }); // end of document ready
})(jQuery); // end of jQuery name space