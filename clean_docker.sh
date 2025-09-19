#!/bin/bash
# clean_docker.sh - Полная очистка AIBot Direct Docker окружения

echo "🧹 ПОЛНАЯ ОЧИСТКА AIBot Direct"
echo "======================================"

# Функция для печати статуса
print_status() {
    if [ $? -eq 0 ]; then
        echo "✅ $1"
    else
        echo "❌ $1 - ошибка (возможно, уже очищено)"
    fi
}

# 1. Остановка и удаление контейнеров проекта
echo ""
echo "🛑 Шаг 1: Остановка контейнеров AIBot Direct..."
docker compose -p localai down --remove-orphans
print_status "Контейнеры остановлены"

# 2. Удаление томов проекта
echo ""
echo "🗑️ Шаг 2: Удаление данных (volumes)..."
docker compose -p localai down -v
print_status "Данные удалены"

# 3. Удаление образов проекта (опционально)
echo ""
read -p "🤔 Удалить все скачанные образы Docker? Это освободит место, но потребует повторной загрузки (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🗑️ Удаление образов..."
    
    # Удаляем образы связанные с проектом
    docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.ID}}" | grep -E "(supabase|n8n|ollama|open-webui|flowise|qdrant|neo4j|searxng|langfuse|postgres|redis|caddy|whisper)" | awk '{print $3}' | xargs docker rmi -f 2>/dev/null
    print_status "Образы проекта удалены"
fi

# 4. Очистка системы Docker (удаляет неиспользуемые ресурсы)
echo ""
echo "🧽 Шаг 3: Очистка системы Docker..."
docker system prune -f
print_status "Система очищена"

# 5. Удаление .env файла
echo ""
echo "📝 Шаг 4: Очистка конфигурации..."
if [ -f ".env" ]; then
    rm .env
    print_status ".env файл удален"
else
    echo "ℹ️ .env файл не найден"
fi

# 6. Очистка папок данных (если есть)
echo ""
echo "📁 Шаг 5: Очистка локальных данных..."
folders_to_clean=("supabase" "neo4j" ".flowise")

for folder in "${folders_to_clean[@]}"; do
    if [ -d "$folder" ]; then
        rm -rf "$folder"
        print_status "Папка $folder удалена"
    fi
done

echo ""
echo "🎉 ОЧИСТКА ЗАВЕРШЕНА!"
echo "======================================"
echo ""
echo "🚀 Теперь можете запустить систему заново:"
echo "   python3 motherlode.py"
echo ""
echo "🌐 Или использовать GUI интерфейс:"
echo "   python3 setup_gui.py"
echo ""
