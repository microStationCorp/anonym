function login() {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var usr = $('#lusername').val()
    var pass = $('#password').val()
    var csrftoken = getCookie('csrftoken');

    $.ajax({
        url: '../login',
        type: 'POST',
        data: {
            'usr': usr,
            'pass': pass
        },
        headers: { "X-CSRFToken": csrftoken },
        success: function (data) {
            if(data['usr']==true){
                location.href='../user'
            }else{
                $('#loginmsg').text(`username or password is incorrect`)
            }
        }, error: function () {
            console.log('error')
        }
    })
}