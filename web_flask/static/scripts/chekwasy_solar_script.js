$( "#chekwasy_solar_form" ).on( "submit", function( event ) {

    // Stop form from submitting normally
    event.preventDefault();

    // Get some values from elements on the page:
    var $form = $( this ),
	first_name = $form.find( "input[name='first_name']" ).val(),
	last_name = $form.find( "input[name='last_name']" ).val(),
	amount = $form.find( "input[name='amount']" ).val(),
	phone = $form.find( "input[name='phone']" ).val(),
	email = $form.find( "input[name='email']" ).val(),
	state = $form.find( "input[name='state']" ).val(),
	city = $form.find( "input[name='city']" ).val(),
	street = $form.find( "input[name='street']" ).val(),
	others = $form.find( "input[name='others']" ).val(),
	url = $form.attr( "action" );

    // Send the data using post
    var posting = $.post( url, { "first_name": first_name, "last_name": last_name, "amount": amount, "phone": phone, "email": email, "state": state, "city": city, "street": street, "others": others } );

    // Put the results in a div
    posting.done(function( data ) {
	alert( "Order Success: " + data + " Email us to cancel your order" );
    } );
} );
