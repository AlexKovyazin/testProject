$.ajax({
    success: function (response) {
        $('.region-select').change(function() {
            let code = $(this).val();
            $('#city-select').load('get_regions/', {id: code}, function () {
                $('.city-select').fadeIn('slow');
            })
        })
    }
});
