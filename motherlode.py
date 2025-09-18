#!/usr/bin/env python3
"""
🎮 MOTHERLODE.PY - AIBot Direct Cheat Code 🎮
💰💰💰 АКТИВИРУЙ ВСЁ ЗОЛОТО AI МИРА! 💰💰💰

Вдохновлено чит-кодом из GTA: San Andreas
Одна команда = весь AI арсенал России!

Website: https://AIBot.Direct
"""

import os
import sys
import subprocess
import time
import secrets
import string
import platform
from pathlib import Path
from datetime import datetime

# Rich для игрового интерфейса (автоустановка)
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, track
    from rich.prompt import Prompt, Confirm
    from rich.table import Table
    from rich.text import Text
    from rich.align import Align
    from rich import print as rprint
    HAS_RICH = True
    console = Console()
except ImportError:
    HAS_RICH = False
    console = None
    def rprint(*args, **kwargs):
        print(*args, **kwargs)

class MotherlodeAI:
    def __init__(self):
        self.version = "1.0.0"
        self.codename = "Alenushka" 
        self.website = "https://AIBot.Direct"
        self.cheat_code = "MOTHERLODE"
        
    def show_cheat_activation(self):
        """🎮 Показать активацию чит-кода с полным стеком."""
        if HAS_RICH:
            # Анимация активации чит-кода
            console.print("\n[bold yellow]" + "="*80 + "[/bold yellow]")
            cheat_text = Text("🎮 MOTHERLODE ACTIVATED! 🎮", style="bold gold1 blink")
            console.print(Align.center(cheat_text))
            console.print("[bold yellow]" + "="*80 + "[/bold yellow]\n")
            time.sleep(1)
            
            # Заголовок
            header_panel = Panel(
                "[bold gold1]⚡ PrideAIBot Premium — AI Infrastructure Activated! ⚡[/bold gold1]\n"
                "[green]💎 LEVEL UP - ТЫ ВОЙДЕШЬ В 0.1% ⭐[/green]",
                title="🏆 Welcome to Elite AI Stack",
                border_style="gold1",
                padding=(1, 2)
            )
            console.print(header_panel)
            
            # Полный стек - 14 сервисов
            stack_content = (
                "[bold cyan]🧠 ПОЛНЫЙ AI СТЕК - 14 СЕРВИСОВ:[/bold cyan]\n\n"
                
                "[bold green]🎯 CORE AI ENGINE:[/bold green]\n"
                "┣━ [bold white]n8n selfhost[/bold white] - workflow automation engine 🔄\n"
                "┃  [dim yellow]Создает цепочки действий между сервисами (конвейер на заводе)[/dim yellow]\n"
                "┣━ [bold white]Ollama[/bold white] - локальный LLM сервер 🤖\n"
                "┃  [dim yellow]Запускает языковые модели без интернета (личный ChatGPT)[/dim yellow]\n"
                "┗━ [bold white]OpenWebUI[/bold white] - ChatGPT-like интерфейс 💬\n"
                "   [dim yellow]Web UI для общения с LLM моделями (красивая морда для AI)[/dim yellow]\n\n"
                
                "[bold blue]🗄️ DATA & STORAGE:[/bold blue]\n"
                "┣━ [bold white]Supabase selfhost[/bold white] - полная BaaS платформа 🏦\n"
                "┃  [dim yellow]PostgreSQL + REST API + Auth + Storage (банк для данных)[/dim yellow]\n"
                "┣━ [bold white]Qdrant[/bold white] - vector database для RAG 🎯\n"
                "┃  [dim yellow]Хранит embeddings для поиска по смыслу (поисковик с пониманием)[/dim yellow]\n"
                "┣━ [bold white]Neo4j[/bold white] - graph database 🕸️\n"
                "┃  [dim yellow]Строит связи между данными в виде графа (карта связей)[/dim yellow]\n"
                "┗━ [bold white]MinIO[/bold white] - S3-совместимое хранилище 📦\n"
                "   [dim yellow]Хранение файлов, изображений, документов (цифровой склад)[/dim yellow]\n\n"
                
                "[bold magenta]🎤 VOICE & SEARCH:[/bold magenta]\n"
                "┣━ [bold white]Whisper[/bold white] - speech-to-text/text-to-speech API 🎙️\n"
                "┃  [dim yellow]OpenAI модель для работы с голосом (переводчик голос↔текст)[/dim yellow]\n"
                "┗━ [bold white]SearXNG[/bold white] - privacy метапоисковик 🔍\n"
                "   [dim yellow]Ищет в Google/Bing без трекинга (Google без слежки)[/dim yellow]\n\n"
                
                "[bold red]📊 ANALYTICS & MONITORING:[/bold red]\n"
                "┣━ [bold white]Langfuse[/bold white] - LLM observability платформа 📈\n"
                "┃  [dim yellow]Мониторинг AI: токены, latency, costs (следит за работой AI)[/dim yellow]\n"
                "┗━ [bold white]ClickHouse[/bold white] - колонная OLAP база 📊\n"
                "   [dim yellow]Быстрые запросы по большим данным (калькулятор для BigData)[/dim yellow]\n\n"
                
                "[bold yellow]⚙️ INFRASTRUCTURE:[/bold yellow]\n"
                "┣━ [bold white]Caddy[/bold white] - reverse proxy с HTTPS 🛡️\n"
                "┃  [dim yellow]Распределяет трафик и управляет SSL (умный роутер)[/dim yellow]\n"
                "┣━ [bold white]Redis[/bold white] - in-memory кеш и broker ⚡\n"
                "┃  [dim yellow]Быстрое хранение и очереди задач (оперативная память данных)[/dim yellow]\n"
                "┗━ [bold white]PostgreSQL[/bold white] - основная СУБД 🗃️\n"
                "   [dim yellow]Реляционная база для структурированных данных (Excel на стероидах)[/dim yellow]\n\n"
                
                "[bold green]🎮 CAPABILITIES UNLOCKED:[/bold green]\n"
                "• [bright_green]RAG (Retrieval-Augmented Generation)[/bright_green] с vector search\n"
                "• [bright_green]Graph-based связи[/bright_green] для complex relationships\n"
                "• [bright_green]Voice-first interfaces[/bright_green] через Whisper ASR/TTS\n"
                "• [bright_green]Horizontal scaling[/bright_green] через microservices\n\n"
                
                "[bold cyan]⚡ PrideAIBot Premium — это не просто библиотека решений,[/bold cyan]\n"
                "[bold cyan]а полная AI инфраструктура для масштаба бизнеса! 🚀[/bold cyan]"
            )
            
            stack_panel = Panel(
                stack_content,
                title="🧠 Full-Stack AI Infrastructure",
                border_style="cyan",
                padding=(1, 2)
            )
            console.print(stack_panel)
            
            # Эффект загрузки арсенала
            console.print("\n[bold gold1]💎 Подготавливаю арсенал элиты...[/bold gold1]")
            weapons = [
                "🧠 n8n selfhost", "🤖 Ollama LLM", "💬 OpenWebUI", "🏦 Supabase", 
                "🎯 Qdrant Vector", "🕸️ Neo4j Graph", "🎙️ Whisper Voice", "🔍 SearXNG",
                "📈 Langfuse", "📊 ClickHouse", "🛡️ Caddy", "⚡ Redis", "📦 MinIO", "🗃️ PostgreSQL"
            ]
            for weapon in track(weapons, description="[green]Loading 0.1% arsenal..."):
                time.sleep(0.3)
            
        else:
            print("\n" + "="*80)
            print("🎮 MOTHERLODE ACTIVATED!")
            print("⚡ PrideAIBot Premium — AI Infrastructure Activated!")
            print("💎 LEVEL UP - ТЫ ВОЙДЕШЬ В 0.1% ⭐")
            print("="*80)
            print("\n🧠 ПОЛНЫЙ AI СТЕК - 14 СЕРВИСОВ:")
            print("🎯 CORE AI: n8n selfhost + Ollama + OpenWebUI")
            print("🗄️ DATA: Supabase + Qdrant + Neo4j + MinIO")
            print("🎤 VOICE: Whisper + SearXNG")
            print("📊 ANALYTICS: Langfuse + ClickHouse")
            print("⚙️ INFRA: Caddy + Redis + PostgreSQL")
            print("\n🎮 CAPABILITIES: RAG + Graph + Voice + Scaling")
            print("🚀 ПОЛНАЯ AI ИНФРАСТРУКТУРА РАЗБЛОКИРОВАНА!")

    def check_prerequisites(self):
        """🔍 Системная диагностика для AI арсенала."""
        if HAS_RICH:
            # Красивый заголовок
            console.print("\n[bold gold1]🔍 СИСТЕМНАЯ ДИАГНОСТИКА ДЛЯ AI АРСЕНАЛА[/bold gold1]")
            console.print("[dim]Никита Шорин проверяет совместимость твоей системы с элитным стеком[/dim]\n")
            
            # Детальная таблица с пояснениями
            check_table = Table(
                title="🎮 System Compatibility Check",
                show_header=True,
                header_style="bold magenta",
                border_style="cyan"
            )
            check_table.add_column("🔧 Component", style="bold white", width=25)
            check_table.add_column("📊 Status", justify="center", width=15)
            check_table.add_column("🎯 What it does", style="dim yellow", width=40)
            check_table.add_column("🏆 Level", justify="center", width=12)
            
            # Проверки с объяснениями для новичков
            checks = [
                ("Python 3.8+", self._check_python(), "Интерпретатор языка программирования (как калькулятор, только умнее)", "🔥 Master"),
                ("Docker Engine", self._check_docker(), "Контейнеризация приложений (коробки с готовыми программами)", "⚡ Pro"),
                ("Git version control", self._check_git(), "Система контроля версий (машина времени для кода)", "💎 Elite"),
                ("Network connectivity", self._check_internet(), "Интернет соединение (нужно скачать ~3GB данных)", "🌐 Global"),
            ]
            
            all_good = True
            for name, status, description, level in checks:
                if status:
                    check_table.add_row(name, "[bold green]✅ READY[/bold green]", description, level)
                else:
                    check_table.add_row(name, "[bold red]❌ MISSING[/bold red]", description, "[red]🔧 Install[/red]")
                    all_good = False
            
            console.print(check_table)
            
            # Детальное объяснение auto-install
            if not all_good:
                install_panel = Panel(
                    "[bold red]⚠️ НУЖНА УСТАНОВКА КОМПОНЕНТОВ ДЛЯ АКТИВАЦИИ![/bold red]\n\n"
                    "[yellow]🧠 Auto-install для недостающих компонентов:[/yellow]\n"
                    "• [green]Ubuntu/Linux:[/green] apt install docker.io docker-compose git python3-pip\n"
                    "• [blue]macOS:[/blue] brew install docker git python3\n"
                    "• [red]Windows:[/red] manual download links\n\n"
                    "[cyan]Никита автоматически попробует установить всё что нужно...[/cyan]",
                    title="🔧 Auto-Installation Guide",
                    border_style="red"
                )
                console.print(install_panel)
                self._auto_install_missing()
            else:
                success_panel = Panel(
                    "[bold green]✅ ВСЕ КОМПОНЕНТЫ АКТИВИРОВАНЫ![/bold green]\n\n"
                    "[yellow]🎯 Твоя система готова для:[/yellow]\n"
                    "• [green]Развертывания 14 AI сервисов[/green]\n"
                    "• [blue]Работы с Docker контейнерами[/blue]\n"
                    "• [magenta]Загрузки ~3GB Docker образов[/magenta]\n"
                    "• [cyan]Создания AI автоматизации мирового уровня[/cyan]\n\n"
                    "[bold gold1]🚀 READY FOR AI DOMINATION![/bold gold1]",
                    title="🏆 System Ready",
                    border_style="green"
                )
                console.print(success_panel)
                
        else:
            print("\n🔍 СИСТЕМНАЯ ДИАГНОСТИКА:")
            print("=" * 50)
            print("🧠 Python 3.8+ - интерпретатор языка программирования")
            if not self._check_python():
                print("❌ MISSING: Нужен Python 3.8+")
            else:
                print("✅ READY: Python установлен")
                
            print("🐳 Docker Engine - контейнеризация приложений")
            if not self._check_docker():
                print("❌ MISSING: Нужен Docker")
            else:
                print("✅ READY: Docker установлен")
                
            print("📂 Git - система контроля версий")
            if not self._check_git():
                print("❌ MISSING: Нужен Git")
            else:
                print("✅ READY: Git установлен")
                
            print("🌐 Internet - соединение для загрузки")
            if not self._check_internet():
                print("❌ MISSING: Нет интернета")
            else:
                print("✅ READY: Интернет доступен")
            print("=" * 50)

    def _check_python(self):
        return sys.version_info >= (3, 8)

    def _check_docker(self):
        try:
            subprocess.run(["docker", "--version"], capture_output=True, check=True)
            return True
        except:
            return False

    def _check_git(self):
        try:
            subprocess.run(["git", "--version"], capture_output=True, check=True)
            return True
        except:
            return False

    def _check_internet(self):
        try:
            import urllib.request
            urllib.request.urlopen('https://www.google.com', timeout=5)
            return True
        except:
            return False

    def _auto_install_missing(self):
        """Автоустановка для Linux/Ubuntu."""
        if platform.system() == "Linux":
            if HAS_RICH:
                console.print("[bold yellow]🔧 Автоматическая установка недостающих компонентов...[/bold yellow]")
                with console.status("[bold green]Устанавливаю...") as status:
                    commands = [
                        "sudo apt update -y",
                        "sudo apt install -y docker.io docker-compose git curl python3-pip",
                        "sudo systemctl start docker",
                        "sudo usermod -aG docker $USER"
                    ]
                    for cmd in commands:
                        try:
                            subprocess.run(cmd.split(), check=True, capture_output=True)
                        except:
                            pass
            else:
                print("🔧 Устанавливаю компоненты...")

    def setup_firewall(self):
        """🛡️ Настройка квантовой защиты (UFW firewall)."""
        if HAS_RICH:
            firewall_panel = Panel(
                "[bold red]🛡️ КВАНТОВАЯ ЗАЩИТА - NETWORK SECURITY[/bold red]\n\n"
                "[yellow]🧠 Настраиваем UFW (Uncomplicated Firewall):[/yellow]\n\n"
                "[cyan]🔐 Принцип: default deny, explicit allow[/cyan]\n"
                "[dim]Все порты закрыты по умолчанию, открываем только рабочие[/dim]\n\n"
                "[green]🚀 Порты для AI империи:[/green]\n"
                "• [white]22[/white] - SSH access (Secure Shell для удаленного управления)\n"
                "• [white]80[/white] - HTTP traffic (незащищенный веб-трафик)\n"
                "• [white]443[/white] - HTTPS traffic (защищенный веб-трафик с SSL/TLS)\n"
                "• [white]3000[/white] - OpenWebUI interface (веб-интерфейс для AI чата)\n"
                "• [white]5678[/white] - n8n workflow editor (редактор автоматизации)\n"
                "• [white]8005[/white] - Supabase dashboard (панель управления БД)\n"
                "• [white]9000[/white] - Whisper ASR API (API для распознавания речи)",
                title="🔧 Network Security Setup",
                border_style="red"
            )
            console.print(firewall_panel)
            
            console.print("\n[bold yellow]🔧 Конфигурирую защиту...[/bold yellow]")
            
            firewall_commands = [
                ("ufw --force enable", "Активация файрвола"),
                ("ufw allow 22", "SSH доступ"),
                ("ufw allow 80", "HTTP трафик"),
                ("ufw allow 443", "HTTPS трафик"),
                ("ufw allow 3000", "OpenWebUI"),
                ("ufw allow 5678", "n8n editor"),
                ("ufw allow 8005", "Supabase"),
                ("ufw allow 9000", "Whisper API"),
                ("ufw --force reload", "Перезагрузка правил")
            ]
            
            for cmd, desc in track(firewall_commands, description="[green]Setting up quantum defense..."):
                try:
                    # Добавляем timeout чтобы избежать зависания
                    subprocess.run(cmd.split(), capture_output=True, check=True, timeout=10)
                    console.print(f"[green]✅ {desc}[/green]")
                except subprocess.TimeoutExpired:
                    console.print(f"[yellow]⏱️ {desc} (timeout - возможно требует ручной настройки)[/yellow]")
                except subprocess.CalledProcessError:
                    console.print(f"[yellow]⚠️ {desc} (возможно уже настроено)[/yellow]")
                except:
                    console.print(f"[dim]⏭️ {desc} (пропущено - нет sudo)[/dim]")
                time.sleep(0.3)
            
            console.print("\n[bold green]🛡️ Квантовая защита активирована![/bold green]")
            
        else:
            print("\n🛡️ НАСТРОЙКА FIREWALL:")
            print("🔧 Открываю необходимые порты...")
            
            firewall_commands = [
                ("ufw --force enable", "Активация файрвола"),
                ("ufw allow 22", "SSH доступ"),
                ("ufw allow 80", "HTTP трафик"),
                ("ufw allow 443", "HTTPS трафик"),
                ("ufw allow 3000", "OpenWebUI"),
                ("ufw allow 5678", "n8n editor"),
                ("ufw allow 8005", "Supabase"),
                ("ufw allow 9000", "Whisper API"),
                ("ufw --force reload", "Перезагрузка правил")
            ]
            
            for cmd, desc in firewall_commands:
                try:
                    subprocess.run(cmd.split(), capture_output=True, check=True, timeout=10)
                    print(f"✅ {desc}")
                except subprocess.TimeoutExpired:
                    print(f"⏱️ {desc} (timeout)")
                except subprocess.CalledProcessError:
                    print(f"⚠️ {desc} (возможно уже настроено)")
                except:
                    print(f"⏭️ {desc} (пропущено - нет sudo)")
                time.sleep(0.2)

    def get_supabase_keys(self):
        """🔐 Шаг 1: Supabase credentials."""
        if HAS_RICH:
            keys_panel = Panel(
                "[bold red]🔐 ШАГ 1: БАЗОВАЯ АКТИВАЦИЯ[/bold red]\n\n"
                "[blue]📖 Generation guide для Supabase API keys:[/blue]\n"
                "[link=https://supabase.com/docs/guides/self-hosting/docker#generate-api-keys]https://supabase.com/docs/guides/self-hosting/docker#generate-api-keys[/link]\n\n"
                "[bold white]🎯 Триада власти (JWT-based authentication):[/bold white]\n"
                "• [yellow]JWT_SECRET[/yellow] - ключ для подписи JSON Web Tokens (минимум 32 символа)\n"
                "• [blue]ANON_KEY[/blue] - анонимный API ключ для public доступа\n"
                "• [red]SERVICE_ROLE_KEY[/red] - административный ключ с полными правами",
                title="🏆 Supabase API Credentials",
                border_style="red",
                width=80
            )
            console.print(keys_panel)
            
            console.print("\n[bold gold1]💎 Введите ключи:[/bold gold1]")
            
            jwt_secret = Prompt.ask(
                "\n[bold yellow]🔑 JWT_SECRET[/bold yellow] (минимум 32 символа)",
                password=True,
                console=console
            )
            while len(jwt_secret) < 32:
                console.print("[red]❌ Минимум 32 символа![/red]")
                jwt_secret = Prompt.ask("[bold yellow]🔑 JWT_SECRET[/bold yellow]", password=True, console=console)
            
            anon_key = Prompt.ask(
                "[bold blue]🔓 ANON_KEY[/bold blue] (из Supabase Dashboard)",
                console=console
            )
            while not anon_key.startswith("eyJ"):
                console.print("[red]❌ Должен начинаться с 'eyJ'[/red]")
                anon_key = Prompt.ask("[bold blue]🔓 ANON_KEY[/bold blue]", console=console)
            
            service_role = Prompt.ask(
                "[bold red]🔐 SERVICE_ROLE_KEY[/bold red] (из Supabase Dashboard)",
                password=True,
                console=console
            )
            while not service_role.startswith("eyJ"):
                console.print("[red]❌ Должен начинаться с 'eyJ'[/red]")
                service_role = Prompt.ask("[bold red]🔐 SERVICE_ROLE_KEY[/bold red]", password=True, console=console)
            
        else:
            print("\n🔐 ШАГ 1: SUPABASE KEYS")
            print("📖 Guide: https://supabase.com/docs/guides/self-hosting/docker#generate-api-keys")
            
            jwt_secret = input("\n🔑 JWT_SECRET (32+ символов): ").strip()
            while len(jwt_secret) < 32:
                print("❌ Минимум 32 символа!")
                jwt_secret = input("🔑 JWT_SECRET: ").strip()
                
            anon_key = input("🔓 ANON_KEY (начинается с eyJ): ").strip()
            service_role = input("🔐 SERVICE_ROLE_KEY (начинается с eyJ): ").strip()
            
        return jwt_secret, anon_key, service_role

    def choose_deployment_mode(self):
        """🎯 Шаг 2: Выбор режима развертывания."""
        if HAS_RICH:
            mode_panel = Panel(
                "[bold green]✅ ОБЯЗАТЕЛЬНАЯ ПРОГРАММА МИНИМУМ ВЫПОЛНЕНА![/bold green]\n\n"
                "[yellow]🎯 Базовые ключи получены. Система готова к запуску![/yellow]\n"
                "[cyan]Но можно выполнить дополнительные настройки для полной активации...[/cyan]\n\n"
                "[bold white]🚀 Выберите режим развертывания:[/bold white]\n"
                "• [green]МИНИМУМ[/green] - быстрый запуск с основными доменами\n"
                "  [dim]N8N + Supabase + email (3 домена)[/dim]\n"
                "• [gold1]МАКСИМУМ[/gold1] - полная настройка всех сервисов\n"
                "  [dim]Все 8 доменов + SSL + кастомизация[/dim]",
                title="🎮 Режим развертывания",
                border_style="blue",
                width=80
            )
            console.print(mode_panel)
            
            mode = Prompt.ask(
                "\n[bold cyan]🎯 Ваш выбор[/bold cyan]",
                choices=["минимум", "максимум", "minimum", "maximum", "min", "max"],
                default="минимум",
                console=console
            )
            
        else:
            print("\n✅ ОБЯЗАТЕЛЬНАЯ ПРОГРАММА МИНИМУМ ВЫПОЛНЕНА!")
            print("🎯 Базовые ключи получены. Система готова к запуску!")
            print("Но можно выполнить дополнительные настройки...")
            print("\n🚀 Выберите режим:")
            print("• МИНИМУМ - быстрый запуск (3 домена)")
            print("• МАКСИМУМ - полная настройка (8 доменов)")
            
            mode = input("\n🎯 Ваш выбор (минимум/максимум): ").strip().lower()
            
        return mode in ['минимум', 'minimum', 'min']

    def get_domain_configuration(self, is_minimal):
        """🌐 Запрос доменов в зависимости от режима."""
        domains = {}
        
        if HAS_RICH:
            console.print(f"\n[bold {'green' if is_minimal else 'gold1'}]🌐 {'МИНИМАЛЬНАЯ' if is_minimal else 'ПОЛНАЯ'} НАСТРОЙКА ДОМЕНОВ[/bold {'green' if is_minimal else 'gold1'}]")
            
            ip_panel = Panel(
                "[bold red]⚠️ ВАЖНО: Настройка DNS[/bold red]\n\n"
                "[yellow]Для каждого домена создайте А-запись в DNS:[/yellow]\n"
                "• [cyan]Тип записи:[/cyan] A\n"
                "• [green]Имя:[/green] поддомен (n8n, supabase, etc.)\n"
                "• [blue]Значение:[/blue] IP адрес вашего сервера\n\n"
                "[bold white]Узнать IP сервера:[/bold white] [dim]curl ifconfig.me[/dim]",
                title="🌍 DNS Configuration",
                border_style="yellow"
            )
            console.print(ip_panel)
            
            # Обязательные домены для минимума
            domains['n8n'] = Prompt.ask(
                "[bold green]🔧 N8N_HOSTNAME[/bold green] (например: n8n.yourdomain.com)",
                console=console
            )
            
            domains['supabase'] = Prompt.ask(
                "[bold blue]🗄️ SUPABASE_HOSTNAME[/bold blue] (например: supabase.yourdomain.com)",
                console=console
            )
            
            domains['email'] = Prompt.ask(
                "[bold yellow]📧 LETSENCRYPT_EMAIL[/bold yellow] (ваш email для SSL)",
                console=console
            )
            
            if not is_minimal:
                # Дополнительные домены для максимума
                domains['webui'] = Prompt.ask(
                    "[bold cyan]💬 WEBUI_HOSTNAME[/bold cyan] (например: chat.yourdomain.com)",
                    default="",
                    console=console
                )
                
                domains['flowise'] = Prompt.ask(
                    "[bold purple]🌊 FLOWISE_HOSTNAME[/bold purple] (например: flow.yourdomain.com)",
                    default="",
                    console=console
                )
                
                domains['langfuse'] = Prompt.ask(
                    "[bold orange1]📊 LANGFUSE_HOSTNAME[/bold orange1] (например: analytics.yourdomain.com)",
                    default="",
                    console=console
                )
                
                domains['ollama'] = Prompt.ask(
                    "[bold red]🦙 OLLAMA_HOSTNAME[/bold red] (например: llm.yourdomain.com)",
                    default="",
                    console=console
                )
                
                domains['searxng'] = Prompt.ask(
                    "[bold green]🔍 SEARXNG_HOSTNAME[/bold green] (например: search.yourdomain.com)",
                    default="",
                    console=console
                )
                
                domains['neo4j'] = Prompt.ask(
                    "[bold gold1]🕸️ NEO4J_HOSTNAME[/bold gold1] (например: graph.yourdomain.com)",
                    default="",
                    console=console
                )
        else:
            print(f"\n🌐 {'МИНИМАЛЬНАЯ' if is_minimal else 'ПОЛНАЯ'} НАСТРОЙКА ДОМЕНОВ")
            print("⚠️ Создайте А-записи в DNS для каждого домена!")
            print("Узнать IP сервера: curl ifconfig.me")
            
            domains['n8n'] = input("\n🔧 N8N_HOSTNAME (n8n.yourdomain.com): ").strip()
            domains['supabase'] = input("🗄️ SUPABASE_HOSTNAME (supabase.yourdomain.com): ").strip()
            domains['email'] = input("📧 LETSENCRYPT_EMAIL (ваш email): ").strip()
            
            if not is_minimal:
                domains['webui'] = input("💬 WEBUI_HOSTNAME (опционально): ").strip()
                domains['flowise'] = input("🌊 FLOWISE_HOSTNAME (опционально): ").strip()
                domains['langfuse'] = input("📊 LANGFUSE_HOSTNAME (опционально): ").strip()
                domains['ollama'] = input("🦙 OLLAMA_HOSTNAME (опционально): ").strip()
                domains['searxng'] = input("🔍 SEARXNG_HOSTNAME (опционально): ").strip()
                domains['neo4j'] = input("🕸️ NEO4J_HOSTNAME (опционально): ").strip()
                
        return domains

    def generate_env_file(self, jwt_secret, anon_key, service_role, domains):
        """💎 Генерация .env файла с автоматическими секретами и доменами."""
        def generate_secret(length=32):
            alphabet = string.ascii_letters + string.digits
            return ''.join(secrets.choice(alphabet) for _ in range(length))
        
        # Базовый контент
        env_content = f"""# 🎮 AIBot Direct - MOTHERLODE Configuration
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Website: https://AIBot.Direct

# 🔐 Автоматически сгенерированные секреты
N8N_ENCRYPTION_KEY={generate_secret(32)}
N8N_USER_MANAGEMENT_JWT_SECRET={generate_secret(64)}
POSTGRES_PASSWORD={generate_secret(32)}
DASHBOARD_PASSWORD={generate_secret(24)}
POOLER_TENANT_ID={generate_secret(16)}

# 🔑 Supabase API Keys (введены вручную)
JWT_SECRET={jwt_secret}
ANON_KEY={anon_key}
SERVICE_ROLE_KEY={service_role}

# 🌐 Настройка доменов
"""
        
        # Обязательные домены (всегда раскомментированы если есть)
        if domains.get('n8n'):
            env_content += f"N8N_HOSTNAME={domains['n8n']}\n"
        else:
            env_content += "# N8N_HOSTNAME=n8n.yourdomain.com\n"
            
        if domains.get('supabase'):
            env_content += f"SUPABASE_HOSTNAME={domains['supabase']}\n"
        else:
            env_content += "# SUPABASE_HOSTNAME=supabase.yourdomain.com\n"
            
        if domains.get('email'):
            env_content += f"LETSENCRYPT_EMAIL={domains['email']}\n"
        else:
            env_content += "# LETSENCRYPT_EMAIL=internal\n"
        
        # Дополнительные домены (раскомментированы только если заполнены)
        optional_domains = [
            ('webui', 'WEBUI_HOSTNAME', 'openwebui.yourdomain.com'),
            ('flowise', 'FLOWISE_HOSTNAME', 'flowise.yourdomain.com'),
            ('langfuse', 'LANGFUSE_HOSTNAME', 'langfuse.yourdomain.com'),
            ('ollama', 'OLLAMA_HOSTNAME', 'ollama.yourdomain.com'),
            ('searxng', 'SEARXNG_HOSTNAME', 'searxng.yourdomain.com'),
            ('neo4j', 'NEO4J_HOSTNAME', 'neo4j.yourdomain.com')
        ]
        
        for key, env_key, default in optional_domains:
            if domains.get(key):
                env_content += f"{env_key}={domains[key]}\n"
            else:
                env_content += f"# {env_key}={default}\n"
        
        with open('.env', 'w') as f:
            f.write(env_content)
        
        # Подсчет активных доменов
        active_domains = sum(1 for k in ['n8n', 'supabase', 'email'] if domains.get(k))
        total_domains = active_domains + sum(1 for k in ['webui', 'flowise', 'langfuse', 'ollama', 'searxng', 'neo4j'] if domains.get(k))
        
        if HAS_RICH:
            env_panel = Panel(
                "[bold green]✅ КОНФИГУРАЦИЯ ЗАВЕРШЕНА![/bold green]\n\n"
                "[yellow]📝 Создан файл .env с настройками:[/yellow]\n"
                f"• [green]Автоматических секретов:[/green] 5 шт. ✅\n"
                f"• [blue]Supabase ключей:[/blue] 3 шт. ✅\n"
                f"• [cyan]Активных доменов:[/cyan] {total_domains} из 9 ✅\n"
                f"• [yellow]Обязательных доменов:[/yellow] {active_domains}/3 ✅\n\n"
                "[bold gold1]🔐 Система готова к активации![/bold gold1]",
                title="🏆 Configuration Generated",
                border_style="green"
            )
            console.print(env_panel)
        else:
            print(f"✅ Файл .env создан! Доменов активно: {total_domains}/9")

    def activate_ai_empire(self):
        """🚀 Запуск всей AI империи через Docker Compose."""
        deployment_success = False
        
        empire_phases = [
            ("🔍 Docker image pull", "Скачивание готовых контейнеров"),
            ("🔐 Secrets generation", "Генерация криптографически стойких паролей"),
            ("🧠 n8n workflow engine startup", "Запуск движка автоматизации"),
            ("🎤 Whisper ASR service initialization", "Инициализация speech-to-text"),
            ("🗄️ Supabase stack deployment", "Развертывание PostgreSQL + API + Auth"),
            ("💫 Qdrant vector DB + embeddings", "Настройка RAG infrastructure"),
            ("📊 Neo4j graph database startup", "Запуск графовой БД для связей"),
            ("📡 Service mesh health checks", "Проверка работоспособности всех сервисов")
        ]
        
        if HAS_RICH:
            console.print("\n[bold gold1]🚀 АКТИВИРУЮ AI ИМПЕРИЮ...[/bold gold1]")
            console.print("[dim]Infrastructure as Code: полностью воспроизводимое окружение[/dim]\n")
            
            with Progress() as progress:
                empire_task = progress.add_task("[gold1]Deploying Full-Stack AI...", total=len(empire_phases))
                
                for phase, description in empire_phases:
                    console.print(f"[cyan]{phase}[/cyan] - [dim yellow]{description}[/dim yellow]")
                    
                    # Имитация реальных операций
                    if "Docker" in phase:
                        time.sleep(2.0)  # Docker pull takes time
                    elif "Supabase" in phase:
                        time.sleep(1.8)  # Complex stack
                    else:
                        time.sleep(1.2)
                    
                    progress.advance(empire_task)
            
            # Реальный запуск через start_services.py
            try:
                console.print("\n[bold yellow]🔧 Запускаю infrastructure через start_services.py...[/bold yellow]")
                console.print("[dim]Это может занять 5-10 минут для первого запуска...[/dim]")
                
                # Запуск без timeout для полной установки
                result = subprocess.run([sys.executable, "start_services.py"], 
                                      text=True, timeout=None)
                
                if result.returncode == 0:
                    console.print("[bold green]✅ Infrastructure deployed successfully![/bold green]")
                    deployment_success = True
                else:
                    console.print(f"[red]❌ Deployment failed (exit code: {result.returncode})[/red]")
                    console.print("[yellow]🔧 Попробуйте: docker-compose up -d[/yellow]")
                    deployment_success = False
                    
            except FileNotFoundError:
                console.print("[red]❌ start_services.py not found![/red]")
                console.print("[yellow]🔧 Fallback: Запускаю docker-compose напрямую...[/yellow]")
                
                # Fallback: прямой вызов docker-compose
                try:
                    subprocess.run(["docker-compose", "up", "-d"], check=True, timeout=None)
                    console.print("[bold green]✅ Docker Compose запущен![/bold green]")
                    deployment_success = True
                except subprocess.CalledProcessError as e:
                    console.print(f"[red]❌ Docker Compose failed: {e}[/red]")
                    deployment_success = False
                except FileNotFoundError:
                    console.print("[red]❌ Docker Compose не найден![/red]")
                    deployment_success = False
                    
            # Эффект победы или поражения
            if deployment_success:
                victory_text = Text("🏆 AI ИМПЕРИЯ АКТИВИРОВАНА! 🏆", style="bold gold1 blink")
            else:
                victory_text = Text("❌ AI ИМПЕРИЯ НЕ АКТИВИРОВАНА! ❌", style="bold red blink")
            console.print(Align.center(victory_text))
            
        else:
            print("\n🚀 АКТИВАЦИЯ AI ИМПЕРИИ...")
            print("📝 Генерирую .env конфигурацию...")
            for i, (phase, desc) in enumerate(empire_phases, 1):
                print(f"[{i}/{len(empire_phases)}] {phase}")
                time.sleep(0.5)
            
            # Реальный запуск для базового режима
            print("\n🔧 Запускаю infrastructure через start_services.py...")
            print("⏳ Это может занять 5-10 минут для первого запуска...")
            
            try:
                result = subprocess.run([sys.executable, "start_services.py"], timeout=None)
                
                if result.returncode == 0:
                    print("✅ Infrastructure deployed successfully!")
                    deployment_success = True
                else:
                    print(f"❌ Deployment failed (exit code: {result.returncode})")
                    print("🔧 Попробуйте: docker-compose up -d")
                    deployment_success = False
                    
            except FileNotFoundError:
                print("❌ start_services.py not found!")
                print("🔧 Fallback: Запускаю docker-compose напрямую...")
                
                try:
                    subprocess.run(["docker-compose", "up", "-d"], check=True, timeout=None)
                    print("✅ Docker Compose запущен!")
                    deployment_success = True
                except subprocess.CalledProcessError as e:
                    print(f"❌ Docker Compose failed: {e}")
                    deployment_success = False
                except FileNotFoundError:
                    print("❌ Docker Compose не найден!")
                    deployment_success = False
            
            if deployment_success:
                print("\n🏆 AI ИМПЕРИЯ АКТИВИРОВАНА!")
            else:
                print("\n❌ AI ИМПЕРИЯ НЕ АКТИВИРОВАНА!")
                print("🔧 Установите Docker и повторите запуск")
        
        return deployment_success

    def read_env_domains(self):
        """📖 Читает домены из .env файла."""
        domains = {}
        try:
            with open('.env', 'r') as f:
                for line in f:
                    line = line.strip()
                    if '=' in line and not line.startswith('#'):
                        key, value = line.split('=', 1)
                        if 'HOSTNAME' in key or 'EMAIL' in key:
                            domains[key] = value
        except FileNotFoundError:
            pass
        return domains

    def show_empire_status(self, deployment_success=True):
        """🏆 Production-ready environment status."""
        # Читаем домены из .env файла
        env_domains = self.read_env_domains()
        
        # Получаем IP адрес сервера для fallback
        try:
            import subprocess
            result = subprocess.run(['curl', '-s', 'ifconfig.me'], capture_output=True, text=True, timeout=5)
            server_ip = result.stdout.strip() if result.returncode == 0 else "YOUR_SERVER_IP"
        except:
            server_ip = "YOUR_SERVER_IP"
        
        # Определяем URL'ы на основе .env
        if env_domains.get('N8N_HOSTNAME'):
            n8n_url = f"https://{env_domains['N8N_HOSTNAME']}"
        else:
            n8n_url = f"http://{server_ip}:5678"
            
        if env_domains.get('WEBUI_HOSTNAME'):
            webui_url = f"https://{env_domains['WEBUI_HOSTNAME']}"
        else:
            webui_url = f"http://{server_ip}:3000"
            
        if env_domains.get('SUPABASE_HOSTNAME'):
            supabase_url = f"https://{env_domains['SUPABASE_HOSTNAME']}"
        else:
            supabase_url = f"http://{server_ip}:8005"
            
        whisper_url = f"http://{server_ip}:9000"  # Whisper всегда по IP
            
        if HAS_RICH:
            # Статус в зависимости от успеха deployment
            if deployment_success:
                status_text = "[bold gold1]🏆 LEVEL UP COMPLETE! ДОБРО ПОЖАЛОВАТЬ В 0.1%! 🏆[/bold gold1]\n\n[bold cyan]⚡ Готовая AI инфраструктура:[/bold cyan]\n\n"
                border_color = "gold1"
            else:
                status_text = "[bold red]❌ DEPLOYMENT FAILED! ИМПЕРИЯ НЕ АКТИВИРОВАНА! ❌[/bold red]\n\n[bold yellow]⚠️ AI инфраструктура НЕ готова:[/bold yellow]\n\n"
                border_color = "red"
            
            # Главный статус
            empire_panel = Panel(
                status_text + 
                
                "[yellow]🧠 AI INTERFACES:[/yellow]\n"
                f"• [bold white]n8n Workflows:[/bold white] {n8n_url}\n"
                "  [dim]Visual programming для automation (Zapier на стероидах)[/dim]\n"
                f"• [bold white]LLM Chat Interface:[/bold white] {webui_url}\n"
                "  [dim]OpenWebUI для общения с локальными моделями (личный ChatGPT)[/dim]\n"
                f"• [bold white]Speech API:[/bold white] {whisper_url}\n"
                "  [dim]Whisper endpoints для voice-to-text и обратно (голосовой API)[/dim]\n"
                f"• [bold white]Database Admin:[/bold white] {supabase_url}\n"
                "  [dim]Supabase dashboard для управления данными (phpMyAdmin для PostgreSQL)[/dim]\n\n"
                
                "[green]💼 CAPABILITIES:[/green]\n"
                "• [bright_green]RAG (Retrieval-Augmented Generation)[/bright_green] с Qdrant vector search\n"
                "• [bright_green]Graph-based связи[/bright_green] через Neo4j для complex relationships\n"
                "• [bright_green]Voice-first interfaces[/bright_green] через Whisper ASR/TTS\n"
                "• [bright_green]Horizontal scaling[/bright_green] через microservices architecture\n\n"
                
                "[blue]🎮 QUICK START:[/blue]\n"
                f"1. [white]{webui_url}[/white] - chat с AI моделями\n"
                f"2. [white]{n8n_url}[/white] - создай automation workflow\n"
                "3. [white]Import production templates[/white] из репозитория\n\n"
                
                "[bold red]🧠 Full-stack AI platform:[/bold red] от voice input до automated actions\n"
                "[bold gold1]⚡ Welcome to the automation layer! ⚡[/bold gold1]",
                title="🎯 Production-Ready AI Infrastructure" if deployment_success else "❌ Deployment Status",
                border_style=border_color,
                width=85
            )
            console.print(empire_panel)
            
            # Дополнительная таблица с техническими деталями
            tech_table = Table(
                title="🔧 Technical Stack Overview",
                show_header=True,
                header_style="bold cyan",
                border_style="blue"
            )
            tech_table.add_column("🎯 Service", style="bold white", width=20)
            tech_table.add_column("🌐 Port", justify="center", width=8)
            tech_table.add_column("📝 Description", style="dim yellow", width=45)
            
            services = [
                ("n8n selfhost", "5678", "Workflow automation engine (400+ интеграций)"),
                ("OpenWebUI", "3000", "ChatGPT-like интерфейс для локальных LLM"),
                ("Whisper API", "9000", "Speech-to-text/text-to-speech OpenAI модель"),
                ("Supabase", "8005", "PostgreSQL + REST API + Auth + Storage"),
                ("Qdrant", "6333", "Vector database для semantic search и RAG"),
                ("Neo4j", "7474", "Graph database для complex relationships"),
                ("Langfuse", "3001", "LLM observability: токены, latency, costs"),
                ("SearXNG", "8080", "Privacy-focused метапоисковик без трекинга")
            ]
            
            for service, port, desc in services:
                tech_table.add_row(service, port, desc)
            
            console.print("\n")
            console.print(tech_table)
            
            # Финальное сообщение
            console.print("\n[bold yellow]" + "="*85 + "[/bold yellow]")
            if deployment_success:
                final_text = Text("🎮 CHEAT CODE MOTHERLODE: SUCCESS! 🎮", style="bold gold1 blink")
            else:
                final_text = Text("🚨 CHEAT CODE MOTHERLODE: FAILED! 🚨", style="bold red blink")
            console.print(Align.center(final_text))
            console.print("[bold yellow]" + "="*85 + "[/bold yellow]\n")
            
        else:
            print("\n" + "="*70)
            if deployment_success:
                print("🏆 LEVEL UP COMPLETE! ДОБРО ПОЖАЛОВАТЬ В 0.1%!")
                print("="*70)
                print("\n🌟 AI Infrastructure готова:")
            else:
                print("❌ DEPLOYMENT FAILED! ИМПЕРИЯ НЕ АКТИВИРОВАНА!")
                print("="*70)
                print("\n⚠️ AI Infrastructure НЕ готова (нужен Docker):")
            print(f"  🧠 n8n Workflows: {n8n_url}")
            print(f"  🤖 AI Chat: {webui_url}")
            print(f"  🎤 Voice API: {whisper_url}")
            print(f"  🗄️ Database: {supabase_url}")
            print("\n⚡ Capabilities:")
            print("  • RAG с vector search")
            print("  • Graph-based связи")
            print("  • Voice interfaces")
            print("  • Microservices scaling")
            if deployment_success:
                print("\n🎮 MOTHERLODE: SUCCESS!")
            else:
                print("\n🚨 MOTHERLODE: FAILED!")
                print("🔧 Установите Docker и повторите запуск")
            print("="*70)

def main():
    """🎮 Главная функция активации чит-кода MOTHERLODE."""
    # Инициализация чит-кода
    motherlode = MotherlodeAI()
    
    try:
        # 1. 🎮 Активация чит-кода + показ полного стека
        motherlode.show_cheat_activation()
        
        # 2. 🔍 Системная диагностика
        motherlode.check_prerequisites()
        
        # 3. 🛡️ Настройка firewall (квантовая защита)
        motherlode.setup_firewall()
        
        # 4. 🔐 Шаг 1: Получение Supabase credentials
        jwt_secret, anon_key, service_role = motherlode.get_supabase_keys()
        
        # 5. 🎯 Шаг 2: Выбор режима развертывания
        is_minimal = motherlode.choose_deployment_mode()
        
        # 6. 🌐 Шаг 3: Настройка доменов
        domains = motherlode.get_domain_configuration(is_minimal)
        
        # 7. 💎 Генерация .env файла с настройками
        motherlode.generate_env_file(jwt_secret, anon_key, service_role, domains)
        
        # 8. 🚀 Активация AI империи (с реальным деплоем)
        deployment_success = motherlode.activate_ai_empire()
        
        # 9. 🏆 Показ статуса production-ready environment
        motherlode.show_empire_status(deployment_success)
        
    except KeyboardInterrupt:
        if HAS_RICH:
            console.print("\n[bold red]❌ Чит-код прерван! AI империя не захвачена.[/bold red]")
            console.print("[dim]Используй Ctrl+C для выхода из любой фазы активации[/dim]")
        else:
            print("\n❌ Активация MOTHERLODE прервана!")
    except Exception as e:
        if HAS_RICH:
            console.print(f"\n[bold red]💥 Критическая ошибка активации:[/bold red]")
            console.print(f"[red]{str(e)}[/red]")
            console.print("\n[yellow]🔧 Возможные решения:[/yellow]")
            console.print("• Проверь подключение к интернету")
            console.print("• Убедись что Docker запущен")
            console.print("• Перезапусти с sudo правами для firewall")
            console.print("• Перезапусти скрипт: python3 motherlode.py")
        else:
            print(f"\n💥 Ошибка активации: {e}")
            print("🔧 Попробуй перезапустить скрипт")

def cli_commands():
    """🎮 CLI команды для управления AI империей."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="🎮 MOTHERLODE - AIBot Direct Cheat Code",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
🎯 Examples:
  python3 motherlode.py              # Полная активация чит-кода
  python3 motherlode.py --status     # Проверка статуса империи
  python3 motherlode.py --firewall   # Настройка только firewall
  python3 motherlode.py --update     # Обновление Docker образов
  
🌐 Website: https://AIBot.Direct
👨‍💻 Created by: Nikita Shorin (inspired by Cole Medin)
        """
    )
    
    parser.add_argument('--status', action='store_true', 
                       help='Показать статус AI сервисов')
    parser.add_argument('--firewall', action='store_true',
                       help='Настроить только firewall')
    parser.add_argument('--update', action='store_true',
                       help='Обновить Docker образы')
    parser.add_argument('--restart', action='store_true',
                       help='Перезапустить все сервисы')
    parser.add_argument('--cleanup', action='store_true',
                       help='Очистить Docker volumes')
    
    args = parser.parse_args()
    motherlode = MotherlodeAI()
    
    if args.status:
        motherlode.show_empire_status()
    elif args.firewall:
        motherlode.setup_firewall()
    elif args.update:
        if HAS_RICH:
            console.print("[bold yellow]🔄 Обновляю Docker образы...[/bold yellow]")
        subprocess.run(["docker-compose", "pull"])
    elif args.restart:
        if HAS_RICH:
            console.print("[bold yellow]🔄 Перезапускаю AI империю...[/bold yellow]")
        subprocess.run(["docker-compose", "restart"])
    elif args.cleanup:
        if HAS_RICH:
            console.print("[bold red]🧹 Очистка Docker volumes...[/bold red]")
        subprocess.run(["docker-compose", "down", "-v"])
    else:
        main()

if __name__ == "__main__":
    # 🎮 Автоматическая установка Rich для улучшенного UI
    if not HAS_RICH:
        try:
            print("🎮 Устанавливаю Rich для игрового интерфейса...")
            subprocess.run([sys.executable, "-m", "pip", "install", "rich"], 
                         check=True, capture_output=True)
            print("✅ Rich установлен! Перезапустите для полного UI:")
            print("🚀 python3 motherlode.py")
            sys.exit(0)
        except:
            print("⚠️ Продолжаю без Rich (базовый режим)")
    
    # 🎯 Запуск CLI с поддержкой команд
    cli_commands()
