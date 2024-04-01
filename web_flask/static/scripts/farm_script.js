const ls = [
        '/farm_user/',
        '/farm_user',
        '/farm_profile/',
        '/farm_profile',
        '/farm_order/',
        '/farm_order',
        '/farm_update/',
        '/farm_update',
    ];

if (ls.includes(window.location.pathname)) {
	const api = 'http://' + "chekwasy.tech";
        $.ajax({
               url: api + '/api/v2/farm_profile',
                    type: 'GET',
                    data: JSON.stringify({}),
                    contentType: 'application/json',
                    dataType: 'json'
                })

                    .done(function(data) {
                                document.getElementById("f_name").innerHTML = `>
                                document.getElementById("Email").innerHTML = `E>
                                document.getElementById("Phone").innerHTML = `P>
                                document.getElementById("Address").innerHTML = >
                    });
        };
