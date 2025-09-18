# 🤖 AIBot Direct - AI Automation Platform

**Чит-код для AI автоматизации вашего бизнеса**  
**Ваша персональная AI помощница Alenushka**

> 🌐 **Website**: [AIBot.Direct](https://AIBot.Direct)  
> 🏗️ **Основано на**: [local-ai-packaged](https://github.com/coleam00/local-ai-packaged) от Cole Medin  
> 📜 **Лицензия**: Apache 2.0 (все оригинальные права сохранены)

## 🚀 Супер простая установка

```bash
git clone -b stable https://github.com/shorin-nikita/aibot-direct.git
cd aibot-direct
python aibot_start.py --profile cpu
```

**Всё!** Через 5 минут у вас будет работать полная AI система.

## ✨ Что получаете

### 🤖 Alenushka - ваша AI помощница  
- ChatGPT-like интерфейс на русском языке
- Интеграция с российскими AI сервисами
- Готовые шаблоны для бизнеса

### 🏢 Готовые бизнес интеграции
- **Битрикс24** - автоматизация CRM
- **AmoCRM** - управление продажами
- **1С** - интеграция с учетными системами
- **Telegram боты** - готовые шаблоны

### 🔧 Простая настройка
- **Автоматические секреты** - все пароли генерируются автоматически
- **Интерактивная настройка Supabase** - система сама спросит нужные ключи
- **Безопасность из коробки** - криптографически стойкие пароли

## 🏗️ Что включено от Cole Medin

AIBot Direct наследует всю мощь local-ai-packaged:

| Компонент | Описание | Автор |
|-----------|----------|-------|
| **n8n** | Workflow automation (400+ интеграций) | n8n team + Cole |
| **Supabase** | Полная BaaS платформа | Cole Medin |
| **Open WebUI** | ChatGPT-like интерфейс | Cole Medin |
| **Ollama** | Локальные LLM модели | Cole Medin |
| **Qdrant** | Векторная база данных | Cole Medin |
| **Flowise** | AI agent builder | Cole Medin |
| **Neo4j** | Графы знаний | Cole Medin |
| **SearXNG** | Приватный поиск | Cole Medin |
| **Langfuse** | Мониторинг LLM | Cole Medin |
| **Caddy** | Автоматический HTTPS | Cole Medin |

**13 готовых AI сервисов из коробки!**

## 🆚 AIBot Direct vs Конкуренты

| Функция | AIBot Direct | ChatGPT | Claude | Другие |
|---------|-------------|---------|--------|--------|
| **Локальное развертывание** | ✅ | ❌ | ❌ | ❌ |
| **Русский интерфейс** | ✅ | Частично | Частично | ❌ |
| **Бизнес интеграции РФ** | ✅ | ❌ | ❌ | ❌ |
| **Полный контроль данных** | ✅ | ❌ | ❌ | ❌ |
| **Готовые workflow** | ✅ | ❌ | ❌ | Частично |
| **Telegram боты** | ✅ | Сложно | Сложно | ❌ |
| **Стоимость** | Бесплатно | $20/мес | $20/мес | Различно |

## 🎮 Команды управления

```bash
# Запуск (основная команда) - система спросит Supabase ключи
python aibot_start.py --profile cpu

# Для GPU Nvidia
python aibot_start.py --profile gpu-nvidia

# Публичное развертывание (с доменами)
python aibot_start.py --environment public

# Статус системы
docker compose -p localai ps

# Остановка
docker compose -p localai down

# Помощь
python aibot_start.py --help
```

## 🌐 Доступные интерфейсы

После запуска будут доступны:

- 🤖 **Alenushka (ваша AI помощница)**: http://localhost:3000
- ⚙️ **n8n (автоматизация)**: http://localhost:5678
- 🗄️ **Supabase (база данных)**: http://localhost:8005
- 🔧 **Flowise (AI builder)**: http://localhost:8003
- 📊 **Мониторинг**: http://localhost:8007

## 💡 Почему AIBot Direct?

### 🇷🇺 Создано для России
- Полная локализация на русский язык
- Интеграция с российскими сервисами
- Готовые решения для местного бизнеса
- Соответствие требованиям по хранению данных

### 🚀 Максимально просто
- Одна команда для установки
- Автоматическая генерация большинства секретов
- Интерактивная настройка только Supabase ключей
- Localhost или собственные домены на выбор

### 🏢 Готов к бизнесу
- Шаблоны для CRM систем
- Telegram боты из коробки
- Интеграция с учетными системами
- Масштабируемая архитектура

## 🙏 Огромная благодарность

**Cole Medin** создал революционную local-ai-packaged систему, без которой AIBot Direct был бы невозможен.

- [Оригинальный проект Cole](https://github.com/coleam00/local-ai-packaged)
- [YouTube канал Cole](https://www.youtube.com/@ColeMedin)

**n8n команде** за отличную платформу автоматизации.

## 🏆 Кто мы

**AIBot Direct** - российская команда разработчиков, специализирующаяся на AI автоматизации для бизнеса.

- 🌐 **Website**: [AIBot.Direct](https://AIBot.Direct)
- 📧 **Email**: team@aibot.direct
- 💬 **Telegram**: @aibot_direct_support

## 📜 Лицензия

Apache License 2.0 - все оригинальные авторские права сохранены.

---

🤖 **AIBot Direct** - превращаем мечты об AI автоматизации в реальность!  
🇷🇺 **Made in Russia** with ❤️ based on Cole's innovation  
🌐 **Больше на**: [AIBot.Direct](https://AIBot.Direct)
