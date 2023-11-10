$( "#chekwasy_buildex_form_botton" ).click(function () {

    const api = 'http://' + window.location.hostname;
    // Stop form from submitting normally
    event.preventDefault();

    // Get some values from elements on the page:
    var $form = $( this );
    first_name = $form.find( "input[name='first_name']" ).val();
    last_name = $form.find( "input[name='last_name']" ).val();
    proposed_build = $form.find( "input[name='proposed_build']" ).val();
    phone = $form.find( "input[name='phone']" ).val();
    email = $form.find( "input[name='email']" ).val();
    land_area = $form.find( "input[name='land_area']" ).val();
    build_area = $form.find( "input[name='build_area']" ).val();
    room = $form.find( "input[name='room']" ).val();
    bathroom = $form.find( "input[name='bathroom']" ).val();
    state = $form.find( "input[name='state']" ).val();
    city = $form.find( "input[name='city']" ).val();
    others = $form.find( "input[name='others']" ).val();

    $.ajax({
	url: api + ':5001/api/v1/chekwasy_buildex/enquiry',
	type: 'POST',
	data: JSON.stringify({ "first_name": first_name, "last_name": last_name, "proposed_build": proposed_build, "phone": phone, "email": email, "land_area": land_area, "build_area": build_area, "room": room, "bathroom": bathroom, "state": state, "city": city, "others": others }),
	contentType: 'application/json',
	dataType: 'json',
	success: msg
    });

} );
function msg (data) {
    alert("success" + data);

}
