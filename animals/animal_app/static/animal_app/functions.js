// Javascript functions for animal app


$(document).ready(function() {
    console.log('ready');
    $('#id_notes').on('keyup', function () {
        $('#notes_submit').prop("disabled", false);
    });

    $(document).on('change',
        '.state-selector',
        function(e) {
        e.target.closest('form').submit();
    });

});

