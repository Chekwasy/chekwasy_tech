$( "#chekwasy_farm_form_botton" ).click(function () {

    const api = 'http://' + window.location.hostname;
    // Stop form from submitting normally
    event.preventDefault();

    // Get some values from elements on the page:
    var $form = $( this );
    first_name = $form.find( "input[name='first_name']" ).val();
    last_name = $form.find( "input[name='last_name']" ).val();
    phone = $form.find( "input[name='phone']" ).val();
    email = $form.find( "input[name='email']" ).val();
    reference = $form.find( "input[name='reference']" ).val();
    state = $form.find( "input[name='state']" ).val();
    city = $form.find( "input[name='city']" ).val();
    street = $form.find( "input[name='street']" ).val();
    order_qty = $form.find( "input[name='order_qty']" ).val();

    $.ajax({
	url: api + ':5001/api/v1/chekwasy_farm/order',
	type: 'POST',
	data: JSON.stringify({ "first_name": first_name, "last_name": last_name, "phone": phone, "email": email, "reference": reference, "state": state, "city": city, "street": street, "order_qty": order_qty }),
	contentType: 'application/json',
	dataType: 'json',
	success: msg
    });

} );
function msg (data) {
    alert("success" + data);

}
