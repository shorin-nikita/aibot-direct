#!/usr/bin/env python3
"""
motherlode_simple.py - AIBot Direct упрощенная версия с 3 уровнями

🎯 УРОВНИ СЛОЖНОСТИ:
1. Level 1: Все локально (localhost:порты)
2. Level 2: n8n + Supabase на доменах, остальное локально  
3. Level 3: Все сервисы на доменах

Created by SHORIN for Russian AI automation.
"""

import os
import sys
import time
import secrets
import subprocess
import platform
import socket
from pathlib import Path

def print_greeting():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║       🤖 AIBot Direct - 3 Уровня Сложности                  ║
║                                                              ║
║  🎯 Level 1: Все локально (быстро)                          ║
║  🎯 Level 2: n8n + Supabase на доменах                      ║  
║  🎯 Level 3: Все сервисы с доменами                         ║
║                                                              ║
║              🇷🇺 Made in Russia by SHORIN                   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")

def check_docker():
    """Проверка Docker."""
    try:
        subprocess.run(['docker', '--version'], capture_output=True, check=True)
        return True
    except:
        return False

def get_memory_gb():
    """Получить RAM для разных OS."""
    try:
        system = platform.system()
        
        if system == "Darwin":  # macOS
            result = subprocess.run(['sysctl', '-n', 'hw.memsize'], capture_output=True, text=True)
            mem_bytes = int(result.stdout.strip())
            return mem_bytes // 1024 // 1024 // 1024  # bytes to GB
            
        elif system == "Linux":
            with open('/proc/meminfo', 'r') as f:
                meminfo = f.read()
                mem_total = int([line for line in meminfo.split('\n') if 'MemTotal' in line][0].split()[1])
                return mem_total // 1024 // 1024  # KB to GB
        else:
            return 8  # Windows default
    except:
        return 8  # Default fallback

def detect_gpu():
    """Определить GPU."""
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

def get_local_ip():
    """Получить локальный IP без зависания."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(1)  # 1 секунда timeout
            s.connect(('8.8.8.8', 80))
            return s.getsockname()[0]
    except:
        return '127.0.0.1'

def choose_level():
    """Выбор уровня сложности."""
    print("\n🎯 ВЫБЕРИТЕ УРОВЕНЬ СЛОЖНОСТИ:")
    print("=" * 50)
    print("1️⃣  Level 1: ВСЕ ЛОКАЛЬНО (рекомендуется для начинающих)")
    print("    • Все сервисы: http://localhost:ПОРТ")
    print("    • Быстрая установка, без доменов")
    print("    • Работает без настройки DNS")
    print()
    print("2️⃣  Level 2: N8N + SUPABASE НА ДОМЕНАХ")
    print("    • n8n: https://n8n.yourdomain.com")
    print("    • Supabase: https://supabase.yourdomain.com") 
    print("    • Остальное: localhost:порт")
    print()
    print("3️⃣  Level 3: ВСЕ С ДОМЕНАМИ (для продакшна)")
    print("    • Все сервисы: https://service.yourdomain.com")
    print("    • Автоматический SSL")
    print("    • Требует настройки DNS")
    print()
    
    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        print("❌ Введите 1, 2 или 3")

def generate_random_key(length=32):
    """Генерация случайного ключа."""
    return secrets.token_hex(length)

def generate_config(level, domain=None, email=None):
    """Генерация конфигурации для выбранного уровня."""
    
    # Базовая конфигурация
    config = {
        'level': level,
        'profile': detect_gpu(),
        'memory_gb': get_memory_gb(),
        
        # Автогенерируемые пароли
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
        
        # Дефолтные Supabase ключи
        'anon_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJhbm9uIiwKICAgICJpc3MiOiAic3VwYWJhc2UtZGVtbyIsCiAgICAiaWF0IjogMTY0MTc2OTIwMCwKICAgICJleHAiOiAxNzk5NTM1NjAwCn0.dc_X5iR_VP_qT0zsiyj_I_OZ2T9FtRU2BBNWN8Bu4GE',
        'service_role_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJzZXJ2aWNlX3JvbGUiLAogICAgImlzcyI6ICJzdXBhYmFzZS1kZW1vIiwKICAgICJpYXQiOiAxNjQxNzY5MjAwLAogICAgImV4cCI6IDE3OTk1MzU2MDAKfQ.DaYlNEoUrrEn2Ig7tqibS-PHK5vgusbcbo7X36XVt4Q'
    }
    
    # Настройка доменов в зависимости от уровня
    if level == 1:
        # Level 1: Все localhost
        config.update({
            'n8n_hostname': ':8001',
            'webui_hostname': ':8002', 
            'flowise_hostname': ':8003',
            'supabase_hostname': ':8005',
            'langfuse_hostname': ':8007',
            'neo4j_hostname': ':8008',
            'letsencrypt_email': 'internal',
            'mode': 'localhost'
        })
        
    elif level == 2:
        # Level 2: n8n + Supabase на доменах
        if not domain:
            domain = input("Введите ваш домен (например: mydomain.com): ").strip()
        if not email:
            email = input("Email для SSL (например: admin@mydomain.com): ").strip()
            
        config.update({
            'n8n_hostname': f'n8n.{domain}',
            'supabase_hostname': f'supabase.{domain}',
            'webui_hostname': ':8002',  # localhost
            'flowise_hostname': ':8003',  # localhost
            'langfuse_hostname': ':8007',  # localhost  
            'neo4j_hostname': ':8008',  # localhost
            'letsencrypt_email': email,
            'mode': 'hybrid'
        })
        
    elif level == 3:
        # Level 3: Все на доменах
        if not domain:
            domain = input("Введите ваш домен (например: mydomain.com): ").strip()
        if not email:
            email = input("Email для SSL (например: admin@mydomain.com): ").strip()
            
        config.update({
            'n8n_hostname': f'n8n.{domain}',
            'webui_hostname': f'ai.{domain}',
            'flowise_hostname': f'flowise.{domain}',
            'supabase_hostname': f'supabase.{domain}',
            'langfuse_hostname': f'analytics.{domain}',
            'neo4j_hostname': f'graph.{domain}',
            'letsencrypt_email': email,
            'mode': 'production'
        })
    
    return config

def create_env_file(config):
    """Создание .env файла."""
    env_content = f"""# ================================================================
# 🤖 AIBot Direct - Level {config['level']} Configuration
# ================================================================
# Автоматически сгенерировано motherlode_simple.py

# ================================================================
# 🔐 СЕКРЕТЫ (автоматически сгенерированы)
# ================================================================
POSTGRES_PASSWORD={config['postgres_password']}
JWT_SECRET={config['jwt_secret']}
ANON_KEY={config['anon_key']}
SERVICE_ROLE_KEY={config['service_role_key']}
N8N_ENCRYPTION_KEY={config['n8n_encryption_key']}
N8N_USER_MANAGEMENT_JWT_SECRET={config['n8n_user_management_jwt_secret']}
DASHBOARD_PASSWORD={config['dashboard_password']}
CLICKHOUSE_PASSWORD={config['clickhouse_password']}
MINIO_ROOT_PASSWORD={config['minio_root_password']}
LANGFUSE_SALT={config['langfuse_salt']}
NEXTAUTH_SECRET={config['nextauth_secret']}
ENCRYPTION_KEY={config['encryption_key']}
FLOWISE_USERNAME={config['flowise_username']}
FLOWISE_PASSWORD={config['flowise_password']}
NEO4J_AUTH={config['neo4j_auth']}
POOLER_TENANT_ID={config['pooler_tenant_id']}

# ================================================================
# 🌐 ДОМЕНЫ/ПОРТЫ (Level {config['level']})
# ================================================================
N8N_HOSTNAME={config['n8n_hostname']}
WEBUI_HOSTNAME={config['webui_hostname']}
FLOWISE_HOSTNAME={config['flowise_hostname']}
SUPABASE_HOSTNAME={config['supabase_hostname']}
LANGFUSE_HOSTNAME={config['langfuse_hostname']}
NEO4J_HOSTNAME={config['neo4j_hostname']}
LETSENCRYPT_EMAIL={config['letsencrypt_email']}

# ================================================================
# 🔧 ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ
# ================================================================
POSTGRES_VERSION=latest
TELEMETRY_ENABLED=true
LANGFUSE_ENABLE_EXPERIMENTAL_FEATURES=true
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_AUTH=LOCALONLYREDIS
SEARXNG_UWSGI_WORKERS=4
SEARXNG_UWSGI_THREADS=4

# Langfuse S3 (MinIO)
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

# ClickHouse
CLICKHOUSE_MIGRATION_URL=clickhouse://clickhouse:9000
CLICKHOUSE_URL=http://clickhouse:8123
CLICKHOUSE_USER=clickhouse
CLICKHOUSE_CLUSTER_ENABLED=false
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print(f"✅ Создан .env файл для Level {config['level']}")

def show_config_summary(config):
    """Показать итоговую конфигурацию."""
    print(f"\n📋 КОНФИГУРАЦИЯ Level {config['level']}:")
    print("=" * 50)
    print(f"🧠 RAM: {config['memory_gb']} GB")
    print(f"🚀 Профиль: {config['profile'].upper()}")
    print(f"⚙️ Режим: {config['mode']}")
    print()
    
    print("🌐 ДОСТУП К СЕРВИСАМ:")
    
    if config['level'] == 1:
        print("🖥️  Все локально:")
        print(f"   • Open WebUI (AI): http://localhost{config['webui_hostname']}")
        print(f"   • n8n Automation: http://localhost{config['n8n_hostname']}")
        print(f"   • Flowise AI: http://localhost{config['flowise_hostname']}")
        print(f"   • Supabase DB: http://localhost{config['supabase_hostname']}")
        print(f"   • Ollama API: http://localhost:11434")
        
    elif config['level'] == 2:
        print("🌐 Домены:")
        print(f"   • n8n: https://{config['n8n_hostname']}")
        print(f"   • Supabase: https://{config['supabase_hostname']}")
        print("🖥️  Локально:")
        print(f"   • Open WebUI: http://localhost{config['webui_hostname']}")
        print(f"   • Flowise: http://localhost{config['flowise_hostname']}")
        print(f"   • Ollama API: http://localhost:11434")
        
    elif config['level'] == 3:
        print("🌐 Все на доменах:")
        print(f"   • Open WebUI: https://{config['webui_hostname']}")
        print(f"   • n8n: https://{config['n8n_hostname']}")
        print(f"   • Flowise: https://{config['flowise_hostname']}")
        print(f"   • Supabase: https://{config['supabase_hostname']}")
        print(f"   • Analytics: https://{config['langfuse_hostname']}")
        print("🖥️  Прямой доступ:")
        print(f"   • Ollama API: http://localhost:11434")

def run_start_services(config):
    """Запуск сервисов."""
    print(f"\n🚀 ЗАПУСК Level {config['level']} ({config['profile'].upper()})")
    print("=" * 50)
    
    try:
        cmd = [
            sys.executable, 'start_services.py',
            '--profile', config['profile'],
            '--environment', 'private' if config['mode'] == 'localhost' else 'public'
        ]
        
        print(f"Команда: {' '.join(cmd)}")
        print("⏳ Запуск может занять 3-5 минут...")
        
        result = subprocess.run(cmd, check=True, timeout=900)
        
        print("✅ Сервисы запущены!")
        return True
        
    except subprocess.TimeoutExpired:
        print("⏰ Timeout! Запуск занял больше 15 минут")
        return False
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка запуска: {e}")
        print("💡 Попробуйте: python3 diagnose.py")
        return False

def main():
    """Главная функция."""
    print_greeting()
    
    # Проверка Docker
    if not check_docker():
        print("❌ Docker не найден!")
        print("📦 Установите Docker Desktop: https://www.docker.com/products/docker-desktop")
        return
    
    print("✅ Docker найден")
    
    # Выбор уровня
    level = choose_level()
    
    # Генерация конфигурации 
    config = generate_config(level)
    
    # Создание .env
    create_env_file(config)
    
    # Показать итог
    show_config_summary(config)
    
    # Подтверждение запуска
    print("\n" + "=" * 50)
    start = input("🚀 Запустить систему? (Y/n): ").strip().lower()
    
    if start != 'n':
        success = run_start_services(config)
        
        if success:
            print(f"\n🎉 Level {config['level']} успешно запущен!")
            print("🔑 ПАРОЛИ:")
            print(f"   Dashboard: {config['dashboard_password']}")
            print(f"   Flowise: admin / {config['flowise_password']}")
        else:
            print(f"\n⚠️ Конфигурация Level {config['level']} создана, но запуск не удался")
            print("🔧 Выполните для диагностики: python3 diagnose.py")

if __name__ == "__main__":
    main()
