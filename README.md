# Weather-collector
## Описание
“Коллектор погоды для https://yandex.ru/dev/weather/ в установленный период времени собирает информацию о погоде крупнейших городов мира (по версии [Wikipedia](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%81%D0%B0%D0%BC%D1%8B%D1%85_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D1%91%D0%BD%D0%BD%D1%8B%D1%85_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D1%85_%D0%B0%D0%B3%D0%BB%D0%BE%D0%BC%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B9)), сохраняя полученные значения в базу данных.”

## Автор:
[Александр Ракитянский](https://github.com/AlexR466/)

## Как запустить проект:

### Клонировать репозиторий и перейти в него в командной строке:

`git clone git@github.com:AlexR466/Weather-collector.git`

`cd Weather-collector`

### Заполнить `.env`:

API_KEY= {ключ, полученный на сайте https://yandex.ru/pogoda/b2b/console/home}  
POSTGRES_HOST=db  
POSTGRES_PORT=5432  
POSTGRES_DB=your_database_name  
POSTGRES_USER=your_user_name  
gitPOSTGRES_PASSWORD=your_password  

### Запустить компоуз:

`docker-compose up -d`

## Техно-стек:
При разработке использовались:
1. Язык программирования для бэкенда - [Python](https://docs.python.org/3/),
2. База данных [Posgresql](https://www.postgresql.org/docs/),
3. Библиотека для работы с базой данных - [SQLAlchemy](https://docs.sqlalchemy.org/en/20/),
4. Инструмент для миграции базы данных - [Alembic](https://alembic.sqlalchemy.org/en/latest/),
5. Для контейниризации - [Docker](https://docs.docker.com/).