#!/usr/bin/env python3
"""
AIBot Direct - AI Automation Platform
Революционная система для автоматизации российского бизнеса

Website: https://AIBot.Direct
"""

import os
import sys
import subprocess
import argparse
import json
import time
import secrets
import string
import shutil
import platform
from pathlib import Path
from datetime import datetime

# Rich library для красивого CLI (опционально)
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, track
    from rich.prompt import Prompt, Confirm
    from rich.text import Text
    from rich.table import Table
    from rich import print as rprint
    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    # Fallback для обычного print если Rich не установлен
    def rprint(*args, **kwargs):
        print(*args, **kwargs)

class AIBotDirectLauncher:
    def __init__(self):
        self.version = "1.0.0"
        self.codename = "Alenushka"
        self.website = "https://AIBot.Direct"
        self.author = "AIBot Direct Team"
        
        # Инициализация Rich console если доступен
        if HAS_RICH:
            self.console = Console()
        else:
            self.console = None
            
        self.ascii_logo = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                   🤖 AIBot Direct 🤖                        ║
    ║                                                              ║
    ║              Чит-код для AI автоматизации                   ║
    ║              Ваша AI помощница Alenushka                   ║
    ║                                                              ║
    ║  🌐 Website: https://AIBot.Direct                            ║
    ║  🎤 С поддержкой голоса и Whisper                           ║
    ╚══════════════════════════════════════════════════════════════╝
        """

    def print_banner(self):
        """Вывести логотип AIBot Direct."""
        if HAS_RICH and self.console:
            # Красивый баннер с Rich
            banner_text = f"""
[bold cyan]🤖 AIBot Direct 🤖[/bold cyan]

[green]Чит-код для AI автоматизации[/green]
[blue]Ваша AI помощница Alenushka[/blue]

[yellow]🌐 Website: {self.website}[/yellow]
[magenta]🎤 С поддержкой голоса и Whisper[/magenta]
[white]Version: {self.version} '{self.codename}'[/white]
            """
            panel = Panel(banner_text, title="🚀 Добро пожаловать!", border_style="cyan")
            self.console.print(panel)
        else:
            # Fallback для обычного терминала
            print(self.ascii_logo)
            print(f"Version: {self.version} '{self.codename}'")
            print(f"Website: {self.website}")
            print()

    def generate_secure_secret(self, length=32):
        """Генерация криптографически стойкого секрета."""
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def configure_supabase(self):
        """Интерактивная настройка Supabase ключей с улучшенным UX."""
        
        if HAS_RICH and self.console:
            # Красивая настройка с Rich
            self.console.print("\n")
            supabase_panel = Panel(
                "[bold yellow]🔐 НАСТРОЙКА SUPABASE[/bold yellow]\n\n"
                "[red]⚠️ Эти ключи ОБЯЗАТЕЛЬНЫ из вашего Supabase проекта![/red]\n"
                "[blue]📋 Dashboard → Settings → API → Project API keys[/blue]\n\n"
                "[green]💡 Займет всего 30 секунд![/green]",
                title="🔑 Обязательные ключи", 
                border_style="yellow"
            )
            self.console.print(supabase_panel)
            
            # Умные промпты с валидацией
            jwt_secret = Prompt.ask(
                "\n[bold green]🔑 JWT_SECRET[/bold green] (минимум 32 символа)", 
                console=self.console
            )
            while len(jwt_secret) < 32:
                self.console.print("[red]❌ Слишком короткий! Нужно минимум 32 символа[/red]")
                jwt_secret = Prompt.ask("[bold green]🔑 JWT_SECRET[/bold green]", console=self.console)
            
            anon_key = Prompt.ask(
                "[bold blue]🔓 ANON_KEY[/bold blue] (начинается с 'eyJ')", 
                console=self.console
            )
            while not anon_key.startswith("eyJ"):
                self.console.print("[red]❌ Должен начинаться с 'eyJ' (JWT токен)[/red]")
                anon_key = Prompt.ask("[bold blue]🔓 ANON_KEY[/bold blue]", console=self.console)
            
            service_role_key = Prompt.ask(
                "[bold red]🔐 SERVICE_ROLE_KEY[/bold red] (начинается с 'eyJ')", 
                console=self.console
            )
            while not service_role_key.startswith("eyJ"):
                self.console.print("[red]❌ Должен начинаться с 'eyJ' (JWT токен)[/red]")
                service_role_key = Prompt.ask("[bold red]🔐 SERVICE_ROLE_KEY[/bold red]", console=self.console)
            
            # Опциональные домены
            domain_panel = Panel(
                "[bold cyan]🌐 НАСТРОЙКА ДОМЕНОВ (ОПЦИОНАЛЬНО)[/bold cyan]\n\n"
                "[yellow]💡 Оставьте пустым для localhost[/yellow]\n"
                "[green]🏠 Идеально для VPS серверов![/green]",
                border_style="cyan"
            )
            self.console.print(domain_panel)
            
            use_domains = Confirm.ask(
                "\n[bold cyan]🤔 Настроить собственные домены?[/bold cyan]", 
                default=False, 
                console=self.console
            )
            
        else:
            # Fallback для обычного терминала
            print("\n" + "="*60)
            print("🔐 НАСТРОЙКА SUPABASE - Обязательные ключи")
            print("="*60)
            
            print("\n🔐 Настройка Supabase JWT секретов:")
            print("⚠️ Эти ключи ДОЛЖНЫ быть получены из вашего Supabase проекта!")
            print("📋 Dashboard -> Settings -> API -> Project API keys")
            
            jwt_secret = input("\n🔑 Введите JWT_SECRET (минимум 32 символа): ").strip()
            while len(jwt_secret) < 32:
                print("❌ JWT_SECRET должен быть минимум 32 символа!")
                jwt_secret = input("🔑 Введите JWT_SECRET: ").strip()
            
            anon_key = input("🔓 Введите ANON_KEY (из Supabase Dashboard): ").strip()
            while not anon_key.startswith("eyJ"):
                print("❌ ANON_KEY должен начинаться с 'eyJ' (JWT токен)")
                anon_key = input("🔓 Введите ANON_KEY: ").strip()
            
            service_role_key = input("🔐 Введите SERVICE_ROLE_KEY (из Supabase Dashboard): ").strip()
            while not service_role_key.startswith("eyJ"):
                print("❌ SERVICE_ROLE_KEY должен начинаться с 'eyJ' (JWT токен)")
                service_role_key = input("🔐 Введите SERVICE_ROLE_KEY: ").strip()
            
            print("\n🌐 Настройка доменов (ОПЦИОНАЛЬНО):")
            print("💡 Оставьте пустым для localhost, или укажите свои домены")
            use_domains = input("\n🤔 Хотите настроить собственные домены? (y/N): ").strip().lower() in ['y', 'yes', 'д', 'да']
        
        hostnames = {}
        if use_domains:
            domains = {
                "N8N_HOSTNAME": "n8n (workflows)",
                "WEBUI_HOSTNAME": "Alenushka (Open WebUI)", 
                "FLOWISE_HOSTNAME": "Flowise (AI builder)",
                "SUPABASE_HOSTNAME": "Supabase (database)",
                "LANGFUSE_HOSTNAME": "Langfuse (monitoring)",
                "OLLAMA_HOSTNAME": "Ollama (LLM server)",
                "SEARXNG_HOSTNAME": "SearXNG (search)",
                "NEO4J_HOSTNAME": "Neo4j (graph DB)"
            }
            
            if HAS_RICH and self.console:
                self.console.print("\n[bold yellow]🌐 Настройка доменов:[/bold yellow]")
                for env_key, description in domains.items():
                    domain = Prompt.ask(
                        f"[cyan]🌐 {description}[/cyan] (пустое = localhost)",
                        default="",
                        console=self.console
                    )
                    if domain:
                        hostnames[env_key] = domain
                
                email = Prompt.ask(
                    "[green]📧 Email для Let's Encrypt SSL[/green] (пустое = internal)",
                    default="internal", 
                    console=self.console
                )
                hostnames["LETSENCRYPT_EMAIL"] = email
            else:
                for env_key, description in domains.items():
                    domain = input(f"🌐 Домен для {description} (пустое = localhost): ").strip()
                    if domain:
                        hostnames[env_key] = domain
                
                email = input("📧 Email для Let's Encrypt SSL (пустое = internal): ").strip()
                hostnames["LETSENCRYPT_EMAIL"] = email if email else "internal"
        
        if HAS_RICH and self.console:
            self.console.print("\n[bold green]✅ Конфигурация Supabase готова![/bold green]")
        else:
            print("\n✅ Конфигурация Supabase готова!")
            
        return jwt_secret, anon_key, service_role_key, hostnames

    def install_ffmpeg(self):
        """Установка FFmpeg для обработки аудио/видео."""
        print("🎵 Проверяю FFmpeg для работы с аудио/видео...")
        
        try:
            subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
            print("✅ FFmpeg уже установлен!")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("📦 Устанавливаю FFmpeg...")
            
        system = platform.system()
        try:
            if system == "Darwin":  # macOS
                subprocess.run(["brew", "install", "ffmpeg"], check=True)
            elif system == "Linux":
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "ffmpeg", "-y"], check=True)
            elif system == "Windows":
                print("⚠️ Для Windows установите FFmpeg вручную:")
                print("   https://ffmpeg.org/download.html")
                return False
            else:
                print(f"⚠️ Неизвестная ОС: {system}")
                return False
            
            print("✅ FFmpeg успешно установлен!")
            return True
            
        except subprocess.CalledProcessError:
            print("❌ Не удалось установить FFmpeg автоматически")
            print("💡 Установите вручную: https://ffmpeg.org/download.html")
            return False

    def generate_env_file(self):
        """Автоматическая генерация .env файла с безопасными секретами."""
        print("🔐 Генерирую безопасные секреты для .env файла...")
        
        # Генерируем секреты
        n8n_encryption_key = self.generate_secure_secret(32)
        n8n_jwt_secret = self.generate_secure_secret(32)
        postgres_password = self.generate_secure_secret(24)
        dashboard_password = self.generate_secure_secret(16)
        
        # ВСЕГДА интерактивная настройка Supabase
        jwt_secret, anon_key, service_role_key, hostnames = self.configure_supabase()
        
        # Дополнительные секреты для всех сервисов
        neo4j_password = self.generate_secure_secret(16)
        clickhouse_password = self.generate_secure_secret(24)
        minio_password = self.generate_secure_secret(20)
        langfuse_salt = self.generate_secure_secret(32)
        nextauth_secret = self.generate_secure_secret(32)
        encryption_key = self.generate_secure_secret(32)
        
        # Базовый шаблон .env
        env_content = f"""# AIBot Direct Configuration
# Автоматически сгенерировано: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Website: https://AIBot.Direct

############
# N8N Configuration - Автоматически сгенерировано
############
N8N_ENCRYPTION_KEY={n8n_encryption_key}
N8N_USER_MANAGEMENT_JWT_SECRET={n8n_jwt_secret}

############
# Supabase Secrets - Введены пользователем
############
POSTGRES_PASSWORD={postgres_password}
JWT_SECRET={jwt_secret}
ANON_KEY={anon_key}
SERVICE_ROLE_KEY={service_role_key}
DASHBOARD_USERNAME=aibot_admin
DASHBOARD_PASSWORD={dashboard_password}
POOLER_TENANT_ID=aibot-direct-{secrets.randbelow(10000):04d}
POOLER_DB_POOL_SIZE=5

############
# Neo4j Secrets - Автоматически сгенерировано
############   
NEO4J_AUTH=neo4j/{neo4j_password}

############
# Langfuse credentials - Автоматически сгенерировано
############
CLICKHOUSE_PASSWORD={clickhouse_password}
MINIO_ROOT_PASSWORD={minio_password}
LANGFUSE_SALT={langfuse_salt}
NEXTAUTH_SECRET={nextauth_secret}
ENCRYPTION_KEY={encryption_key}

############
# Production Hostnames
############"""
        
        # Добавляем hostnames если настроены
        if hostnames:
            for key, value in hostnames.items():
                env_content += f"\n{key}={value}"
        else:
            env_content += """
# Настройте домены если используете собственный хостинг:
# N8N_HOSTNAME=n8n.yourdomain.com
# WEBUI_HOSTNAME=openwebui.yourdomain.com
# FLOWISE_HOSTNAME=flowise.yourdomain.com
# SUPABASE_HOSTNAME=supabase.yourdomain.com
# LANGFUSE_HOSTNAME=langfuse.yourdomain.com
# OLLAMA_HOSTNAME=ollama.yourdomain.com
# SEARXNG_HOSTNAME=searxng.yourdomain.com
# NEO4J_HOSTNAME=neo4j.yourdomain.com
# LETSENCRYPT_EMAIL=your-email@domain.com"""
        
        env_content += f"""

############
# AIBot Direct Settings
############
AIBOT_SYSTEM_NAME=Alenushka
AIBOT_WEBSITE=https://AIBot.Direct
AIBOT_VERSION={self.version}
"""
        
        # Записываем .env файл
        with open(".env", "w", encoding="utf-8") as f:
            f.write(env_content)
        
        print("✅ Файл .env создан с безопасными секретами!")
        print("🔐 Supabase ключи настроены пользователем")
        return True

    def aibot_install(self, profile="cpu", environment="private"):
        """Главная функция установки AIBot Direct."""
        print("🤖 Запускаю установку AIBot Direct (Alenushka)...")
        print(f"🌐 Сайт проекта: {self.website}")
        print("🔐 Потребуется настройка Supabase ключей")
        print()
        
        # 1. Установка FFmpeg
        if not self.install_ffmpeg():
            print("⚠️ FFmpeg не установлен - голосовые функции могут не работать")
        
        # 2. Автоматически генерируем .env
        if not self.generate_env_file():
            return False
        
        # 3. Запускаем базовую систему
        if not self.start_base_system(profile, environment):
            return False
        
        # 4. Настраиваем AIBot Direct компоненты
        self.setup_aibot_components()
        
        print("🎉 AIBot Direct успешно установлен!")
        print(f"🤖 Ваша AI помощница Alenushka готова к работе!")
        self.show_success_info()
        
        return True

    def start_base_system(self, profile, environment):
        """Запуск базовой системы."""
        print("🚀 Запускаю AI экосистему...")
        
        # Проверяем наличие оригинального скрипта
        if not Path("start_services.py").exists():
            print("❌ Файл start_services.py не найден!")
            return False
        
        try:
            # Запускаем оригинальный скрипт
            cmd = [sys.executable, "start_services.py", "--profile", profile, "--environment", environment]
            print(f"⚙️ Команда: {' '.join(cmd)}")
            
            subprocess.run(cmd, check=True)
            print("✅ Базовая система успешно запущена!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Ошибка запуска системы: {e}")
            return False

    def setup_aibot_components(self):
        """Настройка компонентов AIBot Direct."""
        print("🇷🇺 Настраиваю российские AI компоненты...")
        
        # Создаем структуру директорий
        directories = [
            "aibot-russian-ai",
            "aibot-business", 
            "aibot-telegram",
            "aibot-audio",
            "aibot-templates",
            "aibot-configs"
        ]
        
        for directory in directories:
            Path(directory).mkdir(exist_ok=True)
        
        print("✅ Компоненты AIBot Direct настроены!")

    def show_success_info(self):
        """Показать информацию об успешной установке."""
        print("\n" + "="*60)
        print("🎉 ПОЗДРАВЛЯЕМ! AIBot Direct успешно установлен!")
        print("="*60)
        
        endpoints = {
            "🤖 Alenushka (голосовая AI)": "http://localhost:3000",
            "⚙️ n8n Workflows": "http://localhost:5678", 
            "🗄️ Supabase Dashboard": "http://localhost:8005",
            "🔧 Flowise AI Builder": "http://localhost:8003",
            "📊 Langfuse Analytics": "http://localhost:8007",
            "🔍 SearXNG Search": "http://localhost:8006",
            "📈 Neo4j Browser": "http://localhost:8008",
            "🎤 Whisper Speech API": "http://localhost:9000"
        }
        
        print("\n🌐 Доступные интерфейсы:")
        for name, url in endpoints.items():
            print(f"   • {name}: {url}")
        
        print(f"\n🎮 Команды управления:")
        print(f"   python aibot_start.py --help            - помощь")
        print(f"   docker compose -p localai ps            - статус сервисов")
        print(f"   docker compose -p localai down          - остановить все")
        
        print(f"\n🎤 Голосовые возможности:")
        print(f"   • Говорите с Alenushka через микрофон в Open WebUI")
        print(f"   • Загружайте аудиофайлы для транскрипции")
        print(f"   • Telegram боты принимают голосовые сообщения")
        print(f"   • FFmpeg + Whisper обрабатывают любые форматы")
        
        print(f"\n🌐 Больше информации:")
        print(f"   • Сайт: {self.website}")
        print(f"   • Готовые workflow'ы: n8n-business-workflows/")
        print(f"   • Настройка бизнеса: aibot-business/integrations-setup.md")
        
        print("\n" + "="*60)

def main():
    parser = argparse.ArgumentParser(
        description="🤖 AIBot Direct - AI Automation Platform",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Примеры использования:
  python aibot_start.py --profile cpu                     # Установка на CPU
  python aibot_start.py --profile gpu-nvidia              # Установка с GPU Nvidia
  python aibot_start.py --environment public              # Публичное развертывание

Особенности установки:
  🔐 Всегда требуется настройка Supabase ключей (JWT_SECRET, ANON_KEY, SERVICE_ROLE_KEY)
  🌐 Домены опциональны - можно использовать localhost или свои домены
  🔒 Остальные секреты генерируются автоматически
  🎤 FFmpeg устанавливается автоматически для голосовых функций

Больше информации: https://AIBot.Direct
        """
    )
    
    parser.add_argument('--profile', 
                       choices=['cpu', 'gpu-nvidia', 'gpu-amd', 'none'], 
                       default='cpu',
                       help='Профиль оборудования (по умолчанию: cpu)')
    
    parser.add_argument('--environment', 
                       choices=['private', 'public'], 
                       default='private',
                       help='Среда развертывания (по умолчанию: private)')
    
    parser.add_argument('--version', action='version', version='AIBot Direct 1.0.0')
    
    args = parser.parse_args()
    
    launcher = AIBotDirectLauncher()
    launcher.print_banner()
    
    # Запускаем установку
    success = launcher.aibot_install(args.profile, args.environment)
    
    if success:
        print("\n🚀 AIBot Direct готов к работе!")
        sys.exit(0)
    else:
        print("\n❌ Установка не завершена. Проверьте ошибки выше.")
        sys.exit(1)

if __name__ == "__main__":
    main()
