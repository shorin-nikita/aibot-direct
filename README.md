# 🤖 AIBot Direct - Российская AI Платформа

**AIBot Direct** - это простая и надежная российская AI платформа для автоматизации бизнеса. Основана на проверенных open-source решениях с российской локализацией.

## 🎯 Что это?

- 🤖 **Полноценная AI платформа** для российского бизнеса  
- 🗣️ **Русский интерфейс** и поддержка кириллицы
- 🏢 **Готовые интеграции** с Битрикс24, AmoCRM, 1С
- 📱 **Telegram боты** для автоматизации
- 🔒 **Безопасная установка** на VPS

## 🚀 Быстрый старт (3 минуты)

### На VPS сервере:

```bash
# 1. Клонируем проект
git clone https://github.com/shorin-nikita/aibot-direct.git
cd aibot-direct

# 2. Запускаем автоустановку
python3 auto_setup.py

# 3. Следуем инструкциям!
```

**Всё!** Больше ничего делать не нужно.

## 🎛️ Конфигурации

### 🎯 MINIMAL (рекомендуется для старта)
- **N8N** - автоматизация бизнес-процессов
- **Supabase** - база данных и API
- **Caddy** - SSL и проксирование

**Домены**: `n8n.yourdomain.com`, `db.yourdomain.com`

### 🚀 FULL (полные возможности)
- Всё из MINIMAL +
- **OpenWebUI** - чат с AI на русском языке  
- **Flowise** - конструктор AI агентов
- **Langfuse** - аналитика AI взаимодействий
- **Neo4j** - граф база данных

**Домены**: `chat.yourdomain.com`, `flow.yourdomain.com`, `analytics.yourdomain.com`

## 🔑 Что нужно подготовить

### До запуска:
1. **VPS сервер** (Ubuntu/Debian)
2. **Домены** и настроенные DNS записи
3. **Supabase ключи** (генерируются [здесь](https://supabase.com/docs/guides/self-hosting/docker#generate-api-keys))

### Автоматически настроится:
- ✅ Docker и все зависимости
- ✅ SSL сертификаты (Let's Encrypt)  
- ✅ Firewall (порты 80, 443, SSH)
- ✅ Все секретные ключи
- ✅ База данных и конфигурации

## 📋 После установки

### MINIMAL конфигурация:
- 🔧 **N8N**: `https://n8n.yourdomain.com` - создание автоматизаций
- 🗄️ **Supabase**: `https://db.yourdomain.com` - управление данными

### FULL конфигурация:  
- 💬 **AI Chat**: `https://chat.yourdomain.com` - общение с AI на русском
- 🔄 **Flowise**: `https://flow.yourdomain.com` - создание AI агентов
- 📊 **Analytics**: `https://analytics.yourdomain.com` - аналитика AI

## 🏢 Готовые решения для бизнеса

### 📱 Telegram автоматизация
- Прием заказов через Telegram ботов
- Автоматические ответы клиентам  
- Уведомления о новых заявках

### 🗂️ CRM интеграции
- **Битрикс24** - автоматический анализ лидов
- **AmoCRM** - синхронизация сделок
- **1С** - обмен данными

### 🎤 Голосовые возможности
- Распознавание русской речи
- Голосовые заказы через Telegram
- Автоматические транскрипции

## 🛠️ Управление

```bash
# Статус сервисов
docker ps

# Логи
docker compose logs -f

# Остановка
docker compose down

# Перезапуск  
python3 start_services.py --profile cpu --environment public
```

## 🔒 Безопасность

- ✅ Все пароли генерируются автоматически
- ✅ Файл `.env` защищен (права 600)
- ✅ Открыты только порты 80, 443, SSH
- ✅ SSL сертификаты от Let's Encrypt
- ✅ Валидация всех входных данных

## 📚 Документация

- **[Быстрый старт](QUICKSTART.md)** - пошаговая установка
- **[Развертывание на VPS](DEPLOY.md)** - настройка сервера
- **[Примеры интеграций](n8n-tool-workflows/)** - готовые workflow'ы

## 🆘 Проблемы?

### Типичные решения:
```bash
# Если контейнеры не запускаются
docker compose down && docker compose pull
python3 auto_setup.py

# Если нет доступа к сайтам
# Проверьте DNS записи: A record домен → IP сервера

# Если ошибки SSL
# Подождите 5-10 минут после настройки DNS
```

### Поддержка:
- 📧 **Email**: support@aibot.direct
- 💬 **Telegram**: @aibot_support  
- 🐛 **Issues**: [GitHub Issues](https://github.com/shorin-nikita/aibot-direct/issues)

## 🙏 Благодарности

Благодарность **Cole Medin** за базовую архитектуру [local-ai-packaged](https://github.com/coleam00/local-ai-packaged), которая была адаптирована для российского рынка.

## 📜 Лицензия  

Apache License 2.0 - используйте свободно в коммерческих проектах.

---

🤖 **AIBot Direct** - простая российская AI платформа  
🇷🇺 **Made in Russia** для российского бизнеса  
🌐 **Сайт**: https://aibot.direct