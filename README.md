# Куда пойти — Москва глазами Артёма
Сайта о самых интересных местах в Москве. Авторский проект Артёма.

![image](https://github.com/Kilsik/Billboard/assets/123646405/660f6e49-dc1b-48db-bf6a-e0e5d6c3afcf)


[Тут](https://ilsi.pythonanywhere.com/) можно посмотреть демо-версию сайта.

### Как установить

* Скачать [этот script](https://github.com/Kilsik/Billboard)

**Python3 уже должен быть установлен**. 
Используйте `pip` (или `pip3`, если возникает конфликт с Python2) для установки зависимостей:
```sh
pip install -r requirements.txt
```

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.
Доступны переменные:
- `SECRET_KEY` - секретный ключ Django
- `ALLOWED_HOSTS` - список серверов, с которых будут обрабатываться запросы
- `DATABASE_ENGINE` - используемый движок для доступа к БД
- `DATABASE_NAME` - путь к базе данных
- `STATIC_URL` - адрес статических файлов
- `STATICFILES_DIRS` - список каталогов статических файлов
- `MEDIA_URL` - адрес медиа данных
- `MEDIA_ROOT` - каталог хранения медиа данных

Создайте базу данных SQLite:

```sh
python manage.py makemigrations
python manage.py migrate
```

Создайте супер пользователя (администратора) командой:
```sh
python manage.py createcuperuser
```

Запустить сервер:
```sh
python manage.py runserver
```


1. Перейти во вкладку `/admin`.
2. Для корректной работы в БД должен существовать локации с описанием и необходимые фотографии.


### Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

### Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

