# Куда пойти — Москва глазами Артёма
Сайт о самых интересных местах в Москве. Авторский проект Артёма.

![image](https://github.com/Kilsik/Billboard/assets/123646405/531010b4-e428-4148-9e4d-74f506f74a85)


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


### Загрузка данных о локациях
В целях упрощения заполнения базы данными о локациях добавлена утилита load_place. Команда запуска:
```sh
python manage.py load_place http://адрес/файла.json
```

Формат содержимого файла.json:
```
{
    "title": "Лопатинский рудник",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/5daa6346a8294570ddeeaa79e2fbdaf3.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/d18243f83f4f75109ba18f5f57cc82fa.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4d38bd0d0d18c1059325b1e53d784c7c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/9701cd8aef305a31121493c5c8f8a69c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/778a7547e7a8db159efc3a40d18d5734.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b7fd1cbc838ba8c695e9eb309297fd0c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/cbdb9b65ea1f112453ba7c2b2e014a30.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/fbb8dbc80c9530e10d0b2b49d517052e.jpg"
    ],
    "description_short": "В Воскресенском районе, в окрестностях посёлка Фосфоритный располагается одно из самых необычных и экзотических мест Подмосковья — Лопатинский рудник.",
    "description_long": "<p>Здесь вас ждут: ослепительно белый и красноватый песок, столь необычный для Подмосковья; тёмно-серые и жёлтые барханы; озеро на вершине горы; почти полное отсутствие других путешественников; огромные абзетцеры (многоковшовые экскаваторы); преодолимые трудности и ещё много всего интересного!</p><p>У Лопатинского фосфоритного рудника есть своя история.</p><p>В августе 1932 года на Егорьевском фосфоритном местoрождении началась промышленная выработка, использовались различные виды многоковшовых экскаваторов: одни двигались по рельсам, другие шагали «приставным» шагом. В результате работы экскаваторов были созданы невероятные ландшафты — желоба карьеров перемешиваются с песчаными грядами и полями, засеянными соснами.</p><p>Ныне рудник заброшен, а многие карьеры и техногенные впадины затоплены. Здесь образовались озёра с чистой водой и песчаными берегами. Для тех, кто желает побыть в этом уникальном месте несколько дней, в окрестностях работают базы отдыха. И вся эта подмосковная экзотика находится всего лишь в 100 км от МКАД!</p><p>Как добраться общественным транспортом: до платформы 88-й километр электричками Рязанского направления. Далее на автобусе до поселка Фосфоритный.</p><address class=\"post-list-item-info\"><span class=\"address\"><i class=\"font-icon icon-location\"></i> Московская область (90 км от Москвы в Рязанском направлении), между Воскресенском и Егорьевском.</span></address>",
    "coordinates": {
        "lng": "38.68171061700625",
        "lat": "55.31744823804868"
    }
}
```

### Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

