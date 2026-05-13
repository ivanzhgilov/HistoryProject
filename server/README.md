## Backend (FastAPI)

### Установка

```powershell
cd server
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Запуск

```powershell
cd ..
.\run.ps1 -InstallDeps
```

Если запускаешь напрямую из `server/`, используй:

```powershell
uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
```

Открыть сайт:
- `http://127.0.0.1:8000/`

API:
- `http://localhost:8000/api/health`
- `http://localhost:8000/api/epochs`
- `http://localhost:8000/api/epochs/epoch-1`
- `http://localhost:8000/api/sources`

Логи:
- консоль
- файл `server/logs/app.log` (rotating)

### .env

Настройки запуска и логов лежат в `server/.env`.
Базовый шаблон: `server/.env.example`.

### Тесты

```powershell
cd ..
.\run-tests.ps1 -InstallDeps
```

### Структура `server/src`

- `src/main.py` — сборка приложения
- `src/core/` — пути, конфиг, логирование
- `src/api/` — API-роуты
- `src/web/` — роуты страниц и редиректы
- `src/middlewares/` — middleware
- `src/services/` — бизнес-логика (работа с данными)
- `src/schemas/` — Pydantic-модели ответов
- `src/utils/` — утилиты
