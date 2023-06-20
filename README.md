# django-demo

1. Создаем виртуальное окружение
>*python -m venv venv*
2. Активируем виртуальное окружение
>*source venv/bin/activate*
3. Устанавливаем необходимые пакеты
>*pip install -r requirements.txt*
4. Запускаем миграции в БД
>*./manage.py migrate*
5. Создаем суперпользователя
>*./manage.py createsuperuser*
6. Запускаем локальный сервер разработки
>*./manage.py runserver*
7. Открываем в браузере *http://127.0.0.1:8000/admin*

*Опционально:*
- Скопировать json-файлы с данными в *app/fixtures*
- Загрузить данные из *fixtures*
>*./manage.py loaddata имя_файла_с_данными.json*
