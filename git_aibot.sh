#!/bin/bash
# git_aibot.sh - AIBot Direct Git Helper

echo "🤖 AIBot Direct - AI Automation Platform"
echo "🌐 Website: https://AIBot.Direct"
echo "🏗️ Based on local-ai-packaged by Cole Medin"
echo "🤖 Ваша AI помощница: Alenushka"

case "${1:-help}" in
    "help"|"")
        echo ""
        echo "Команды:"
        echo "  git_aibot.sh install     - Установка AIBot Direct"
        echo "  git_aibot.sh status      - Статус системы"
        echo ""
        echo "Основные команды:"
        echo "  python aibot_start.py --profile cpu     # Стандартная установка"
        ;;
    "install")
        echo "🚀 Запускаю установку AIBot Direct..."
        python3 aibot_start.py --profile cpu
        ;;
    "status")
        echo "📊 Статус AIBot Direct:"
        docker compose -p localai ps 2>/dev/null || echo "Система не запущена"
        ;;
esac
