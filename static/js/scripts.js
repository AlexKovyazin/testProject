// document.addEventListener('submit', (e) => {
// // Отключаем событие по умолчанию
//     e.preventDefault();
// // Очищаем поля формы
//     e.target.submit();
//     e.target.reset();
// });

document.querySelector('#submit-form').onclick = function () {
    document.getElementById('user-create-form').submit();
    // не отрабатывает :(
    document.getElementById('user-create-form').reset();
}

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


document.querySelector('#export-to-xlsx').onclick = function () {
    $.ajax({
        type: 'POST',
        url: '/download_users_xlsx/',
        success: function () {
            alert('.xlsx файл сгенерирован')
        }
    })
}

document.querySelector('#export-to-pdf').onclick = function () {
    $.ajax({
        type: 'POST',
        url: '/download_users_pdf/',
        success: function () {
            alert('.pdf файл сгенерирован')
        }
    })
}
