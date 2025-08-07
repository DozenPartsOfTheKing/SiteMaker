# Empire Agency - FastAPI Service

🚀 Быстрый и современный веб-сервис для агентства Empire Анны Чернавских.

## 🎯 Возможности

- ⚡ **FastAPI** - современный и быстрый веб-фреймворк
- 🎨 **Красивый UI** - адаптивный дизайн с Tailwind CSS
- 📱 **Мобильная версия** - отлично выглядит на всех устройствах
- 🔧 **API endpoints** - для интеграции с другими сервисами
- 🐳 **Docker поддержка** - легкое развертывание

## 🚀 Быстрый старт

### Локальный запуск

1. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

2. **Запустите сервер:**
```bash
python main.py
```

3. **Откройте в браузере:**
```
http://localhost:8000
```

### Docker запуск

1. **Соберите и запустите с Docker Compose:**
```bash
docker-compose up --build
```

2. **Или используйте Docker напрямую:**
```bash
docker build -t empire-agency .
docker run -p 8000:8000 empire-agency
```

## 📋 API Endpoints

- `GET /` - Главная страница
- `GET /health` - Проверка состояния сервиса
- `GET /api/info` - Информация об агентстве
- `GET /static/*` - Статические файлы

## 🛠️ Разработка

### Структура проекта
```
SiteMaker/
├── main.py              # FastAPI приложение
├── requirements.txt      # Python зависимости
├── Dockerfile           # Docker конфигурация
├── docker-compose.yml   # Docker Compose
├── static/
│   └── app.html        # Главная страница
└── README.md           # Документация
```

### Переменные окружения
- `PYTHONPATH=/app` - путь к приложению
- `PYTHONUNBUFFERED=1` - небуферизованный вывод

## 🔧 Технологии

- **Backend:** FastAPI + Uvicorn
- **Frontend:** HTML + Tailwind CSS + JavaScript
- **Container:** Docker + Docker Compose
- **Language:** Python 3.11

## 📞 Контакты

- **Телефон:** +7 (906) 770-07-03
- **Email:** pr@empireagency.ru
- **WhatsApp:** https://wa.me/79067700703
- **Telegram:** @agencyempire

## 🎨 Особенности дизайна

- Градиентные эффекты
- Анимации при скролле
- Адаптивная навигация
- Современный UI/UX
- Оптимизация для мобильных устройств

---

**Empire Agency** - создаем истории, которые запоминаются! ✨ 