function signup() {

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

    var usr = $('#susername').val()
    var fname = $('#fname').val()
    var lname = $("#lname").val()
    var pass1 = $('#password1').val()
    var pass2 = $('#password2').val()
    var csrftoken = getCookie('csrftoken');
    $('#umsg').text('')
    $('#fmsg').text('')
    $('#lmsg').text('')
    $('#pmsg').text('')

    if (usr == '') {
        $('#umsg').text('please fill username')
    } else if (fname == '') {
        $('#fmsg').text('please fill first name')
    } else if (lname == '') {
        $('#lmsg').text('please fill first name')
    } else if (pass1 == '' || pass2 == '') {
        $('#pmsg').text('passwords may not be blank')
    } else if (pass1 != pass2) {
        $('#pmsg').text(`passwords doesn't match`)
    } else {
        $.ajax({
            url: '../signup',
            type: 'POST',
            data: {
                'usr': usr,
                'fname': fname,
                'lname': lname,
                'pass1': pass1,
                'pass2': pass2
            },
            headers: { "X-CSRFToken": csrftoken },
            success: function (data) {
                $('#msg').text(data['msg'])
            }, error: function () {
                console.log('error')
            }
        })
    }

}