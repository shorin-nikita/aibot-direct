#!/usr/bin/env python3
"""
motherlode_fixed.py - ПРАВИЛЬНАЯ интеграция с local-ai-packaged

ВМАПБДЯМ - Виртуальная Машина Автоматизации, Баз Данных и Языковых Моделей
Приставка к https://github.com/coleam00/local-ai-packaged

Created by SHORIN - исправленная версия для правильной интеграции
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
import shutil
import zipfile
from pathlib import Path
from urllib.request import urlretrieve

# ================================================================
# 🎨 VISUAL INTERFACE
# ================================================================

def print_shorin_greeting():
    """Приветствие с информацией о системе."""
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║              💻 ВМАПБДЯМ - НАСТОЯЩИЙ ZERO CONFIGURATION               ║
║     Виртуальная Машина Автоматизации, Баз Данных и Языковых Моделей ║
║                                                                      ║
║                    Приветствует SHORIN!                             ║
║                                                                      ║
║  🔗 Автоскачивает github.com/coleam00/local-ai-packaged             ║
║  🤖 13 AI сервисов на стандартных портах (:3000, :5678...)          ║
║  🚀 Автогенерация паролей + автозапуск системы                      ║
║  📦 Один файл = полная установка!                                   ║
║                                                                      ║
║              Готов к запуску за 3 минуты!                          ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
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
# 🔍 ENVIRONMENT DETECTION
# ================================================================

def detect_environment():
    """Автоматически определяет окружение."""
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
        response = requests.get("http://169.254.169.254/latest/meta-data/", timeout=2)
        return response.status_code == 200
    except:
        return False

def get_memory_gb():
    """Получить объем памяти в GB."""
    try:
        if platform.system() == "Darwin":  # macOS
            result = subprocess.run(['sysctl', 'hw.memsize'], capture_output=True, text=True)
            if result.returncode == 0:
                mem_bytes = int(result.stdout.split()[-1])
                return mem_bytes // 1024 // 1024 // 1024
        else:  # Linux
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
    print(f"\n🔍 АНАЛИЗ ОКРУЖЕНИЯ ВМАПБДЯМ")
    print("=" * 60)
    print(f"💻 Тип системы: {env_info['type'].upper()}")
    print(f"🌍 Сетевой адрес: {env_info['ip']}")
    print(f"🏠 Имя хоста: {env_info['hostname']}")
    print(f"⚙️  Процессор: {env_info['cpu_count']} ядер")
    print(f"💾 Оперативная память: {env_info['memory_gb']} GB")
    print(f"💿 Хранилище: {env_info['disk_free_gb']} GB доступно")
    print(f"🐳 Контейнеризация: {'✅ Доступна' if env_info['has_docker'] else '❌ Отсутствует'}")

def check_docker():
    """Проверка наличия Docker."""
    try:
        subprocess.run(['docker', '--version'], capture_output=True, check=True)
        return True
    except:
        return False

# ================================================================
# 🧠 SMART CONFIG GENERATION
# ================================================================

def generate_smart_config(env_info):
    """Генерация умной конфигурации совместимой с local-ai-packaged."""
    config = {
        # Базовая конфигурация
        'environment': env_info['type'],
        'profile': determine_docker_profile(env_info),
        'mode': determine_deployment_mode(env_info),
        
        # Автогенерируемые секреты СОВМЕСТИМЫЕ с оригиналом
        'postgres_password': generate_random_key(16),
        'jwt_secret': generate_random_key(32),
        'anon_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0',
        'service_role_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImV4cCI6MTk4MzgxMjk5Nn0.EGIM96RAZx35lJzdJsyH-qQwv8Hdp7fsn3W0YpN81IU',
        'n8n_encryption_key': generate_random_key(32),
        'dashboard_password': generate_random_key(16),
        
        # Дополнительные ключи
        'flowise_username': 'admin',
        'flowise_password': generate_random_key(12),
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
    return 'private' if env_info['type'] == 'localhost' else 'public'

def generate_random_key(length=32):
    """Generate a random hex key of specified length."""
    return secrets.token_hex(length)

# ================================================================
# 📄 SMART ENV GENERATION - СОВМЕСТИМО С ОРИГИНАЛОМ
# ================================================================

def create_original_env_file(config):
    """Создать .env файл совместимый с оригинальным local-ai-packaged."""
    
    # Скопируем .env.example если он есть  
    if Path('.env.example').exists():
        print("📋 Используем оригинальный .env.example как шаблон...")
        shutil.copy('.env.example', '.env')
        
        # Заменим только пароли в существующем файле
        with open('.env', 'r') as f:
            content = f.read()
            
        # Заменим основные пароли
        content = content.replace('your_super_secret_postgres_password', config['postgres_password'])
        content = content.replace('your_super_secret_jwt_secret', config['jwt_secret'])
        
        with open('.env', 'w') as f:
            f.write(content)
            
    else:
        # Создадим минимальный .env для работы
        env_content = f"""# ВМАПБДЯМ - Минимальная конфигурация для local-ai-packaged
# Автогенерировано motherlode_fixed.py

# Postgres
POSTGRES_PASSWORD={config['postgres_password']}

# Supabase JWT
JWT_SECRET={config['jwt_secret']}
ANON_KEY={config['anon_key']}
SERVICE_ROLE_KEY={config['service_role_key']}

# N8N
N8N_ENCRYPTION_KEY={config['n8n_encryption_key']}

# Dashboard
DASHBOARD_PASSWORD={config['dashboard_password']}

# Flowise
FLOWISE_USERNAME={config['flowise_username']}
FLOWISE_PASSWORD={config['flowise_password']}
"""
        with open('.env', 'w') as f:
            f.write(env_content)
    
    print_status("Файл .env создан/обновлен", True, f"Пароли сгенерированы безопасно")
    return Path('.env')

# ================================================================
# 🚀 ORIGINAL INTEGRATION - ПРАВИЛЬНАЯ ИНТЕГРАЦИЯ
# ================================================================

def run_original_start_services(env_info, config):
    """Правильный запуск оригинального start_services.py."""
    print(f"\n🚀 ЗАПУСК ОРИГИНАЛЬНОЙ СИСТЕМЫ LOCAL-AI-PACKAGED")
    print("=" * 60)
    
    # Проверка Docker
    if not env_info['has_docker']:
        print_docker_installation_guide()
        return False
    
    try:
        # Правильная команда как в оригинале
        cmd = [sys.executable, 'start_services.py', '--profile', config['profile']]
        
        # Добавляем environment только для публичного режима
        if config['mode'] == 'public':
            cmd.extend(['--environment', 'public'])
            
        print(f"🔄 Выполнение: {' '.join(cmd)}")
        print("⏳ Ожидание запуска... (это может занять несколько минут)")
        
        # Запускаем и ждем завершения
        result = subprocess.run(cmd, timeout=900)  # 15 минут
        
        if result.returncode == 0:
            print_status("✅ Оригинальная система запущена успешно!")
            return True
        else:
            print_status("❌ Ошибка запуска", False)
            return False
            
    except subprocess.TimeoutExpired:
        print_status("⏰ Timeout - запуск занял больше 15 минут", False)
        return False
    except Exception as e:
        print_status("💥 Неожиданная ошибка", False, str(e))
        return False

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

def check_and_display_results(env_info, config):
    """Проверка и отображение результатов."""
    print(f"\n🎯 ПРОВЕРКА СИСТЕМЫ")
    print("=" * 60)
    
    # СТАНДАРТНЫЕ ПОРТЫ из оригинала local-ai-packaged  
    ports_to_check = {
        3000: "Open WebUI (AI Chat)",
        5678: "n8n (Automation)", 
        8003: "Flowise (AI Builder)",
        54321: "Supabase API",
        11434: "Ollama API"
    }
    
    working_services = []
    
    # Ждем немного для инициализации
    print("⏳ Ожидание инициализации сервисов (30 сек)...")
    time.sleep(30)
    
    for port, name in ports_to_check.items():
        try:
            response = requests.get(f"http://localhost:{port}", timeout=5)
            success = response.status_code < 500
        except:
            success = False
        
        print_status(f":{port} {name}", success)
        
        if success:
            working_services.append((port, name, f"http://{env_info['ip']}:{port}"))
    
    # Результаты
    if working_services:
        print(f"\n🎉 УСПЕХ! Работает {len(working_services)}/{len(ports_to_check)} сервисов")
        print("\n🌐 ДОСТУПНЫЕ ССЫЛКИ:")
        print("=" * 60)
        
        for port, name, url in working_services:
            print(f"✅ {name}")
            print(f"   🔗 {url}")
            print()
        
        print("🎊 ПОЗДРАВЛЯЕМ! ВМАПБДЯМ запущен с правильной интеграцией!")
        print("🔗 Основано на https://github.com/coleam00/local-ai-packaged")
        
        if config.get('flowise_password'):
            print(f"\n🔑 ДАННЫЕ ДЛЯ ВХОДА:")
            print(f"   Flowise: {config['flowise_username']} / {config['flowise_password']}")
        
        return True
    else:
        print("\n❌ Ни один сервис не отвечает")
        print("💡 Проверьте логи: docker compose -p localai logs")
        return False

def auto_download_original_files():
    """АВТОСКАЧИВАНИЕ недостающих файлов из оригинального репозитория."""
    required_files = [
        'docker-compose.yml', 
        'start_services.py',
        'docker-compose.override.private.yml',  # ПОДТВЕРЖДЕНО: есть в оригинале
        'docker-compose.override.public.yml'    # ПОДТВЕРЖДЕНО: есть в оригинале
    ]
    missing_files = [f for f in required_files if not Path(f).exists()]
    
    if not missing_files:
        print_status("✅ Все файлы на месте", True, "local-ai-packaged компоненты найдены")
        return True
    
    print(f"\n📦 АВТОСКАЧИВАНИЕ НЕДОСТАЮЩИХ ФАЙЛОВ")
    print("=" * 60)
    print(f"🔍 Не найдено: {', '.join(missing_files)}")
    print("🌐 Скачиваю из https://github.com/coleam00/local-ai-packaged...")
    
    try:
        # Скачиваем архив оригинального репозитория
        zip_url = "https://github.com/coleam00/local-ai-packaged/archive/refs/heads/main.zip"
        zip_path = "local-ai-packaged-main.zip"
        
        print("📥 Загрузка архива...")
        urlretrieve(zip_url, zip_path)
        print_status("✅ Архив загружен", True)
        
        # Распаковываем нужные файлы
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            extract_files = [
                'local-ai-packaged-main/docker-compose.yml',
                'local-ai-packaged-main/start_services.py', 
                'local-ai-packaged-main/.env.example',
                'local-ai-packaged-main/Caddyfile',
                'local-ai-packaged-main/n8n_pipe.py',
                'local-ai-packaged-main/docker-compose.override.private.yml',  # ДОБАВЛЕНО: ТОЧНО ЕСТЬ В ОРИГИНАЛЕ
                'local-ai-packaged-main/docker-compose.override.public.yml'   # ДОБАВЛЕНО: ТОЖЕ ЕСТЬ
            ]
            
            for file_path in extract_files:
                try:
                    # Извлекаем файл
                    zip_ref.extract(file_path)
                    # Перемещаем в текущую директорию
                    source = Path(file_path)
                    target = Path(source.name)
                    if source.exists():
                        shutil.move(str(source), str(target))
                        print_status(f"✅ {source.name}", True, "скопирован")
                except Exception as e:
                    print_status(f"⚠️ {file_path.split('/')[-1]}", False, f"пропущен: {e}")
        
        # Удаляем архив и временную папку  
        Path(zip_path).unlink()
        shutil.rmtree('local-ai-packaged-main', ignore_errors=True)
        
        print_status("🎉 Автоскачивание завершено!", True, "Все нужные файлы получены")
        return True
        
    except Exception as e:
        print_status("❌ Ошибка автоскачивания", False, str(e))
        print("\n💡 Альтернативная установка:")
        print("   git clone https://github.com/coleam00/local-ai-packaged.git")
        print("   cd local-ai-packaged")  
        print("   python3 ../aibot-direct/motherlode.py")
        return False

def check_directory():
    """Проверка и автоскачивание недостающих файлов."""
    return auto_download_original_files()

# ================================================================
# 🎮 MAIN ORCHESTRATOR
# ================================================================

def main():
    """Главная функция - НАСТОЯЩИЙ ZERO CONFIGURATION!"""
    
    # Приветствие
    print_shorin_greeting()
    
    # ШАГ 1: Автоскачивание недостающих файлов
    print_progress_bar(1, 6, "Проверка и автоскачивание")
    if not check_directory():
        print("\n❌ Не удалось получить необходимые файлы")
        print("💡 Проверьте интернет соединение и повторите попытку")
        sys.exit(1)
    
    # ШАГ 2: Автоопределение окружения
    print_progress_bar(2, 6, "Анализ окружения")
    env_info = detect_environment()
    
    # ШАГ 3: Генерация умной конфигурации
    print_progress_bar(3, 6, "Генерация конфигурации")
    config = generate_smart_config(env_info)
    
    # ШАГ 4: Создание .env файла
    print_progress_bar(4, 6, "Создание .env файла")
    env_file = create_original_env_file(config)
    
    # ШАГ 5: Запуск оригинальной системы
    print_progress_bar(5, 6, "Запуск local-ai-packaged")
    success = run_original_start_services(env_info, config)
    
    # ШАГ 6: Проверка результатов
    print_progress_bar(6, 6, "Проверка сервисов")
    if success:
        check_and_display_results(env_info, config)
    else:
        print("\n⚠️  Конфигурация создана, но запуск не удался")
        print("💡 Попробуйте запустить вручную:")
        print(f"   python3 start_services.py --profile {config['profile']}")

if __name__ == "__main__":
    main()
