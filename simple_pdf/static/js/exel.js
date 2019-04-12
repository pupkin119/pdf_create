function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



function upload() {

    $('#progress_manual').show();
    var fd = new FormData();
    var files = $('#file')[0].files[0];
    fd.append('file',files);

// $.ajax({
//     csrfmiddlewaretoken: getCookie('csrftoken'),
//     url: $(this).attr('action'),
//     type: $(this).attr('method'),
//     data: fd,
//     // data: $("#registerSubmit").serialize(),
//     cache: false,
//     processData: false,
//     contentType: false,
//     success: function(data) {
//         alert('success');
//     }
// });

var new_url = 'http://127.0.0.1:8000/preview/';

var href = 'http://127.0.0.1:8000/upload_exel';
$.ajax({
        type: "post",
        url: href,
        async: true,
        data: fd,
        cache: false,
        processData: false,
        contentType: false,
        success: function (data) {
            $('#progress_manual').hide();
            // alert('yes');
            window.location = new_url + data['success'];

        }

    });

return false;
}