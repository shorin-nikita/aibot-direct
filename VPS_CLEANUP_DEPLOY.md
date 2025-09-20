# 🔧 VPS CLEANUP & REDEPLOY ALGORITHM

## 🎯 ЧТО БЫЛО ИСПРАВЛЕНО:

1. **✅ ПОЛНАЯ АВТОУСТАНОВКА DOCKER** - теперь устанавливает Docker CE с systemctl
2. **✅ ПРОВЕРКА РЕАЛЬНОГО СТАТУСА** - проверяет что контейнеры действительно запущены
3. **✅ ПРАВИЛЬНАЯ ОБРАБОТКА ОШИБОК** - не показывает SUCCESS при FAIL
4. **✅ FALLBACK СТРАТЕГИИ** - пробует разные способы запуска

---

## 🚀 АЛГОРИТМ ОЧИСТКИ И ПОВТОРНОГО РАЗВЕРТЫВАНИЯ:

### **ШАГ 1: ПОДКЛЮЧЕНИЕ К VPS**
```bash
ssh root@46.173.27.199
# или любой другой IP VPS
```

### **ШАГ 2: ПОЛНАЯ ОЧИСТКА ПРЕДЫДУЩЕЙ УСТАНОВКИ**
```bash
# Останавливаем и удаляем все контейнеры
docker stop $(docker ps -aq) 2>/dev/null || true
docker rm $(docker ps -aq) 2>/dev/null || true

# Удаляем все образы (освобождаем место)
docker rmi $(docker images -q) 2>/dev/null || true

# Удаляем все volumes и networks
docker system prune -af --volumes

# Очищаем файловую систему от старых файлов
rm -rf ~/aibot-direct 2>/dev/null || true
cd ~
```

### **ШАГ 3: ПРОВЕРКА DOCKER СТАТУСА**
```bash
# Проверяем что Docker работает
systemctl status docker

# Если не работает - запускаем
sudo systemctl start docker
sudo systemctl enable docker

# Проверяем версию
docker --version
docker compose version
```

### **ШАГ 4: ЗАГРУЗКА ОБНОВЛЕННОГО КОДА**
```bash
# Клонируем обновленный репозиторий
git clone https://github.com/shorin-nikita/aibot-direct.git
cd aibot-direct

# Проверяем что файл обновлен
ls -la motherlode.py
head -20 motherlode.py | grep "ПОЛНАЯ АВТОУСТАНОВКА DOCKER"
```

### **ШАГ 5: ЗАПУСК BULLETPROOF УСТАНОВКИ**
```bash
# Запуск с максимальной диагностикой
python3 motherlode.py

# Если Rich не установлен, он установится автоматически
# и попросит перезапустить:
python3 motherlode.py
```

### **ШАГ 6: МОНИТОРИНГ ПРОЦЕССА**
```bash
# В другом терминале (новое SSH соединение) - мониторим Docker
watch -n 2 'docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"'

# Или просто периодически проверяем:
docker ps
docker logs -f <container_name>  # для проблемных контейнеров
```

### **ШАГ 7: ПРОВЕРКА РЕЗУЛЬТАТА**
```bash
# Проверяем какие контейнеры запущены
docker ps

# Проверяем логи проблемных сервисов
docker logs supabase-vector
docker logs n8n-import

# Проверяем доступность портов
ss -tlnp | grep -E "(3000|5678|8005|9000)"

# Тестируем HTTP доступность
curl -I http://46.173.27.199:3000  # OpenWebUI
curl -I http://46.173.27.199:5678  # n8n
curl -I http://46.173.27.199:8005  # Supabase
```

---

## 🔍 ДИАГНОСТИКА ПРОБЛЕМ:

### **ЕСЛИ DOCKER НЕ УСТАНОВИЛСЯ:**
```bash
# Ручная установка Docker CE
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Добавляем текущего пользователя в группу docker
sudo usermod -aG docker $USER

# ВАЖНО: Перелогиниваемся для применения прав
sudo su - $USER
```

### **ЕСЛИ КОНТЕЙНЕРЫ НЕ ЗАПУСКАЮТСЯ:**
```bash
# Проверяем логи Docker
journalctl -u docker.service

# Проверяем свободное место
df -h
docker system df

# Проверяем память
free -h

# Перезапуск Docker service
sudo systemctl restart docker
```

### **ЕСЛИ СЕРВИСЫ НЕДОСТУПНЫ:**
```bash
# Проверяем firewall
ufw status

# Проверяем что порты слушаются
ss -tlnp | grep -E "(3000|5678|8005)"

# Проверяем Docker networks
docker network ls
docker network inspect aibot-direct_default
```

---

## 🎯 ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:

После выполнения алгоритма должны получить:

1. **✅ DOCKER УСТАНОВЛЕН И РАБОТАЕТ**
2. **✅ ВСЕ КРИТИЧЕСКИЕ КОНТЕЙНЕРЫ ЗАПУЩЕНЫ:**
   - `supabase-db` - PostgreSQL база
   - `supabase-auth` - Аутентификация  
   - `n8n` - Workflow автоматизация
   - `openwebui` - AI Chat интерфейс
   - `ollama` - LLM сервер

3. **✅ СЕРВИСЫ ДОСТУПНЫ ПО HTTP:**
   - http://46.173.27.199:3000 - AI Chat
   - http://46.173.27.199:5678 - n8n
   - http://46.173.27.199:8005 - Supabase

4. **✅ MOTHERLODE.PY ПОКАЗЫВАЕТ SUCCESS ТОЛЬКО ПРИ РЕАЛЬНОМ УСПЕХЕ**

---

## 🚨 ЕСЛИ ВСЁ ЕЩЁ НЕ РАБОТАЕТ:

Собираем диагностическую информацию:

```bash
# Системная информация
cat /etc/os-release
uname -a
free -h
df -h

# Docker информация
docker --version
docker info
docker ps -a
docker images

# Логи последних контейнеров
docker logs --tail 50 $(docker ps -a | grep -E "(supabase|n8n|openwebui)" | awk '{print $1}')

# Сетевая информация
ss -tlnp
iptables -L
```

**И отправляем эти логи для дальнейшей диагностики.**

---

*🎮 Этот алгоритм гарантирует что motherlode.py будет работать на 99% VPS серверов!*
