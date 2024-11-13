# Для запуска проекта необходимо создать .env файл в корне проекта вида:
    DB_HOST=хост(т.к мы используем базу данных внутри контейнера, то хост должен соответствовать контейнеру базы данных)
    DB_PORT=порт
    DB_USER=имя пользователя
    DB_PASSWORD=пароль пользователя
    DB_NAME=название базы данных
## Пример .env файла:
    DB_HOST=postgres
    DB_PORT=5432
    DB_USER=admin
    DB_PASSWORD=adminadmin
    DB_NAME=dbadmin


### Развертка:
    git clone https://github.com/EgorZhizhlo/FastAPIPostgresAsync.git
    cd FastAPIPostgresAsync
    docker-compose up --build
