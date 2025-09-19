#!/bin/bash
# emergency_fix.sh - Экстренное исправление AIBot Direct

echo "🚨 ЭКСТРЕННОЕ ИСПРАВЛЕНИЕ AIBot Direct"
echo "========================================"

# Функция для печати статуса
print_status() {
    if [ $? -eq 0 ]; then
        echo "✅ $1"
    else
        echo "❌ $1 - ОШИБКА"
    fi
}

# 1. Остановка всех контейнеров
echo "🛑 Остановка всех контейнеров..."
docker compose -p localai down
print_status "Остановка контейнеров"

# 2. Очистка системы
echo "🧹 Очистка Docker системы..."
docker system prune -f
docker image prune -f
print_status "Очистка системы"

# 3. Проверка ресурсов
echo "📊 Проверка ресурсов системы..."
echo "💾 Память:"
free -h
echo "💿 Диск:"
df -h /

# 4. Добавление swap если нужно
if [ ! -f /swapfile ]; then
    echo "💫 Создание swap файла..."
    sudo fallocate -l 2G /swapfile
    sudo chmod 600 /swapfile  
    sudo mkswap /swapfile
    sudo swapon /swapfile
    print_status "Создание swap"
fi

# 5. Настройка Docker timeout
echo "⏱️ Увеличение timeout..."
export COMPOSE_HTTP_TIMEOUT=600
export DOCKER_CLIENT_TIMEOUT=600
print_status "Настройка timeout"

# 6. Проверка портов
echo "🔍 Проверка занятых портов..."
netstat -tulpn | grep -E ":(3000|5678|8003|8005|8006|8007|9000|11434)" | head -5

# 7. Минимальный запуск
echo "🚀 МИНИМАЛЬНЫЙ ЗАПУСК (только критические сервисы)"
echo "=================================================="

# Запуск по очереди с паузами
services=("postgres" "redis" "ollama" "open-webui" "n8n")

for service in "${services[@]}"; do
    echo "⏳ Запуск $service..."
    docker compose -p localai up -d $service
    if [ $? -eq 0 ]; then
        echo "✅ $service запущен"
        sleep 5  # Пауза между запусками
    else
        echo "❌ $service не запустился"
    fi
done

# 8. Проверка результата
echo "🔍 Проверка состояния..."
sleep 10
docker compose -p localai ps

# 9. Тест портов
echo "🌐 Тест доступности..."
ports=(3000 5678 8003 11434)

for port in "${ports[@]}"; do
    if curl -s --connect-timeout 5 http://localhost:$port > /dev/null; then
        echo "✅ :$port доступен"
    else
        echo "❌ :$port недоступен"
    fi
done

echo ""
echo "🎯 РЕЗУЛЬТАТ:"
echo "============="
echo "Если порты доступны - система работает!"
echo ""
echo "🌐 Попробуйте открыть:"
echo "• http://$(hostname -I | awk '{print $1}'):3000 - Open WebUI"  
echo "• http://$(hostname -I | awk '{print $1}'):5678 - n8n"
echo "• http://$(hostname -I | awk '{print $1}'):8003 - Flowise"
echo ""
echo "📝 Если не работает, выполните:"
echo "python3 diagnose.py"
