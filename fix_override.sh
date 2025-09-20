#!/bin/bash
# 🔧 ЭКСТРЕННОЕ ИСПРАВЛЕНИЕ: Создание недостающего docker-compose.override.private.yml
# Для VPS 46.173.27.199

echo "🔧 ИСПРАВЛЯЕМ ОШИБКУ: docker-compose.override.private.yml"

# Создаем недостающий файл
cat > docker-compose.override.private.yml << 'EOF'
# Override для приватного режима (localhost/VPS без доменов)  
# Автоматически создано fix_override.sh

services:
  # Все сервисы используют стандартные порты без SSL/доменов
  # Этот файл нужен для совместимости с оригинальным start_services.py
  
  # Заглушка - никаких дополнительных настроек не требуется
  # Все сервисы уже настроены в основном docker-compose.yml
EOF

echo "✅ Файл docker-compose.override.private.yml создан"

# Перезапускаем систему
echo "🚀 Перезапуск системы..."
python3 start_services.py --profile cpu

echo "🎯 Исправление завершено!"
echo "🌐 Проверьте http://46.173.27.199:3000 (Open WebUI)"
echo "⚙️ Проверьте http://46.173.27.199:5678 (n8n)"
