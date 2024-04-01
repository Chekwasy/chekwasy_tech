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
function getCookieValue(cookieName) {
    var name = cookieName + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var cookieArray = decodedCookie.split(';');

    for (var i = 0; i < cookieArray.length; i++) {
        var cookie = cookieArray[i].trim();
        if (cookie.indexOf(name) === 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return "";
}
if (ls.includes(window.location.pathname)) {
    var cooki = getCookieValue("farm_session_id");
    const api = 'http://' + "chekwasy.tech"
    $.ajax({
        url: api + '/api/v2/farm_check/' + cooki,
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
