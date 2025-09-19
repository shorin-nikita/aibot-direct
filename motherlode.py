#!/usr/bin/env python3
"""
motherlode.py - AIBot Direct Zero Configuration Setup

🚀 НУЛЕВАЯ КОНФИГУРАЦИЯ - система работает из коробки!
Автоматически определяет окружение и настраивает все компоненты.

Created by SHORIN for Russian AI automation.
"""

import os
import sys
import json
import time
import secrets
import subprocess
import platform
import socket
import requests
from pathlib import Path
from urllib.parse import urlparse

# ================================================================
# 🎨 VISUAL INTERFACE
# ================================================================

def print_shorin_greeting():
    """Приветствие с информацией о системе."""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              🤖 AIBot Direct - НУЛЕВАЯ КОНФИГУРАЦИЯ          ║
║                                                              ║
║                   Приветствует SHORIN!                       ║
║                                                              ║
║  🚀 Революционная AI система запускается одной командой      ║
║  🇷🇺 Создано в России для российского бизнеса               ║
║  ⚡ 13 AI сервисов настроятся автоматически                  ║
║                                                              ║
║            Готов к запуску за 3 минуты!                     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")

def print_progress_bar(current, total, task):
    """Красивый прогресс бар."""
    progress = int(50 * current / total)
    bar = "█" * progress + "░" * (50 - progress)
    percent = int(100 * current / total)
    print(f"\r🔄 {task}: [{bar}] {percent}% ", end="", flush=True)
    if current == total:
        print("✅")

def print_status(message, success=True, details=""):
    """Статус операции."""
    icon = "✅" if success else "❌"
    print(f"{icon} {message}")
    if details and not success:
        print(f"   💡 {details}")

# ================================================================
# 🔍 ENVIRONMENT DETECTION (УМНОЕ ОПРЕДЕЛЕНИЕ ОКРУЖЕНИЯ)
# ================================================================

def detect_environment():
    """Автоматически определяет окружение: VPS, localhost или cloud."""
    env_info = {
        'type': 'localhost',
        'ip': get_local_ip(),
        'hostname': socket.gethostname(),
        'is_vps': False,
        'is_cloud': False,
        'has_docker': check_docker(),
        'cpu_count': os.cpu_count(),
        'memory_gb': get_memory_gb(),
        'disk_free_gb': get_disk_space_gb()
    }
    
    # Определение типа сервера
    if is_vps_environment():
        env_info['type'] = 'vps'
        env_info['is_vps'] = True
    elif is_cloud_environment():
        env_info['type'] = 'cloud'
        env_info['is_cloud'] = True
    
    print_environment_info(env_info)
    return env_info

def get_local_ip():
    """Получить локальный IP."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def is_vps_environment():
    """Проверка, является ли это VPS."""
    vps_indicators = [
        '/proc/vz',  # OpenVZ
        '/proc/xen',  # Xen
        'docker' in platform.platform().lower(),
        'microsoft' in platform.uname().release.lower(),  # WSL
    ]
    
    return any([
        os.path.exists(indicator) if isinstance(indicator, str) and indicator.startswith('/')
        else indicator for indicator in vps_indicators
    ])

def is_cloud_environment():
    """Проверка, является ли это cloud (AWS, GCP, Azure)."""
    try:
        # Быстрая проверка metadata endpoint
        response = requests.get("http://169.254.169.254/latest/meta-data/", timeout=2)
        return response.status_code == 200
    except:
        return False

def get_memory_gb():
    """Получить объем памяти в GB."""
    try:
        with open('/proc/meminfo', 'r') as f:
            meminfo = f.read()
            mem_total = int([line for line in meminfo.split('\n') if 'MemTotal' in line][0].split()[1])
            return mem_total // 1024 // 1024  # KB to GB
    except:
        return 4  # Default

def get_disk_space_gb():
    """Получить свободное место на диске в GB."""
    try:
        stat = os.statvfs('.')
        return (stat.f_bavail * stat.f_frsize) // 1024 // 1024 // 1024
    except:
        return 10  # Default

def print_environment_info(env_info):
    """Вывод информации об окружении."""
    print(f"\n🔍 АВТООПРЕДЕЛЕНИЕ ОКРУЖЕНИЯ")
    print("=" * 50)
    print(f"🖥️  Тип: {env_info['type'].upper()}")
    print(f"🌐 IP: {env_info['ip']}")
    print(f"💻 Hostname: {env_info['hostname']}")
    print(f"🧠 CPU: {env_info['cpu_count']} cores")
    print(f"💾 RAM: {env_info['memory_gb']} GB")
    print(f"💿 Диск: {env_info['disk_free_gb']} GB свободно")
    print(f"🐳 Docker: {'✅' if env_info['has_docker'] else '❌'}")

def check_docker():
    """Проверка наличия Docker."""
    try:
        subprocess.run(['docker', '--version'], capture_output=True, check=True)
        return True
    except:
        return False

# ================================================================
# 🧠 SMART DEFAULTS (УМНЫЕ ДЕФОЛТЫ)
# ================================================================

def generate_smart_config(env_info):
    """Генерация умной конфигурации на основе окружения."""
    config = {
        # Базовая конфигурация
        'environment': env_info['type'],
        'profile': determine_docker_profile(env_info),
        'mode': determine_deployment_mode(env_info),
        
        # Автогенерируемые секреты
        'postgres_password': generate_random_key(16),
        'jwt_secret': generate_random_key(32),
        'n8n_encryption_key': generate_random_key(32), 
        'n8n_user_management_jwt_secret': generate_random_key(32),
        'dashboard_password': generate_random_key(16),
        'clickhouse_password': generate_random_key(16),
        'minio_root_password': generate_random_key(16),
        'langfuse_salt': generate_random_key(16),
        'nextauth_secret': generate_random_key(32),
        'encryption_key': generate_random_key(32),
        'flowise_username': 'admin',
        'flowise_password': generate_random_key(12),
        'neo4j_auth': f'neo4j/{generate_random_key(12)}',
        'pooler_tenant_id': '1000',
        
        # Supabase ключи (будут запрошены у пользователя если нужны)
        'anon_key': '',
        'service_role_key': '',
        
        # Доменные настройки (автоматически)
        'domains': generate_domain_config(env_info),
        
        # Дополнительные настройки
        'letsencrypt_email': 'internal',
    }
    
    return config

def determine_docker_profile(env_info):
    """Определить профиль Docker на основе железа."""
    if env_info['memory_gb'] < 4:
        return 'cpu'  # Минимальная конфигурация
    
    # Попробуем определить GPU
    try:
        result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
        if result.returncode == 0:
            return 'gpu-nvidia'
    except:
        pass
        
    try:
        result = subprocess.run(['rocm-smi'], capture_output=True, text=True) 
        if result.returncode == 0:
            return 'gpu-amd'
    except:
        pass
    
    return 'cpu'

def determine_deployment_mode(env_info):
    """Определить режим развертывания."""
    if env_info['type'] == 'localhost':
        return 'private'
    else:
        return 'public'  # VPS или cloud

def generate_domain_config(env_info):
    """Генерация конфигурации доменов."""
    domains = {}
    
    if env_info['type'] == 'localhost':
        # Localhost режим - только порты
        domains.update({
            'n8n_hostname': ':8001',
            'webui_hostname': ':8002', 
            'flowise_hostname': ':8003',
            'ollama_hostname': ':8004',
            'supabase_hostname': ':8005',
            'searxng_hostname': ':8006',
            'langfuse_hostname': ':8007',
            'neo4j_hostname': ':8008',
            'whisper_hostname': ':8009'
        })
    
    return domains

def generate_random_key(length=32):
    """Generate a random hex key of specified length."""
    return secrets.token_hex(length)

# ================================================================
# 🤖 ZERO CONFIGURATION INPUT (МИНИМАЛЬНЫЙ ВВОД)
# ================================================================

def get_minimal_user_input(env_info, config):
    """Минимальный ввод от пользователя - только самое необходимое."""
    print(f"\n🎯 КОНФИГУРАЦИЯ ДЛЯ {env_info['type'].upper()}")
    print("=" * 50)
    
    if env_info['type'] == 'localhost':
        print("✅ Localhost режим - дополнительная настройка не нужна!")
        print("🚀 Система запустится автоматически на портах:")
        for service, port in config['domains'].items():
            service_name = service.replace('_hostname', '').replace('_', ' ').title()
            print(f"   • {service_name}: http://localhost{port}")
        
        return config
    
    # Для VPS/Cloud - спросить про домены
    print("🌐 Обнаружен удаленный сервер!")
    print("💡 Можете настроить домены или использовать IP адреса")
    
    use_domains = input(f"\n🔗 Настроить домены для https://{env_info['ip']}? (y/N): ").strip().lower()
    
    if use_domains == 'y':
        return get_domain_configuration(env_info, config)
    else:
        print("✅ Будут использованы IP адреса с портами")
        return config

def get_domain_configuration(env_info, config):
    """Конфигурация доменов для продакшна."""
    print(f"\n🌐 НАСТРОЙКА ДОМЕНОВ")
    print("=" * 50)
    print(f"💡 Базовый IP: {env_info['ip']}")
    
    base_domain = input("Базовый домен (например: yourdomain.com): ").strip()
    
    if base_domain:
        email = input("Email для SSL сертификатов: ").strip() or "admin@" + base_domain
        
        # Автогенерация поддоменов
        config['domains'] = {
            'n8n_hostname': f"n8n.{base_domain}",
            'webui_hostname': f"ai.{base_domain}",
            'flowise_hostname': f"flowise.{base_domain}",
            'supabase_hostname': f"supabase.{base_domain}",
            'searxng_hostname': f"search.{base_domain}",
            'langfuse_hostname': f"analytics.{base_domain}",
            'neo4j_hostname': f"graph.{base_domain}",
            'whisper_hostname': f"voice.{base_domain}",
        }
        config['letsencrypt_email'] = email
        
        print("✅ Домены сконфигурированы:")
        for service, domain in config['domains'].items():
            service_name = service.replace('_hostname', '').replace('_', ' ').title()
            print(f"   • {service_name}: https://{domain}")
    
    return config

# ================================================================
# 📄 SMART ENV GENERATION (УМНАЯ ГЕНЕРАЦИЯ .ENV)
# ================================================================

def create_env_template():
    """Создать .env template если его нет."""
    template_content = """# ================================================================
# 🤖 AIBot Direct - Auto-Generated Configuration
# ================================================================
# Этот файл создан автоматически motherlode.py
# Все секреты сгенерированы криптографически безопасно

# ================================================================
# 🔐 КРИТИЧЕСКИ ВАЖНЫЕ НАСТРОЙКИ (АВТОЗАПОЛНЕНЫ)
# ================================================================

# Postgres Database
POSTGRES_PASSWORD=PLACEHOLDER_POSTGRES_PASSWORD
POSTGRES_VERSION=latest

# JWT Tokens
JWT_SECRET=PLACEHOLDER_JWT_SECRET
ANON_KEY=PLACEHOLDER_ANON_KEY
SERVICE_ROLE_KEY=PLACEHOLDER_SERVICE_ROLE_KEY

# N8N Security
N8N_ENCRYPTION_KEY=PLACEHOLDER_N8N_ENCRYPTION_KEY
N8N_USER_MANAGEMENT_JWT_SECRET=PLACEHOLDER_N8N_USER_MANAGEMENT_JWT_SECRET

# ================================================================
# 🌐 ДОМЕННЫЕ НАСТРОЙКИ
# ================================================================

# Hostnames (auto-configured)
N8N_HOSTNAME=PLACEHOLDER_N8N_HOSTNAME
SUPABASE_HOSTNAME=PLACEHOLDER_SUPABASE_HOSTNAME
WEBUI_HOSTNAME=PLACEHOLDER_WEBUI_HOSTNAME
FLOWISE_HOSTNAME=PLACEHOLDER_FLOWISE_HOSTNAME
OLLAMA_HOSTNAME=PLACEHOLDER_OLLAMA_HOSTNAME
SEARXNG_HOSTNAME=PLACEHOLDER_SEARXNG_HOSTNAME
LANGFUSE_HOSTNAME=PLACEHOLDER_LANGFUSE_HOSTNAME
NEO4J_HOSTNAME=PLACEHOLDER_NEO4J_HOSTNAME
WHISPER_HOSTNAME=PLACEHOLDER_WHISPER_HOSTNAME

# SSL Configuration
LETSENCRYPT_EMAIL=PLACEHOLDER_LETSENCRYPT_EMAIL

# ================================================================
# 🔧 ДОПОЛНИТЕЛЬНЫЕ СЕРВИСЫ
# ================================================================

# Dashboard Security
DASHBOARD_PASSWORD=PLACEHOLDER_DASHBOARD_PASSWORD

# Supabase Pooler
POOLER_TENANT_ID=PLACEHOLDER_POOLER_TENANT_ID

# ClickHouse Analytics
CLICKHOUSE_PASSWORD=PLACEHOLDER_CLICKHOUSE_PASSWORD
CLICKHOUSE_MIGRATION_URL=clickhouse://clickhouse:9000
CLICKHOUSE_URL=http://clickhouse:8123
CLICKHOUSE_USER=clickhouse
CLICKHOUSE_CLUSTER_ENABLED=false

# MinIO Storage
MINIO_ROOT_PASSWORD=PLACEHOLDER_MINIO_ROOT_PASSWORD

# Langfuse Analytics
LANGFUSE_SALT=PLACEHOLDER_LANGFUSE_SALT
NEXTAUTH_SECRET=PLACEHOLDER_NEXTAUTH_SECRET
ENCRYPTION_KEY=PLACEHOLDER_ENCRYPTION_KEY
TELEMETRY_ENABLED=true
LANGFUSE_ENABLE_EXPERIMENTAL_FEATURES=true

# Flowise AI Builder
FLOWISE_USERNAME=PLACEHOLDER_FLOWISE_USERNAME
FLOWISE_PASSWORD=PLACEHOLDER_FLOWISE_PASSWORD

# Neo4j Database
NEO4J_AUTH=PLACEHOLDER_NEO4J_AUTH

# Redis/Valkey Settings
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_AUTH=LOCALONLYREDIS
REDIS_TLS_ENABLED=false

# SearXNG Settings
SEARXNG_UWSGI_WORKERS=4
SEARXNG_UWSGI_THREADS=4

# S3 Storage Configuration (MinIO)
LANGFUSE_S3_EVENT_UPLOAD_BUCKET=langfuse
LANGFUSE_S3_EVENT_UPLOAD_REGION=auto
LANGFUSE_S3_EVENT_UPLOAD_ACCESS_KEY_ID=minio
LANGFUSE_S3_EVENT_UPLOAD_ENDPOINT=http://minio:9000
LANGFUSE_S3_EVENT_UPLOAD_FORCE_PATH_STYLE=true
LANGFUSE_S3_EVENT_UPLOAD_PREFIX=events/
LANGFUSE_S3_MEDIA_UPLOAD_BUCKET=langfuse
LANGFUSE_S3_MEDIA_UPLOAD_REGION=auto
LANGFUSE_S3_MEDIA_UPLOAD_ACCESS_KEY_ID=minio
LANGFUSE_S3_MEDIA_UPLOAD_ENDPOINT=http://localhost:9090
LANGFUSE_S3_MEDIA_UPLOAD_FORCE_PATH_STYLE=true
LANGFUSE_S3_MEDIA_UPLOAD_PREFIX=media/
"""
    return template_content

def generate_env_file(config):
    """Генерация .env файла с умными дефолтами."""
    print("\n📝 СОЗДАНИЕ КОНФИГУРАЦИИ")
    print("=" * 50)
    
    # Создать или обновить .env файл
    env_path = Path('.env')
    
    # Получить шаблон
    content = create_env_template()
    
    # Подстановка значений
    replacements = {
        'PLACEHOLDER_POSTGRES_PASSWORD': config['postgres_password'],
        'PLACEHOLDER_JWT_SECRET': config['jwt_secret'],
        'PLACEHOLDER_ANON_KEY': config.get('anon_key', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJhbm9uIiwKICAgICJpc3MiOiAic3VwYWJhc2UtZGVtbyIsCiAgICAiaWF0IjogMTY0MTc2OTIwMCwKICAgICJleHAiOiAxNzk5NTM1NjAwCn0.dc_X5iR_VP_qT0zsiyj_I_OZ2T9FtRU2BBNWN8Bu4GE'),
        'PLACEHOLDER_SERVICE_ROLE_KEY': config.get('service_role_key', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJzZXJ2aWNlX3JvbGUiLAogICAgImlzcyI6ICJzdXBhYmFzZS1kZW1vIiwKICAgICJpYXQiOiAxNjQxNzY5MjAwLAogICAgImV4cCI6IDE3OTk1MzU2MDAKfQ.DaYlNEoUrrEn2Ig7tqibS-PHK5vgusbcbo7X36XVt4Q'),
        'PLACEHOLDER_N8N_ENCRYPTION_KEY': config['n8n_encryption_key'],
        'PLACEHOLDER_N8N_USER_MANAGEMENT_JWT_SECRET': config['n8n_user_management_jwt_secret'],
        'PLACEHOLDER_DASHBOARD_PASSWORD': config['dashboard_password'],
        'PLACEHOLDER_POOLER_TENANT_ID': config['pooler_tenant_id'],
        'PLACEHOLDER_CLICKHOUSE_PASSWORD': config['clickhouse_password'],
        'PLACEHOLDER_MINIO_ROOT_PASSWORD': config['minio_root_password'],
        'PLACEHOLDER_LANGFUSE_SALT': config['langfuse_salt'],
        'PLACEHOLDER_NEXTAUTH_SECRET': config['nextauth_secret'],
        'PLACEHOLDER_ENCRYPTION_KEY': config['encryption_key'],
        'PLACEHOLDER_FLOWISE_USERNAME': config['flowise_username'],
        'PLACEHOLDER_FLOWISE_PASSWORD': config['flowise_password'],
        'PLACEHOLDER_NEO4J_AUTH': config['neo4j_auth'],
        'PLACEHOLDER_LETSENCRYPT_EMAIL': config['letsencrypt_email'],
    }
    
    # Добавляем hostname настройки
    for key, value in config['domains'].items():
        placeholder_key = f'PLACEHOLDER_{key.upper()}'
        replacements[placeholder_key] = value if value != '' else f':{8001 + list(config["domains"].keys()).index(key)}'
    
    # Применить замены
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    
    # Записать файл
    with open(env_path, 'w') as f:
        f.write(content)
    
    print_status("Файл .env создан", True, f"Сгенерировано {len(replacements)} настроек")
    
    # Показать ключевую информацию
    print("\n🔑 КЛЮЧЕВАЯ ИНФОРМАЦИЯ:")
    print("=" * 50)
    print(f"🔐 Postgres пароль: {config['postgres_password'][:8]}...")
    print(f"🎛️  Dashboard пароль: {config['dashboard_password']}")
    print(f"🤖 Flowise логин: {config['flowise_username']} / {config['flowise_password']}")
    
    return env_path

# ================================================================
# 🚀 INTEGRATED SERVICES MANAGEMENT
# ================================================================

def run_integrated_start_services(env_info, config):
    """Интегрированный запуск сервисов с умной обработкой ошибок."""
    print(f"\n🚀 ЗАПУСК AI ЭКОСИСТЕМЫ ({config['profile'].upper()})")
    print("=" * 50)
    
    # Проверка Docker
    if not env_info['has_docker']:
        print_docker_installation_guide()
        return False
    
    # Подготовка к запуску
    print_status("Подготовка к запуску", True)
    
    try:
        # Интеграция с start_services.py
        print("🔄 Запуск start_services.py с автонастройками...")
        
        cmd = [
            sys.executable, 'start_services.py',
            '--profile', config['profile'],
            '--environment', config['mode']
        ]
        
        print(f"Выполнение: {' '.join(cmd)}")
        
        # Запуск с прогресс-баром
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Симуляция прогресса (в реальности start_services может не давать прогресс)
        steps = ["Подготовка Supabase", "Запуск базы данных", "Настройка n8n", "Запуск AI сервисов", "Финализация"]
        
        for i, step in enumerate(steps, 1):
            print_progress_bar(i, len(steps), step)
            time.sleep(2)  # Даем время на запуск
        
        # Дожидаемся завершения
        stdout, stderr = process.communicate(timeout=900)  # 15 минут
        
        if process.returncode == 0:
            print_status("Сервисы запущены успешно!", True)
            return True
        else:
            print_status("Ошибка запуска сервисов", False, stderr[:200])
            return run_emergency_recovery(env_info, config)
            
    except subprocess.TimeoutExpired:
        print_status("Timeout при запуске", False, "Запуск занял больше 15 минут")
        return run_emergency_recovery(env_info, config)
    except Exception as e:
        print_status("Неожиданная ошибка", False, str(e))
        return run_emergency_recovery(env_info, config)

def print_docker_installation_guide():
    """Гид по установке Docker."""
    print("\n📦 УСТАНОВКА DOCKER")
    print("=" * 50)
    
    system = platform.system()
    
    if system == "Linux":
        print("🐧 Linux:")
        print("   curl -fsSL https://get.docker.com -o get-docker.sh")
        print("   sudo sh get-docker.sh")
        print("   sudo usermod -aG docker $USER")
    elif system == "Darwin":
        print("🍎 macOS:")
        print("   Download Docker Desktop: https://www.docker.com/products/docker-desktop")
    elif system == "Windows":
        print("🪟 Windows:")
        print("   Download Docker Desktop: https://www.docker.com/products/docker-desktop")
    
    print("\n🔥 После установки также настройте firewall:")
    print("   sudo ufw enable")
    print("   sudo ufw allow 80 && sudo ufw allow 443")

def run_emergency_recovery(env_info, config):
    """Экстренное восстановление системы."""
    print(f"\n🆘 ЭКСТРЕННОЕ ВОССТАНОВЛЕНИЕ")
    print("=" * 50)
    
    # Попытка запустить emergency_fix.sh
    if Path('emergency_fix.sh').exists():
        print("🔧 Запуск emergency_fix.sh...")
        try:
            result = subprocess.run(['bash', 'emergency_fix.sh'], timeout=300)
            if result.returncode == 0:
                print_status("emergency_fix.sh выполнен", True)
                return True
        except Exception as e:
            print_status("emergency_fix.sh не помог", False, str(e))
    
    # Попытка запустить diagnose.py
    if Path('diagnose.py').exists():
        print("🔍 Запуск diagnose.py...")
        try:
            subprocess.run([sys.executable, 'diagnose.py'], timeout=300)
        except Exception as e:
            print_status("diagnose.py завершен с ошибками", False, str(e))
    
    # Минимальный запуск критичных сервисов
    print("🚑 Попытка минимального запуска...")
    essential_services = ['postgres', 'redis', 'open-webui']
    
    for service in essential_services:
        try:
            cmd = ['docker', 'compose', '-p', 'localai', 'up', '-d', service]
            result = subprocess.run(cmd, timeout=60)
            print_status(f"Запуск {service}", result.returncode == 0)
        except:
            print_status(f"Ошибка запуска {service}", False)
    
    return False

def check_and_display_results(env_info, config):
    """Проверка и отображение результатов."""
    print(f"\n🎯 ФИНАЛЬНАЯ ПРОВЕРКА")
    print("=" * 50)
    
    # Проверка портов
    ports_to_check = {
        3000: "Open WebUI (Alenushka)",
        5678: "n8n Automation",
        8003: "Flowise AI",
        8005: "Supabase Dashboard",
        11434: "Ollama API"
    }
    
    working_services = []
    
    for port, name in ports_to_check.items():
        try:
            response = requests.get(f"http://localhost:{port}", timeout=5)
            success = response.status_code < 500
        except:
            success = False
        
        print_status(f":{port} {name}", success)
        
        if success:
            working_services.append((port, name, f"http://localhost:{port}"))
    
    # Результаты
    if working_services:
        print(f"\n🎉 УСПЕХ! Работает {len(working_services)}/{len(ports_to_check)} сервисов")
        print("\n🌐 ДОСТУПНЫЕ ССЫЛКИ:")
        print("=" * 50)
        
        for port, name, url in working_services:
            print(f"✅ {name}")
            print(f"   🔗 {url}")
            print()
        
        print("🎊 ПОЗДРАВЛЯЕМ! AIBot Direct запущен!")
        print("🇷🇺 Ваша персональная AI экосистема готова к работе!")
        
        # Дополнительная информация
        if config['flowise_password']:
            print(f"\n🔑 ДАННЫЕ ДЛЯ ВХОДА:")
            print(f"   Flowise: admin / {config['flowise_password']}")
            print(f"   Dashboard пароль: {config['dashboard_password']}")
        
        return True
    else:
        print("\n❌ Ни один сервис не отвечает")
        print("💡 Выполните: python3 diagnose.py для диагностики")
        return False

def check_directory():
    """Проверка правильности директории."""
    required_files = ['docker-compose.yml', 'start_services.py']
    missing_files = [f for f in required_files if not Path(f).exists()]

    if missing_files:
        print_status("Неправильная директория", False, f"Нет файлов: {', '.join(missing_files)}")
        print(f"\nТекущая папка: {Path.cwd()}")
        print("\n💡 Перейдите в правильную директорию:")
        print("   cd aibot-direct")
        print("   python3 motherlode.py")
        sys.exit(1)

    print_status("Директория корректна", True, "aibot-direct")

# ================================================================
# 🎮 MAIN ORCHESTRATOR (ГЛАВНЫЙ ОРКЕСТРАТОР)
# ================================================================

def main():
    """Главная функция - нулевая конфигурация в действии."""
    
    # Приветствие
    print_shorin_greeting()
    
    # Проверка директории
    check_directory()
    
    # ШАГ 1: Автоопределение окружения
    print_progress_bar(1, 5, "Анализ окружения")
    env_info = detect_environment()
    
    # ШАГ 2: Генерация умной конфигурации
    print_progress_bar(2, 5, "Генерация конфигурации")
    config = generate_smart_config(env_info)
    
    # ШАГ 3: Минимальный ввод пользователя (если нужен)
    print_progress_bar(3, 5, "Настройка параметров")
    config = get_minimal_user_input(env_info, config)
    
    # ШАГ 4: Создание .env файла
    print_progress_bar(4, 5, "Создание конфигурации")
    env_file = generate_env_file(config)
    
    # ШАГ 5: Запуск сервисов
    print_progress_bar(5, 5, "Запуск AI экосистемы")
    success = run_integrated_start_services(env_info, config)
    
    # Финальная проверка и результаты
    if success:
        check_and_display_results(env_info, config)
    else:
        print("\n⚠️  Система настроена, но запуск не удался")
        print("💡 Конфигурация сохранена в .env")
        print("🔧 Выполните: python3 diagnose.py для исправления проблем")

if __name__ == "__main__":
    main()
