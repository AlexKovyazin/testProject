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
