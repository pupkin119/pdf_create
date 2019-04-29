$(document).ready(function () {
    // $('.tooltipped').tooltip();
});

function to_manual() {
    var location1 = window.location.hostname;
    var new_url = location1 + '/manual';
    // var new_url = 'http://127.0.0.1:8000/manual';
    window.location.pathname = '/manual';
}

function to_exel() {
    var location1 = window.location.hostname;
    var new_url = location1 + '/exel';
    // var new_url = 'http://127.0.0.1:8000/exel';
    window.location.pathname = '/exel';
}