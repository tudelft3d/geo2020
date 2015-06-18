$( "a[data-toggle='collapse']" ).click(function(event) {
  event.preventDefault();
  $($(this).attr('href')).toggle();
});