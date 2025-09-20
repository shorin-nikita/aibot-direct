#!/usr/bin/env python3
"""
🤖 AIBot Direct - Auto Setup
Простой и надежный скрипт автоустановки

Версия: 2.0 (Clean)
Автор: Shorin Nikita  
Сайт: https://aibot.direct
"""

import os
import secrets
import subprocess
import sys
import getpass
import re
from pathlib import Path

def print_logo():
    """Простой логотип"""
    print("""
🤖 ======================================
   AIBot Direct - Russian AI Platform
   Простая автоматическая установка
======================================
""")

def log(message, level="INFO"):
    """Простое логирование"""
    if level == "ERROR":
        print(f"❌ {message}")
    elif level == "SUCCESS": 
        print(f"✅ {message}")
    elif level == "WARNING":
        print(f"⚠️  {message}")
    else:
        print(f"ℹ️  {message}")

def run_cmd(cmd, show_output=False):
    """Выполнение команды"""
    try:
        if show_output:
            log(f"Выполняю: {cmd}")
        result = subprocess.run(cmd, shell=True, check=True, capture_output=not show_output, text=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def generate_key(length=32):
    """Генерация ключа"""
    return secrets.token_hex(length)

def generate_password(length=16):
    """Генерация пароля"""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(secrets.choice(chars) for _ in range(length))

def validate_email(email):
    """Проверка email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_domain(domain):
    """Проверка домена"""
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9.-]*[a-zA-Z0-9]\.[a-zA-Z]{2,}$'
    return re.match(pattern, domain) is not None

def get_input(prompt, validator=None, secret=False):
    """Безопасный ввод с валидацией"""
    for _ in range(3):
        if secret:
            value = getpass.getpass(f"{prompt}: ")
        else:
            value = input(f"{prompt}: ").strip()
        
        if not value:
            log("Поле не может быть пустым", "ERROR")
            continue
            
        if validator and not validator(value):
            log("Неверный формат", "ERROR")
            continue
            
        return value
    
    log("Превышено количество попыток", "ERROR")
    return None

def setup_firewall():
    """Настройка портов"""
    log("Настройка портов...")
    
    commands = [
        "sudo ufw --force enable",
        "sudo ufw allow 80/tcp", 
        "sudo ufw allow 443/tcp",
        "sudo ufw allow ssh"
    ]
    
    for cmd in commands:
        if not run_cmd(cmd):
            log(f"Не удалось выполнить: {cmd}", "WARNING")
            return False
    
    log("Порты настроены (80, 443, SSH)", "SUCCESS")
    return True

def get_config_choice():
    """Выбор конфигурации"""
    print("""
Выберите конфигурацию:

1. MINIMAL - N8N + Supabase (быстрый старт)
2. FULL    - Полный AI стек (все возможности)
""")
    
    while True:
        choice = input("Ваш выбор (1/2): ").strip()
        if choice == "1":
            return "minimal"
        elif choice == "2":
            return "full"
        log("Введите 1 или 2", "ERROR")

def collect_data(config):
    """Сбор данных от пользователя"""
    data = {}
    
    log(f"Настройка для {config.upper()} конфигурации")
    
    # Основные данные
    data['email'] = get_input("Email для SSL", validate_email)
    if not data['email']:
        return None
        
    data['n8n_domain'] = get_input("Домен для N8N (например: n8n.yourdomain.com)", validate_domain)
    if not data['n8n_domain']:
        return None
        
    data['supabase_domain'] = get_input("Домен для Supabase (например: db.yourdomain.com)", validate_domain)  
    if not data['supabase_domain']:
        return None
    
    # Дополнительные домены для FULL
    if config == "full":
        data['chat_domain'] = get_input("Домен для чата (например: chat.yourdomain.com)", validate_domain)
        data['flow_domain'] = get_input("Домен для Flowise (например: flow.yourdomain.com)", validate_domain) 
        data['analytics_domain'] = get_input("Домен для Analytics (например: analytics.yourdomain.com)", validate_domain)
        
        if not all([data['chat_domain'], data['flow_domain'], data['analytics_domain']]):
            return None
    
    # Supabase ключи
    log("Supabase API ключи (генерируйте на: https://supabase.com/docs/guides/self-hosting/docker#generate-api-keys)")
    
    data['jwt_secret'] = get_input("JWT_SECRET (минимум 32 символа)", lambda x: len(x) >= 32, secret=True)
    data['anon_key'] = get_input("ANON_KEY", lambda x: len(x) >= 100)
    data['service_role_key'] = get_input("SERVICE_ROLE_KEY", lambda x: len(x) >= 100)
    
    if not all([data['jwt_secret'], data['anon_key'], data['service_role_key']]):
        return None
    
    return data

def create_env(config, data):
    """Создание .env файла"""
    log("Создание .env файла...")
    
    # Резервная копия
    if os.path.exists('.env'):
        os.rename('.env', '.env.backup')
    
    # Генерация секретов
    secrets_data = {
        'n8n_key': generate_key(32),
        'n8n_jwt': generate_key(32), 
        'postgres_pass': generate_password(32),
        'dashboard_pass': generate_password(16),
        'secret_base': generate_key(64)
    }
    
    if config == "full":
        secrets_data.update({
            'neo4j_pass': generate_password(16),
            'clickhouse_pass': generate_password(24),
            'minio_pass': generate_password(24),
            'langfuse_salt': generate_key(32),
            'next_secret': generate_key(32),
            'encryption_key': generate_key(32)
        })
    
    # Содержимое .env
    env_content = f"""# AIBot Direct - Auto Generated Configuration
# Дата: {subprocess.check_output(['date'], shell=True, text=True).strip()}

############
# N8N Configuration
############
N8N_ENCRYPTION_KEY={secrets_data['n8n_key']}
N8N_USER_MANAGEMENT_JWT_SECRET={secrets_data['n8n_jwt']}

############
# Supabase Configuration  
############
POSTGRES_PASSWORD={secrets_data['postgres_pass']}
JWT_SECRET={data['jwt_secret']}
ANON_KEY={data['anon_key']}
SERVICE_ROLE_KEY={data['service_role_key']}
DASHBOARD_USERNAME=admin
DASHBOARD_PASSWORD={secrets_data['dashboard_pass']}
POOLER_TENANT_ID=1000

############
# Domain Configuration
############
N8N_HOSTNAME={data['n8n_domain']}
SUPABASE_HOSTNAME={data['supabase_domain']}
LETSENCRYPT_EMAIL={data['email']}
"""

    if config == "full":
        env_content += f"""
############
# Full Stack Domains
############
WEBUI_HOSTNAME={data['chat_domain']}
FLOWISE_HOSTNAME={data['flow_domain']}
LANGFUSE_HOSTNAME={data['analytics_domain']}

############
# Additional Services
############
NEO4J_AUTH=neo4j/{secrets_data['neo4j_pass']}
CLICKHOUSE_PASSWORD={secrets_data['clickhouse_pass']}
MINIO_ROOT_PASSWORD={secrets_data['minio_pass']}
LANGFUSE_SALT={secrets_data['langfuse_salt']}
NEXTAUTH_SECRET={secrets_data['next_secret']}
ENCRYPTION_KEY={secrets_data['encryption_key']}
"""
    
    # Базовые настройки
    env_content += f"""
############
# Base Configuration
############
POSTGRES_HOST=db
POSTGRES_DB=postgres
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POOLER_PROXY_PORT_TRANSACTION=6543
POOLER_DEFAULT_POOL_SIZE=20
POOLER_MAX_CLIENT_CONN=100
SECRET_KEY_BASE={secrets_data['secret_base']}
POOLER_DB_POOL_SIZE=5
KONG_HTTP_PORT=8000
KONG_HTTPS_PORT=8443
PGRST_DB_SCHEMAS=public,storage,graphql_public
SITE_URL=http://localhost:3000
JWT_EXPIRY=3600
DISABLE_SIGNUP=false
API_EXTERNAL_URL=http://localhost:8000
ENABLE_EMAIL_SIGNUP=true
ENABLE_EMAIL_AUTOCONFIRM=true
STUDIO_DEFAULT_ORGANIZATION=AIBot Direct
STUDIO_DEFAULT_PROJECT=Russian AI Platform
"""
    
    # Запись файла
    try:
        with open('.env', 'w', encoding='utf-8') as f:
            f.write(env_content)
        os.chmod('.env', 0o600)
        log(".env файл создан", "SUCCESS")
        return True
    except Exception as e:
        log(f"Ошибка создания .env: {e}", "ERROR")
        return False

def start_services(config):
    """Запуск сервисов"""
    log("Запуск сервисов...")
    
    profile = "cpu"  # По умолчанию CPU
    cmd = f"python3 start_services.py --profile {profile} --environment public"
    
    log(f"Выполняю: {cmd}")
    return run_cmd(cmd, show_output=True)

def show_summary(config, data):
    """Итоговая информация"""
    print(f"""
🎉 УСТАНОВКА ЗАВЕРШЕНА!

Конфигурация: {config.upper()}

Доступные сервисы:
✅ N8N (Автоматизация): https://{data['n8n_domain']}
✅ Supabase (База): https://{data['supabase_domain']}
""")
    
    if config == "full":
        print(f"""✅ Чат (AI): https://{data['chat_domain']}
✅ Flowise (AI Builder): https://{data['flow_domain']} 
✅ Analytics: https://{data['analytics_domain']}""")
    
    print(f"""
ВАЖНО:
- Настройте DNS записи для всех доменов
- SSL сертификаты создадутся автоматически
- Файл .env содержит все настройки

AIBot Direct готов к работе! 🤖
""")

def main():
    """Основная функция"""
    print_logo()
    
    # Проверки
    if not os.path.exists('.env.example'):
        log("Файл .env.example не найден. Запустите из папки проекта", "ERROR")
        sys.exit(1)
    
    try:
        # Этапы установки
        log("Этап 1/5: Выбор конфигурации")
        config = get_config_choice()
        
        log("Этап 2/5: Настройка портов")
        setup_firewall()
        
        log("Этап 3/5: Сбор данных")  
        data = collect_data(config)
        if not data:
            log("Не удалось собрать данные", "ERROR")
            sys.exit(1)
        
        log("Этап 4/5: Создание конфигурации")
        if not create_env(config, data):
            sys.exit(1)
        
        log("Этап 5/5: Запуск сервисов")
        if start_services(config):
            show_summary(config, data)
        else:
            log("Ошибка запуска сервисов", "ERROR")
            sys.exit(1)
            
    except KeyboardInterrupt:
        log("\nУстановка прервана", "WARNING") 
        sys.exit(0)
    except Exception as e:
        log(f"Критическая ошибка: {e}", "ERROR")
        sys.exit(1)

if __name__ == "__main__":
    main()