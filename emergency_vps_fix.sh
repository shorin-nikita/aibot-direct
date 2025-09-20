#!/bin/bash
# emergency_vps_fix.sh - Экстренное исправление для VPS

echo "🆘 ЭКСТРЕННОЕ ИСПРАВЛЕНИЕ ВМАПБДЯМ НА VPS"
echo "========================================"

# Остановить все контейнеры
echo "🛑 Остановка контейнеров..."
docker compose -p localai down --remove-orphans 2>/dev/null

# Исправить .env файл
echo "🔧 Исправление .env конфигурации..."
if [ -f ".env" ]; then
    # Исправить критические переменные
    sed -i 's/DOCKER_SOCKET_LOCATION=/DOCKER_SOCKET_LOCATION=\/var\/run\/docker.sock/g' .env
    
    # Добавить недостающие переменные
    if ! grep -q "POSTGRES_HOST=" .env; then
        echo "POSTGRES_HOST=db" >> .env
    fi
    if ! grep -q "POSTGRES_PORT=" .env; then
        echo "POSTGRES_PORT=5432" >> .env  
    fi
    if ! grep -q "POSTGRES_DB=" .env; then
        echo "POSTGRES_DB=postgres" >> .env
    fi
    if ! grep -q "SITE_URL=" .env; then
        echo "SITE_URL=http://localhost:3000" >> .env
    fi
    if ! grep -q "API_EXTERNAL_URL=" .env; then
        echo "API_EXTERNAL_URL=http://localhost:54321" >> .env
    fi
    
    echo "✅ .env файл исправлен"
else
    echo "❌ .env файл не найден! Пересоздайте его:"
    echo "python3 motherlode.py"
    exit 1
fi

# Упрощенный запуск без Supabase (которая вызывает проблемы)
echo "🚀 Запуск упрощенной версии ВМАПБДЯМ..."

# Создать упрощенный docker-compose
cat > docker-compose.simple.yml << 'EOF'
version: '3.8'

services:
  postgres:
    image: postgres:latest
    restart: unless-stopped
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:alpine
    restart: unless-stopped
    ports:
      - "6379:6379"
    command: redis-server --save 30 1
    volumes:
      - redis_data:/data

  ollama:
    image: ollama/ollama:latest
    restart: unless-stopped
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    environment:
      - OLLAMA_CONTEXT_LENGTH=8192

  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    restart: unless-stopped
    ports:
      - "3000:8080"
    volumes:
      - webui_data:/app/backend/data
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434

  n8n:
    image: n8nio/n8n:latest
    restart: unless-stopped  
    ports:
      - "5678:5678"
    environment:
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
      - DB_POSTGRESDB_USER=postgres
      - DB_POSTGRESDB_PASSWORD=${POSTGRES_PASSWORD}
      - DB_POSTGRESDB_DATABASE=postgres
      - N8N_ENCRYPTION_KEY=${N8N_ENCRYPTION_KEY}
    volumes:
      - n8n_data:/home/node/.n8n
    depends_on:
      - postgres

  flowise:
    image: flowiseai/flowise
    restart: unless-stopped
    ports:
      - "8003:3001"
    environment:
      - PORT=3001
      - FLOWISE_USERNAME=${FLOWISE_USERNAME}
      - FLOWISE_PASSWORD=${FLOWISE_PASSWORD}
    volumes:
      - flowise_data:/root/.flowise

volumes:
  postgres_data:
  redis_data:
  ollama_data:
  webui_data:
  n8n_data:
  flowise_data:
EOF

echo "📦 Запуск упрощенной системы..."
docker compose -f docker-compose.simple.yml up -d

echo "⏳ Ожидание запуска сервисов (60 секунд)..."
sleep 60

echo "🔍 Проверка статуса:"
docker compose -f docker-compose.simple.yml ps

echo "🌐 Получение внешнего IP..."
EXTERNAL_IP=$(curl -s ifconfig.me || curl -s ipinfo.io/ip || echo "31.128.36.9")

echo ""
echo "✅ ВМАПБДЯМ УПРОЩЕННАЯ ВЕРСИЯ ЗАПУЩЕНА!"
echo "======================================"
echo "🌐 Ваши сервисы доступны по адресам:"
echo "• http://$EXTERNAL_IP:3000 - Open WebUI (AI Чат)"
echo "• http://$EXTERNAL_IP:5678 - n8n (Автоматизация)"  
echo "• http://$EXTERNAL_IP:8003 - Flowise (AI Конструктор)"
echo "• http://$EXTERNAL_IP:11434 - Ollama API"
echo ""
echo "🔑 Данные для входа:"
echo "• Flowise: admin / $(grep FLOWISE_PASSWORD .env | cut -d'=' -f2)"
echo ""
echo "📊 Проверить статус: docker compose -f docker-compose.simple.yml ps"
echo "🛑 Остановить: docker compose -f docker-compose.simple.yml down"
