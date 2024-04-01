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
    const sess = document.getElementById("farm_session_id").innerHTML
	const api = 'http://' + "chekwasy.tech";
    $.ajax({
        url: api + '/api/v2/farm_check/' + sess,
        type: 'GET',
        data: JSON.stringify({}),
        contentType: 'application/json',
        dataType: 'json'
    })

    .done(function(data) {
    })
    .fail(function() {
        window.location.href = "/farm_login";
    });
};
