# anverali_django

====================================
Действия для разворачивания проектов
====================================

Создание и работа с виртуальной средой.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Зайти в папку проекта еклипса и выполнить::

   python3 -m venv .venv

потом::

   . .venv/bin/activate

Установить сразу все нужные модули::

   pip install -r requiremen.txt

Создание суперпользователя::

   python manage.py createsuperuser

DataDase::
'NAME': 'anverali',
'USER': 'anverali',
'PASSWORD': 'anverali',
'HOST': 'localhost',
'PORT': '5432',
