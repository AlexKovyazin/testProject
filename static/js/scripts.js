let userCreateForm = document.getElementById('user-create-form')

userCreateForm.submit = function () {
    userCreateForm.submit();
    console.log('Форма подтверждена');
    userCreateForm.reset();
    console.log('Форма очищена');
}

// Загрузка списка городов по выбранному ранее региону
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

// Запрос на генерацию .xlsx файла
document.querySelector('#export-to-xlsx').onclick = function () {
    $.ajax({
        type: 'POST',
        url: '/download_users_xlsx/',
        success: function () {
            alert('.xlsx файл сгенерирован');
        }
    })
}

// Запрос на генерацию .pdf файла
document.querySelector('#export-to-pdf').onclick = function () {
    $.ajax({
        type: 'POST',
        url: '/download_users_pdf/',
        success: function () {
            alert('.pdf файл сгенерирован')
        }
    })
}
