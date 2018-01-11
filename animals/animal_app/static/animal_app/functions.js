// Javascript functions for animal app


$(document).ready(function() {
    console.log('ready');
    $('#id_notes').on('keyup', function () {
        console.log('key');
        $('#notes_submit').prop("disabled", false);
    });
});

