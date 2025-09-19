#!/usr/bin/env python3
"""
diagnose.py - Диагностика и исправление проблем AIBot Direct

Этот скрипт проверяет все сервисы и дает точные инструкции по исправлению.
"""

import os
import subprocess
import sys
import time
import requests
from pathlib import Path

def run_command_safe(cmd, capture_output=True):
    """Безопасно выполнить команду."""
    try:
        if capture_output:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            return result.returncode == 0, result.stdout, result.stderr
        else:
            result = subprocess.run(cmd, check=False)
            return result.returncode == 0, "", ""
    except Exception as e:
        return False, "", str(e)

def print_header(text):
    """Красивый заголовок."""
    print(f"\n{'=' * 60}")
    print(f"🔍 {text}")
    print(f"{'=' * 60}")

def print_status(service, status, details=""):
    """Статус сервиса."""
    icon = "✅" if status else "❌"
    print(f"{icon} {service:<30} {details}")

def check_docker():
    """Проверка Docker."""
    print_header("ПРОВЕРКА DOCKER")
    
    # Docker установлен?
    success, _, _ = run_command_safe(["docker", "--version"])
    print_status("Docker установлен", success)
    
    if not success:
        print("💡 Установите Docker: curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh")
        return False
    
    # Docker запущен?
    success, _, _ = run_command_safe(["docker", "ps"])
    print_status("Docker запущен", success)
    
    if not success:
        print("💡 Запустите Docker: sudo systemctl start docker")
        return False
        
    return True

def check_containers():
    """Проверка контейнеров."""
    print_header("СТАТУС КОНТЕЙНЕРОВ")
    
    success, output, _ = run_command_safe(["docker", "compose", "-p", "localai", "ps", "--format", "table"])
    
    if not success:
        print_status("Docker Compose проект", False, "localai проект не найден")
        return False
    
    print(output)
    
    # Подсчет рабочих контейнеров
    lines = output.strip().split('\n')[1:]  # Пропустить заголовок
    running = sum(1 for line in lines if 'Up' in line or 'running' in line)
    total = len(lines)
    
    print(f"\n📊 Статистика: {running}/{total} контейнеров работают")
    
    return running > 0

def check_ports():
    """Проверка доступности портов."""
    print_header("ПРОВЕРКА ПОРТОВ")
    
    ports = {
        3000: "Open WebUI (Alenushka)",
        5678: "n8n Automation", 
        8003: "Flowise AI",
        8005: "Supabase Dashboard",
        8006: "SearXNG Search",
        8007: "Langfuse Analytics",
        11434: "Ollama API",
        9000: "Whisper API"
    }
    
    working_ports = []
    
    for port, name in ports.items():
        try:
            response = requests.get(f"http://localhost:{port}", timeout=5)
            success = response.status_code < 500
        except:
            success = False
        
        print_status(f":{port} {name}", success)
        if success:
            working_ports.append((port, name))
    
    print(f"\n📊 Доступно портов: {len(working_ports)}/{len(ports)}")
    
    if working_ports:
        print("\n🌐 РАБОЧИЕ ССЫЛКИ:")
        for port, name in working_ports:
            print(f"   • http://localhost:{port} - {name}")
    
    return len(working_ports) > 0

def check_logs():
    """Проверка логов проблемных сервисов."""
    print_header("АНАЛИЗ ЛОГОВ ОШИБОК")
    
    problematic_services = [
        "supabase-vector",
        "n8n-import", 
        "n8n",
        "supabase-db"
    ]
    
    for service in problematic_services:
        print(f"\n🔍 Логи {service}:")
        success, output, error = run_command_safe([
            "docker", "logs", "--tail", "10", f"localai-{service}-1"
        ])
        
        if success and output:
            print(f"   {output[:200]}...")
        elif success and error:
            print(f"   {error[:200]}...")
        else:
            print(f"   Контейнер {service} не найден или не запущен")

def fix_common_issues():
    """Исправление частых проблем."""
    print_header("АВТОМАТИЧЕСКОЕ ИСПРАВЛЕНИЕ")
    
    fixes = [
        ("Остановка конфликтующих контейнеров", ["docker", "compose", "-p", "localai", "down"]),
        ("Очистка Docker кэша", ["docker", "system", "prune", "-f"]),
        ("Очистка старых образов", ["docker", "image", "prune", "-f"]),
        ("Проверка свободного места", ["df", "-h", "/"]),
    ]
    
    for description, cmd in fixes:
        print(f"🔧 {description}...")
        success, output, error = run_command_safe(cmd)
        
        if success:
            print("   ✅ Выполнено")
            if "df" in cmd:
                # Показать использование диска
                lines = output.split('\n')
                for line in lines:
                    if '/' in line and '%' in line:
                        print(f"   📊 {line}")
        else:
            print(f"   ❌ Ошибка: {error[:100]}")

def minimal_start():
    """Минимальный запуск только критических сервисов."""
    print_header("МИНИМАЛЬНЫЙ ЗАПУСК")
    
    essential_services = [
        "postgres",
        "redis", 
        "ollama",
        "open-webui",
        "n8n"
    ]
    
    print("🚀 Запуск только критически важных сервисов...")
    
    for service in essential_services:
        print(f"   ⏳ Запуск {service}...")
        success, _, error = run_command_safe([
            "docker", "compose", "-p", "localai", "up", "-d", service
        ])
        
        if success:
            print(f"   ✅ {service} запущен")
        else:
            print(f"   ❌ {service} не запустился: {error[:100]}")
        
        time.sleep(2)  # Пауза между запусками

def generate_report():
    """Генерация отчета с рекомендациями."""
    print_header("ОТЧЕТ И РЕКОМЕНДАЦИИ")
    
    print("""
🎯 ПЛАН ДЕЙСТВИЙ:

1️⃣ СРОЧНЫЕ ИСПРАВЛЕНИЯ:
   • Добавьте swap памяти: sudo fallocate -l 2G /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile
   • Увеличьте timeout Docker: export COMPOSE_HTTP_TIMEOUT=600
   • Настройте Docker зеркала для обхода блокировок

2️⃣ АЛЬТЕРНАТИВНЫЕ РЕШЕНИЯ:
   • Используйте только localhost (без доменов SSL)
   • Запускайте сервисы по очереди, а не все сразу
   • Отключите проблемные сервисы (vector, analytics)

3️⃣ ДИАГНОСТИКА:
   • Проверьте логи: docker compose -p localai logs [service-name]
   • Мониторьте ресурсы: htop, df -h
   • Тестируйте порты: curl http://localhost:3000

4️⃣ ЭКСТРЕННЫЙ РЕЖИМ:
   • Запуск только Open WebUI: docker run -p 3000:8080 ghcr.io/open-webui/open-webui:main
   • Локальный Ollama: curl https://ollama.ai/install.sh | sh
""")

def main():
    """Главная функция диагностики."""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    🔧 AIBot Direct Doctor                    ║
║                                                              ║
║              Диагностика и исправление проблем               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    # Базовые проверки
    if not check_docker():
        print("\n❌ Docker не настроен. Исправьте и запустите снова.")
        return
    
    # Проверка текущего состояния
    containers_running = check_containers()
    ports_working = check_ports()
    
    # Если ничего не работает - исправляем
    if not containers_running and not ports_working:
        print("\n🚨 Система полностью не работает. Запускаем исправления...")
        fix_common_issues()
        minimal_start()
        
        # Повторная проверка
        print("\n🔄 Повторная проверка после исправлений...")
        time.sleep(10)
        check_containers()
        check_ports()
    
    # Анализ логов для диагностики
    check_logs()
    
    # Финальные рекомендации
    generate_report()

if __name__ == "__main__":
    main()
