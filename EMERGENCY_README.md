# 🚨 ЭКСТРЕННОЕ ИСПРАВЛЕНИЕ AIBot Direct

## 🎯 У вас есть 3 готовых решения:

### 🚀 **Решение 1: Экстренное исправление (РЕКОМЕНДУЕТСЯ)**
```bash
cd aibot-direct
bash emergency_fix.sh
```
**Что делает:**
- ✅ Останавливает все сломанные контейнеры
- ✅ Очищает систему от мусора  
- ✅ Добавляет swap память
- ✅ Запускает только критические сервисы
- ✅ Тестирует доступность портов

### 🔍 **Решение 2: Полная диагностика**
```bash
cd aibot-direct
python3 diagnose.py
```
**Что делает:**
- 🔍 Проверяет Docker, контейнеры, порты
- 📊 Показывает статистику системы
- 📋 Анализирует логи ошибок
- 💡 Дает конкретные рекомендации

### 🛠️ **Решение 3: Ручные команды**
Если скрипты не работают:

```bash
# Остановка всего
docker compose -p localai down

# Очистка
docker system prune -f

# Добавление памяти
sudo fallocate -l 2G /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile

# Запуск только основного
docker compose -p localai up -d postgres redis ollama open-webui n8n

# Проверка
docker compose -p localai ps
```

## 🌐 **После исправления проверьте:**

- **Open WebUI (Alenushka):** `http://ВАШ_IP:3000`
- **n8n Automation:** `http://ВАШ_IP:5678` 
- **Flowise AI:** `http://ВАШ_IP:8003`

## ❓ **Если ничего не помогает:**

1. **Проверьте память:** `free -h`
2. **Проверьте диск:** `df -h`
3. **Посмотрите логи:** `docker compose -p localai logs --tail 20`

## 🆘 **Минимальный запуск Open WebUI:**
```bash
# Если вообще ничего не работает
docker run -d -p 3000:8080 --name emergency-ai ghcr.io/open-webui/open-webui:main
```

Тогда AI будет доступен на `http://ВАШ_IP:3000`

---
**📞 Техподдержка:** Если проблемы остаются, покажите результат команды: `bash emergency_fix.sh`
