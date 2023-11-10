$(document).ready(function() {
    $( '#chekwasy_annie_form' ).on( "submit", function( event ) {
	const api = 'http://' + "chekwasy.tech";
	$.ajax({
	    url: api + '/api/v1/annie_couture/order',
	    type: 'POST',
	    data: JSON.stringify({first_name: $('#first_name').val(), last_name: $('#last_name').val(), phone: $('#phone').val(), email: $('#email').val(), choice: $('#choice').val(), state: $('#state').val(), city: $('#city').val(), street: $('#street').val(), others: $('#others').val(), link: $('#link').val()}),
	    contentType: 'application/json',
	    dataType: 'json'
	})

	    .done(function(data) {
		alert("Thank You. We will process your order after payment comfirmation");
	    })
	event.preventDefault();
    })
});
