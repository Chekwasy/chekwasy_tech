$(document).ready(function() {
    $( '#chekwasy_solar_form' ).on( "submit", function( event ) {
	const api = 'https://' + "chekwasy.tech";
	$.ajax({
	    url: api + '/api/v1/chekwasy_solar/order',
	    type: 'POST',
	    data: JSON.stringify({first_name: $('#first_name').val(), last_name: $('#last_name').val(), phone: $('#phone').val(), email: $('#email').val(), amount: $('#amount').val(), state: $('#state').val(), city: $('#city').val(), street: $('#street').val(), others: $('#others').val()}),
	    contentType: 'application/json',
	    dataType: 'json'
	})

	    .done(function(data) {
		alert("Thank You. We will process your order after payment comfirmation");
	    })
	event.preventDefault();
    })
});