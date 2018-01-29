// Javascript functions for animal app


$(document).ready(function() {
    $('#notes_submit').hide();
    $('#id_notes').on('keyup', function () {
        //$('#notes_submit').prop("disabled", false);
        $('#notes_submit').show();
    });

    $(document).on('change',
        '.state-selector',
        function(e) {
        e.target.closest('form').submit();
    });

});

