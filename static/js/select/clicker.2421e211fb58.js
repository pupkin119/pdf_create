function printMousePos(event) {
    //   document.body.textContent =
    //     "clientX: " + event.clientX +
    //     " - clientY: " + event.clientY;

    $("#type-x").val(event.clientX);
    $("#type-y").val(event.clientY);
    // inputx.val = event.clientX;
    // inputx = $('#type_x');
    // inputx.val = event.clientX;
    // inputy = document.getElementById('type_y');
    // inputy.val = event.clientY;
}

document.addEventListener("click", printMousePos);

function disableMousePos() {
    document.removeEventListener("click", printMousePos);
}

function enableMousePos() {
    document.addEventListener("click", printMousePos);
}

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

function addGroup() {
    var my_data = [];
    $.ajax({
        type: "POST",
        url: $('#'),
        data: {
            'csrfmiddlewaretoken': getCookie('csrftoken')
        },
        dataType: 'json',
        success: function (data) {
            console.error(data);

            if (data['success']) {
                for (var i = 0; i < data.length; i++) {
                    my_data.push(data[i]);
                }
            }

        }

    });
    return my_data
}

$('#disable').click(disableMousePos);
$('#enable').click(enableMousePos);

$(document).ready(function () {

        //
        // $('#cancel_button').click(function () {
        //     var href = $(this).attr("href");
        //     console.info(href);
        //
        //     if (href) {
        //         window.location = href;
        //     }
        //
        // });



        $('#enter').click(function () {

            var url = $("#enter").attr("data-url");

            $.ajax({
                type: "POST",
                url: url,
                data: {
                    'csrfmiddlewaretoken': getCookie('csrftoken')
                },
                dataType: 'json',
                success: function (data) {
                    console.error(data);

                    // if (data['success']) {

                    console.error('succsess')

                    // }

                }

            });


        });

        // function get_linedata() {
        //     var url = $("#chartjs_line").attr("data-url");
        //
        //     $.ajax({
        //         type: "POST",
        //         url: url,
        //         data: {
        //             'local_id': 5,
        //             'csrfmiddlewaretoken': getCookie('csrftoken')
        //         },
        //         dataType: 'json',
        //         success: function (data) {
        //             console.error(data);
        //
        //             var mydata = [];
        //             for (i = 0; i < data.length; i++) {
        //                 mydata.push(data[i]["sum"])
        //             }
        //
        //             return mydata
        //         }
        //
        //     });
        // }
    }
);



