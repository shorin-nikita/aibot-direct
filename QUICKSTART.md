# ⚡ Быстрый старт AIBot Direct

## 🎯 За 5 минут от установки до работы

### Шаг 1: Подготовка сервера
```bash
# На Ubuntu/Debian VPS
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 git docker.io docker-compose-plugin
sudo usermod -aG docker $USER
newgrp docker
```

### Шаг 2: Клонирование и запуск
```bash
git clone https://github.com/shorin-nikita/aibot-direct.git
cd aibot-direct
python3 auto_setup.py
```

### Шаг 3: Выбираете конфигурацию
- **1 (MINIMAL)** - N8N + Supabase (для начала)
- **2 (FULL)** - Полный AI стек (все возможности)

### Шаг 4: Вводите данные
- Email для SSL сертификатов
- Домены (например: `n8n.yourdomain.com`)  
- [Supabase ключи](https://supabase.com/docs/guides/self-hosting/docker#generate-api-keys)

### Шаг 5: Готово! 🎉

Через 5-10 минут все сервисы будут доступны по вашим доменам с SSL.

## 🔑 Подготовка Supabase ключей

1. Перейдите на: https://supabase.com/docs/guides/self-hosting/docker#generate-api-keys
2. Сгенерируйте 3 ключа:
   - **JWT_SECRET** (32+ символа)
   - **ANON_KEY** (длинный JWT токен)
   - **SERVICE_ROLE_KEY** (длинный JWT токен)

## 🌐 Настройка DNS

**До запуска** создайте A-записи:

### Для MINIMAL:
```
n8n.yourdomain.com → IP_СЕРВЕРА
db.yourdomain.com → IP_СЕРВЕРА
```

### Для FULL:
```
n8n.yourdomain.com → IP_СЕРВЕРА  
db.yourdomain.com → IP_СЕРВЕРА
chat.yourdomain.com → IP_СЕРВЕРА
flow.yourdomain.com → IP_СЕРВЕРА
analytics.yourdomain.com → IP_СЕРВЕРА
```

## 🎯 После установки

### MINIMAL - доступные сервисы:
- **N8N**: `https://n8n.yourdomain.com` - автоматизация
- **Supabase**: `https://db.yourdomain.com` - база данных

### FULL - дополнительно:
- **Chat**: `https://chat.yourdomain.com` - AI чат на русском
- **Flowise**: `https://flow.yourdomain.com` - AI конструктор  
- **Analytics**: `https://analytics.yourdomain.com` - аналитика

## 🛠️ Первые шаги в N8N

1. Откройте `https://n8n.yourdomain.com`
2. Создайте аккаунт (локальный, не на сервисе N8N)
3. Импортируйте готовые workflow'ы из папки `n8n-tool-workflows/`
4. Настройте интеграции с вашими CRM/Telegram

## 📱 Настройка Telegram бота

1. Создайте бота через @BotFather
2. Получите токен бота
3. В N8N используйте Telegram Trigger
4. Настройте webhook для приема сообщений

## 🏢 Интеграция с CRM

### Битрикс24:
1. Получите входящий webhook в Битрикс24
2. В N8N используйте HTTP Request node
3. Импортируйте готовый workflow из `n8n-tool-workflows/`

### AmoCRM:
1. Создайте интеграцию в AmoCRM
2. Получите access_token
3. Используйте готовые workflow'ы

## ❓ Часто задаваемые вопросы

### Q: Сколько времени занимает установка?
**A:** 5-10 минут активной работы + 5-15 минут ожидания (загрузка Docker образов, SSL сертификаты)

### Q: Какие домены использовать?
**A:** Любые поддомены вашего основного домена. Например: `ai.company.com`, `crm.company.com`

### Q: Что делать если SSL не работает?
**A:** 
1. Проверьте DNS записи (`nslookup yourdomain.com`)
2. Подождите до 24 часов распространения DNS
3. Перезапустите: `docker compose restart caddy`

### Q: Можно ли изменить конфигурацию?
**A:** Да! Отредактируйте `.env` файл и выполните `docker compose up -d`

### Q: Как обновить?
**A:**
```bash
docker compose down
docker compose pull  
python3 start_services.py --profile cpu --environment public
```

## 🔧 Устранение проблем

### Если контейнеры не запускаются:
```bash
# Проверить логи
docker compose logs

# Полная переустановка
docker compose down -v
python3 auto_setup.py
```

### Если нет доступа к интерфейсам:
1. Проверьте статус: `docker ps`
2. Проверьте порты: `sudo ufw status`
3. Проверьте DNS: `nslookup n8n.yourdomain.com`

### Если ошибки в N8N:
1. Проверьте подключение к базе данных
2. Убедитесь что Supabase запущен: `docker ps | grep supabase`
3. Проверьте .env файл на корректность ключей

## 📞 Помощь

- 🐛 **Баги**: [GitHub Issues](https://github.com/shorin-nikita/aibot-direct/issues)
- 💬 **Telegram**: @aibot_support
- 📧 **Email**: support@aibot.direct

---

🚀 **Готово!** Теперь у вас есть полноценная российская AI платформа!
