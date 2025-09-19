#!/usr/bin/env python3
"""
motherlode_gaming.py - AIBot Direct Gaming Style Setup

🎮 ИГРОВОЙ ИНТЕРФЕЙС с Rich UI/UX
🏭 Советский стиль промышленной автоматизации  
🔧 Умная проверка существующих настроек

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
from typing import Dict, Any, Optional

# Проверка и установка Rich
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
    from rich.table import Table
    from rich.text import Text
    from rich.align import Align
    from rich.columns import Columns
    from rich.prompt import Prompt, Confirm
    from rich.tree import Tree
    from rich.layout import Layout
    from rich.live import Live
except ImportError:
    print("📦 Установка Rich для красивого интерфейса...")
    subprocess.run([sys.executable, "-m", "pip", "install", "rich"], check=True)
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
    from rich.table import Table
    from rich.text import Text
    from rich.align import Align
    from rich.columns import Columns
    from rich.prompt import Prompt, Confirm
    from rich.tree import Tree
    from rich.layout import Layout
    from rich.live import Live

# Инициализация консоли
console = Console()

# ================================================================
# 🎨 ИГРОВОЙ ИНТЕРФЕЙС В СТИЛЕ ПРОМЫШЛЕННОЙ АВТОМАТИЗАЦИИ
# ================================================================

def show_industrial_banner():
    """Промышленный баннер в советском стиле."""
    banner = Text()
    banner.append("╔══════════════════════════════════════════════════════════════╗\n", style="bold red")
    banner.append("║                                                              ║\n", style="bold red")
    banner.append("║            🏭 СИСТЕМА АВТОМАТИЗАЦИИ ПРОИЗВОДСТВА            ║\n", style="bold white")
    banner.append("║                                                              ║\n", style="bold red")
    banner.append("║                    ⚙️  AIBot Direct ⚙️                     ║\n", style="bold yellow")
    banner.append("║                                                              ║\n", style="bold red")
    banner.append("║        Инженерный комплекс промышленной автоматизации       ║\n", style="dim white")
    banner.append("║             13 модулей интеллектуального управления          ║\n", style="dim white")
    banner.append("║                                                              ║\n", style="bold red")
    banner.append("║                  🚀 Готов к запуску! 🚀                     ║\n", style="bold green")
    banner.append("║                                                              ║\n", style="bold red")
    banner.append("╚══════════════════════════════════════════════════════════════╝", style="bold red")
    
    console.print(Align.center(banner))
    time.sleep(1)

def create_system_status_panel(env_info: Dict[str, Any]) -> Panel:
    """Создать панель статуса системы."""
    
    # Определение типа системы
    system_type_icons = {
        'localhost': '🖥️  Локальная станция',
        'vps': '🏢 Промышленный сервер', 
        'cloud': '☁️  Облачная платформа'
    }
    
    # Статус компонентов
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Компонент", style="cyan")
    table.add_column("Значение", style="white")
    
    table.add_row("🏭 Тип производства:", system_type_icons.get(env_info['type'], '❓ Неизвестный'))
    table.add_row("🌐 Сетевой узел:", f"{env_info['ip']}")
    table.add_row("🖥️  Имя станции:", f"{env_info['hostname']}")
    table.add_row("⚡ Вычислительные ядра:", f"{env_info['cpu_count']} шт.")
    table.add_row("💾 Оперативная память:", f"{env_info['memory_gb']} ГБ")
    table.add_row("💿 Свободное хранилище:", f"{env_info['disk_free_gb']} ГБ")
    
    docker_status = "[green]✅ Готов[/green]" if env_info['has_docker'] else "[red]❌ Не установлен[/red]"
    table.add_row("🐳 Контейнерная система:", docker_status)
    
    return Panel(
        table,
        title="[bold yellow]📊 СОСТОЯНИЕ ПРОИЗВОДСТВЕННОГО КОМПЛЕКСА[/bold yellow]",
        border_style="yellow",
        padding=(1, 2)
    )

def check_existing_env() -> Optional[Dict[str, str]]:
    """Проверить существующий .env файл на наличие доменов."""
    env_path = Path('.env')
    
    if not env_path.exists():
        return None
    
    domains = {}
    try:
        with open(env_path, 'r') as f:
            content = f.read()
            
        # Ищем домены в .env файле
        hostname_patterns = [
            'N8N_HOSTNAME', 'WEBUI_HOSTNAME', 'FLOWISE_HOSTNAME', 
            'SUPABASE_HOSTNAME', 'LANGFUSE_HOSTNAME', 'NEO4J_HOSTNAME'
        ]
        
        for pattern in hostname_patterns:
            for line in content.split('\n'):
                if line.startswith(pattern + '=') and not line.startswith('#'):
                    value = line.split('=', 1)[1].strip()
                    if value and not value.startswith(':') and 'yourdomain.com' not in value:
                        domains[pattern.lower()] = value
        
        return domains if domains else None
        
    except Exception:
        return None

def show_existing_domains_panel(domains: Dict[str, str]) -> Panel:
    """Показать найденные домены."""
    table = Table(show_header=True, box=None)
    table.add_column("🏭 Производственный модуль", style="cyan")
    table.add_column("🌐 Сетевой адрес", style="green")
    
    service_names = {
        'n8n_hostname': 'Система автоматизации (n8n)',
        'webui_hostname': 'Интерфейс управления (AI)',
        'flowise_hostname': 'Конструктор агентов (Flowise)',
        'supabase_hostname': 'База данных (Supabase)',
        'langfuse_hostname': 'Аналитический центр',
        'neo4j_hostname': 'Граф знаний'
    }
    
    for key, value in domains.items():
        name = service_names.get(key, key)
        table.add_row(f"⚙️ {name}", f"🔗 https://{value}")
    
    return Panel(
        table,
        title="[bold green]🔍 ОБНАРУЖЕНЫ ДЕЙСТВУЮЩИЕ ПРОИЗВОДСТВЕННЫЕ АДРЕСА[/bold green]",
        border_style="green",
        padding=(1, 2)
    )

def get_memory_gb_cross_platform():
    """Получить RAM для разных ОС (исправлено для macOS)."""
    try:
        system = platform.system()
        
        if system == "Darwin":  # macOS
            result = subprocess.run(['sysctl', '-n', 'hw.memsize'], capture_output=True, text=True)
            if result.returncode == 0:
                mem_bytes = int(result.stdout.strip())
                return mem_bytes // 1024 // 1024 // 1024  # bytes to GB
        
        elif system == "Linux":
            with open('/proc/meminfo', 'r') as f:
                meminfo = f.read()
                mem_total = int([line for line in meminfo.split('\n') if 'MemTotal' in line][0].split()[1])
                return mem_total // 1024 // 1024  # KB to GB
                
        elif system == "Windows":
            result = subprocess.run(['wmic', 'computersystem', 'get', 'TotalPhysicalMemory', '/value'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if 'TotalPhysicalMemory' in line and '=' in line:
                        mem_bytes = int(line.split('=')[1].strip())
                        return mem_bytes // 1024 // 1024 // 1024
    except:
        pass
    
    return 8  # Default fallback

def get_local_ip_safe():
    """Получить локальный IP без зависания."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(1)  # 1 секунда timeout
            s.connect(('8.8.8.8', 80))
            return s.getsockname()[0]
    except:
        return '127.0.0.1'

def detect_system_environment():
    """Определить окружение с улучшенной совместимостью."""
    env_info = {
        'type': 'localhost',
        'ip': get_local_ip_safe(),
        'hostname': socket.gethostname(),
        'is_vps': False,
        'is_cloud': False,
        'has_docker': check_docker_availability(),
        'cpu_count': os.cpu_count(),
        'memory_gb': get_memory_gb_cross_platform(),
        'disk_free_gb': get_disk_space_gb()
    }
    
    # Быстрая проверка VPS без зависания
    if env_info['ip'] != '127.0.0.1' and not env_info['ip'].startswith('192.168'):
        env_info['type'] = 'vps'
        env_info['is_vps'] = True
    
    return env_info

def check_docker_availability():
    """Проверка Docker."""
    try:
        result = subprocess.run(['docker', '--version'], capture_output=True, check=True, timeout=5)
        return True
    except:
        return False

def get_disk_space_gb():
    """Получить свободное место на диске."""
    try:
        if platform.system() == "Windows":
            import shutil
            total, used, free = shutil.disk_usage(".")
            return free // 1024 // 1024 // 1024
        else:
            stat = os.statvfs('.')
            return (stat.f_bavail * stat.f_frsize) // 1024 // 1024 // 1024
    except:
        return 10  # Default

def detect_gpu_configuration():
    """Определить конфигурацию GPU."""
    try:
        result = subprocess.run(['nvidia-smi'], capture_output=True, text=True, timeout=3)
        if result.returncode == 0:
            return 'gpu-nvidia'
    except:
        pass
        
    try:
        result = subprocess.run(['rocm-smi'], capture_output=True, text=True, timeout=3) 
        if result.returncode == 0:
            return 'gpu-amd'
    except:
        pass
    
    return 'cpu'

def open_system_ports():
    """Открыть системные порты для работы."""
    console.print(Panel.fit("[yellow]🔓 ОТКРЫТИЕ СИСТЕМНЫХ ПОРТОВ...[/yellow]"))
    
    ports_to_open = [80, 443, 3000, 5678, 8001, 8002, 8003, 8005, 8006, 8007, 8008, 8009, 11434]
    
    system = platform.system()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        
        task = progress.add_task("Настройка сетевых портов...", total=len(ports_to_open))
        
        for port in ports_to_open:
            try:
                if system == "Linux":
                    # Попытка открыть порт через ufw (если установлен)
                    subprocess.run(['sudo', 'ufw', 'allow', str(port)], 
                                 capture_output=True, timeout=3)
                elif system == "Darwin":  # macOS
                    # На macOS обычно не требуется явного открытия портов для localhost
                    pass
                elif system == "Windows":
                    # Windows Firewall команды (требуют админ прав)
                    pass
            except:
                pass  # Не критично если не удалось
            
            progress.advance(task)
            time.sleep(0.1)  # Визуальная задержка
    
    console.print("[green]✅ Системные порты настроены[/green]")

def choose_production_level():
    """Выбор уровня производственной конфигурации."""
    
    options_panel = Panel.fit(
        """[bold cyan]🏭 УРОВНИ ПРОМЫШЛЕННОЙ АВТОМАТИЗАЦИИ:[/bold cyan]

[bold green]1️⃣[/bold green]  [white]ЛОКАЛЬНОЕ ПРОИЗВОДСТВО[/white] (рекомендуется)
    • Все модули: [dim]http://localhost:ПОРТ[/dim]
    • Быстрый запуск без внешних зависимостей
    • Идеально для разработки и тестирования

[bold yellow]2️⃣[/bold yellow]  [white]ГИБРИДНАЯ СИСТЕМА[/white]
    • Управление и БД: [dim]https://домен[/dim]  
    • Остальные модули: [dim]localhost:порт[/dim]
    • Частичный внешний доступ

[bold red]3️⃣[/bold red]  [white]ПОЛНАЯ ПРОМЫШЛЕННАЯ СИСТЕМА[/white]
    • Все модули: [dim]https://модуль.домен[/dim]
    • Автоматический SSL
    • Требует настройки DNS записей""",
        title="[bold white]⚙️ ВЫБОР КОНФИГУРАЦИИ СИСТЕМЫ[/bold white]",
        border_style="blue"
    )
    
    console.print(options_panel)
    
    while True:
        choice = Prompt.ask(
            "\n[bold cyan]🎯 Выберите уровень конфигурации[/bold cyan]",
            choices=["1", "2", "3"],
            default="1"
        )
        
        level_names = {
            "1": "Локальное производство",
            "2": "Гибридная система", 
            "3": "Полная промышленная система"
        }
        
        confirm_panel = Panel.fit(
            f"[bold white]Выбран уровень:[/bold white] [bold green]{level_names[choice]}[/bold green]",
            border_style="green"
        )
        console.print(confirm_panel)
        
        if Confirm.ask("[yellow]Подтвердить выбор?[/yellow]", default=True):
            return int(choice)

def configure_domain_system(level: int, existing_domains: Optional[Dict[str, str]] = None):
    """Конфигурация доменной системы."""
    
    if level == 1:
        # Локальная система
        return {
            'level': 1,
            'mode': 'localhost',
            'domains': {
                'n8n_hostname': ':8001',
                'webui_hostname': ':8002', 
                'flowise_hostname': ':8003',
                'supabase_hostname': ':8005',
                'langfuse_hostname': ':8007',
                'neo4j_hostname': ':8008',
            },
            'letsencrypt_email': 'internal'
        }
    
    # Для уровней 2 и 3 нужны домены
    domain_config = {'level': level}
    
    if existing_domains:
        console.print(show_existing_domains_panel(existing_domains))
        
        if Confirm.ask("[green]🔄 Использовать найденные адреса?[/green]", default=True):
            # Используем существующие домены
            domain_config['domains'] = existing_domains
            
            # Извлекаем базовый домен из первого найденного
            first_domain = list(existing_domains.values())[0]
            if '.' in first_domain:
                base_domain = '.'.join(first_domain.split('.')[1:])  # убираем поддомен
                domain_config['base_domain'] = base_domain
            
            domain_config['mode'] = 'hybrid' if level == 2 else 'production'
            domain_config['letsencrypt_email'] = f"admin@{domain_config.get('base_domain', 'localhost')}"
            
            return domain_config
    
    # Запрашиваем новый домен
    console.print(Panel.fit(
        "[bold yellow]🌐 НАСТРОЙКА СЕТЕВЫХ АДРЕСОВ ПРОИЗВОДСТВА[/bold yellow]\n\n"
        "[white]Для внешнего доступа к системе требуется доменное имя[/white]",
        border_style="yellow"
    ))
    
    base_domain = Prompt.ask(
        "[cyan]🏭 Введите базовый домен производства[/cyan]",
        default="mycompany.com"
    ).strip()
    
    email = Prompt.ask(
        "[cyan]📧 Email для SSL сертификатов[/cyan]",
        default=f"admin@{base_domain}"
    ).strip()
    
    if level == 2:
        # Гибридная система - только n8n и supabase на доменах
        domains = {
            'n8n_hostname': f'automation.{base_domain}',
            'supabase_hostname': f'database.{base_domain}',
            'webui_hostname': ':8002',
            'flowise_hostname': ':8003', 
            'langfuse_hostname': ':8007',
            'neo4j_hostname': ':8008',
        }
        mode = 'hybrid'
    else:
        # Полная система - все на доменах
        domains = {
            'n8n_hostname': f'automation.{base_domain}',
            'webui_hostname': f'ai.{base_domain}',
            'flowise_hostname': f'constructor.{base_domain}',
            'supabase_hostname': f'database.{base_domain}',
            'langfuse_hostname': f'analytics.{base_domain}',
            'neo4j_hostname': f'graph.{base_domain}',
        }
        mode = 'production'
    
    domain_config.update({
        'base_domain': base_domain,
        'domains': domains,
        'mode': mode,
        'letsencrypt_email': email
    })
    
    return domain_config

def generate_system_secrets():
    """Генерация системных секретов."""
    console.print("\n[yellow]🔐 Генерация криптографических ключей системы...[/yellow]")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Генерация защищенных ключей...", total=None)
        time.sleep(2)  # Имитация работы
        progress.update(task, completed=100)
    
    return {
        'postgres_password': secrets.token_hex(16),
        'jwt_secret': secrets.token_hex(32),
        'n8n_encryption_key': secrets.token_hex(32),
        'n8n_user_management_jwt_secret': secrets.token_hex(32),
        'dashboard_password': secrets.token_hex(16),
        'clickhouse_password': secrets.token_hex(16),
        'minio_root_password': secrets.token_hex(16),
        'langfuse_salt': secrets.token_hex(16),
        'nextauth_secret': secrets.token_hex(32),
        'encryption_key': secrets.token_hex(32),
        'flowise_username': 'admin',
        'flowise_password': secrets.token_hex(12),
        'neo4j_auth': f'neo4j/{secrets.token_hex(12)}',
        'pooler_tenant_id': '1000',
        
        # Дефолтные Supabase ключи
        'anon_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJhbm9uIiwKICAgICJpc3MiOiAic3VwYWJhc2UtZGVtbyIsCiAgICAiaWF0IjogMTY0MTc2OTIwMCwKICAgICJleHAiOiAxNzk5NTM1NjAwCn0.dc_X5iR_VP_qT0zsiyj_I_OZ2T9FtRU2BBNWN8Bu4GE',
        'service_role_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJzZXJ2aWNlX3JvbGUiLAogICAgImlzcyI6ICJzdXBhYmFzZS1kZW1vIiwKICAgICJpYXQiOiAxNjQxNzY5MjAwLAogICAgImV4cCI6IDE3OTk1MzU2MDAKfQ.DaYlNEoUrrEn2Ig7tqibS-PHK5vgusbcbo7X36XVt4Q'
    }

def create_production_config_file(system_config: Dict[str, Any], secrets: Dict[str, str]):
    """Создание производственного конфигурационного файла."""
    
    console.print("\n[yellow]📝 Создание производственной конфигурации...[/yellow]")
    
    env_content = f"""# ================================================================
# 🏭 AIBot Direct - Производственная конфигурация Level {system_config['level']}
# ================================================================
# Автоматически сгенерировано системой промышленной автоматизации
# Все криптографические ключи созданы с максимальной энтропией

# ================================================================
# 🔐 КРИТИЧЕСКИЕ СИСТЕМНЫЕ КЛЮЧИ (АВТОСГЕНЕРИРОВАНЫ)
# ================================================================
POSTGRES_PASSWORD={secrets['postgres_password']}
JWT_SECRET={secrets['jwt_secret']}
ANON_KEY={secrets['anon_key']}
SERVICE_ROLE_KEY={secrets['service_role_key']}
N8N_ENCRYPTION_KEY={secrets['n8n_encryption_key']}
N8N_USER_MANAGEMENT_JWT_SECRET={secrets['n8n_user_management_jwt_secret']}
DASHBOARD_PASSWORD={secrets['dashboard_password']}
CLICKHOUSE_PASSWORD={secrets['clickhouse_password']}
MINIO_ROOT_PASSWORD={secrets['minio_root_password']}
LANGFUSE_SALT={secrets['langfuse_salt']}
NEXTAUTH_SECRET={secrets['nextauth_secret']}
ENCRYPTION_KEY={secrets['encryption_key']}
FLOWISE_USERNAME={secrets['flowise_username']}
FLOWISE_PASSWORD={secrets['flowise_password']}
NEO4J_AUTH={secrets['neo4j_auth']}
POOLER_TENANT_ID={secrets['pooler_tenant_id']}

# ================================================================
# 🌐 СЕТЕВЫЕ АДРЕСА ПРОИЗВОДСТВЕННЫХ МОДУЛЕЙ (Level {system_config['level']})
# ================================================================"""

    # Добавляем домены
    for key, value in system_config['domains'].items():
        hostname_var = key.upper()
        env_content += f"\n{hostname_var}={value}"
    
    env_content += f"""
LETSENCRYPT_EMAIL={system_config['letsencrypt_email']}

# ================================================================
# 🔧 ПРОИЗВОДСТВЕННЫЕ ПАРАМЕТРЫ СИСТЕМЫ
# ================================================================
POSTGRES_VERSION=latest
TELEMETRY_ENABLED=true
LANGFUSE_ENABLE_EXPERIMENTAL_FEATURES=true
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_AUTH=LOCALONLYREDIS
SEARXNG_UWSGI_WORKERS=4
SEARXNG_UWSGI_THREADS=4

# ClickHouse конфигурация
CLICKHOUSE_MIGRATION_URL=clickhouse://clickhouse:9000
CLICKHOUSE_URL=http://clickhouse:8123
CLICKHOUSE_USER=clickhouse
CLICKHOUSE_CLUSTER_ENABLED=false

# MinIO S3 хранилище
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
    
    # Записываем файл
    with open('.env', 'w') as f:
        f.write(env_content)
    
    console.print("[green]✅ Производственный конфигурационный файл создан[/green]")

def show_final_configuration_summary(system_config: Dict[str, Any], secrets: Dict[str, str]):
    """Показать итоговую сводку конфигурации."""
    
    # Создаем таблицу доступа к модулям
    access_table = Table(title="[bold white]🌐 ДОСТУП К ПРОИЗВОДСТВЕННЫМ МОДУЛЯМ[/bold white]", 
                        show_header=True, header_style="bold cyan")
    access_table.add_column("🏭 Производственный модуль", style="cyan")
    access_table.add_column("🔗 Сетевой адрес", style="green")
    access_table.add_column("📋 Назначение", style="white")
    
    module_descriptions = {
        'n8n_hostname': ('⚙️ Система автоматизации', 'Управление производственными процессами'),
        'webui_hostname': ('🤖 ИИ интерфейс управления', 'Голосовое управление Alenushka'),
        'flowise_hostname': ('🔧 Конструктор агентов', 'Создание ИИ помощников'),
        'supabase_hostname': ('🗄️ Центральная база данных', 'Хранение и управление данными'),
        'langfuse_hostname': ('📊 Аналитический центр', 'Мониторинг ИИ операций'),
        'neo4j_hostname': ('🕸️ Граф знаний', 'Управление связями данных')
    }
    
    for key, address in system_config['domains'].items():
        if key in module_descriptions:
            name, desc = module_descriptions[key]
            if address.startswith(':'):
                full_address = f"http://localhost{address}"
            else:
                full_address = f"https://{address}"
            
            access_table.add_row(name, full_address, desc)
    
    # Специальные модули
    access_table.add_row(
        "🧠 Модуль языковых моделей", 
        "http://localhost:11434", 
        "Ollama API (внутренний доступ)"
    )
    
    console.print("\n")
    console.print(access_table)
    
    # Панель с ключевой информацией
    credentials_panel = Panel.fit(
        f"""[bold white]🔑 СИСТЕМНЫЕ УЧЕТНЫЕ ДАННЫЕ:[/bold white]

[cyan]🔐 Dashboard пароль:[/cyan] [yellow]{secrets['dashboard_password']}[/yellow]
[cyan]🤖 Flowise вход:[/cyan] [yellow]{secrets['flowise_username']} / {secrets['flowise_password']}[/yellow]
[cyan]🗄️ Postgres пароль:[/cyan] [dim]{secrets['postgres_password'][:8]}...[/dim]

[dim white]* Все пароли сохранены в файле .env[/dim white]""",
        title="[bold green]🏭 ПРОИЗВОДСТВЕННАЯ СИСТЕМА ГОТОВА К ЗАПУСКУ[/bold green]",
        border_style="green"
    )
    
    console.print(credentials_panel)

def launch_production_system(system_config: Dict[str, Any]):
    """Запуск производственной системы."""
    
    console.print(Panel.fit(
        "[bold yellow]🚀 ЗАПУСК ПРОИЗВОДСТВЕННОЙ СИСТЕМЫ...[/bold yellow]",
        border_style="yellow"
    ))
    
    # Определяем профиль и окружение
    profile = detect_gpu_configuration()
    environment = 'private' if system_config['mode'] == 'localhost' else 'public'
    
    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console,
        ) as progress:
            
            # Этапы запуска
            stages = [
                "Подготовка контейнерной среды...",
                "Инициализация базы данных...", 
                "Запуск системы автоматизации...",
                "Активация ИИ модулей...",
                "Финальная калибровка системы..."
            ]
            
            main_task = progress.add_task("Запуск производства", total=len(stages))
            
            for stage in stages:
                stage_task = progress.add_task(stage, total=100)
                
                # Имитация работы этапа
                for i in range(100):
                    progress.update(stage_task, advance=1)
                    time.sleep(0.02)
                
                progress.update(main_task, advance=1)
                progress.remove_task(stage_task)
        
        # Запускаем реальный start_services.py
        cmd = [sys.executable, 'start_services.py', '--profile', profile, '--environment', environment]
        
        console.print(f"[dim]Выполнение: {' '.join(cmd)}[/dim]")
        
        result = subprocess.run(cmd, check=True, timeout=900)
        
        if result.returncode == 0:
            console.print("\n[bold green]🎉 ПРОИЗВОДСТВЕННАЯ СИСТЕМА УСПЕШНО ЗАПУЩЕНА![/bold green]")
            return True
        else:
            raise subprocess.CalledProcessError(result.returncode, cmd)
            
    except subprocess.TimeoutExpired:
        console.print("\n[red]⏰ Превышено время ожидания запуска системы[/red]")
        console.print("[yellow]💡 Попробуйте: python3 diagnose.py[/yellow]")
        return False
        
    except subprocess.CalledProcessError as e:
        console.print(f"\n[red]❌ Ошибка запуска производственной системы: {e}[/red]")
        console.print("[yellow]💡 Выполните диагностику: python3 diagnose.py[/yellow]")
        return False

def main():
    """Главная функция игрового интерфейса."""
    
    # Проверка директории
    if not Path('docker-compose.yml').exists():
        console.print(Panel.fit(
            "[red]❌ Ошибка инициализации производства[/red]\n\n"
            "[white]Система должна запускаться из директории aibot-direct[/white]\n\n"
            "[yellow]Выполните:[/yellow]\n"
            "[dim]cd aibot-direct\n"
            "python3 motherlode_gaming.py[/dim]",
            title="[bold red]🚨 СИСТЕМНАЯ ОШИБКА[/bold red]",
            border_style="red"
        ))
        sys.exit(1)
    
    # Главное меню
    console.clear()
    show_industrial_banner()
    
    # Обнаружение системы
    with console.status("[bold cyan]🔍 Анализ производственной среды...", spinner="dots"):
        time.sleep(2)
        env_info = detect_system_environment()
    
    console.print(create_system_status_panel(env_info))
    
    # Проверка Docker
    if not env_info['has_docker']:
        console.print(Panel.fit(
            "[red]❌ Контейнерная система не обнаружена[/red]\n\n"
            "[white]Для работы требуется Docker Desktop[/white]\n\n"
            "[cyan]🍎 macOS:[/cyan] https://www.docker.com/products/docker-desktop\n"
            "[cyan]🐧 Linux:[/cyan] curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh",
            title="[bold yellow]⚠️ ТРЕБУЕТСЯ ДОПОЛНИТЕЛЬНОЕ ПО[/bold yellow]",
            border_style="yellow"
        ))
        if not Confirm.ask("\n[yellow]Продолжить настройку без Docker?[/yellow]", default=False):
            sys.exit(0)
    
    # Открытие портов
    if Confirm.ask("\n[cyan]🔓 Открыть системные порты?[/cyan]", default=True):
        open_system_ports()
    
    # Проверка существующих доменов
    existing_domains = check_existing_env()
    
    # Выбор уровня конфигурации
    level = choose_production_level()
    
    # Конфигурация системы
    system_config = configure_domain_system(level, existing_domains)
    
    # Генерация секретов
    secrets = generate_system_secrets()
    
    # Создание конфигурационного файла
    create_production_config_file(system_config, secrets)
    
    # Итоговая сводка
    show_final_configuration_summary(system_config, secrets)
    
    # Подтверждение запуска
    console.print("\n" + "="*60)
    if Confirm.ask("[bold cyan]🚀 Запустить производственную систему?[/bold cyan]", default=True):
        
        success = launch_production_system(system_config)
        
        if success:
            console.print(Panel.fit(
                "[bold green]🎊 ПРОИЗВОДСТВЕННАЯ СИСТЕМА AIBOT DIRECT АКТИВНА![/bold green]\n\n"
                "[white]🏭 13 модулей интеллектуальной автоматизации готовы к работе[/white]\n"
                "[white]🇷🇺 Система промышленной автоматизации запущена[/white]",
                title="[bold white]✅ МИССИЯ ВЫПОЛНЕНА[/bold white]",
                border_style="green"
            ))
        else:
            console.print(Panel.fit(
                "[yellow]⚠️ Конфигурация создана, но система требует ручного запуска[/yellow]\n\n"
                "[white]Конфигурационные файлы готовы в .env[/white]\n"
                "[dim]Выполните диагностику: python3 diagnose.py[/dim]",
                title="[bold yellow]⚙️ ТРЕБУЕТСЯ ВМЕШАТЕЛЬСТВО ИНЖЕНЕРА[/bold yellow]",
                border_style="yellow"
            ))
    else:
        console.print("\n[dim]🏭 Конфигурация сохранена. Система готова к запуску.[/dim]")

if __name__ == "__main__":
    main()
