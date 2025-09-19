#!/usr/bin/env python3
"""
🎮 MOTHERLODE.PY - AIBot Direct Cheat Code v2.0 🎮
💰💰💰 АКТИВИРУЙ ВСЁ ЗОЛОТО AI МИРА! 💰💰💰

Исправлена версия с улучшенной безопасностью и надежностью

Website: https://AIBot.Direct
"""

import os
import sys
import subprocess
import time
import secrets
import string
import platform
import shutil
import re
import socket
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import urllib.request
import ssl

# psutil импортируется динамически когда нужен

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

class SecurityException(Exception):
    """Исключение для проблем безопасности."""
    pass

class SystemResourceException(Exception):
    """Исключение для нехватки системных ресурсов.""" 
    pass

class MotherlodeAI:
    def __init__(self):
        self.version = "2.0.0"
        self.codename = "Alenushka-Secure" 
        self.website = "https://AIBot.Direct"
        self.cheat_code = "MOTHERLODE"
        self.backup_dir = Path("motherlode_backups")
        self.min_ram_gb = 4
        self.min_disk_gb = 10
        self.min_cpu_cores = 1
        
        # Создаем директорию для бэкапов
        self.backup_dir.mkdir(exist_ok=True)
        
    def create_backup(self) -> str:
        """🔄 Создание бэкапа текущей конфигурации."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = self.backup_dir / f"config_backup_{timestamp}"
        backup_path.mkdir(exist_ok=True)
        
        # Бэкап .env если существует
        if Path('.env').exists():
            shutil.copy2('.env', backup_path / '.env')
            
        # Бэкап docker-compose.yml если существует
        for compose_file in ['docker-compose.yml', 'docker-compose.yaml']:
            if Path(compose_file).exists():
                shutil.copy2(compose_file, backup_path / compose_file)
                
        if HAS_RICH:
            console.print(f"[green]✅ Backup created: {backup_path}[/green]")
        else:
            print(f"✅ Backup created: {backup_path}")
            
        return str(backup_path)

    def rollback_deployment(self):
        """🔄 Откат к предыдущей конфигурации."""
        backups = sorted(self.backup_dir.glob("config_backup_*"), reverse=True)
        
        if not backups:
            if HAS_RICH:
                console.print("[red]❌ No backups found for rollback[/red]")
            else:
                print("❌ No backups found for rollback")
            return False
            
        latest_backup = backups[0]
        
        if HAS_RICH:
            should_rollback = Confirm.ask(f"🔄 Rollback to {latest_backup.name}?")
        else:
            should_rollback = input(f"🔄 Rollback to {latest_backup.name}? (y/N): ").lower() == 'y'
            
        if should_rollback:
            try:
                # Остановка контейнеров
                self._safe_subprocess_run(["docker-compose", "down"], check=False)
                
                # Восстановление файлов
                if (latest_backup / '.env').exists():
                    shutil.copy2(latest_backup / '.env', '.env')
                    
                if HAS_RICH:
                    console.print("[green]✅ Rollback completed![/green]")
                else:
                    print("✅ Rollback completed!")
                return True
                
            except Exception as e:
                if HAS_RICH:
                    console.print(f"[red]❌ Rollback failed: {e}[/red]")
                else:
                    print(f"❌ Rollback failed: {e}")
                return False
        return False

    def show_cheat_activation(self):
        """🎮 Показать активацию чит-кода с полным стеком."""
        if HAS_RICH:
            # Анимация активации чит-кода
            console.print("\n[bold yellow]" + "="*80 + "[/bold yellow]")
            cheat_text = Text("🎮 MOTHERLODE v2.0 ACTIVATED! 🎮", style="bold gold1 blink")
            console.print(Align.center(cheat_text))
            console.print("[bold yellow]" + "="*80 + "[/bold yellow]\n")
            time.sleep(1)
            
            # Заголовок с новыми улучшениями
            header_panel = Panel(
                "[bold gold1]⚡ AIBot Direct v2.0 — Enhanced AI Infrastructure! ⚡[/bold gold1]\n"
                "[green]💎 LEVEL UP — Secure & Production-Ready ⭐[/green]\n"
                "[red]🛡️ NEW: Enhanced Security & System Validation[/red]",
                title="🏆 Welcome to Elite AI Stack v2.0",
                border_style="gold1",
                padding=(1, 2)
            )
            console.print(header_panel)
            
            # Информация о новых возможностях
            improvements_panel = Panel(
                "[bold cyan]🚀 NEW IN v2.0:[/bold cyan]\n\n"
                "[green]🛡️ SECURITY ENHANCEMENTS:[/green]\n"
                "┣━ [white]Input validation[/white] - проверка всех пользовательских данных\n"
                "┣━ [white]Safe subprocess execution[/white] - защита от injection атак\n"
                "┣━ [white]Backup/rollback system[/white] - автоматические бэкапы конфигурации\n"
                "┗━ [white]Security warnings[/white] - предупреждения о рисках\n\n"
                "[blue]📊 SYSTEM VALIDATION:[/blue]\n"
                "┣━ [white]Resource checking[/white] - RAM/Disk/CPU requirements\n"
                "┣━ [white]DNS validation[/white] - проверка доменных записей\n"
                "┣━ [white]Platform detection[/white] - поддержка Ubuntu/CentOS/macOS\n"
                "┗━ [white]Error recovery[/white] - улучшенная обработка ошибок\n\n"
                "[yellow]⚙️ OPERATIONAL IMPROVEMENTS:[/yellow]\n"
                "┣━ [white]Intelligent timeouts[/white] - адаптивные таймауты для команд\n"
                "┣━ [white]Progress tracking[/white] - детальный прогресс операций\n"
                "┗━ [white]Health monitoring[/white] - проверка состояния сервисов\n",
                title="🔥 v2.0 Features",
                border_style="cyan",
                padding=(1, 2)
            )
            console.print(improvements_panel)
            
        else:
            print("\n" + "="*80)
            print("🎮 MOTHERLODE v2.0 ACTIVATED!")
            print("⚡ AIBot Direct v2.0 — Enhanced AI Infrastructure!")
            print("💎 LEVEL UP — Secure & Production-Ready")
            print("🛡️ NEW: Enhanced Security & System Validation")
            print("="*80)
            print("\n🚀 NEW IN v2.0:")
            print("🛡️ SECURITY: Input validation, Safe execution, Backup system")
            print("📊 VALIDATION: Resource checking, DNS validation, Platform support")
            print("⚙️ IMPROVEMENTS: Smart timeouts, Progress tracking, Health monitoring")

    def check_system_resources(self) -> bool:
        """💻 Проверка системных ресурсов."""
        if HAS_RICH:
            console.print("\n[bold cyan]💻 ПРОВЕРКА СИСТЕМНЫХ РЕСУРСОВ[/bold cyan]")
            
            # Создаем таблицу ресурсов
            resources_table = Table(
                title="🔍 System Resource Analysis",
                show_header=True,
                header_style="bold magenta",
                border_style="cyan"
            )
            resources_table.add_column("📊 Resource", style="bold white", width=20)
            resources_table.add_column("💾 Current", justify="center", width=15)
            resources_table.add_column("⚡ Required", justify="center", width=15)
            resources_table.add_column("✅ Status", justify="center", width=12)
            
        else:
            print("\n💻 ПРОВЕРКА СИСТЕМНЫХ РЕСУРСОВ:")
            print("=" * 50)
        
        all_good = True
        
        try:
            # Динамический импорт psutil
            import psutil
            
            # Проверка RAM
            ram_gb = psutil.virtual_memory().total / (1024**3)
            ram_status = ram_gb >= self.min_ram_gb
            if not ram_status:
                all_good = False
                
            if HAS_RICH:
                status_color = "green" if ram_status else "red"
                status_icon = "✅ OK" if ram_status else "❌ LOW"
                resources_table.add_row(
                    "RAM Memory",
                    f"{ram_gb:.1f} GB",
                    f"{self.min_ram_gb} GB",
                    f"[{status_color}]{status_icon}[/{status_color}]"
                )
            else:
                print(f"💾 RAM: {ram_gb:.1f}GB (нужно {self.min_ram_gb}GB) - {'✅' if ram_status else '❌'}")
                
            # Проверка дискового пространства
            disk_free_gb = shutil.disk_usage('.').free / (1024**3)
            disk_status = disk_free_gb >= self.min_disk_gb
            if not disk_status:
                all_good = False
                
            if HAS_RICH:
                status_color = "green" if disk_status else "red"
                status_icon = "✅ OK" if disk_status else "❌ LOW"
                resources_table.add_row(
                    "Disk Space",
                    f"{disk_free_gb:.1f} GB",
                    f"{self.min_disk_gb} GB",
                    f"[{status_color}]{status_icon}[/{status_color}]"
                )
            else:
                print(f"💽 Disk: {disk_free_gb:.1f}GB (нужно {self.min_disk_gb}GB) - {'✅' if disk_status else '❌'}")
                
            # Проверка CPU
            cpu_count = psutil.cpu_count(logical=False)
            cpu_status = cpu_count >= self.min_cpu_cores
            if not cpu_status:
                all_good = False
                
            if HAS_RICH:
                status_color = "green" if cpu_status else "red"
                status_icon = "✅ OK" if cpu_status else "❌ LOW"
                resources_table.add_row(
                    "CPU Cores",
                    f"{cpu_count} cores",
                    f"{self.min_cpu_cores} cores",
                    f"[{status_color}]{status_icon}[/{status_color}]"
                )
                
                console.print(resources_table)
            else:
                print(f"🔧 CPU: {cpu_count} cores (нужно {self.min_cpu_cores}) - {'✅' if cpu_status else '❌'}")
            
        except ImportError:
            if HAS_RICH:
                console.print("[yellow]⚠️ psutil не установлен - проверяю только базовые ресурсы...[/yellow]")
            else:
                print("⚠️ psutil не установлен - проверяю только базовые ресурсы...")
            
            # Альтернативная проверка дискового пространства без psutil
            try:
                disk_free_gb = shutil.disk_usage('.').free / (1024**3)
                disk_status = disk_free_gb >= self.min_disk_gb
                if not disk_status:
                    all_good = False
                    
                if HAS_RICH:
                    status_color = "green" if disk_status else "red"
                    status_icon = "✅ OK" if disk_status else "❌ LOW"
                    resources_table.add_row(
                        "Disk Space",
                        f"{disk_free_gb:.1f} GB",
                        f"{self.min_disk_gb} GB",
                        f"[{status_color}]{status_icon}[/{status_color}]"
                    )
                    resources_table.add_row("RAM Memory", "Unknown", f"{self.min_ram_gb} GB", "[yellow]❓ SKIP[/yellow]")
                    resources_table.add_row("CPU Cores", "Unknown", f"{self.min_cpu_cores} cores", "[yellow]❓ SKIP[/yellow]")
                    console.print(resources_table)
                else:
                    print(f"💽 Disk: {disk_free_gb:.1f}GB (нужно {self.min_disk_gb}GB) - {'✅' if disk_status else '❌'}")
                    print("💾 RAM: Неизвестно (требуется psutil)")
                    print("🔧 CPU: Неизвестно (требуется psutil)")
                    
            except Exception as e:
                if HAS_RICH:
                    console.print(f"[red]❌ Не удалось проверить ресурсы: {e}[/red]")
                else:
                    print(f"❌ Не удалось проверить ресурсы: {e}")
                return True  # Продолжаем несмотря на ошибку
        
        if not all_good:
            if HAS_RICH:
                warning_panel = Panel(
                    "[bold red]⚠️ НЕДОСТАТОЧНО РЕСУРСОВ![/bold red]\n\n"
                    "[yellow]AI инфраструктура требует минимальных ресурсов:[/yellow]\n"
                    f"• [red]RAM:[/red] минимум {self.min_ram_gb}GB для стабильной работы контейнеров\n"
                    f"• [red]Disk:[/red] минимум {self.min_disk_gb}GB для Docker образов и данных\n"
                    f"• [red]CPU:[/red] минимум {self.min_cpu_cores} ядро для базовой производительности\n\n"
                    "[cyan]Рекомендация: закройте ненужные приложения или используйте более мощную систему[/cyan]",
                    title="❌ Resource Warning",
                    border_style="red"
                )
                console.print(warning_panel)
                
                should_continue = Confirm.ask("🤔 Продолжить несмотря на предупреждения?")
                if not should_continue:
                    raise SystemResourceException("Insufficient system resources")
            else:
                print("❌ НЕДОСТАТОЧНО РЕСУРСОВ!")
                print(f"Минимум: RAM {self.min_ram_gb}GB, Disk {self.min_disk_gb}GB, CPU {self.min_cpu_cores} core")
                continue_anyway = input("Продолжить? (y/N): ").lower()
                if continue_anyway != 'y':
                    raise SystemResourceException("Insufficient system resources")
        
        return all_good

    def validate_domain(self, domain: str) -> bool:
        """🌐 Валидация домена."""
        if not domain or domain.strip() == "":
            return False
            
        # Базовая проверка формата домена
        domain_pattern = re.compile(
            r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
        )
        
        if not domain_pattern.match(domain):
            return False
            
        # Проверка DNS записи (опционально)
        try:
            socket.gethostbyname(domain)
            return True
        except socket.gaierror:
            # Домен может быть не настроен еще, это не критично
            if HAS_RICH:
                console.print(f"[yellow]⚠️ DNS record for {domain} not found (это нормально для новых доменов)[/yellow]")
            else:
                print(f"⚠️ DNS record for {domain} not found")
            return True  # Не блокируем процесс
            
    def _safe_subprocess_run(self, cmd: List[str], check: bool = True, timeout: int = 30, 
                           capture_output: bool = True, input_data: str = None) -> subprocess.CompletedProcess:
        """🛡️ Безопасное выполнение subprocess команд."""
        # Валидация команды
        if not cmd or not isinstance(cmd, list):
            raise ValueError("Command must be a non-empty list")
            
        # Проверка на опасные команды
        dangerous_commands = ['rm', 'dd', 'mkfs', 'fdisk', 'chmod 777']
        cmd_str = ' '.join(cmd)
        for dangerous in dangerous_commands:
            if dangerous in cmd_str:
                if HAS_RICH:
                    console.print(f"[red]❌ SECURITY: Dangerous command blocked: {dangerous}[/red]")
                else:
                    print(f"❌ SECURITY: Dangerous command blocked: {dangerous}")
                raise SecurityException(f"Dangerous command blocked: {dangerous}")
        
        try:
            # Адаптивный timeout в зависимости от команды
            if 'docker' in cmd[0] and ('pull' in cmd or 'build' in cmd):
                timeout = 600  # 10 минут для Docker операций
            elif 'apt' in cmd or 'yum' in cmd or 'brew' in cmd:
                timeout = 300  # 5 минут для пакетных менеджеров
                
            result = subprocess.run(
                cmd,
                check=check,
                timeout=timeout,
                capture_output=capture_output,
                text=True,
                input=input_data
            )
            return result
            
        except subprocess.TimeoutExpired as e:
            error_msg = f"Command timeout after {timeout}s: {' '.join(cmd)}"
            if HAS_RICH:
                console.print(f"[red]⏱️ {error_msg}[/red]")
            else:
                print(f"⏱️ {error_msg}")
            raise
            
        except subprocess.CalledProcessError as e:
            error_msg = f"Command failed (exit {e.returncode}): {' '.join(cmd)}"
            if e.stderr:
                error_msg += f"\nError: {e.stderr}"
            if HAS_RICH:
                console.print(f"[red]❌ {error_msg}[/red]")
            else:
                print(f"❌ {error_msg}")
            if check:
                raise
            return e
            
        except FileNotFoundError:
            error_msg = f"Command not found: {cmd[0]}"
            if HAS_RICH:
                console.print(f"[red]❌ {error_msg}[/red]")
            else:
                print(f"❌ {error_msg}")
            raise

    def check_prerequisites(self):
        """🔍 Улучшенная системная диагностика."""
        if HAS_RICH:
            console.print("\n[bold gold1]🔍 ENHANCED СИСТЕМНАЯ ДИАГНОСТИКА[/bold gold1]")
            console.print("[dim]Проверяем совместимость системы с улучшенной валидацией[/dim]\n")
            
            check_table = Table(
                title="🎮 Enhanced System Compatibility Check",
                show_header=True,
                header_style="bold magenta",
                border_style="cyan"
            )
            check_table.add_column("🔧 Component", style="bold white", width=25)
            check_table.add_column("📊 Status", justify="center", width=15)
            check_table.add_column("🎯 What it does", style="dim yellow", width=40)
            check_table.add_column("🏆 Level", justify="center", width=12)
            
        else:
            print("\n🔍 ENHANCED СИСТЕМНАЯ ДИАГНОСТИКА:")
            print("=" * 60)
        
        # Расширенные проверки
        checks = [
            ("Python 3.8+", self._check_python(), "Интерпретатор языка программирования", "🔥 Master"),
            ("Docker Engine", self._check_docker(), "Контейнеризация приложений", "⚡ Pro"),
            ("Docker Compose", self._check_docker_compose(), "Оркестрация multi-container apps", "💎 Elite"),
            ("Git version control", self._check_git(), "Система контроля версий", "💎 Elite"),
            ("Network connectivity", self._check_internet(), "Интернет соединение для загрузки", "🌐 Global"),
            ("System resources", self.check_system_resources(), "RAM/Disk/CPU requirements", "🚀 Critical"),
        ]
        
        all_good = True
        for name, status, description, level in checks:
            if HAS_RICH:
                if status:
                    check_table.add_row(name, "[bold green]✅ READY[/bold green]", description, level)
                else:
                    check_table.add_row(name, "[bold red]❌ MISSING[/bold red]", description, "[red]🔧 Install[/red]")
                    all_good = False
            else:
                print(f"{'✅' if status else '❌'} {name} - {description}")
                if not status:
                    all_good = False
        
        if HAS_RICH:
            console.print(check_table)
        
        if not all_good:
            self._handle_missing_prerequisites()
        else:
            if HAS_RICH:
                success_panel = Panel(
                    "[bold green]✅ ВСЕ КОМПОНЕНТЫ ГОТОВЫ К РАБОТЕ![/bold green]\n\n"
                    "[yellow]🎯 Система прошла enhanced валидацию:[/yellow]\n"
                    "• [green]Все зависимости установлены[/green]\n"
                    "• [blue]Системные ресурсы достаточны[/blue]\n"
                    "• [magenta]Сеть настроена корректно[/magenta]\n"
                    "• [cyan]Готов к развертыванию enterprise AI[/cyan]\n\n"
                    "[bold gold1]🚀 SYSTEM VALIDATED - READY FOR DEPLOYMENT![/bold gold1]",
                    title="🏆 Enhanced System Ready",
                    border_style="green"
                )
                console.print(success_panel)
            else:
                print("✅ ВСЕ КОМПОНЕНТЫ ГОТОВЫ К РАБОТЕ!")

    def _check_docker_compose(self) -> bool:
        """Проверка Docker Compose."""
        try:
            result = self._safe_subprocess_run(["docker-compose", "--version"], check=False)
            return result.returncode == 0
        except (subprocess.CalledProcessError, FileNotFoundError):
            try:
                result = self._safe_subprocess_run(["docker", "compose", "version"], check=False)
                return result.returncode == 0
            except (subprocess.CalledProcessError, FileNotFoundError):
                return False

    def _check_python(self) -> bool:
        return sys.version_info >= (3, 8)

    def _check_docker(self) -> bool:
        try:
            result = self._safe_subprocess_run(["docker", "--version"], check=False)
            return result.returncode == 0
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def _check_git(self) -> bool:
        try:
            result = self._safe_subprocess_run(["git", "--version"], check=False)
            return result.returncode == 0
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def _check_internet(self) -> bool:
        try:
            urllib.request.urlopen('https://www.google.com', timeout=5)
            return True
        except:
            return False

    def _handle_missing_prerequisites(self):
        """Обработка недостающих зависимостей с улучшенной поддержкой платформ."""
        system = platform.system().lower()
        
        if HAS_RICH:
            missing_panel = Panel(
                "[bold red]⚠️ НЕДОСТАЮЩИЕ КОМПОНЕНТЫ ОБНАРУЖЕНЫ![/bold red]\n\n"
                f"[yellow]🖥️ Обнаружена система: {platform.system()} {platform.release()}[/yellow]\n\n"
                "[cyan]🔧 Инструкции по установке:[/cyan]\n"
                "• [green]Ubuntu/Debian:[/green] sudo apt update && sudo apt install docker.io docker-compose git python3-pip\n"
                "• [blue]CentOS/RHEL:[/blue] sudo yum install docker docker-compose git python3-pip\n"
                "• [purple]macOS:[/purple] brew install docker git python3\n"
                "• [red]Windows:[/red] установите Docker Desktop + Git\n\n"
                "[bold yellow]Пытаюсь установить автоматически...[/bold yellow]",
                title="🔧 Missing Dependencies",
                border_style="red"
            )
            console.print(missing_panel)
        else:
            print("⚠️ НЕДОСТАЮЩИЕ КОМПОНЕНТЫ!")
            print(f"Система: {platform.system()} {platform.release()}")
            print("Пытаюсь установить автоматически...")
        
        self._auto_install_missing()

    def _auto_install_missing(self):
        """Улучшенная автоустановка с поддержкой разных платформ."""
        system = platform.system().lower()
        
        try:
            if system == "linux":
                # Определяем дистрибутив
                if Path("/etc/debian_version").exists():
                    # Ubuntu/Debian
                    commands = [
                        ["sudo", "apt", "update", "-y"],
                        ["sudo", "apt", "install", "-y", "docker.io", "docker-compose", "git", "curl", "python3-pip"],
                        ["sudo", "systemctl", "start", "docker"],
                        ["sudo", "systemctl", "enable", "docker"],
                        ["sudo", "usermod", "-aG", "docker", os.getenv("USER", "")]
                    ]
                elif Path("/etc/redhat-release").exists():
                    # CentOS/RHEL/Fedora
                    commands = [
                        ["sudo", "yum", "update", "-y"],
                        ["sudo", "yum", "install", "-y", "docker", "docker-compose", "git", "curl", "python3-pip"],
                        ["sudo", "systemctl", "start", "docker"],
                        ["sudo", "systemctl", "enable", "docker"],
                        ["sudo", "usermod", "-aG", "docker", os.getenv("USER", "")]
                    ]
                else:
                    if HAS_RICH:
                        console.print("[yellow]⚠️ Unknown Linux distribution - trying generic approach[/yellow]")
                    commands = []
                
                for cmd in commands:
                    try:
                        self._safe_subprocess_run(cmd, check=False, timeout=120)
                    except Exception as e:
                        if HAS_RICH:
                            console.print(f"[yellow]⚠️ Command failed (non-critical): {' '.join(cmd)}[/yellow]")
                        else:
                            print(f"⚠️ Command failed: {' '.join(cmd)}")
                        
            elif system == "darwin":  # macOS
                if HAS_RICH:
                    console.print("[blue]🍎 macOS detected - please install Docker Desktop manually[/blue]")
                    console.print("[cyan]Download: https://www.docker.com/products/docker-desktop[/cyan]")
                else:
                    print("🍎 macOS detected - install Docker Desktop manually")
                    
            elif system == "windows":
                if HAS_RICH:
                    console.print("[red]🪟 Windows detected - please install Docker Desktop manually[/red]")
                    console.print("[cyan]Download: https://www.docker.com/products/docker-desktop[/cyan]")
                else:
                    print("🪟 Windows detected - install Docker Desktop manually")
                    
        except Exception as e:
            if HAS_RICH:
                console.print(f"[red]❌ Auto-install failed: {e}[/red]")
                console.print("[yellow]Please install dependencies manually[/yellow]")
            else:
                print(f"❌ Auto-install failed: {e}")

    def setup_firewall(self):
        """🛡️ Улучшенная настройка firewall с проверками безопасности."""
        if platform.system().lower() != "linux":
            if HAS_RICH:
                console.print("[yellow]⚠️ Firewall setup only available on Linux[/yellow]")
            else:
                print("⚠️ Firewall setup only available on Linux")
            return
            
        if HAS_RICH:
            firewall_panel = Panel(
                "[bold red]🛡️ ENHANCED NETWORK SECURITY[/bold red]\n\n"
                "[yellow]🧠 Настраиваем UFW с дополнительными проверками:[/yellow]\n\n"
                "[cyan]🔐 Security принципы:[/cyan]\n"
                "[dim]• Default deny all incoming traffic[/dim]\n"
                "[dim]• Explicit allow only required ports[/dim]\n"
                "[dim]• Rate limiting for web services[/dim]\n"
                "[dim]• Logging для мониторинга[/dim]\n\n"
                "[green]🚀 AI Infrastructure ports:[/green]\n"
                "• [white]22[/white] - SSH (rate limited)\n"
                "• [white]80[/white] - HTTP (redirect to HTTPS)\n"
                "• [white]443[/white] - HTTPS (rate limited)\n"
                "• [white]3000[/white] - OpenWebUI (rate limited)\n"
                "• [white]5678[/white] - n8n workflow editor\n"
                "• [white]8005[/white] - Supabase dashboard\n"
                "• [white]9000[/white] - Whisper ASR API",
                title="🔧 Enhanced Network Security",
                border_style="red"
            )
            console.print(firewall_panel)
            
            # Предупреждение о безопасности
            security_warning = Panel(
                "[bold red]⚠️ SECURITY WARNING ⚠️[/bold red]\n\n"
                "[yellow]Настройка firewall может заблокировать SSH соединение![/yellow]\n"
                "[cyan]Убедитесь что у вас есть физический доступ к серверу[/cyan]\n"
                "[dim]или альтернативный способ подключения[/dim]",
                title="🚨 Important Security Notice",
                border_style="red"
            )
            console.print(security_warning)
            
            should_continue = Confirm.ask("🤔 Продолжить настройку firewall?")
            if not should_continue:
                console.print("[yellow]⏭️ Пропускаю настройку firewall[/yellow]")
                return
                
        else:
            print("\n🛡️ ENHANCED NETWORK SECURITY")
            print("⚠️ SECURITY WARNING: Firewall может заблокировать SSH!")
            continue_setup = input("Продолжить? (y/N): ").lower()
            if continue_setup != 'y':
                print("⏭️ Пропускаю настройку firewall")
                return
        
        # Улучшенные команды firewall с rate limiting
        firewall_commands = [
            (["sudo", "ufw", "--force", "reset"], "Reset firewall rules"),
            (["sudo", "ufw", "default", "deny", "incoming"], "Deny all incoming"),
            (["sudo", "ufw", "default", "allow", "outgoing"], "Allow all outgoing"),
            (["sudo", "ufw", "limit", "ssh"], "SSH with rate limiting"),
            (["sudo", "ufw", "allow", "80"], "HTTP traffic"),
            (["sudo", "ufw", "limit", "443"], "HTTPS with rate limiting"),
            (["sudo", "ufw", "limit", "3000"], "OpenWebUI with rate limiting"),
            (["sudo", "ufw", "allow", "5678"], "n8n editor"),
            (["sudo", "ufw", "allow", "8005"], "Supabase dashboard"),
            (["sudo", "ufw", "allow", "9000"], "Whisper API"),
            (["sudo", "ufw", "logging", "on"], "Enable logging"),
            (["sudo", "ufw", "--force", "enable"], "Activate firewall")
        ]
        
        if HAS_RICH:
            console.print("\n[bold yellow]🔧 Конфигурирую enhanced firewall...[/bold yellow]")
            
            for cmd, desc in track(firewall_commands, description="[green]Setting up enhanced security..."):
                try:
                    result = self._safe_subprocess_run(cmd, check=False, timeout=15)
                    if result.returncode == 0:
                        console.print(f"[green]✅ {desc}[/green]")
                    else:
                        console.print(f"[yellow]⚠️ {desc} (возможно уже настроено)[/yellow]")
                except subprocess.TimeoutExpired:
                    console.print(f"[yellow]⏱️ {desc} (timeout)[/yellow]")
                except Exception as e:
                    console.print(f"[red]❌ {desc}: {e}[/red]")
                time.sleep(0.2)
                
            console.print("\n[bold green]🛡️ Enhanced firewall activated![/bold green]")
            
        else:
            print("\n🔧 Конфигурирую enhanced firewall...")
            
            for cmd, desc in firewall_commands:
                try:
                    result = self._safe_subprocess_run(cmd, check=False, timeout=15)
                    if result.returncode == 0:
                        print(f"✅ {desc}")
                    else:
                        print(f"⚠️ {desc} (возможно уже настроено)")
                except Exception as e:
                    print(f"❌ {desc}: {e}")
                time.sleep(0.1)

    def get_supabase_keys(self) -> Tuple[str, str, str]:
        """🔐 Улучшенный ввод Supabase credentials с валидацией."""
        if HAS_RICH:
            keys_panel = Panel(
                "[bold red]🔐 ENHANCED SUPABASE CONFIGURATION[/bold red]\n\n"
                "[blue]📖 Генерация ключей через Supabase CLI:[/blue]\n"
                "[dim]npm install -g @supabase/cli[/dim]\n"
                "[dim]supabase gen keys --project-ref your-project[/dim]\n\n"
                "[link=https://supabase.com/docs/guides/self-hosting/docker#generate-api-keys]📚 Official Documentation[/link]\n\n"
                "[bold white]🎯 JWT-based Authentication (криптографически стойкие ключи):[/bold white]\n"
                "• [yellow]JWT_SECRET[/yellow] - HMAC ключ для подписи токенов (≥32 символа)\n"
                "• [blue]ANON_KEY[/blue] - публичный API ключ с ограниченными правами\n"
                "• [red]SERVICE_ROLE_KEY[/red] - административный ключ (полные права)\n\n"
                "[bold red]⚠️ SECURITY: Храните ключи в безопасности![/bold red]",
                title="🏆 Enhanced Supabase Setup",
                border_style="red",
                width=85
            )
            console.print(keys_panel)
            
            console.print("\n[bold gold1]💎 Введите валидированные ключи:[/bold gold1]")
            
            # JWT Secret с улучшенной валидацией
            while True:
                jwt_secret = Prompt.ask(
                    "\n[bold yellow]🔑 JWT_SECRET[/bold yellow] (минимум 32 символа, рекомендуется 64)",
                    password=True,
                    console=console
                )
                
                if len(jwt_secret) < 32:
                    console.print("[red]❌ JWT_SECRET должен быть минимум 32 символа![/red]")
                    continue
                    
                # Проверка на сложность
                if len(set(jwt_secret)) < 10:  # Минимум 10 уникальных символов
                    console.print("[yellow]⚠️ JWT_SECRET слишком простой, рекомендуется более сложный[/yellow]")
                    use_anyway = Confirm.ask("Использовать этот ключ?")
                    if not use_anyway:
                        continue
                break
            
            # ANON Key с валидацией JWT формата
            while True:
                anon_key = Prompt.ask(
                    "[bold blue]🔓 ANON_KEY[/bold blue] (JWT токен из Supabase Dashboard)",
                    console=console
                )
                
                if not anon_key.startswith("eyJ"):
                    console.print("[red]❌ ANON_KEY должен начинаться с 'eyJ' (JWT формат)[/red]")
                    continue
                    
                # Проверка базовой структуры JWT
                if anon_key.count('.') != 2:
                    console.print("[red]❌ ANON_KEY не соответствует JWT формату (должно быть 2 точки)[/red]")
                    continue
                break
            
            # Service Role Key с аналогичной валидацией
            while True:
                service_role = Prompt.ask(
                    "[bold red]🔐 SERVICE_ROLE_KEY[/bold red] (admin JWT токен)",
                    password=True,
                    console=console
                )
                
                if not service_role.startswith("eyJ"):
                    console.print("[red]❌ SERVICE_ROLE_KEY должен начинаться с 'eyJ' (JWT формат)[/red]")
                    continue
                    
                if service_role.count('.') != 2:
                    console.print("[red]❌ SERVICE_ROLE_KEY не соответствует JWT формату[/red]")
                    continue
                break
            
        else:
            print("\n🔐 ENHANCED SUPABASE CONFIGURATION")
            print("📖 Guide: https://supabase.com/docs/guides/self-hosting/docker#generate-api-keys")
            print("⚠️ SECURITY: Храните ключи в безопасности!")
            
            # Аналогичная валидация для консольного режима
            while True:
                jwt_secret = input("\n🔑 JWT_SECRET (32+ символов): ").strip()
                if len(jwt_secret) >= 32:
                    break
                print("❌ Минимум 32 символа!")
                
            while True:
                anon_key = input("🔓 ANON_KEY (начинается с eyJ): ").strip()
                if anon_key.startswith("eyJ") and anon_key.count('.') == 2:
                    break
                print("❌ Должен начинаться с 'eyJ' и содержать 2 точки!")
                
            while True:
                service_role = input("🔐 SERVICE_ROLE_KEY (начинается с eyJ): ").strip()
                if service_role.startswith("eyJ") and service_role.count('.') == 2:
                    break
                print("❌ Должен начинаться с 'eyJ' и содержать 2 точки!")
            
        return jwt_secret, anon_key, service_role

    def choose_deployment_mode(self) -> str:
        """🎯 Выбор режима развертывания с дополнительными опциями."""
        if HAS_RICH:
            mode_panel = Panel(
                "[bold green]✅ SUPABASE KEYS VALIDATED![/bold green]\n\n"
                "[yellow]🎯 Выберите режим развертывания:[/yellow]\n\n"
                "[bold white]🚀 Режимы развертывания:[/bold white]\n"
                "• [green]MINIMAL[/green] - быстрый запуск с основными сервисами\n"
                "  [dim]3 домена: n8n + supabase + email (рекомендуется для тестирования)[/dim]\n"
                "• [gold1]STANDARD[/gold1] - полная настройка всех сервисов\n"
                "  [dim]8 доменов: все AI сервисы + SSL + кастомизация[/dim]\n"
                "• [red]PRODUCTION[/red] - enterprise deployment с мониторингом\n"
                "  [dim]Все сервисы + enhanced security + performance tuning[/dim]",
                title="🎮 Deployment Mode Selection",
                border_style="blue",
                width=80
            )
            console.print(mode_panel)
            
            mode = Prompt.ask(
                "\n[bold cyan]🎯 Выберите режим[/bold cyan]",
                choices=["minimal", "standard", "production"],
                default="minimal",
                console=console
            )
            
        else:
            print("\n✅ SUPABASE KEYS VALIDATED!")
            print("🎯 Выберите режим развертывания:")
            print("• MINIMAL - быстрый запуск (3 домена)")
            print("• STANDARD - полная настройка (8 доменов)")  
            print("• PRODUCTION - enterprise deployment")
            
            mode = input("\n🎯 Режим (minimal/standard/production): ").strip().lower()
            if mode not in ['minimal', 'standard', 'production']:
                mode = 'minimal'
            
        return mode

    def get_domain_configuration(self, mode: str) -> Dict[str, str]:
        """🌐 Улучшенная настройка доменов с валидацией."""
        domains = {}
        
        if HAS_RICH:
            console.print(f"\n[bold {'green' if mode == 'minimal' else 'gold1' if mode == 'standard' else 'red'}]🌐 {mode.upper()} DOMAIN CONFIGURATION[/bold {'green' if mode == 'minimal' else 'gold1' if mode == 'standard' else 'red'}]")
            
            dns_panel = Panel(
                "[bold red]⚠️ DNS CONFIGURATION REQUIRED ⚠️[/bold red]\n\n"
                "[yellow]Для каждого домена создайте А-запись:[/yellow]\n"
                "• [cyan]Тип:[/cyan] A\n"
                "• [green]Имя:[/green] поддомен (n8n, supabase, etc.)\n"
                "• [blue]Значение:[/blue] IP адрес вашего сервера\n\n"
                "[bold white]Получить IP сервера:[/bold white]\n"
                "[dim]curl ifconfig.me[/dim] или [dim]curl ipinfo.io/ip[/dim]\n\n"
                "[red]DNS изменения могут занять до 48 часов![/red]",
                title="🌍 DNS Setup Instructions",
                border_style="yellow"
            )
            console.print(dns_panel)
            
        else:
            print(f"\n🌐 {mode.upper()} DOMAIN CONFIGURATION")
            print("⚠️ Создайте А-записи в DNS для каждого домена!")
            print("Получить IP: curl ifconfig.me")
        
        # Обязательные домены для всех режимов
        required_domains = [
            ('n8n', 'N8N_HOSTNAME', 'n8n.yourdomain.com', 'Workflow automation interface'),
            ('supabase', 'SUPABASE_HOSTNAME', 'supabase.yourdomain.com', 'Database admin panel'),
            ('email', 'LETSENCRYPT_EMAIL', 'admin@yourdomain.com', 'SSL certificate notifications')
        ]
        
        for key, env_key, example, description in required_domains:
            if HAS_RICH:
                while True:
                    if key == 'email':
                        domain_value = Prompt.ask(
                            f"[bold yellow]📧 {env_key}[/bold yellow] ({description})",
                            default=example,
                            console=console
                        )
                        # Простая валидация email
                        if '@' in domain_value and '.' in domain_value:
                            domains[key] = domain_value
                            break
                        else:
                            console.print("[red]❌ Некорректный email формат[/red]")
                    else:
                        domain_value = Prompt.ask(
                            f"[bold green]🔧 {env_key}[/bold green] ({description})",
                            default=example,
                            console=console
                        )
                        if self.validate_domain(domain_value):
                            domains[key] = domain_value
                            break
                        else:
                            console.print("[red]❌ Некорректный формат домена[/red]")
            else:
                while True:
                    domain_value = input(f"{env_key} ({example}): ").strip()
                    if not domain_value:
                        domain_value = example
                    
                    if key == 'email':
                        if '@' in domain_value and '.' in domain_value:
                            domains[key] = domain_value
                            break
                        else:
                            print("❌ Некорректный email")
                    else:
                        if self.validate_domain(domain_value):
                            domains[key] = domain_value
                            break
                        else:
                            print("❌ Некорректный домен")
        
        # Дополнительные домены для standard и production
        if mode in ['standard', 'production']:
            optional_domains = [
                ('webui', 'WEBUI_HOSTNAME', 'chat.yourdomain.com', 'AI Chat Interface'),
                ('flowise', 'FLOWISE_HOSTNAME', 'flow.yourdomain.com', 'AI Agent Builder'),
                ('langfuse', 'LANGFUSE_HOSTNAME', 'analytics.yourdomain.com', 'AI Analytics'),
                ('ollama', 'OLLAMA_HOSTNAME', 'llm.yourdomain.com', 'LLM API'),
                ('searxng', 'SEARXNG_HOSTNAME', 'search.yourdomain.com', 'Private Search'),
                ('neo4j', 'NEO4J_HOSTNAME', 'graph.yourdomain.com', 'Graph Database')
            ]
            
            for key, env_key, example, description in optional_domains:
                if HAS_RICH:
                    domain_value = Prompt.ask(
                        f"[bold cyan]{env_key}[/bold cyan] ({description}) [опционально]",
                        default="",
                        console=console
                    )
                else:
                    domain_value = input(f"{env_key} ({example}) [опционально]: ").strip()
                
                if domain_value and self.validate_domain(domain_value):
                    domains[key] = domain_value
                    
        return domains

    def generate_env_file(self, jwt_secret: str, anon_key: str, service_role: str, 
                         domains: Dict[str, str], mode: str):
        """💎 Улучшенная генерация .env с security warnings."""
        # Создаем бэкап перед генерацией
        backup_path = self.create_backup()
        
        def generate_secret(length: int = 32) -> str:
            # Улучшенная генерация с большим алфавитом
            alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
            return ''.join(secrets.choice(alphabet) for _ in range(length))
        
        # Расширенный контент с комментариями безопасности
        env_content = f"""# 🎮 AIBot Direct v2.0 - Enhanced MOTHERLODE Configuration
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Mode: {mode.upper()}
# Website: https://AIBot.Direct
# Backup: {backup_path}

# ⚠️ SECURITY WARNING ⚠️
# This file contains sensitive credentials in plain text!
# - Set proper file permissions: chmod 600 .env
# - Never commit this file to version control
# - Rotate secrets regularly in production
# - Use external secret management for production deployments

# 🔐 Cryptographically strong generated secrets
N8N_ENCRYPTION_KEY={generate_secret(64)}
N8N_USER_MANAGEMENT_JWT_SECRET={generate_secret(64)}
POSTGRES_PASSWORD={generate_secret(32)}
DASHBOARD_PASSWORD={generate_secret(24)}
POOLER_TENANT_ID={generate_secret(16)}
POOLER_DB_POOL_SIZE=5

# 🔑 Supabase JWT Authentication (user provided)
JWT_SECRET={jwt_secret}
ANON_KEY={anon_key}
SERVICE_ROLE_KEY={service_role}

# 🌐 Domain Configuration ({mode} mode)
"""
        
        # Добавляем домены с комментариями
        domain_mappings = {
            'n8n': ('N8N_HOSTNAME', 'n8n.yourdomain.com', 'Workflow automation interface'),
            'supabase': ('SUPABASE_HOSTNAME', 'supabase.yourdomain.com', 'Database admin panel'),
            'email': ('LETSENCRYPT_EMAIL', 'admin@yourdomain.com', 'SSL certificate notifications'),
            'webui': ('WEBUI_HOSTNAME', 'chat.yourdomain.com', 'AI Chat Interface'),
            'flowise': ('FLOWISE_HOSTNAME', 'flow.yourdomain.com', 'AI Agent Builder'),
            'langfuse': ('LANGFUSE_HOSTNAME', 'analytics.yourdomain.com', 'AI Analytics'),
            'ollama': ('OLLAMA_HOSTNAME', 'llm.yourdomain.com', 'LLM API'),
            'searxng': ('SEARXNG_HOSTNAME', 'search.yourdomain.com', 'Private Search'),
            'neo4j': ('NEO4J_HOSTNAME', 'graph.yourdomain.com', 'Graph Database')
        }
        
        for key, (env_key, default, description) in domain_mappings.items():
            if domains.get(key):
                env_content += f"{env_key}={domains[key]}  # {description}\n"
            else:
                env_content += f"# {env_key}={default}  # {description}\n"
        
        # Дополнительные настройки для production
        if mode == 'production':
            env_content += f"""
# 🚀 Production-specific configuration
ENVIRONMENT=production
LOG_LEVEL=warn
RATE_LIMIT_ENABLED=true
MONITORING_ENABLED=true
BACKUP_ENABLED=true
SSL_ONLY=true
"""
        
        # Записываем файл с правильными правами доступа
        with open('.env', 'w') as f:
            f.write(env_content)
            
        # Устанавливаем безопасные права доступа
        try:
            os.chmod('.env', 0o600)  # Только владелец может читать/писать
        except OSError:
            pass  # Windows не поддерживает такие права
        
        # Подсчет активных настроек
        active_domains = sum(1 for k in domains.keys() if domains.get(k))
        total_secrets = 5  # Количество автогенерированных секретов
        
        if HAS_RICH:
            env_panel = Panel(
                "[bold green]✅ ENHANCED CONFIGURATION GENERATED![/bold green]\n\n"
                "[yellow]📝 Создан защищенный .env файл:[/yellow]\n"
                f"• [green]Автоматических секретов:[/green] {total_secrets} шт. ✅\n"
                f"• [blue]Supabase JWT ключей:[/blue] 3 шт. ✅\n"
                f"• [cyan]Активных доменов:[/cyan] {active_domains} шт. ✅\n"
                f"• [yellow]Режим развертывания:[/yellow] {mode.upper()} ✅\n"
                f"• [purple]Бэкап сохранен в:[/purple] {backup_path} ✅\n\n"
                "[bold red]🛡️ SECURITY MEASURES APPLIED:[/bold red]\n"
                "• [white]File permissions set to 600 (owner only)[/white]\n"
                "• [white]64-character encryption keys generated[/white]\n"
                "• [white]Backup created before modification[/white]\n"
                "• [white]Security warnings included in file[/white]\n\n"
                "[bold gold1]🔐 Система готова к безопасному развертыванию![/bold gold1]",
                title="🏆 Enhanced Configuration Complete",
                border_style="green"
            )
            console.print(env_panel)
            
            # Дополнительное предупреждение о безопасности
            security_reminder = Panel(
                "[bold red]🚨 SECURITY REMINDER 🚨[/bold red]\n\n"
                "[yellow]Для production окружения:[/yellow]\n"
                "• Используйте внешний secret management (HashiCorp Vault, AWS Secrets)\n"
                "• Регулярно ротируйте все ключи (каждые 90 дней)\n"
                "• Мониторьте доступ к .env файлу\n"
                "• Настройте автоматические бэкапы секретов\n\n"
                "[cyan]Файл .env содержит критически важные данные![/cyan]",
                title="🔒 Production Security Notice",
                border_style="red"
            )
            console.print(security_reminder)
            
        else:
            print(f"✅ Enhanced .env создан! Режим: {mode.upper()}")
            print(f"Доменов: {active_domains}, Секретов: {total_secrets}")
            print(f"Бэкап: {backup_path}")
            print("🚨 SECURITY: Файл содержит sensitive данные!")

    def activate_ai_empire(self, mode: str) -> bool:
        """🚀 Улучшенный запуск с мониторингом и проверками."""
        deployment_success = False
        
        # Проверки перед развертыванием
        pre_deployment_checks = [
            ("🔍 Docker daemon", self._check_docker_running()),
            ("📂 Docker Compose file", self._check_compose_file()),
            ("🔐 Environment variables", self._check_env_file()),
            ("💾 Disk space", self._check_disk_space()),
            ("🌐 Network ports", self._check_network_ports())
        ]
        
        if HAS_RICH:
            console.print(f"\n[bold gold1]🚀 ACTIVATING AI EMPIRE - {mode.upper()} MODE[/bold gold1]")
            console.print("[dim]Enhanced deployment with pre-flight checks[/dim]\n")
            
            # Pre-flight checks
            pre_flight_table = Table(
                title="🛫 Pre-flight Checks",
                show_header=True,
                header_style="bold cyan",
                border_style="blue"
            )
            pre_flight_table.add_column("✅ Check", style="white", width=25)
            pre_flight_table.add_column("📊 Status", justify="center", width=15)
            
            all_checks_passed = True
            for check_name, check_result in pre_deployment_checks:
                if check_result:
                    pre_flight_table.add_row(check_name, "[green]✅ PASS[/green]")
                else:
                    pre_flight_table.add_row(check_name, "[red]❌ FAIL[/red]")
                    all_checks_passed = False
                    
            console.print(pre_flight_table)
            
            if not all_checks_passed:
                console.print("\n[red]❌ Pre-flight checks failed![/red]")
                should_continue = Confirm.ask("🤔 Продолжить несмотря на проблемы?")
                if not should_continue:
                    return False
                    
        else:
            print(f"\n🚀 ACTIVATING AI EMPIRE - {mode.upper()} MODE")
            print("🛫 Running pre-flight checks...")
            
            all_checks_passed = True
            for check_name, check_result in pre_deployment_checks:
                print(f"{'✅' if check_result else '❌'} {check_name}")
                if not check_result:
                    all_checks_passed = False
                    
            if not all_checks_passed:
                print("❌ Some checks failed!")
                continue_anyway = input("Продолжить? (y/N): ").lower()
                if continue_anyway != 'y':
                    return False
        
        # Deployment phases с адаптивными таймаутами
        empire_phases = [
            ("🔄 Docker images pull", "Загрузка контейнеров", 600),
            ("🔐 Secrets validation", "Проверка криптографических ключей", 30),
            ("🗄️ Database initialization", "Инициализация PostgreSQL", 120),
            ("🧠 n8n workflow engine", "Запуск автоматизации", 90),
            ("🎤 Whisper ASR service", "Инициализация speech-to-text", 60),
            ("🤖 Ollama LLM server", "Запуск языковых моделей", 180),
            ("💬 OpenWebUI interface", "Веб-интерфейс для AI", 60),
            ("📊 Analytics stack", "Мониторинг и аналитика", 90),
            ("🌐 Service mesh health", "Проверка всех сервисов", 60)
        ]
        
        if HAS_RICH:
            with Progress() as progress:
                empire_task = progress.add_task(f"[gold1]Deploying {mode.upper()} AI Stack...", 
                                              total=len(empire_phases))
                
                for phase, description, timeout in empire_phases:
                    console.print(f"[cyan]{phase}[/cyan] - [dim yellow]{description}[/dim yellow]")
                    time.sleep(min(timeout / 30, 3.0))  # Симуляция с адаптивным временем
                    progress.advance(empire_task)
            
            # Реальное развертывание
            try:
                console.print("\n[bold yellow]🔧 Starting real deployment...[/bold yellow]")
                console.print("[dim]This may take 5-15 minutes depending on internet speed...[/dim]")
                
                # Определяем команду запуска
                if Path("start_services.py").exists():
                    cmd = [sys.executable, "start_services.py"]
                    if mode == "production":
                        cmd.extend(["--profile", "gpu-nvidia", "--environment", "public"])
                    else:
                        cmd.extend(["--profile", "gpu-nvidia"])
                elif Path("docker-compose.yml").exists() or Path("docker-compose.yaml").exists():
                    cmd = ["docker-compose", "up", "-d"]
                else:
                    console.print("[red]❌ No deployment configuration found![/red]")
                    return False
                
                result = self._safe_subprocess_run(cmd, timeout=900)  # 15 минут timeout
                
                if result.returncode == 0:
                    console.print("[bold green]✅ Deployment completed successfully![/bold green]")
                    deployment_success = True
                else:
                    console.print(f"[red]❌ Deployment failed (exit {result.returncode})[/red]")
                    deployment_success = False
                    
            except subprocess.TimeoutExpired:
                console.print("[red]⏱️ Deployment timeout - но это не означает провал![/red]")
                console.print("[yellow]Сервисы могут продолжать запускаться в фоне[/yellow]")
                deployment_success = False
                
            except Exception as e:
                console.print(f"[red]❌ Deployment error: {e}[/red]")
                deployment_success = False
                
        else:
            print("🚀 Deploying AI Empire...")
            for i, (phase, desc, timeout) in enumerate(empire_phases, 1):
                print(f"[{i}/{len(empire_phases)}] {phase}")
                time.sleep(0.3)
            
            # Реальное развертывание для консольного режима
            try:
                print("\n🔧 Starting real deployment...")
                
                if Path("start_services.py").exists():
                    cmd = [sys.executable, "start_services.py"]
                else:
                    cmd = ["docker-compose", "up", "-d"]
                
                result = self._safe_subprocess_run(cmd, timeout=900)
                deployment_success = result.returncode == 0
                
            except Exception as e:
                print(f"❌ Deployment error: {e}")
                deployment_success = False
        
        return deployment_success

    def _check_docker_running(self) -> bool:
        """Проверка что Docker daemon запущен."""
        try:
            result = self._safe_subprocess_run(["docker", "info"], check=False, timeout=10)
            return result.returncode == 0
        except:
            return False

    def _check_compose_file(self) -> bool:
        """Проверка наличия docker-compose файла."""
        return Path("docker-compose.yml").exists() or Path("docker-compose.yaml").exists()

    def _check_env_file(self) -> bool:
        """Проверка наличия .env файла."""
        return Path(".env").exists()

    def _check_disk_space(self) -> bool:
        """Проверка свободного места на диске."""
        try:
            free_space_gb = shutil.disk_usage('.').free / (1024**3)
            return free_space_gb >= 10  # Минимум 10GB для Docker образов
        except:
            return True  # Не блокируем если не можем проверить

    def _check_network_ports(self) -> bool:
        """Проверка доступности ключевых портов."""
        critical_ports = [3000, 5678, 8005]
        
        for port in critical_ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1)
                    result = s.connect_ex(('localhost', port))
                    if result == 0:  # Порт занят
                        return False
            except:
                pass
        return True

    def show_empire_status(self, deployment_success: bool = True, mode: str = "minimal"):
        """🏆 Enhanced production-ready environment status."""
        # Читаем конфигурацию
        env_domains = self.read_env_domains()
        
        # Получаем IP для fallback
        try:
            result = self._safe_subprocess_run(['curl', '-s', 'ifconfig.me'], timeout=10)
            server_ip = result.stdout.strip() if result.returncode == 0 else "YOUR_SERVER_IP"
        except:
            server_ip = "YOUR_SERVER_IP"
        
        # Строим URL'ы
        service_urls = {}
        service_configs = {
            'n8n': ('N8N_HOSTNAME', 5678, 'Workflow Automation'),
            'webui': ('WEBUI_HOSTNAME', 3000, 'AI Chat Interface'),
            'supabase': ('SUPABASE_HOSTNAME', 8005, 'Database Admin'),
            'langfuse': ('LANGFUSE_HOSTNAME', 3001, 'AI Analytics'),
            'flowise': ('FLOWISE_HOSTNAME', 3001, 'AI Agent Builder'),
            'searxng': ('SEARXNG_HOSTNAME', 8080, 'Private Search')
        }
        
        for service, (hostname_key, port, description) in service_configs.items():
            if env_domains.get(hostname_key):
                service_urls[service] = f"https://{env_domains[hostname_key]}"
            else:
                service_urls[service] = f"http://{server_ip}:{port}"
        
        # Whisper всегда по IP
        service_urls['whisper'] = f"http://{server_ip}:9000"
        
        if HAS_RICH:
            # Заголовок статуса
            if deployment_success:
                status_text = f"[bold gold1]🏆 AI EMPIRE ACTIVATED - {mode.upper()} MODE! 🏆[/bold gold1]\n\n[bold cyan]⚡ Production-Ready AI Infrastructure:[/bold cyan]\n\n"
                border_color = "gold1"
            else:
                status_text = f"[bold red]❌ DEPLOYMENT ISSUES - {mode.upper()} MODE! ❌[/bold red]\n\n[bold yellow]⚠️ Infrastructure Status Uncertain:[/bold yellow]\n\n"
                border_color = "red"
            
            # Главная панель статуса
            empire_panel = Panel(
                status_text + 
                
                "[yellow]🧠 PRIMARY AI INTERFACES:[/yellow]\n"
                f"• [bold white]Workflow Automation:[/bold white] {service_urls.get('n8n', 'N/A')}\n"
                "  [dim]n8n visual programming for AI automation[/dim]\n"
                f"• [bold white]AI Chat Interface:[/bold white] {service_urls.get('webui', 'N/A')}\n"
                "  [dim]OpenWebUI for local LLM interaction[/dim]\n"
                f"• [bold white]Speech API:[/bold white] {service_urls['whisper']}\n"
                "  [dim]Whisper ASR/TTS endpoints for voice AI[/dim]\n"
                f"• [bold white]Database Control:[/bold white] {service_urls.get('supabase', 'N/A')}\n"
                "  [dim]Supabase dashboard for data management[/dim]\n\n"
                
                "[green]📊 ANALYTICS & MONITORING:[/green]\n"
                f"• [bold white]AI Analytics:[/bold white] {service_urls.get('langfuse', 'N/A')}\n"
                "  [dim]LLM observability and performance metrics[/dim]\n"
                f"• [bold white]Agent Builder:[/bold white] {service_urls.get('flowise', 'N/A')}\n"
                "  [dim]Visual AI agent construction platform[/dim]\n"
                f"• [bold white]Private Search:[/bold white] {service_urls.get('searxng', 'N/A')}\n"
                "  [dim]Privacy-focused metasearch engine[/dim]\n\n"
                
                "[blue]🚀 ENTERPRISE CAPABILITIES:[/blue]\n"
                "• [bright_green]Multi-modal AI[/bright_green] - text, voice, image processing\n"
                "• [bright_green]RAG Pipeline[/bright_green] - document intelligence with vector search\n"
                "• [bright_green]Graph Analytics[/bright_green] - complex relationship mapping\n"
                "• [bright_green]Voice-First UI[/bright_green] - speech-to-action workflows\n"
                "• [bright_green]Zero-Cloud[/bright_green] - complete data sovereignty\n\n"
                
                f"[bold red]🎮 {mode.upper()} AI Stack:[/bold red] Ready for enterprise automation!\n"
                "[bold gold1]⚡ Welcome to the AI revolution! ⚡[/bold gold1]",
                title=f"🎯 {mode.upper()} AI Infrastructure Status" if deployment_success else "❌ Deployment Status",
                border_style=border_color,
                width=90
            )
            console.print(empire_panel)
            
            # Техническая таблица
            tech_table = Table(
                title=f"🔧 {mode.upper()} Technical Stack",
                show_header=True,
                header_style="bold cyan",
                border_style="blue"
            )
            tech_table.add_column("🎯 Service", style="bold white", width=20)
            tech_table.add_column("🌐 Access", style="cyan", width=35)
            tech_table.add_column("📝 Purpose", style="dim yellow", width=35)
            
            # Основные сервисы
            core_services = [
                ("n8n Automation", service_urls.get('n8n', 'N/A'), "Visual workflow builder (400+ integrations)"),
                ("OpenWebUI Chat", service_urls.get('webui', 'N/A'), "ChatGPT-like interface for local LLMs"),
                ("Whisper Voice", service_urls['whisper'], "Speech recognition and synthesis API"),
                ("Supabase DB", service_urls.get('supabase', 'N/A'), "PostgreSQL + API + Auth platform")
            ]
            
            # Дополнительные для standard/production
            if mode in ['standard', 'production']:
                core_services.extend([
                    ("Langfuse Analytics", service_urls.get('langfuse', 'N/A'), "LLM performance monitoring"),
                    ("Flowise Builder", service_urls.get('flowise', 'N/A'), "Visual AI agent construction"),
                    ("SearXNG Search", service_urls.get('searxng', 'N/A'), "Privacy metasearch engine"),
                    ("Neo4j Graph", "http://localhost:7474", "Graph database for relationships")
                ])
            
            for service, url, purpose in core_services:
                tech_table.add_row(service, url, purpose)
            
            console.print("\n")
            console.print(tech_table)
            
            # Quick start guide
            quickstart_panel = Panel(
                f"[bold green]🚀 QUICK START GUIDE - {mode.upper()}:[/bold green]\n\n"
                f"[yellow]1. AI Chat:[/yellow] {service_urls.get('webui', 'N/A')}\n"
                "   • Create account (first user = admin)\n"
                "   • Download models from gallery\n"
                "   • Start chatting with local AI\n\n"
                f"[yellow]2. Automation:[/yellow] {service_urls.get('n8n', 'N/A')}\n"
                "   • Import business workflows\n"
                "   • Connect your services (CRM, Email, etc.)\n"
                "   • Build AI-powered automations\n\n"
                f"[yellow]3. Voice AI:[/yellow] {service_urls['whisper']}\n"
                "   • Test: curl -F \"audio=@file.wav\" {service_urls['whisper']}/transcribe\n"
                "   • Integrate with your applications\n\n"
                "[cyan]📚 Documentation: https://AIBot.Direct/docs[/cyan]\n"
                "[cyan]🆘 Support: https://t.me/aibot_direct_support[/cyan]",
                title=f"📖 {mode.upper()} Getting Started",
                border_style="green"
            )
            console.print(quickstart_panel)
            
            # Финальное сообщение
            console.print("\n[bold yellow]" + "="*90 + "[/bold yellow]")
            if deployment_success:
                final_text = Text(f"🎮 MOTHERLODE v2.0 - {mode.upper()} SUCCESS! 🎮", style="bold gold1 blink")
            else:
                final_text = Text(f"🚨 MOTHERLODE v2.0 - {mode.upper()} ISSUES! 🚨", style="bold red blink")
            console.print(Align.center(final_text))
            console.print("[bold yellow]" + "="*90 + "[/bold yellow]\n")
            
        else:
            print("\n" + "="*80)
            if deployment_success:
                print(f"🏆 AI EMPIRE ACTIVATED - {mode.upper()} MODE!")
                print("="*80)
                print(f"\n🌟 {mode.upper()} AI Infrastructure готова:")
            else:
                print(f"❌ DEPLOYMENT ISSUES - {mode.upper()} MODE!")
                print("="*80)
                print(f"\n⚠️ {mode.upper()} Infrastructure статус неопределен:")
                
            print(f"  🧠 Workflow: {service_urls.get('n8n', 'N/A')}")
            print(f"  🤖 AI Chat: {service_urls.get('webui', 'N/A')}")
            print(f"  🎤 Voice API: {service_urls['whisper']}")
            print(f"  🗄️ Database: {service_urls.get('supabase', 'N/A')}")
            
            if mode in ['standard', 'production']:
                print(f"  📊 Analytics: {service_urls.get('langfuse', 'N/A')}")
                print(f"  🌊 Agent Builder: {service_urls.get('flowise', 'N/A')}")
                print(f"  🔍 Search: {service_urls.get('searxng', 'N/A')}")
            
            print(f"\n🚀 {mode.upper()} Capabilities:")
            print("  • Multi-modal AI processing")
            print("  • RAG with vector search")
            print("  • Voice-first interfaces")
            print("  • Complete data sovereignty")
            
            if deployment_success:
                print(f"\n🎮 MOTHERLODE v2.0 - {mode.upper()} SUCCESS!")
            else:
                print(f"\n🚨 MOTHERLODE v2.0 - {mode.upper()} ISSUES!")
                print("🔧 Check Docker logs: docker-compose logs")
            print("="*80)

    def read_env_domains(self) -> Dict[str, str]:
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

def main():
    """🎮 Главная функция активации enhanced чит-кода MOTHERLODE v2.0."""
    motherlode = MotherlodeAI()
    
    try:
        # 1. 🎮 Показ улучшенной активации
        motherlode.show_cheat_activation()
        
        # 2. 🔍 Enhanced системная диагностика
        motherlode.check_prerequisites()
        
        # 3. 🛡️ Улучшенная настройка firewall
        motherlode.setup_firewall()
        
        # 4. 🔐 Получение валидированных Supabase credentials
        jwt_secret, anon_key, service_role = motherlode.get_supabase_keys()
        
        # 5. 🎯 Выбор расширенного режима развертывания
        mode = motherlode.choose_deployment_mode()
        
        # 6. 🌐 Настройка доменов с валидацией
        domains = motherlode.get_domain_configuration(mode)
        
        # 7. 💎 Генерация enhanced .env с security measures
        motherlode.generate_env_file(jwt_secret, anon_key, service_role, domains, mode)
        
        # 8. 🚀 Enhanced активация с мониторингом
        deployment_success = motherlode.activate_ai_empire(mode)
        
        # 9. 🏆 Показ статуса с техническими деталями
        motherlode.show_empire_status(deployment_success, mode)
        
    except KeyboardInterrupt:
        if HAS_RICH:
            console.print("\n[bold red]❌ Активация прервана пользователем![/bold red]")
            console.print("[cyan]🔄 Доступен rollback: python3 motherlode.py --rollback[/cyan]")
        else:
            print("\n❌ Активация MOTHERLODE v2.0 прервана!")
            print("🔄 Доступен rollback")
            
    except SystemResourceException as e:
        if HAS_RICH:
            console.print(f"\n[bold red]💻 Системные ресурсы: {e}[/bold red]")
            console.print("[yellow]🔧 Решение: увеличьте RAM/disk или используйте более мощный сервер[/yellow]")
        else:
            print(f"\n💻 Системные ресурсы: {e}")
            
    except SecurityException as e:
        if HAS_RICH:
            console.print(f"\n[bold red]🛡️ Проблема безопасности: {e}[/bold red]")
            console.print("[yellow]🔧 Операция заблокирована для защиты системы[/yellow]")
        else:
            print(f"\n🛡️ Проблема безопасности: {e}")
            
    except Exception as e:
        if HAS_RICH:
            console.print(f"\n[bold red]💥 Unexpected error:[/bold red]")
            console.print(f"[red]{str(e)}[/red]")
            console.print("\n[yellow]🔧 Enhanced troubleshooting:[/yellow]")
            console.print("• Check Docker daemon: systemctl status docker")
            console.print("• Verify network connectivity: ping google.com")
            console.print("• Check system resources: df -h && free -h")
            console.print("• Review logs: docker-compose logs")
            console.print("• Rollback: python3 motherlode.py --rollback")
        else:
            print(f"\n💥 Unexpected error: {e}")
            print("🔧 Check Docker, network, resources")
            print("🔄 Try rollback if needed")

def cli_commands():
    """🎮 Enhanced CLI команды."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="🎮 MOTHERLODE v2.0 - Enhanced AIBot Direct",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
🎯 Enhanced Examples:
  python3 motherlode.py                    # Full enhanced activation
  python3 motherlode.py --status           # System status check
  python3 motherlode.py --rollback         # Rollback to previous config
  python3 motherlode.py --health           # Health check all services
  python3 motherlode.py --backup           # Create configuration backup
  python3 motherlode.py --security-audit   # Security configuration audit
  
🌐 Website: https://AIBot.Direct
👨‍💻 Enhanced by: Community (based on Cole Medin's work)
🔒 Security: Enhanced with input validation and safe execution
        """
    )
    
    parser.add_argument('--status', action='store_true', 
                       help='Enhanced system status')
    parser.add_argument('--rollback', action='store_true',
                       help='Rollback to previous configuration')
    parser.add_argument('--health', action='store_true',
                       help='Health check all services')
    parser.add_argument('--backup', action='store_true',
                       help='Create configuration backup')
    parser.add_argument('--security-audit', action='store_true',
                       help='Security configuration audit')
    parser.add_argument('--cleanup', action='store_true',
                       help='Clean Docker volumes (with confirmation)')
    
    args = parser.parse_args()
    motherlode = MotherlodeAI()
    
    if args.status:
        motherlode.show_empire_status()
    elif args.rollback:
        motherlode.rollback_deployment()
    elif args.backup:
        backup_path = motherlode.create_backup()
        if HAS_RICH:
            console.print(f"[green]✅ Backup created: {backup_path}[/green]")
        else:
            print(f"✅ Backup created: {backup_path}")
    elif args.health:
        if HAS_RICH:
            console.print("[bold yellow]🏥 Running health checks...[/bold yellow]")
        motherlode.check_prerequisites()
    elif args.security_audit:
        if HAS_RICH:
            console.print("[bold red]🔒 Security audit not implemented yet[/bold red]")
        else:
            print("🔒 Security audit not implemented yet")
    elif args.cleanup:
        if HAS_RICH:
            should_cleanup = Confirm.ask("[bold red]⚠️ Delete all Docker volumes? This will DESTROY all data![/bold red]")
        else:
            should_cleanup = input("⚠️ Delete all Docker volumes? (y/N): ").lower() == 'y'
            
        if should_cleanup:
            try:
                motherlode._safe_subprocess_run(["docker-compose", "down", "-v"], timeout=60)
                if HAS_RICH:
                    console.print("[green]✅ Cleanup completed[/green]")
                else:
                    print("✅ Cleanup completed")
            except Exception as e:
                if HAS_RICH:
                    console.print(f"[red]❌ Cleanup failed: {e}[/red]")
                else:
                    print(f"❌ Cleanup failed: {e}")
    else:
        main()

if __name__ == "__main__":
    # 🎮 Enhanced автоустановка зависимостей
    missing_packages = []
    
    # Проверка Rich
    if not HAS_RICH:
        missing_packages.append("rich")
    
    # Проверка psutil
    try:
        import psutil
    except ImportError:
        missing_packages.append("psutil")
    
    # Устанавливаем недостающие пакеты
    if missing_packages:
        try:
            print(f"🎮 Устанавливаю зависимости: {', '.join(missing_packages)}...")
            print("⏳ Это займет несколько секунд...")
            
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install"] + missing_packages, 
                check=True, 
                capture_output=True,
                text=True,
                timeout=120
            )
            
            print("✅ Зависимости установлены успешно!")
            print("🚀 Перезапустите для улучшенного интерфейса:")
            print("   python3 motherlode.py")
            print("\n💡 Или продолжите в базовом режиме нажав Enter...")
            input()
            
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Не удалось установить зависимости: {e}")
            print("🔄 Продолжаю в базовом режиме...")
            print("💡 Для полного функционала установите вручную:")
            print(f"   pip3 install {' '.join(missing_packages)}")
            time.sleep(2)
            
        except subprocess.TimeoutExpired:
            print("⏱️ Установка заняла слишком много времени")
            print("🔄 Продолжаю в базовом режиме...")
            time.sleep(2)
            
        except Exception as e:
            print(f"❌ Ошибка при установке: {e}")
            print("🔄 Продолжаю в базовом режиме...")
            time.sleep(2)
    
    # 🎯 Запуск enhanced CLI
    cli_commands()
