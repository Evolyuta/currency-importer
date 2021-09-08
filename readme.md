# Установка

**Создать окружение**:
`virtualenv -p python3 .` и `source bin/activate`

**Установить django**:
`pip install django`

**Установить requests**:
`pip install requests`

**Создать админа**:
`python manage.py migrate`, `python manage.py createsuperuser`

**Запустить миграции приложения**:
`python manage.py makemigrations`, `python manage.py migrate`

**Запустить сервер**:
`python manage.py runserver`

# Использование

-) Зайти в /admin/app/currency/

-) Создать несколько валют

-) Зайти в /admin/app/currencycomparison/

-) Нажать на кнопку "Import"