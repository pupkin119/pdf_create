// $( document ).ready(function(){
//
//     $('.carousel.carousel-slider').carousel({
//     fullWidth: true,
//         noWrap: true
//     // indicators: true
//     });
//
// });

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

function get_next() {
  var elem = $('#carousel');

  var instance = M.Carousel.getInstance(elem);
  instance.next();
}
var row = 1;
var num = 1;

function generate_row() {
    var text = "<row id='panel_row_'" + row +">";
    text += "</row>";

    var before_row = parseInt(row) - 1;

    $('#panel_row_' + before_row).append(text)
}

function generate_card() {

    var elem = $("#panel_row_" + row);
    // var text = "<div class=\"card\" style=\"width: 18rem;\" id='card_elem_"+ num +"'>";
    // text += "<div class=\"card-body\">";
    // text += "<h5 class=\"card-title\">#" + num + "</h5>";
    // text += "<label>ФИО участника</label>";
    // text += "<input type='text' id='name_'"+ num +"> </input>";
    // text += "<label>Курс</label>";
    // text += "<input type='text' id='course_'" + num +"> </input>";


    // var text = "<div class=\"col s3\" id='col_elem_" + num + "'>";
    // text += "<div class=\"card\">";
    // // text += "<div class=\"card-image\">";
    // // text += "<img src=\"https://materializecss.com/images/sample-1.jpg\">";
    // text += "<span class=\"card-title\">#"+ num+"</span>";
    // text += "<a class=\"btn-floating halfway-fab waves-effect waves-light red\"><i class=\"material-icons\">add</i></a>";
    // // text += "</div>";
    // text += "<div class=\"card-action\">";
    // // text += "<div class=\"input-field col s6\" id='name_'"+ num +">";
    // // text += "<i class=\"material-icons prefix\">account_circle</i>";
    // // text += "<input id=\"icon_prefix\" type=\"text\" class=\"validate\">";
    // // text += "<label for=\"icon_prefix\">First Name</label>";
    // //     text += "<label>ФИО участника</label>";
    // // text += "<input type='text' id='name_'"+ num +"> </input>";
    //
    // // text += "<label>Курс</label>";
    // // text += "<input type='text' id='course_'" + num +"> </input>";
    // text += "<p>I am a very simple card. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.";
    // text += "</p>";
    // text += "<div class=\"input-field col s6\" id='name_'"+ num +">";
    // text += "<i class=\"material-icons prefix\">account_circle</i>";
    // text += "<input id=\"icon_prefix\" type=\"text\" class=\"validate\">";
    // text += "<label for=\"icon_prefix\">First Name</label>";
    // text += "</div>";
    // text += "</div>";
    // text += "</div>";
    // text += "</div>";

    // var text = "<div class=\"row\">";
    var text = "<div class=\"col s3\ id='col_elem_" + num + "'>";
    text += "<div class=\"card blue-grey darken-1\">";
    text += "<div class=\"card-content white-text\">";
    text += "<span class=\"card-title\" style='color: black'>#" + num + "</span>";
    // text += "<a class=\"btn-floating halfway-fab waves-effect waves-light red\"><i class=\"material-icons\" onclick='generate_card()'>add</i></a>";
    text += "</div>";
    text += "<div class=\"card-action\">";
    text += "<div class=\"input-field col s12\">";
    text += "<i class=\"material-icons prefix\">account_circle</i>";
    text += "<input type=\"text\" class=\"validate\" id='name_" + num + "'>";
    text += "<label for=\"icon_prefix\">ФИО</label>";
    text += "</div>";
    // text += "<a href=\"#\"></a>";
    text += "<div class=\"input-field col s12\">";
    text += "<i class=\"material-icons prefix\">check_circle</i>";
    text += "<input type=\"tel\" class=\"validate\" id='course_"+ num +"'>";
    text += "<label for=\"icon_telephone\">Курс</label>";
    text += "</div>";
    // text += "<p> </p>";
    // text += "<a href=\"#\"></a>";
    text += "</div>";
    text += "</div>";
    text += "</div>";
    // text += "</div>";

    elem.append(text);


    if (parseInt(num) == 8){
        $('#btn_add_card').attr('disabled','disabled');
        return;
    }

    num = num + 1;
    if (num % 4) {
        generate_row();
    }


}

function manual() {

    $('#row_1').hide();
    get_next();

    $('#btn_2').text('Перейти дальше');
    $('#btn_2').attr("onclick","generate_manual_pdf()");

    $('#head_2').text('Заполни поля');
        var button = "<a class=\"btn\" style='border-radius: 50%;' onclick=\"generate_card();\" id=\"btn_add_card\">+</a>";

    $('#head_2').append(button);

    var text = generate_card();

    $('#panel_row_1').append(text);
}

function generate_manual_pdf() {
    var names = [];
    var courses = [];
    for (i = 1; i < num; i++) {

        names.push($('#name_' + i).val());
        courses.push($('#course_' + i).val());
    }
    var href = 'http://127.0.0.1:8000/cutaway/manual';
    $.ajax({
        type: "POST",
        url: href,
        async: false,
        data: {
            'csrfmiddlewaretoken': getCookie('csrftoken'),
            names: names,
            courses: courses
        },
        dataType: 'json',
        success: function (data) {
            alert('yes');
        }

    });
}
