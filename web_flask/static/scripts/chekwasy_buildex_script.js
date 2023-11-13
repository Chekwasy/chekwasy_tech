$(document).ready(function() {
    $( '#chekwasy_buildex_form' ).on( "submit", function( event ) {
	const api = 'https://' + "chekwasy.tech";
	$.ajax({
	    url: api + '/api/v1/chekwasy_buildex/enquiry',
	    type: 'POST',
	    data: JSON.stringify({first_name: $('#first_name').val(), last_name: $('#last_name').val(), phone: $('#phone').val(), email: $('#email').val(), proposed_build: $('#proposed_build').val(), land_area: $('#land_area').val(), build_area: $('#build_area').val(), room: $('#room').val(), bathroom: $('#bathroom').val(), state: $('#state').val(), city: $('#city').val(), others: $('#others').val() }),
	    contentType: 'application/json',
	    dataType: 'json'
	})

	    .done(function(data) {
		alert("Thank You. You will get a feedback from us via email submitted");
	    })
	event.preventDefault();
    })
});
