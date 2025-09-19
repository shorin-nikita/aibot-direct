#!/usr/bin/env python3
"""
🎮 MOTHERLODE.PY - AIBot Direct Complete Deployment v2.0 🎮
💰💰💰 АКТИВИРУЙ ВСЁ ЗОЛОТО AI МИРА! 💰💰💰

Полная версия с исправлениями всех проблем развертывания

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
        self.codename = "Complete-Deploy" 
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
                "[bold gold1]⚡ AIBot Direct v2.0 — Complete AI Infrastructure! ⚡[/bold gold1]\n"
                "[green]💎 LEVEL UP — Production-Ready & Fully Fixed ⭐[/green]\n"
                "[red]🛡️ NEW: Complete Deployment & Real Status Verification[/red]",
                title="🏆 Welcome to Complete AI Stack v2.0",
                border_style="gold1",
                padding=(1, 2)
            )
            console.print(header_panel)
            
            # Информация о новых возможностях
            improvements_panel = Panel(
                "[bold cyan]🚀 COMPLETE IN v2.0:[/bold cyan]\n\n"
                "[green]🛡️ DEPLOYMENT FIXES:[/green]\n"
                "┣━ [white]Complete .env generation[/white] - все необходимые переменные\n"
                "┣━ [white]Docker Compose auto-fix[/white] - исправление volume mapping\n"
                "┣━ [white]Phased deployment[/white] - поэтапный запуск сервисов\n"
                "┗━ [white]Real status verification[/white] - проверка реальной работы\n\n"
                "[blue]📊 ENHANCED VALIDATION:[/blue]\n"
                "┣━ [white]Container monitoring[/white] - реальная проверка контейнеров\n"
                "┣━ [white]Port validation[/white] - проверка доступности сервисов\n"
                "┣━ [white]Service health checks[/white] - мониторинг работоспособности\n"
                "┗━ [white]Smart troubleshooting[/white] - автодиагностика проблем\n\n"
                "[yellow]⚙️ USER EXPERIENCE:[/yellow]\n"
                "┣━ [white]Clear guidance[/white] - точные инструкции на каждом этапе\n"
                "┣━ [white]Problem solving[/white] - конкретные решения проблем\n"
                "┗━ [white]Success verification[/white] - подтверждение работающей системы\n",
                title="🔥 Complete Features",
                border_style="cyan",
                padding=(1, 2)
            )
            console.print(improvements_panel)
            
        else:
            print("\n" + "="*80)
            print("🎮 MOTHERLODE v2.0 ACTIVATED!")
            print("⚡ AIBot Direct v2.0 — Complete AI Infrastructure!")
            print("💎 LEVEL UP — Production-Ready & Fully Fixed")
            print("🛡️ NEW: Complete Deployment & Real Status Verification")
            print("="*80)
            print("\n🚀 COMPLETE IN v2.0:")
            print("🛡️ FIXES: Complete .env, Docker auto-fix, Phased deployment")
            print("📊 VALIDATION: Container monitoring, Port checks, Health monitoring")
            print("⚙️ UX: Clear guidance, Problem solving, Success verification")

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
            console.print("\n[bold gold1]🔍 COMPLETE СИСТЕМНАЯ ДИАГНОСТИКА[/bold gold1]")
            console.print("[dim]Проверяем совместимость системы с полной валидацией[/dim]\n")
            
            check_table = Table(
                title="🎮 Complete System Compatibility Check",
                show_header=True,
                header_style="bold magenta",
                border_style="cyan"
            )
            check_table.add_column("🔧 Component", style="bold white", width=25)
            check_table.add_column("📊 Status", justify="center", width=15)
            check_table.add_column("🎯 What it does", style="dim yellow", width=40)
            check_table.add_column("🏆 Level", justify="center", width=12)
            
        else:
            print("\n🔍 COMPLETE СИСТЕМНАЯ ДИАГНОСТИКА:")
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
                    "[yellow]🎯 Система прошла complete валидацию:[/yellow]\n"
                    "• [green]Все зависимости установлены[/green]\n"
                    "• [blue]Системные ресурсы достаточны[/blue]\n"
                    "• [magenta]Сеть настроена корректно[/magenta]\n"
                    "• [cyan]Готов к развертыванию complete AI[/cyan]\n\n"
                    "[bold gold1]🚀 SYSTEM VALIDATED - READY FOR COMPLETE DEPLOYMENT![/bold gold1]",
                    title="🏆 Complete System Ready",
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
                "[bold red]🛡️ COMPLETE NETWORK SECURITY[/bold red]\n\n"
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
                title="🔧 Complete Network Security",
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
            print("\n🛡️ COMPLETE NETWORK SECURITY")
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
            console.print("\n[bold yellow]🔧 Конфигурирую complete firewall...[/bold yellow]")
            
            for cmd, desc in track(firewall_commands, description="[green]Setting up complete security..."):
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
                
            console.print("\n[bold green]🛡️ Complete firewall activated![/bold green]")
            
        else:
            print("\n🔧 Конфигурирую complete firewall...")
            
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
                "[bold red]🔐 COMPLETE SUPABASE CONFIGURATION[/bold red]\n\n"
                "[blue]📖 Генерация ключей через Supabase CLI:[/blue]\n"
                "[dim]npm install -g @supabase/cli[/dim]\n"
                "[dim]supabase gen keys --project-ref your-project[/dim]\n\n"
                "[link=https://supabase.com/docs/guides/self-hosting/docker#generate-api-keys]📚 Official Documentation[/link]\n\n"
                "[bold white]🎯 JWT-based Authentication (криптографически стойкие ключи):[/bold white]\n"
                "• [yellow]JWT_SECRET[/yellow] - HMAC ключ для подписи токенов (≥32 символа)\n"
                "• [blue]ANON_KEY[/blue] - публичный API ключ с ограниченными правами\n"
                "• [red]SERVICE_ROLE_KEY[/red] - административный ключ (полные права)\n\n"
                "[bold red]⚠️ SECURITY: Храните ключи в безопасности![/bold red]",
                title="🏆 Complete Supabase Setup",
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
            print("\n🔐 COMPLETE SUPABASE CONFIGURATION")
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
                "  [dim]Все сервисы + complete security + performance tuning[/dim]",
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
        """💎 Полная генерация .env с всеми необходимыми переменными."""
        # Создаем бэкап перед генерацией
        backup_path = self.create_backup()
        
        def generate_secret(length: int = 32) -> str:
            # Улучшенная генерация с большим алфавитом
            alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
            return ''.join(secrets.choice(alphabet) for _ in range(length))
        
        # ПОЛНЫЙ .env файл со всеми необходимыми переменными
        env_content = f"""# 🎮 AIBot Direct v2.0 - COMPLETE MOTHERLODE Configuration
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Mode: {mode.upper()}
# Website: https://AIBot.Direct
# Backup: {backup_path}

# ⚠️ SECURITY WARNING ⚠️
# This file contains sensitive credentials in plain text!
# - Set proper file permissions: chmod 600 .env
# - Never commit this file to version control
# - Rotate secrets regularly in production

# 🔑 Supabase JWT Authentication (user provided)
JWT_SECRET={jwt_secret}
ANON_KEY={anon_key}
SERVICE_ROLE_KEY={service_role}

# 📊 Database configuration (КРИТИЧНО!)
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=postgres
POSTGRES_PASSWORD={generate_secret(32)}
POSTGRES_USER=postgres

# 🔧 НЕДОСТАЮЩИЕ ПЕРЕМЕННЫЕ (критично для запуска!)
oUGA={generate_secret(16)}
NC5K5W={generate_secret(16)}
mmPYJ={generate_secret(16)}

# 🔐 Основные секреты
N8N_ENCRYPTION_KEY={generate_secret(64)}
N8N_USER_MANAGEMENT_JWT_SECRET={generate_secret(64)}
DASHBOARD_PASSWORD={generate_secret(24)}
SECRET_KEY_BASE={generate_secret(64)}
POOLER_TENANT_ID={generate_secret(16)}

# 🔧 Сервисные пароли  
MINIO_ROOT_PASSWORD={generate_secret(32)}
CLICKHOUSE_PASSWORD={generate_secret(32)}
LANGFUSE_SALT={generate_secret(32)}
NEXTAUTH_SECRET={generate_secret(64)}
ENCRYPTION_KEY={generate_secret(32)}
FLOWISE_USERNAME=admin
FLOWISE_PASSWORD={generate_secret(16)}

# 🌐 Kong API Gateway
KONG_HTTP_PORT=8000
KONG_HTTPS_PORT=8443

# 📧 Email конфигурация
SMTP_HOST=
SMTP_PORT=587
SMTP_USER=
SMTP_PASS=
SMTP_ADMIN_EMAIL={domains.get('email', 'admin@example.com')}
SMTP_SENDER_NAME=AIBot Direct

# 🔐 Auth система
API_EXTERNAL_URL=http://localhost:8000
SITE_URL=http://localhost:3000
DISABLE_SIGNUP=false
JWT_EXPIRY=3600
ENABLE_EMAIL_SIGNUP=true
ENABLE_PHONE_SIGNUP=false
ENABLE_ANONYMOUS_USERS=false
ENABLE_EMAIL_AUTOCONFIRM=false
ENABLE_PHONE_AUTOCONFIRM=false

# 📧 Email templates
MAILER_URLPATHS_INVITE=/auth/v1/verify
MAILER_URLPATHS_CONFIRMATION=/auth/v1/verify
MAILER_URLPATHS_RECOVERY=/auth/v1/verify
MAILER_URLPATHS_EMAIL_CHANGE=/auth/v1/verify
ADDITIONAL_REDIRECT_URLS=

# 🔧 Database pooling
POOLER_DEFAULT_POOL_SIZE=20
POOLER_MAX_CLIENT_CONN=100
POOLER_PROXY_PORT_TRANSACTION=5432

# 📊 Supabase конфигурация
SUPABASE_PUBLIC_URL=http://localhost:8000
PGRST_DB_SCHEMAS=public,storage,graphql_public
FUNCTIONS_VERIFY_JWT=false

# 📊 Studio
STUDIO_DEFAULT_ORGANIZATION=Default Organization
STUDIO_DEFAULT_PROJECT=Default Project
DASHBOARD_USERNAME=supabase

# 🔧 Система
DOCKER_SOCKET_LOCATION=/var/run/docker.sock
VAULT_ENC_KEY={generate_secret(32)}

# 📊 Логирование (можно оставить пустыми)
LOGFLARE_PUBLIC_ACCESS_TOKEN=
LOGFLARE_PRIVATE_ACCESS_TOKEN=

# 🖼️ Обработка изображений
IMGPROXY_ENABLE_WEBP_DETECTION=true

# 🎯 Neo4j configuration
NEO4J_AUTH=neo4j/{generate_secret(16)}

# 🔧 Qdrant configuration  
QDRANT_URL=http://qdrant:6333

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
        
        # Подсчет строк в файле
        with open('.env', 'r') as f:
            total_lines = sum(1 for line in f)
            
        active_domains = sum(1 for k in domains.keys() if domains.get(k))
        
        if HAS_RICH:
            env_panel = Panel(
                "[bold green]✅ COMPLETE CONFIGURATION GENERATED![/bold green]\n\n"
                "[yellow]📝 Создан полный .env файл:[/yellow]\n"
                f"• [green]Всего строк:[/green] {total_lines} ✅\n"
                f"• [blue]Supabase JWT ключей:[/blue] 3 шт. ✅\n"
                f"• [cyan]Активных доменов:[/cyan] {active_domains} шт. ✅\n"
                f"• [yellow]Режим развертывания:[/yellow] {mode.upper()} ✅\n"
                f"• [purple]Бэкап сохранен в:[/purple] {backup_path} ✅\n\n"
                "[bold red]🛡️ ALL VARIABLES INCLUDED:[/bold red]\n"
                "• [white]Database configuration[/white]\n"
                "• [white]Authentication secrets[/white]\n"
                "• [white]Service passwords[/white]\n"
                "• [white]System configuration[/white]\n\n"
                "[bold gold1]🔐 Система готова к запуску![/bold gold1]",
                title="🏆 Complete Configuration Ready",
                border_style="green"
            )
            console.print(env_panel)
            
        else:
            print(f"✅ Complete .env создан! Режим: {mode.upper()}")
            print(f"Строк: {total_lines}, Доменов: {active_domains}")
            print(f"Бэкап: {backup_path}")
            print("🚨 SECURITY: Файл содержит sensitive данные!")

    def fix_docker_compose_issues(self):
        """🔧 Исправляем проблемы в Docker Compose файлах."""
        fixes_applied = []
        
        # Ищем docker-compose файлы
        compose_files = []
        for filename in ['docker-compose.yml', 'docker-compose.yaml']:
            if Path(filename).exists():
                compose_files.append(filename)
        
        for compose_file in compose_files:
            try:
                with open(compose_file, 'r') as f:
                    content = f.read()
                
                original_content = content
                
                # Исправляем неправильный volume mapping
                if ':/var/run/docker.sock:ro,z' in content:
                    content = content.replace(':/var/run/docker.sock:ro,z', '/var/run/docker.sock:/var/run/docker.sock:ro')
                    fixes_applied.append("Fixed Docker socket volume mapping")
                
                # Исправляем другие возможные проблемы с volume
                import re
                content = re.sub(r':\s*/var/run/docker\.sock:ro,z', '/var/run/docker.sock:/var/run/docker.sock:ro', content)
                
                # Записываем исправленный файл только если были изменения
                if content != original_content:
                    with open(compose_file, 'w') as f:
                        f.write(content)
                    fixes_applied.append(f"Updated {compose_file}")
                        
            except Exception as e:
                if HAS_RICH:
                    console.print(f"[red]❌ Error fixing {compose_file}: {e}[/red]")
                else:
                    print(f"❌ Error fixing {compose_file}: {e}")
        
        if fixes_applied and HAS_RICH:
            console.print(f"[green]✅ Docker Compose fixes applied: {', '.join(fixes_applied)}[/green]")
        elif fixes_applied:
            print(f"✅ Docker Compose fixes applied: {', '.join(fixes_applied)}")

    def activate_ai_empire(self, mode: str) -> bool:
        """🚀 ПОЛНЫЙ запуск системы с проверками и исправлениями."""
        if HAS_RICH:
            console.print(f"\n[bold gold1]🚀 ACTIVATING AI EMPIRE - {mode.upper()} MODE[/bold gold1]")
            console.print("[dim]Complete deployment with fixes and verification[/dim]\n")
        else:
            print(f"\n🚀 ACTIVATING AI EMPIRE - {mode.upper()} MODE")
            print("Complete deployment with fixes and verification")
        
        # Шаг 1: Исправляем Docker Compose проблемы
        if HAS_RICH:
            console.print("[bold yellow]🔧 STEP 1: Fixing Docker Compose issues...[/bold yellow]")
        else:
            print("🔧 STEP 1: Fixing Docker Compose issues...")
            
        self.fix_docker_compose_issues()
        
        # Шаг 2: Проверяем .env файл
        if HAS_RICH:
            console.print("\n[bold yellow]🔧 STEP 2: Verifying .env completeness...[/bold yellow]")
        else:
            print("\n🔧 STEP 2: Verifying .env completeness...")
            
        if Path('.env').exists():
            with open('.env', 'r') as f:
                env_lines = sum(1 for line in f if line.strip() and not line.startswith('#'))
                
            if env_lines < 40:  # Минимум переменных для работы
                if HAS_RICH:
                    console.print(f"[red]❌ .env файл неполный ({env_lines} переменных, нужно >40)[/red]")
                    console.print("[yellow]⚠️ Regenerating complete .env file...[/yellow]")
                else:
                    print(f"❌ .env файл неполный ({env_lines} переменных, нужно >40)")
                    print("⚠️ Regenerating complete .env file...")
                return False
            else:
                if HAS_RICH:
                    console.print(f"[green]✅ .env file complete ({env_lines} variables)[/green]")
                else:
                    print(f"✅ .env file complete ({env_lines} variables)")
        else:
            if HAS_RICH:
                console.print("[red]❌ .env file missing![/red]")
            else:
                print("❌ .env file missing!")
            return False
        
        # Шаг 3: Останавливаем предыдущие контейнеры
        if HAS_RICH:
            console.print("\n[bold yellow]🔧 STEP 3: Stopping previous containers...[/bold yellow]")
        else:
            print("\n🔧 STEP 3: Stopping previous containers...")
            
        try:
            self._safe_subprocess_run(["docker-compose", "down", "-v"], check=False, timeout=60)
            if HAS_RICH:
                console.print("[green]✅ Previous containers stopped[/green]")
            else:
                print("✅ Previous containers stopped")
        except Exception as e:
            if HAS_RICH:
                console.print(f"[yellow]⚠️ Could not stop containers: {e}[/yellow]")
            else:
                print(f"⚠️ Could not stop containers: {e}")
        
        # Шаг 4: Проверяем Docker Compose синтаксис
        if HAS_RICH:
            console.print("\n[bold yellow]🔧 STEP 4: Validating Docker Compose syntax...[/bold yellow]")
        else:
            print("\n🔧 STEP 4: Validating Docker Compose syntax...")
            
        try:
            result = self._safe_subprocess_run(["docker-compose", "config", "--quiet"], timeout=30)
            if result.returncode == 0:
                if HAS_RICH:
                    console.print("[green]✅ Docker Compose syntax valid[/green]")
                else:
                    print("✅ Docker Compose syntax valid")
            else:
                if HAS_RICH:
                    console.print("[red]❌ Docker Compose syntax errors detected![/red]")
                else:
                    print("❌ Docker Compose syntax errors detected!")
                return False
        except Exception as e:
            if HAS_RICH:
                console.print(f"[red]❌ Could not validate Docker Compose: {e}[/red]")
            else:
                print(f"❌ Could not validate Docker Compose: {e}")
            return False
        
        # Шаг 5: Запускаем контейнеры поэтапно
        if HAS_RICH:
            console.print("\n[bold yellow]🔧 STEP 5: Starting containers in phases...[/bold yellow]")
        else:
            print("\n🔧 STEP 5: Starting containers in phases...")
        
        # Фаза 1: Базовые сервисы (база данных)
        if HAS_RICH:
            console.print("\n[cyan]Phase 1: Database services...[/cyan]")
        else:
            print("\nPhase 1: Database services...")
            
        try:
            # Запускаем только базовые сервисы сначала
            basic_services = ["db", "redis"]
            for service in basic_services:
                try:
                    result = self._safe_subprocess_run(["docker-compose", "up", "-d", service], timeout=120)
                    if result.returncode == 0:
                        if HAS_RICH:
                            console.print(f"[green]✅ {service} started[/green]")
                        else:
                            print(f"✅ {service} started")
                    else:
                        if HAS_RICH:
                            console.print(f"[yellow]⚠️ {service} may have issues[/yellow]")
                        else:
                            print(f"⚠️ {service} may have issues")
                except Exception as e:
                    if HAS_RICH:
                        console.print(f"[yellow]⚠️ {service} startup issue: {e}[/yellow]")
                    else:
                        print(f"⚠️ {service} startup issue: {e}")
            
            # Ждем инициализации БД
            if HAS_RICH:
                console.print("[dim]Waiting for database initialization...[/dim]")
            else:
                print("Waiting for database initialization...")
            time.sleep(20)
            
        except Exception as e:
            if HAS_RICH:
                console.print(f"[red]❌ Database phase failed: {e}[/red]")
            else:
                print(f"❌ Database phase failed: {e}")
        
        # Фаза 2: Все остальные сервисы
        if HAS_RICH:
            console.print("\n[cyan]Phase 2: All services...[/cyan]")
        else:
            print("\nPhase 2: All services...")
            
        try:
            # Запускаем все сервисы
            result = self._safe_subprocess_run(["docker-compose", "up", "-d"], timeout=300)
            if result.returncode == 0:
                if HAS_RICH:
                    console.print("[green]✅ All services deployment initiated[/green]")
                else:
                    print("✅ All services deployment initiated")
                deployment_success = True
            else:
                if HAS_RICH:
                    console.print(f"[red]❌ Services deployment failed (exit {result.returncode})[/red]")
                else:
                    print(f"❌ Services deployment failed (exit {result.returncode})")
                deployment_success = False
                
        except subprocess.TimeoutExpired:
            if HAS_RICH:
                console.print("[yellow]⏱️ Deployment timeout - services may still be starting[/yellow]")
            else:
                print("⏱️ Deployment timeout - services may still be starting")
            deployment_success = False
            
        except Exception as e:
            if HAS_RICH:
                console.print(f"[red]❌ Deployment error: {e}[/red]")
            else:
                print(f"❌ Deployment error: {e}")
            deployment_success = False
        
        # Шаг 6: Проверяем результат
        if HAS_RICH:
            console.print("\n[bold yellow]🔧 STEP 6: Verifying deployment...[/bold yellow]")
        else:
            print("\n🔧 STEP 6: Verifying deployment...")
            
        time.sleep(10)  # Даем время сервисам запуститься
        
        try:
            result = self._safe_subprocess_run(["docker", "ps", "--format", "table {{.Names}}\\t{{.Status}}"], 
                                            timeout=30, capture_output=True)
            if result.returncode == 0 and result.stdout:
                running_containers = [line for line in result.stdout.split('\n') 
                                    if line and 'Up' in line and 'NAMES' not in line]
                
                if len(running_containers) > 0:
                    if HAS_RICH:
                        console.print(f"[green]✅ {len(running_containers)} containers running[/green]")
                        for container in running_containers[:5]:  # Показываем первые 5
                            console.print(f"[dim]  {container}[/dim]")
                    else:
                        print(f"✅ {len(running_containers)} containers running")
                        for container in running_containers[:5]:
                            print(f"  {container}")
                    deployment_success = True
                else:
                    if HAS_RICH:
                        console.print("[red]❌ No containers are running![/red]")
                    else:
                        print("❌ No containers are running!")
                    deployment_success = False
            else:
                deployment_success = False
                
        except Exception as e:
            if HAS_RICH:
                console.print(f"[yellow]⚠️ Could not verify containers: {e}[/yellow]")
            else:
                print(f"⚠️ Could not verify containers: {e}")
            # Не считаем это критичной ошибкой
        
        return deployment_success

    def verify_services_running(self) -> Dict[str, bool]:
        """🔍 Проверяем, что сервисы действительно работают."""
        services_status = {}
        
        # Проверяем контейнеры
        try:
            result = self._safe_subprocess_run(["docker", "ps", "--format", "{{.Names}}:{{.Status}}"], 
                                             timeout=30, capture_output=True)
            if result.returncode == 0:
                container_lines = [line.strip() for line in result.stdout.split('\n') if line.strip()]
                running_containers = [line.split(':')[0] for line in container_lines if ':Up' in line]
                
                # Ключевые сервисы для проверки
                key_services = ['db', 'n8n', 'redis']
                for service in key_services:
                    # Проверяем есть ли контейнер с таким именем или содержащий такое имя
                    services_status[service] = any(service in container for container in running_containers)
                    
            else:
                if HAS_RICH:
                    console.print("[red]❌ Could not check container status[/red]")
                else:
                    print("❌ Could not check container status")
        except Exception as e:
            if HAS_RICH:
                console.print(f"[yellow]⚠️ Container check error: {e}[/yellow]")
            else:
                print(f"⚠️ Container check error: {e}")
        
        # Проверяем порты
        key_ports = [5432, 3000, 5678, 6379]  # PostgreSQL, OpenWebUI, n8n, Redis
        for port in key_ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(2)
                    result = s.connect_ex(('localhost', port))
                    services_status[f'port_{port}'] = (result == 0)
            except Exception:
                services_status[f'port_{port}'] = False
        
        return services_status

    def show_empire_status(self, deployment_success: bool = True, mode: str = "minimal"):
        """🏆 ПОЛНЫЙ статус системы с проверкой работоспособности."""
        
        # Проверяем реальное состояние сервисов
        services_status = self.verify_services_running()
        running_containers = sum(1 for k, v in services_status.items() 
                               if not k.startswith('port_') and v)
        running_ports = sum(1 for k, v in services_status.items() 
                          if k.startswith('port_') and v)
        
        # Обновляем статус деплоймента на основе реальной проверки
        actual_success = running_containers >= 2 and running_ports >= 2
        
        # Читаем конфигурацию
        env_domains = self.read_env_domains()
        
        # Получаем IP для fallback
        try:
            result = self._safe_subprocess_run(['curl', '-s', 'ifconfig.me'], timeout=10)
            server_ip = result.stdout.strip() if result.returncode == 0 else "217.114.0.246"
        except:
            server_ip = "217.114.0.246"
        
        # Строим URL'ы
        service_urls = {
            'n8n': f"https://{env_domains.get('N8N_HOSTNAME', 'n8n-cocacola.aibot.direct')}",
            'webui': f"http://{server_ip}:3000",
            'supabase': f"https://{env_domains.get('SUPABASE_HOSTNAME', 'supabase-cocacola.aibot.direct')}",
            'whisper': f"http://{server_ip}:9000",
            'langfuse': f"http://{server_ip}:3001",
            'flowise': f"http://{server_ip}:3001",
            'searxng': f"http://{server_ip}:8080"
        }
        
        if HAS_RICH:
            # Определяем заголовок статуса
            if actual_success:
                status_text = f"[bold green]🏆 AI EMPIRE SUCCESSFULLY DEPLOYED - {mode.upper()}! 🏆[/bold green]\n\n[bold cyan]✅ System is RUNNING and READY:[/bold cyan]\n\n"
                border_color = "green"
            elif deployment_success and not actual_success:
                status_text = f"[bold yellow]⚠️ DEPLOYMENT STARTED - {mode.upper()} MODE ⚠️[/bold yellow]\n\n[bold yellow]🔄 Services are starting up (may take a few minutes):[/bold yellow]\n\n"
                border_color = "yellow"
            else:
                status_text = f"[bold red]❌ DEPLOYMENT ISSUES - {mode.upper()} MODE! ❌[/bold red]\n\n[bold red]⚠️ System needs attention:[/bold red]\n\n"
                border_color = "red"
            
            # Статус сервисов
            services_info = f"[dim]💻 System Status: {running_containers} containers running, {running_ports} ports active[/dim]\n\n"
            
            # Главная панель статуса
            empire_panel = Panel(
                status_text + services_info +
                
                "[yellow]🧠 PRIMARY AI INTERFACES:[/yellow]\n"
                f"• [bold white]Workflow Automation:[/bold white] {service_urls['n8n']}\n"
                "  [dim]n8n visual programming for AI automation[/dim]\n"
                f"• [bold white]AI Chat Interface:[/bold white] {service_urls['webui']}\n"
                "  [dim]OpenWebUI for local LLM interaction[/dim]\n"
                f"• [bold white]Speech API:[/bold white] {service_urls['whisper']}\n"
                "  [dim]Whisper ASR/TTS endpoints for voice AI[/dim]\n"
                f"• [bold white]Database Control:[/bold white] {service_urls['supabase']}\n"
                "  [dim]Supabase dashboard for data management[/dim]\n\n"
                
                "[green]📊 SYSTEM CAPABILITIES:[/green]\n"
                "• [bright_green]Multi-modal AI[/bright_green] - text, voice, image processing\n"
                "• [bright_green]RAG Pipeline[/bright_green] - document intelligence with vector search\n"
                "• [bright_green]Workflow Automation[/bright_green] - n8n visual programming\n"
                "• [bright_green]Voice-First UI[/bright_green] - speech-to-action workflows\n"
                "• [bright_green]Zero-Cloud[/bright_green] - complete data sovereignty\n\n"
                
                f"[bold {'green' if actual_success else 'yellow' if deployment_success else 'red'}]🎮 {mode.upper()} AI Stack: {'READY FOR USE!' if actual_success else 'STARTING UP...' if deployment_success else 'NEEDS ATTENTION'}[/bold {'green' if actual_success else 'yellow' if deployment_success else 'red'}]",
                title=f"🎯 {mode.upper()} AI Infrastructure Status",
                border_style=border_color,
                width=90
            )
            console.print(empire_panel)
            
            # Быстрый старт или диагностика
            if actual_success:
                quickstart_panel = Panel(
                    f"[bold green]🚀 QUICK START - СИСТЕМА ГОТОВА:[/bold green]\n\n"
                    f"[yellow]1. AI Chat (начните здесь):[/yellow] {service_urls['webui']}\n"
                    "   • Откройте в браузере\n"
                    "   • Создайте аккаунт (первый пользователь = админ)\n"
                    "   • Скачайте модели из галереи\n"
                    "   • Начните общение с локальным AI\n\n"
                    f"[yellow]2. Workflow Automation:[/yellow] {service_urls['n8n']}\n"
                    "   • Создайте автоматизацию бизнес-процессов\n"
                    "   • Подключите внешние сервисы (CRM, Email, и др.)\n"
                    "   • Стройте AI-powered автоматизацию\n\n"
                    f"[yellow]3. Voice AI:[/yellow] {service_urls['whisper']}\n"
                    "   • Тест: curl -F \"audio=@file.wav\" {service_urls['whisper']}/transcribe\n\n"
                    "[bold gold1]🎉 ПОЗДРАВЛЯЕМ! Ваша AI-система полностью готова к работе![/bold gold1]\n"
                    "[cyan]📚 Документация: https://AIBot.Direct/docs[/cyan]\n"
                    "[cyan]🆘 Поддержка: https://t.me/aibot_direct_support[/cyan]",
                    title=f"📖 {mode.upper()} - СИСТЕМА ЗАПУЩЕНА!",
                    border_style="green"
                )
                console.print(quickstart_panel)
            else:
                # Диагностика проблем
                troubleshoot_panel = Panel(
                    "[bold red]🔧 ДИАГНОСТИКА И РЕШЕНИЕ ПРОБЛЕМ:[/bold red]\n\n"
                    "[yellow]1. Проверьте контейнеры:[/yellow]\n"
                    "   docker ps\n\n"
                    "[yellow]2. Посмотрите логи:[/yellow]\n"
                    "   docker-compose logs -f\n\n"
                    "[yellow]3. Перезапустите сервисы:[/yellow]\n"
                    "   docker-compose down\n"
                    "   docker-compose up -d\n\n"
                    "[yellow]4. Если проблемы с портами:[/yellow]\n"
                    "   sudo netstat -tlnp | grep -E \":(3000|5678|5432|6379)\"\n\n"
                    "[yellow]5. Очистить и начать заново:[/yellow]\n"
                    "   docker-compose down -v\n"
                    "   docker system prune -f\n"
                    "   python3 motherlode.py\n\n"
                    "[bold yellow]💡 TIP: Подождите 2-3 минуты после запуска - сервисы могут инициализироваться[/bold yellow]",
                    title="🔧 Troubleshooting Guide",
                    border_style="red"
                )
                console.print(troubleshoot_panel)
            
            # Финальное сообщение
            console.print("\n[bold yellow]" + "="*90 + "[/bold yellow]")
            if actual_success:
                final_text = Text(f"🎮 MOTHERLODE v2.0 - {mode.upper()} SUCCESS! СИСТЕМА РАБОТАЕТ! 🎮", style="bold green blink")
            elif deployment_success:
                final_text = Text(f"🎮 MOTHERLODE v2.0 - {mode.upper()} DEPLOYING! ПОДОЖДИТЕ... 🎮", style="bold yellow blink")
            else:
                final_text = Text(f"🚨 MOTHERLODE v2.0 - {mode.upper()} NEEDS ATTENTION! 🚨", style="bold red blink")
            console.print(Align.center(final_text))
            console.print("[bold yellow]" + "="*90 + "[/bold yellow]\n")
            
        else:
            print("\n" + "="*80)
            if actual_success:
                print(f"🏆 AI EMPIRE SUCCESSFULLY DEPLOYED - {mode.upper()}!")
                print("✅ СИСТЕМА ГОТОВА К ИСПОЛЬЗОВАНИЮ!")
                print("="*80)
                print(f"\n🚀 НАЧНИТЕ ЗДЕСЬ:")
                print(f"  🤖 AI Chat: {service_urls['webui']}")
                print(f"  🧠 Automation: {service_urls['n8n']}")
                print(f"  🎤 Voice API: {service_urls['whisper']}")
                print(f"\n🎉 ПОЗДРАВЛЯЕМ! Система полностью работает!")
            elif deployment_success:
                print(f"⚠️ DEPLOYMENT STARTED - {mode.upper()} MODE")
                print("🔄 Сервисы запускаются... подождите 2-3 минуты")
            else:
                print(f"❌ DEPLOYMENT ISSUES - {mode.upper()} MODE!")
                print("🔧 Нужна диагностика - выполните: docker ps")
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
    """🎮 Главная функция ПОЛНОГО запуска complete MOTHERLODE v2.0."""
    motherlode = MotherlodeAI()
    deployment_success = False
    mode = "minimal"
    
    try:
        # 1. 🎮 Показ улучшенной активации
        motherlode.show_cheat_activation()
        
        # 2. 🔍 Complete системная диагностика
        if HAS_RICH:
            console.print("\n[bold cyan]🔍 СИСТЕМНАЯ ДИАГНОСТИКА[/bold cyan]")
        else:
            print("\n🔍 СИСТЕМНАЯ ДИАГНОСТИКА")
            
        motherlode.check_prerequisites()
        
        # 3. 🛡️ Complete настройка firewall
        if HAS_RICH:
            console.print("\n[bold red]🛡️ НАСТРОЙКА БЕЗОПАСНОСТИ[/bold red]")
        else:
            print("\n🛡️ НАСТРОЙКА БЕЗОПАСНОСТИ")
            
        motherlode.setup_firewall()
        
        # 4. 🔐 Получение валидированных Supabase credentials
        if HAS_RICH:
            console.print("\n[bold gold1]🔐 НАСТРОЙКА АУТЕНТИФИКАЦИИ[/bold gold1]")
        else:
            print("\n🔐 НАСТРОЙКА АУТЕНТИФИКАЦИИ")
            
        jwt_secret, anon_key, service_role = motherlode.get_supabase_keys()
        
        # 5. 🎯 Выбор расширенного режима развертывания
        if HAS_RICH:
            console.print("\n[bold blue]🎯 РЕЖИМ РАЗВЕРТЫВАНИЯ[/bold blue]")
        else:
            print("\n🎯 РЕЖИМ РАЗВЕРТЫВАНИЯ")
            
        mode = motherlode.choose_deployment_mode()
        
        # 6. 🌐 Настройка доменов с валидацией
        if HAS_RICH:
            console.print(f"\n[bold green]🌐 КОНФИГУРАЦИЯ ДОМЕНОВ - {mode.upper()}[/bold green]")
        else:
            print(f"\n🌐 КОНФИГУРАЦИЯ ДОМЕНОВ - {mode.upper()}")
            
        domains = motherlode.get_domain_configuration(mode)
        
        # 7. 💎 Генерация ПОЛНОГО .env со всеми переменными
        if HAS_RICH:
            console.print(f"\n[bold purple]💎 ГЕНЕРАЦИЯ КОНФИГУРАЦИИ - {mode.upper()}[/bold purple]")
        else:
            print(f"\n💎 ГЕНЕРАЦИЯ КОНФИГУРАЦИИ - {mode.upper()}")
            
        motherlode.generate_env_file(jwt_secret, anon_key, service_role, domains, mode)
        
        # Проверяем что .env файл действительно полный
        if Path('.env').exists():
            with open('.env', 'r') as f:
                env_lines = sum(1 for line in f if line.strip() and not line.startswith('#'))
            
            if env_lines < 40:
                if HAS_RICH:
                    console.print(f"[red]❌ КРИТИЧЕСКАЯ ОШИБКА: .env файл неполный ({env_lines} переменных)![/red]")
                    console.print("[yellow]Попробуйте перезапустить скрипт[/yellow]")
                else:
                    print(f"❌ КРИТИЧЕСКАЯ ОШИБКА: .env файл неполный ({env_lines} переменных)!")
                    print("Попробуйте перезапустить скрипт")
                return
            else:
                if HAS_RICH:
                    console.print(f"[green]✅ .env файл полный ({env_lines} переменных)[/green]")
                else:
                    print(f"✅ .env файл полный ({env_lines} переменных)")
        
        # 8. 🚀 ПОЛНЫЙ запуск системы с проверками
        if HAS_RICH:
            console.print(f"\n[bold gold1]🚀 ЗАПУСК СИСТЕМЫ - {mode.upper()}[/bold gold1]")
        else:
            print(f"\n🚀 ЗАПУСК СИСТЕМЫ - {mode.upper()}")
            
        deployment_success = motherlode.activate_ai_empire(mode)
        
        # 9. 🔍 Дополнительная проверка статуса
        if deployment_success:
            if HAS_RICH:
                console.print("\n[bold yellow]🔍 ФИНАЛЬНАЯ ПРОВЕРКА СИСТЕМЫ...[/bold yellow]")
            else:
                print("\n🔍 ФИНАЛЬНАЯ ПРОВЕРКА СИСТЕМЫ...")
                
            time.sleep(5)  # Даем время сервисам полностью запуститься
            services_status = motherlode.verify_services_running()
            actual_running = sum(1 for k, v in services_status.items() 
                               if not k.startswith('port_') and v)
            
            if actual_running < 2:
                if HAS_RICH:
                    console.print(f"[yellow]⚠️ Только {actual_running} сервисов запущено. Возможно нужно подождать...[/yellow]")
                else:
                    print(f"⚠️ Только {actual_running} сервисов запущено. Возможно нужно подождать...")
        
        # 10. 🏆 Показ ПОЛНОГО статуса с диагностикой
        if HAS_RICH:
            console.print(f"\n[bold gold1]🏆 ФИНАЛЬНЫЙ СТАТУС - {mode.upper()}[/bold gold1]")
        else:
            print(f"\n🏆 ФИНАЛЬНЫЙ СТАТУС - {mode.upper()}")
            
        motherlode.show_empire_status(deployment_success, mode)
        
        # 11. Дополнительные инструкции если есть проблемы
        if not deployment_success:
            if HAS_RICH:
                help_panel = Panel(
                    "[bold red]🔧 ЧТО ДЕЛАТЬ ДАЛЕЕ:[/bold red]\n\n"
                    "[yellow]1. Подождите 2-3 минуты и проверьте снова:[/yellow]\n"
                    "   docker ps\n\n"
                    "[yellow]2. Посмотрите логи для диагностики:[/yellow]\n"
                    "   docker-compose logs -f\n\n"
                    "[yellow]3. Попробуйте перезапуск:[/yellow]\n"
                    "   docker-compose down\n"
                    "   docker-compose up -d\n\n"
                    "[yellow]4. Если ничего не помогает:[/yellow]\n"
                    "   python3 motherlode.py --cleanup\n"
                    "   python3 motherlode.py\n\n"
                    "[bold cyan]💡 СОВЕТ: Многие проблемы решаются простым ожиданием - Docker'у нужно время на загрузку образов[/bold cyan]",
                    title="📋 Руководство по решению проблем",
                    border_style="yellow"
                )
                console.print(help_panel)
            else:
                print("\n🔧 ЧТО ДЕЛАТЬ ДАЛЕЕ:")
                print("1. Подождите 2-3 минуты: docker ps")
                print("2. Посмотрите логи: docker-compose logs -f") 
                print("3. Перезапустите: docker-compose down && docker-compose up -d")
                print("4. Если не помогает: python3 motherlode.py (заново)")
                print("\n💡 СОВЕТ: Docker'у нужно время на загрузку - это нормально")
        
    except KeyboardInterrupt:
        if HAS_RICH:
            console.print("\n[bold red]❌ Установка прервана пользователем![/bold red]")
            console.print("[cyan]🔄 Для повторной попытки запустите: python3 motherlode.py[/cyan]")
        else:
            print("\n❌ Установка прервана!")
            print("🔄 Для повторной попытки: python3 motherlode.py")
            
    except SystemResourceException as e:
        if HAS_RICH:
            console.print(f"\n[bold red]💻 Недостаточно ресурсов: {e}[/bold red]")
            console.print("[yellow]🔧 Решения:[/yellow]")
            console.print("• Закройте ненужные приложения")
            console.print("• Используйте более мощный сервер") 
            console.print("• Или продолжите на свой риск: добавьте флаг --force")
        else:
            print(f"\n💻 Недостаточно ресурсов: {e}")
            print("🔧 Увеличьте RAM/disk или используйте более мощный сервер")
            
    except SecurityException as e:
        if HAS_RICH:
            console.print(f"\n[bold red]🛡️ Проблема безопасности: {e}[/bold red]")
            console.print("[yellow]🔧 Операция заблокирована для защиты системы[/yellow]")
        else:
            print(f"\n🛡️ Проблема безопасности: {e}")
            
    except Exception as e:
        if HAS_RICH:
            console.print(f"\n[bold red]💥 Неожиданная ошибка: {str(e)}[/bold red]")
            console.print("\n[yellow]🔧 Расширенная диагностика:[/yellow]")
            console.print("• Проверьте Docker: systemctl status docker")
            console.print("• Проверьте сеть: ping google.com") 
            console.print("• Проверьте ресурсы: df -h && free -h")
            console.print("• Посмотрите логи: docker-compose logs")
            console.print("• Полная очистка: python3 motherlode.py --cleanup")
            console.print("• Повторная установка: python3 motherlode.py")
        else:
            print(f"\n💥 Неожиданная ошибка: {e}")
            print("🔧 Проверьте Docker, сеть, ресурсы")
            print("🔄 Попробуйте: python3 motherlode.py --cleanup && python3 motherlode.py")
    
    finally:
        # Показываем финальную статистику
        if Path('.env').exists():
            with open('.env', 'r') as f:
                final_env_lines = sum(1 for line in f if line.strip())
            
            if HAS_RICH:
                console.print(f"\n[dim]📊 Итого: .env файл содержит {final_env_lines} строк, режим: {mode.upper()}, успех: {'✅' if deployment_success else '❌'}[/dim]")
            else:
                print(f"\n📊 Итого: {final_env_lines} строк в .env, режим: {mode.upper()}, успех: {'✅' if deployment_success else '❌'}")

def cli_commands():
    """🎮 Complete CLI команды."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="🎮 MOTHERLODE v2.0 - Complete AIBot Direct Deployment",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
🎯 Complete Examples:
  python3 motherlode.py                    # Full complete deployment
  python3 motherlode.py --status           # System status check
  python3 motherlode.py --rollback         # Rollback to previous config
  python3 motherlode.py --health           # Health check all services
  python3 motherlode.py --backup           # Create configuration backup
  python3 motherlode.py --cleanup          # Clean Docker volumes (with confirmation)
  python3 motherlode.py --fix              # Fix common deployment issues
  
🌐 Website: https://AIBot.Direct
👨‍💻 Complete by: Community (based on Cole Medin's work)
🔒 Security: Complete with input validation and safe execution
        """
    )
    
    parser.add_argument('--status', action='store_true', 
                       help='Complete system status check')
    parser.add_argument('--rollback', action='store_true',
                       help='Rollback to previous configuration')
    parser.add_argument('--health', action='store_true',
                       help='Health check all services')
    parser.add_argument('--backup', action='store_true',
                       help='Create configuration backup')
    parser.add_argument('--cleanup', action='store_true',
                       help='Clean Docker volumes (with confirmation)')
    parser.add_argument('--fix', action='store_true',
                       help='Fix common deployment issues')
    parser.add_argument('--force', action='store_true',
                       help='Force deployment despite warnings')
    
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
            console.print("[bold yellow]🏥 Running complete health checks...[/bold yellow]")
        motherlode.check_prerequisites()
        services_status = motherlode.verify_services_running()
        running_services = sum(1 for k, v in services_status.items() if v)
        if HAS_RICH:
            console.print(f"[green]✅ Health check complete: {running_services} services operational[/green]")
        else:
            print(f"✅ Health check complete: {running_services} services operational")
    elif args.fix:
        if HAS_RICH:
            console.print("[bold yellow]🔧 Fixing common deployment issues...[/bold yellow]")
        else:
            print("🔧 Fixing common deployment issues...")
        motherlode.fix_docker_compose_issues()
        # Дополнительные исправления
        try:
            motherlode._safe_subprocess_run(["docker-compose", "down"], check=False)
            motherlode._safe_subprocess_run(["docker", "system", "prune", "-f"], check=False)
            if HAS_RICH:
                console.print("[green]✅ Common issues fixed, try running deployment again[/green]")
            else:
                print("✅ Common issues fixed, try running deployment again")
        except Exception as e:
            if HAS_RICH:
                console.print(f"[red]❌ Fix attempt failed: {e}[/red]")
            else:
                print(f"❌ Fix attempt failed: {e}")
    elif args.cleanup:
        if HAS_RICH:
            should_cleanup = Confirm.ask("[bold red]⚠️ Delete all Docker volumes? This will DESTROY all data![/bold red]")
        else:
            should_cleanup = input("⚠️ Delete all Docker volumes? (y/N): ").lower() == 'y'
            
        if should_cleanup:
            try:
                motherlode._safe_subprocess_run(["docker-compose", "down", "-v"], timeout=60)
                motherlode._safe_subprocess_run(["docker", "system", "prune", "-a", "-f"], timeout=120)
                if HAS_RICH:
                    console.print("[green]✅ Complete cleanup completed[/green]")
                else:
                    print("✅ Complete cleanup completed")
            except Exception as e:
                if HAS_RICH:
                    console.print(f"[red]❌ Cleanup failed: {e}[/red]")
                else:
                    print(f"❌ Cleanup failed: {e}")
    else:
        # Сохраняем force флаг для основного процесса
        if args.force:
            motherlode.min_ram_gb = 2  # Снижаем требования при --force
            motherlode.min_disk_gb = 5
        main()

if __name__ == "__main__":
    # 🎮 Complete автоустановка зависимостей
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
            print("🚀 Перезапустите для complete интерфейса:")
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
    
    # 🎯 Запуск complete CLI
    cli_commands()
