$(document).ready(function () {
    $('.tooltipped').tooltip();
});

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

    // if (!($('#town').val())) {
    //     M.toast({html: 'Заполните город!'});
    //     $('#progress_manual').hide();
    //     return;
    // }

    $('#progress_manual').show();
    var fd = new FormData();
    var files = $('#file')[0].files[0];
    fd.append('file', files);
    // fd.append('town', $('#town').val());

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
// location = window.location.hostname;
// var new_url = location + '/preview/';

    var href = '/upload_exel';
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
            window.location = /preview/ + data['success'];

        }

    });

    return false;
}