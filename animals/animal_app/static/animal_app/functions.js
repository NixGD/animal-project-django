// Javascript functions for animal app


$(document).ready(function() {
    console.log('ready');
    $('#id_notes').on('keyup', function () {
        console.log('key');
        $('#notes_submit').prop("disabled", false);
    });

    $(document).on('change',
        '.state-selector',
        function(e) {
        console.log('noticed change in ' + e.target);
        e.target.closest('form').submit();
    });

});

