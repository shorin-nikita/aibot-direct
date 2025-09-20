#!/bin/bash
# fix_docker_socket.sh - Исправление проблемы с Docker socket

echo "🔧 ИСПРАВЛЕНИЕ ПРОБЛЕМЫ DOCKER SOCKET..."

# Исправить DOCKER_SOCKET_LOCATION в .env
if [ -f ".env" ]; then
    echo "📝 Исправление .env файла..."
    
    # Заменить пустую переменную на правильный путь
    sed -i 's/DOCKER_SOCKET_LOCATION=/DOCKER_SOCKET_LOCATION=\/var\/run\/docker.sock/g' .env
    
    # Добавить недостающие переменные если их нет
    grep -q "POSTGRES_HOST=" .env || echo "POSTGRES_HOST=db" >> .env
    grep -q "POSTGRES_PORT=" .env || echo "POSTGRES_PORT=5432" >> .env
    grep -q "POSTGRES_DB=" .env || echo "POSTGRES_DB=postgres" >> .env
    grep -q "SITE_URL=" .env || echo "SITE_URL=http://localhost:3000" >> .env
    grep -q "API_EXTERNAL_URL=" .env || echo "API_EXTERNAL_URL=http://localhost:54321" >> .env
    
    echo "✅ .env файл исправлен"
else
    echo "❌ .env файл не найден!"
    exit 1
fi

echo "🚀 Пробуем запустить систему заново..."

# Остановить все контейнеры
docker compose -p localai down --remove-orphans 2>/dev/null

# Запуск только критичных сервисов без Supabase
echo "🔄 Запуск базовых сервисов..."
docker compose up -d postgres redis ollama-cpu open-webui n8n flowise

echo "⏳ Ждем 30 секунд для запуска..."
sleep 30

echo "🔍 Проверка статуса:"
docker compose ps

echo "✅ ГОТОВО! Проверьте порты:"
echo "• http://$(curl -s ifconfig.me):3000 - Open WebUI"  
echo "• http://$(curl -s ifconfig.me):5678 - n8n"
echo "• http://$(curl -s ifconfig.me):8003 - Flowise"
