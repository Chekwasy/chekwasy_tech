$(document).ready(function() {
    $( '#Login' ).on( "submit", function( event ) {
		const api = 'http://' + "chekwasy.tech";
		$.ajax({
		    url: api + '/api/v2/farm_sessions',
		    type: 'POST',
		    data: JSON.stringify({email: $('#email').val(), password: $('#password').val() }),
		    contentType: 'application/json',
		    dataType: 'json'
		})

		    .done(function(data) {
			alert("You are now logged in");
			window.location.href = "/farm_user";
		    })
		    .fail(function() {
		    	alert("An Error Occurred. Try Again");
		    });
		event.preventDefault();
	});

    $( '#GenTokenPwd' ).on( "submit", function( event ) {
		const api = 'http://' + "chekwasy.tech";
		$.ajax({
		    url: api + '/api/v2/farm_reset_password',
		    type: 'POST',
		    data: JSON.stringify({email: $('#email').val()}),
		    contentType: 'application/json',
		    dataType: 'json'
		})

		    .done(function(data) {
			alert("Reset Token Generated and sent to your mail. Enter the token with your new password");
			window.location.href = "/farm_tk";
		    })
		    .fail(function() {
		    	alert("An Error Occurred. Please Check Your Email")
		    });
		event.preventDefault();
    });

    $( '#Reset_pwd' ).on( "submit", function( event ) {
		const api = 'http://' + "chekwasy.tech";
		const n1 = $('#Password1').val();
		const n2 = $('#Password2').val();
		if (n1 !== n2) {
			alert("Password did not match");
		} 
		else {
			$.ajax({
			    url: api + '/api/v2/farm_reset_password',
			    type: 'PUT',
			    data: JSON.stringify({email: $('#email').val(), reset_token: $('#token').val(), new_password: n2}),
			    contentType: 'application/json',
			    dataType: 'json'
			})

			    .done(function(data) {
				alert("Reset Token Generated and sent to your mail. Enter the token with your new password");
				window.location.href = "/farm_tk";
			    })
			    .fail(function() {
			    	alert("An Error Occurred. Please Cross Check Your Response")
			    });
			event.preventDefault();
		}
	});
	let zzz = '';
    $( "#RegisterCheck" ).on( "click", function() {
		const api = 'http://' + "chekwasy.tech";
		$.ajax({
		    url: api + '/api/v2/farm_verify',
		    type: 'GET',
		    data: JSON.stringify({email: $('#email').val()}),
		    contentType: 'application/json',
		    dataType: 'json'
		})

		    .done(function(data) {
			zzz = data.verify_token;
		    })
		    .fail(function() {
		    	alert("Invalid Email");
		    });
	});
	$( '#Register' ).on( "submit", function( event ) {
		const api = 'http://' + "chekwasy.tech";
		const n1 = $('#password').val();
		const n2 = $('#password2').val();
		tok = $('#token').val();
		if ((n1 !== n2) || (zzz !== tok)) {
			alert("Incorrect Token");
		}
		else {
			$.ajax({
			    url: api + '/api/v2/farm_users',
			    type: 'POST',
			    data: JSON.stringify({email: $('#email').val(), reset_token: $('#token').val(), new_password: n2}),
			    contentType: 'application/json',
			    dataType: 'json'
			})

			    .done(function(data) {
				alert(`Farm User Account Created Sucessfully ${data.email} \n You Can Now Login`);
				window.location.href = "/farm_login";
			    })
			    .fail(function() {
			    	alert("An Error Occurred. Please Cross Check Your Response")
			    });
			event.preventDefault();
		}
	});
	$( '#Farm_order' ).on( "submit", function( event ) {
		const api = 'http://' + "chekwasy.tech";
		$.ajax({
		    url: api + '/api/v2/farm_order',
		    type: 'POST',
		    data: JSON.stringify({order_qty: $('#qty').val(), note: $('#note').val()}),
		    contentType: 'application/json',
		    dataType: 'json'
		})

		    .done(function(data) {
			alert("Order Created. More Info sent to your mail");
			window.location.href = "/farm_order";
		    })
		    .fail(function() {
		    	alert("An Error Occurred.")
		    });
		event.preventDefault();
    });
    $( "#Logout" ).on( "click", function() {
		const api = 'http://' + "chekwasy.tech";
		$.ajax({
		    url: api + '/api/v2/farm_sessions',
		    type: 'DELETE',
		    data: JSON.stringify({}),
		    contentType: 'application/json',
		    dataType: 'json'
		})

		    .done(function(data) {
				alert("Logged Out");
				window.location.href = "/farm_login";
		    })
		    .fail(function() {
		    	alert("Session Expired");
		    	window.location.href = "/farm_login";
		    });
	});
	if (window.location.pathname === '/farm_profile') {
		const api = 'http://' + "chekwasy.tech";
		$.ajax({
		    url: api + '/api/v2/farm_profile',
		    type: 'GET',
		    data: JSON.stringify({}),
		    contentType: 'application/json',
		    dataType: 'json'
		})

		    .done(function(data) {
				document.getElementById("f_name").innerHTML = `Full Name: ${data.first_name} ${data.last_name}`;
				document.getElementById("Email").innerHTML = `Email: ${data.email}`;
				document.getElementById("Phone").innerHTML = `Phone: ${data.phone}`;
				document.getElementById("Address").innerHTML = `Address: ${data.street}, ${data.city}, ${data.state}.`;
		    });
	};
	$( '#Farm_update' ).on( "submit", function( event ) {
		const api = 'http://' + "chekwasy.tech";
		const s = document.getElementById('state');
		const stat = s.options[s.selectedIndex].text;
		$.ajax({
		    url: api + '/api/v2/farm_profile',
		    type: 'PUT',
		    data: JSON.stringify({first_name: $('#first_name').val(), last_name: $('#last_name').val(), street: $('#address').val(), city: $('#city').val(), state: stat}),
		    contentType: 'application/json',
		    dataType: 'json'
		})

		    .done(function(data) {
			alert("Profile Updated Successfully.");
			window.location.href = "/farm_profile";
		    })
		    .fail(function() {
		    	alert("An Error Occurred. Try Again")
		    });
		event.preventDefault();
    });
});
