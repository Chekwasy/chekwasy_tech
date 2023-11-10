$(document).ready(function() {
    $( '#chekwasy_farm_form' ).on( "submit", function( event ) {
	const api = 'http://' + "chekwasy.tech";
	$.ajax({
	    url: api + '/api/v1/chekwasy_farm/order',
	    type: 'POST',
	    data: JSON.stringify({first_name: $('#first_name').val(), last_name: $('#last_name').val(), phone: $('#phone').val(), email: $('#email').val(), reference: $('#reference').val(), state: $('#state').val(), city: $('#city').val(), street: $('#street').val(), order_qty: $('#order_qty').val() }),
	    contentType: 'application/json',
	    dataType: 'json'
	})

	    .done(function(data) {
		alert("Thank You. We will process your order and deliver within 7days after payment comfirmation");
	    })
	event.preventDefault();
    })
});
