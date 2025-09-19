#!/usr/bin/env python3
"""
setup_gui.py - Web GUI для motherlode.py

Простой веб-интерфейс для нулевой конфигурации AIBot Direct
"""

import json
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import webbrowser

# Импортируем функции из motherlode
try:
    from motherlode import (
        detect_environment, 
        generate_smart_config, 
        generate_env_file,
        run_integrated_start_services,
        check_and_display_results
    )
except ImportError:
    print("❌ Не удалось импортировать motherlode.py")
    print("💡 Убедитесь, что файл setup_gui.py в той же папке что и motherlode.py")
    sys.exit(1)

class SetupHandler(BaseHTTPRequestHandler):
    """Обработчик HTTP запросов для GUI."""
    
    def do_GET(self):
        """Обработка GET запросов."""
        if self.path == '/':
            self.serve_main_page()
        elif self.path == '/api/environment':
            self.serve_environment_info()
        elif self.path == '/api/status':
            self.serve_status()
        elif self.path.startswith('/static/'):
            self.serve_static_file()
        else:
            self.send_error(404)
    
    def do_POST(self):
        """Обработка POST запросов."""
        if self.path == '/api/setup':
            self.handle_setup()
        else:
            self.send_error(404)
    
    def serve_main_page(self):
        """Отдача главной страницы."""
        html_content = self.get_main_html()
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))
    
    def serve_environment_info(self):
        """API для получения информации об окружении."""
        try:
            env_info = detect_environment()
            config = generate_smart_config(env_info)
            
            response = {
                'environment': env_info,
                'config': {
                    'type': config['environment'],
                    'profile': config['profile'],
                    'mode': config['mode'],
                    'domains': config['domains']
                }
            }
            
            self.send_json_response(response)
        except Exception as e:
            self.send_error_response(str(e))
    
    def handle_setup(self):
        """Обработка запуска установки."""
        try:
            # Получаем данные
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # Запускаем установку в отдельном потоке
            setup_thread = threading.Thread(target=self.run_setup_process, args=(data,))
            setup_thread.daemon = True
            setup_thread.start()
            
            self.send_json_response({'status': 'started', 'message': 'Установка запущена'})
            
        except Exception as e:
            self.send_error_response(str(e))
    
    def run_setup_process(self, config_data):
        """Запуск процесса установки."""
        global setup_status
        
        try:
            setup_status = {'step': 1, 'message': 'Определение окружения...', 'progress': 20}
            env_info = detect_environment()
            
            setup_status = {'step': 2, 'message': 'Генерация конфигурации...', 'progress': 40}
            config = generate_smart_config(env_info)
            
            # Применяем пользовательские настройки
            if 'use_domains' in config_data and config_data['use_domains']:
                config['domains'].update(config_data.get('domains', {}))
            
            setup_status = {'step': 3, 'message': 'Создание .env файла...', 'progress': 60}
            generate_env_file(config)
            
            setup_status = {'step': 4, 'message': 'Запуск сервисов...', 'progress': 80}
            success = run_integrated_start_services(env_info, config)
            
            setup_status = {'step': 5, 'message': 'Проверка результатов...', 'progress': 100}
            if success:
                check_and_display_results(env_info, config)
                setup_status['status'] = 'success'
                setup_status['message'] = 'Установка завершена успешно!'
            else:
                setup_status['status'] = 'error'
                setup_status['message'] = 'Установка завершена с ошибками'
                
        except Exception as e:
            setup_status = {
                'status': 'error',
                'message': f'Ошибка установки: {str(e)}',
                'progress': 0
            }
    
    def serve_status(self):
        """API для получения статуса установки."""
        global setup_status
        self.send_json_response(setup_status)
    
    def send_json_response(self, data):
        """Отправка JSON ответа."""
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
    
    def send_error_response(self, error_message):
        """Отправка ошибки."""
        self.send_response(500)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        error_data = {'error': error_message}
        self.wfile.write(json.dumps(error_data, ensure_ascii=False).encode('utf-8'))
    
    def get_main_html(self):
        """HTML код главной страницы."""
        return """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🤖 AIBot Direct - Установка</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.2);
        }
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        .header h1 {
            font-size: 2.5em;
            margin: 0;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .env-info {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 30px;
            border-left: 5px solid #667eea;
        }
        .env-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }
        .env-label {
            font-weight: 600;
            color: #555;
        }
        .env-value {
            font-family: 'Monaco', 'Menlo', monospace;
            background: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.9em;
        }
        .config-section {
            margin-bottom: 30px;
        }
        .config-title {
            font-size: 1.3em;
            font-weight: 600;
            margin-bottom: 15px;
            color: #444;
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: #555;
        }
        .form-input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        .form-input:focus {
            outline: none;
            border-color: #667eea;
        }
        .form-checkbox {
            margin-right: 10px;
        }
        .domains-section {
            background: #f0f8ff;
            padding: 20px;
            border-radius: 10px;
            border: 2px dashed #667eea;
            display: none;
        }
        .domains-section.show {
            display: block;
        }
        .btn {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 50px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
            width: 100%;
            margin-top: 20px;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        }
        .btn:disabled {
            background: #ccc;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }
        .progress-section {
            display: none;
            margin-top: 30px;
        }
        .progress-bar {
            width: 100%;
            height: 8px;
            background: #e0e0e0;
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 15px;
        }
        .progress-fill {
            height: 100%;
            background: linear-gradient(45deg, #667eea, #764ba2);
            transition: width 0.5s ease;
            width: 0%;
        }
        .progress-message {
            text-align: center;
            font-weight: 500;
            color: #555;
        }
        .status-success {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }
        .status-error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }
        .service-links {
            display: none;
            margin-top: 20px;
        }
        .service-link {
            display: block;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 8px;
            margin-bottom: 10px;
            text-decoration: none;
            color: #667eea;
            font-weight: 500;
            transition: background 0.3s;
        }
        .service-link:hover {
            background: #e9ecef;
        }
        .flag {
            display: inline-block;
            margin-right: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><span class="flag">🤖</span>AIBot Direct</h1>
            <p><span class="flag">🇷🇺</span><strong>НУЛЕВАЯ КОНФИГУРАЦИЯ</strong> - AI система готова за 3 минуты!</p>
        </div>

        <div class="env-info" id="envInfo">
            <h3>🔍 Анализ окружения...</h3>
            <p>Определяем оптимальные настройки для вашей системы</p>
        </div>

        <div class="config-section">
            <div class="config-title">⚙️ Настройки развертывания</div>
            
            <div class="form-group">
                <label class="form-label">
                    <input type="checkbox" class="form-checkbox" id="useDomainsCheck" onchange="toggleDomains()">
                    Настроить домены для публичного доступа
                </label>
            </div>

            <div class="domains-section" id="domainsSection">
                <div class="form-group">
                    <label class="form-label" for="baseDomain">Базовый домен:</label>
                    <input type="text" class="form-input" id="baseDomain" placeholder="yourdomain.com">
                    <small>Будут автоматически созданы поддомены: ai.yourdomain.com, n8n.yourdomain.com и т.д.</small>
                </div>
                
                <div class="form-group">
                    <label class="form-label" for="email">Email для SSL сертификатов:</label>
                    <input type="email" class="form-input" id="email" placeholder="admin@yourdomain.com">
                </div>
            </div>
        </div>

        <button class="btn" id="setupBtn" onclick="startSetup()">
            🚀 Запустить AI экосистему!
        </button>

        <div class="progress-section" id="progressSection">
            <div class="progress-bar">
                <div class="progress-fill" id="progressFill"></div>
            </div>
            <div class="progress-message" id="progressMessage">Подготовка к запуску...</div>
        </div>

        <div id="statusMessage"></div>

        <div class="service-links" id="serviceLinks">
            <h3>🌐 Доступные сервисы:</h3>
            <a href="http://localhost:3000" class="service-link" target="_blank">
                🤖 Open WebUI (Alenushka) - ваша AI помощница
            </a>
            <a href="http://localhost:5678" class="service-link" target="_blank">
                ⚙️ n8n Automation - автоматизация бизнеса
            </a>
            <a href="http://localhost:8003" class="service-link" target="_blank">
                🔧 Flowise AI Builder - конструктор AI агентов
            </a>
            <a href="http://localhost:8005" class="service-link" target="_blank">
                🗄️ Supabase Dashboard - база данных
            </a>
        </div>
    </div>

    <script>
        let setupInProgress = false;

        // Загрузка информации об окружении при старте
        window.onload = function() {
            loadEnvironmentInfo();
        };

        function loadEnvironmentInfo() {
            fetch('/api/environment')
                .then(response => response.json())
                .then(data => {
                    displayEnvironmentInfo(data);
                })
                .catch(error => {
                    console.error('Ошибка загрузки окружения:', error);
                    document.getElementById('envInfo').innerHTML = 
                        '<h3>❌ Ошибка загрузки</h3><p>Не удалось определить окружение</p>';
                });
        }

        function displayEnvironmentInfo(data) {
            const env = data.environment;
            const config = data.config;
            
            const envHtml = `
                <h3>✅ Окружение определено</h3>
                <div class="env-item">
                    <span class="env-label">🖥️ Тип:</span>
                    <span class="env-value">${env.type.toUpperCase()}</span>
                </div>
                <div class="env-item">
                    <span class="env-label">🌐 IP:</span>
                    <span class="env-value">${env.ip}</span>
                </div>
                <div class="env-item">
                    <span class="env-label">🧠 CPU:</span>
                    <span class="env-value">${env.cpu_count} cores</span>
                </div>
                <div class="env-item">
                    <span class="env-label">💾 RAM:</span>
                    <span class="env-value">${env.memory_gb} GB</span>
                </div>
                <div class="env-item">
                    <span class="env-label">🐳 Docker:</span>
                    <span class="env-value">${env.has_docker ? '✅ Установлен' : '❌ Не найден'}</span>
                </div>
                <div class="env-item">
                    <span class="env-label">🚀 Профиль:</span>
                    <span class="env-value">${config.profile.toUpperCase()}</span>
                </div>
            `;
            
            document.getElementById('envInfo').innerHTML = envHtml;

            // Если localhost, скрыть опцию доменов
            if (env.type === 'localhost') {
                document.getElementById('useDomainsCheck').parentElement.style.display = 'none';
            }

            // Если нет Docker, отключить кнопку
            if (!env.has_docker) {
                const btn = document.getElementById('setupBtn');
                btn.disabled = true;
                btn.textContent = '❌ Установите Docker для продолжения';
            }
        }

        function toggleDomains() {
            const checkbox = document.getElementById('useDomainsCheck');
            const domainsSection = document.getElementById('domainsSection');
            
            if (checkbox.checked) {
                domainsSection.classList.add('show');
            } else {
                domainsSection.classList.remove('show');
            }
        }

        function startSetup() {
            if (setupInProgress) return;
            
            setupInProgress = true;
            const btn = document.getElementById('setupBtn');
            btn.disabled = true;
            btn.textContent = '⏳ Установка...';
            
            document.getElementById('progressSection').style.display = 'block';
            
            const setupData = {
                use_domains: document.getElementById('useDomainsCheck').checked,
                base_domain: document.getElementById('baseDomain').value,
                email: document.getElementById('email').value
            };
            
            fetch('/api/setup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(setupData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'started') {
                    monitorProgress();
                } else {
                    showError('Не удалось запустить установку: ' + data.message);
                }
            })
            .catch(error => {
                showError('Ошибка запуска: ' + error.message);
            });
        }

        function monitorProgress() {
            const interval = setInterval(() => {
                fetch('/api/status')
                    .then(response => response.json())
                    .then(data => {
                        updateProgress(data);
                        
                        if (data.status === 'success') {
                            clearInterval(interval);
                            showSuccess();
                        } else if (data.status === 'error') {
                            clearInterval(interval);
                            showError(data.message);
                        }
                    })
                    .catch(error => {
                        console.error('Ошибка мониторинга:', error);
                    });
            }, 2000);
        }

        function updateProgress(data) {
            const progressFill = document.getElementById('progressFill');
            const progressMessage = document.getElementById('progressMessage');
            
            if (data.progress) {
                progressFill.style.width = data.progress + '%';
            }
            
            if (data.message) {
                progressMessage.textContent = data.message;
            }
        }

        function showSuccess() {
            const statusDiv = document.getElementById('statusMessage');
            statusDiv.innerHTML = `
                <div class="status-success">
                    <h3>🎉 Установка завершена успешно!</h3>
                    <p>Ваша AI экосистема AIBot Direct готова к работе!</p>
                </div>
            `;
            
            document.getElementById('serviceLinks').style.display = 'block';
            
            const btn = document.getElementById('setupBtn');
            btn.textContent = '✅ Установка завершена';
            btn.style.background = '#28a745';
        }

        function showError(message) {
            const statusDiv = document.getElementById('statusMessage');
            statusDiv.innerHTML = `
                <div class="status-error">
                    <h3>❌ Ошибка установки</h3>
                    <p>${message}</p>
                    <p><strong>Выполните в терминале:</strong></p>
                    <code>python3 diagnose.py</code>
                </div>
            `;
            
            const btn = document.getElementById('setupBtn');
            btn.disabled = false;
            btn.textContent = '🔄 Повторить установку';
            setupInProgress = false;
        }
    </script>
</body>
</html>
        """

# Глобальная переменная для статуса установки
setup_status = {'message': 'Готов к установке', 'progress': 0}

def start_server(port=8080):
    """Запуск веб-сервера."""
    try:
        server = HTTPServer(('localhost', port), SetupHandler)
        print(f"🌐 GUI доступен по адресу: http://localhost:{port}")
        print("🚀 Откройте браузер для графической установки")
        
        # Автоматически открыть браузер
        threading.Timer(1.0, lambda: webbrowser.open(f'http://localhost:{port}')).start()
        
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Сервер остановлен")
    except OSError as e:
        if e.errno == 48:  # Port already in use
            print(f"❌ Порт {port} уже занят. Попробуйте другой порт:")
            print(f"   python3 setup_gui.py --port {port + 1}")
        else:
            print(f"❌ Ошибка сервера: {e}")

def main():
    """Главная функция."""
    import argparse
    
    parser = argparse.ArgumentParser(description='AIBot Direct GUI Setup')
    parser.add_argument('--port', type=int, default=8080, help='Port for web interface (default: 8080)')
    args = parser.parse_args()
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          🤖 AIBot Direct - Графический интерфейс             ║
║                                                              ║
║               Нулевая конфигурация в браузере                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    start_server(args.port)

if __name__ == "__main__":
    main()
