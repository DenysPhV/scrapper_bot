<!-- @format -->

# scrapper_bot

Scrapper Bot - это бот Discord, предназначенный для скрапинга данных с веб-сайтов, обработки CSV файлов, взаимодействия с API сервисами и сохранения данных в базе данных PostgreSQL.

## Установка

1. Клонируйте репозиторий на локальную машину:

   ```bash
   git clone https://github.com/your_username/scrapper_bot.git
   ```

2. Установите зависимости, используя pip:

   ```bash
   pip install -r requirements.txt
   ```

## Использование

1. Убедитесь, что вы настроили все необходимые параметры в файле `.env`, такие как токены для доступа к сервисам и параметры подключения к базе данных.

2. Запустите приложение с помощью Docker Compose:

   ```bash
   docker-compose up --build
   ```

3. Бот будет доступен на вашем сервере Discord по заданному префиксу.

## Структура проекта

```
   scrapper_bot/
│
├── bot/
│
│ ├── db/
│ │ ├── connection.py
│ │ ├── database_manager.py
│ │ └── execute.py
│ │
│ ├── functions/
│ │ └── registration_by_phone.py
│ │
│ ├── handlers/
│ │ ├── bot_handler.py
│ │ ├── api_handler.py
│ │ └── csv_handler.py
│ │
│ ├── log/
│ │ └── logger.py
│ │
│ ├── settings/
│ │ └── settings.py
│ │
│ └── main.py
│
├── .env
│
├── .gitignore
│
├── Dockerfile
│
├── docker-compose.yaml
│
├── LICENSE
│
├── README.md
│
└── requirements.txt

```

[Apache License Version 2.0](LICENSE)
