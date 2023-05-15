# CRUD для yatube

Реализация API для проекта yatube.

## Технологии и запуск проекта

Проект написан на языке python, с использованием django
и django REST framework. Необходимые для работы проекта
зависимости описаны в файле requirements.txt

Для запуска проекта:
- Клонируйте репозиторий
``` 
- git clone https://github.com/AVinAnd/api_yatube.git 
```
- Активируйте виртуальное окружение 

```
python -m venv venv
source venv/scripts/activate
```
- Установите зависимости

``` 
pip install -r requirements.txt
```
- Выполните миграции 
```
python manage.py makemigrations
python manage.py migrate
```
- Запустите проект
```
python manage.py runserver
```

Проект доступен по адресу http://127.0.0.1:8000/

## Ресурсы API yatube
- api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.

- api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.

- api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.

- api/v1/groups/ (GET): получаем список всех групп.

- api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.

- api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста post_id или создаём новый, указав id поста, который хотим прокомментировать.

- api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.

В ответ на запросы POST, PUT и PATCH, API возвращает объект, который был добавлен или изменён.

### Об авторе
Андрей Виноградов - python-developer, выпускник Яндекс Практикума по курсу Python-разработчик
