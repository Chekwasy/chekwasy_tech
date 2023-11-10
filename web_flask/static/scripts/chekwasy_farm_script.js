$(document).ready(function() {
    $( '#chekwasy_farm_form' ).on( "submit", function( event ) {
	const api = 'http://' + window.location.hostname;
	$.ajax({
	    url: 'chekwasy.tech/api/v1/chekwasy_farm/order',
	    type: 'POST',
	    data: {"first_name": $('#first_name').val(), "last_name": $('#last_name').val(), "phone": $('#phone').val(), "email": $('#email').val(), "reference": $('#reference').val(), "state": $('#state').val(), "city": $('#city').val(), "street": $('#street').val(), "#order_qty": $('#order_qty').val() }
	})

	    .done(function(data) {
		alert("success" + data)
	    })
	event.preventDefault();
    })
});
