#!/usr/bin/env python3
"""
🚀 QUICK FIX - LANGFUSE_SALT для AI стека

Быстрое исправление ошибки с отсутствующей переменной LANGFUSE_SALT
и другими критически важными переменными.

Использование:
    python3 quick_fix_langfuse.py

Создает или дополняет .env файл недостающими переменными.
"""

import os
import secrets
from pathlib import Path

def generate_secret(length=32):
    """Генерация случайного ключа."""
    return secrets.token_hex(length)

def get_missing_vars():
    """Возвращает критически важные переменные, которые часто отсутствуют."""
    return {
        'LANGFUSE_SALT': generate_secret(32),
        'ENCRYPTION_KEY': generate_secret(32),
        'NEXTAUTH_SECRET': generate_secret(32),
        'CLICKHOUSE_PASSWORD': generate_secret(16),
        'MINIO_ROOT_PASSWORD': generate_secret(16),
        'TELEMETRY_ENABLED': 'true',
        'LANGFUSE_ENABLE_EXPERIMENTAL_FEATURES': 'true',
        'CLICKHOUSE_USER': 'clickhouse',
        'CLICKHOUSE_MIGRATION_URL': 'clickhouse://clickhouse:9000',
        'CLICKHOUSE_URL': 'http://clickhouse:8123',
        'CLICKHOUSE_CLUSTER_ENABLED': 'false',
        'REDIS_HOST': 'redis',
        'REDIS_PORT': '6379',
        'REDIS_AUTH': 'LOCALONLYREDIS',
        'REDIS_TLS_ENABLED': 'false',
        'LANGFUSE_INIT_USER_NAME': 'Admin',
        'LANGFUSE_INIT_USER_PASSWORD': generate_secret(16)
    }

def check_existing_env():
    """Проверяет существующий .env файл."""
    env_vars = {}
    if Path('.env').exists():
        print("✅ Найден существующий .env файл")
        with open('.env', 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip()
        print(f"📊 Загружено {len(env_vars)} существующих переменных")
    else:
        print("⚠️  Файл .env не найден - будет создан новый")
    
    return env_vars

def add_missing_vars(existing_vars):
    """Добавляет недостающие переменные."""
    required_vars = get_missing_vars()
    missing_vars = {}
    
    for key, value in required_vars.items():
        if key not in existing_vars:
            missing_vars[key] = value
    
    if not missing_vars:
        print("🎉 Все критически важные переменные уже присутствуют!")
        return False
    
    print(f"➕ Нужно добавить {len(missing_vars)} переменных:")
    for key in missing_vars.keys():
        print(f"   🔑 {key}")
    
    # Добавляем недостающие переменные в .env
    with open('.env', 'a') as f:
        f.write(f"\n# 🚀 Добавлено quick_fix_langfuse.py\n")
        f.write(f"# Время: {secrets.token_hex(4)}\n\n")
        
        for key, value in missing_vars.items():
            f.write(f"{key}={value}\n")
    
    print("✅ Недостающие переменные добавлены в .env файл!")
    return True

def main():
    """Главная функция."""
    print("🚀 QUICK FIX - LANGFUSE_SALT и критические переменные")
    print("=" * 60)
    
    # Проверяем текущий статус
    existing_vars = check_existing_env()
    
    # Добавляем недостающие переменные  
    if add_missing_vars(existing_vars):
        print("\n🎯 ИСПРАВЛЕНИЕ ЗАВЕРШЕНО!")
        print("\n📝 Следующие шаги:")
        print("1. Перезапустите AI стек:")
        print("   docker-compose down")
        print("   docker-compose up -d")
        print("\n2. Проверьте логи:")
        print("   docker-compose logs -f langfuse-worker")
        print("\n3. Откройте веб-интерфейсы:")
        print("   - http://IP:3000 (OpenWebUI)")
        print("   - http://IP:5678 (n8n)")
        print("   - http://IP:8005 (Supabase)")
    else:
        print("\n✅ Конфигурация уже корректна!")
        print("Если проблемы остаются, проверьте логи:")
        print("   docker-compose logs -f")

if __name__ == "__main__":
    main()
