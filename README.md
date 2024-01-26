# fastapi-beanie-template

Базовая архитектура для приложения.

Стек: MongoDB, beanie, Fastapi


Рассуждения

У нас есть 5 методов для взаимодействия - GET POST PATCH PUT DELETE.
Помимо методов мы можем использовать полезную нагрузку в headers, URI, payload
headers - заголовки, например для авторизации
URI - для выборки документа из ресурса, например /users/1
payload для передачи данных в формате json, применим к методами POST, PUT, PATCH

В этой солянке будем придерживаться к луковой архитектуре.
app(db(service(endpoint(data))))

Таким образом можно построить схему взаимодействия
1-Пользователь обращается к ресурсу делая запрос на endpoint * и передает ему некоторые данные.
2-Endpoint занимается валидацией данных с помощью pydantic и вызывает нужный сервис * и передаёт ему данные.
3-Сервис работает с базой данных и производит нужную операцию.
4-Сервис сериализует выходные данные и возвращает результат для endpoint.
5-Endpoint возвращает данные пользователю.

* - необязательно

