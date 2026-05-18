# Эволюция русской технической мысли

Многостраничный сайт с FastAPI-бэкендом.

## Структура

- `frontend/` — HTML/CSS/JS
- `server/` — FastAPI API + раздача фронтенда
- `robots.txt` и `sitemap.xml` — SEO-файлы

## Быстрый старт

```powershell
.\run.ps1 -InstallDeps
```

Открыть: `http://127.0.0.1:8000/`

## Конфигурация через .env

Скопируй `server/.env.example` в `server/.env` и при необходимости измени значения:

- `APP_HOST` — хост запуска (`127.0.0.1`)
- `APP_PORT` — порт (`8000`)
- `APP_RELOAD` — авто-перезапуск (`true`/`false`)
- `LOG_LEVEL` — уровень логов (`INFO`, `DEBUG`, ...)

## Тесты

```powershell
.\run-tests.ps1 -InstallDeps
```

## URL-структура

- `/` — главная
- `/epoch-1`, `/epoch-2`, `/epoch-3`, `/epoch-4`, `/event` `/sources` — страницы эпох, событий и источников
- `/api/health`, `/api/epochs`, `/api/epochs/{id}`, `/api/sources` — API
