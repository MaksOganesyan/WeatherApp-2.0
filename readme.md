# Инструкция по настройке и запуску Django-проекта

Данное руководство описывает шаги по настройке и запуску Django-проекта на другом ПК с возможностью доступа с мобильного устройства.

## Предварительные требования

Перед началом убедитесь, что на целевом ПК установлено следующее программное обеспечение:

- **Python 3.x**
- **Git**
- **Виртуальная среда (`venv`)**

## Инструкции по настройке

### 1. Клонирование репозитория

Склонируйте репозиторий проекта командой:

```bash
git clone <repository-url>
```

Перейдите в каталог проекта:

```bash
cd <project-directory>
```

### 2. Настройка виртуальной среды

Создайте виртуальную среду:

```bash
python -m venv env
```

Активируйте виртуальную среду:

- На **Windows**:
  ```bash
  env\Scripts\activate
  ```
- На **Linux/macOS**:
  ```bash
  source env/bin/activate
  ```

### 3. Установка зависимостей проекта

Установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

### 4. Настройка `ALLOWED_HOSTS`

Откройте файл `settings.py`, расположенный в каталоге проекта, и установите `ALLOWED_HOSTS` для разрешения всех хостов или конкретных IP:

```python
ALLOWED_HOSTS = ['*']
```

Либо укажите IP-адрес ПК:

```python
ALLOWED_HOSTS = ['192.168.x.x']
```

### 5. Применение миграций

Выполните команду для применения миграций базы данных:

```bash
python manage.py migrate
```

### 6. Запуск сервера

Запустите сервер разработки Django, привязав его ко всем сетевым интерфейсам:

```bash
python manage.py runserver 0.0.0.0:8000
```

### 7. Настройка брандмауэра

Убедитесь, что брандмауэр ПК позволяет подключения на порт 8000:

#### Для **Windows**:

1. Откройте **Брандмауэр Защитника Windows**.
2. Перейдите в **Дополнительные параметры**.
3. Создайте новое **правило для входящих подключений**:
   - Выберите **Порт**.
   - Укажите **TCP** и порт **8000**.
   - Разрешите подключение.
   - Назовите правило и завершите настройку.

#### Для **Linux**:

Если используется `ufw`, выполните команды:

```bash
sudo ufw allow 8000
sudo ufw reload
```

### 8. Доступ к серверу с телефона

Найдите локальный IP-адрес ПК:

- На **Windows**:
  ```bash
  ipconfig
  ```
- На **Linux/macOS**:
  ```bash
  ifconfig
  ```

На телефоне откройте браузер и перейдите по адресу:

```plaintext
http://<ip-адрес-пк>:8000
```

Замените `<ip-адрес-пк>` на фактический IP-адрес вашего ПК.

## Примечания

- Убедитесь, что и ПК, и мобильное устройство подключены к одной сети.
- Данная настройка предназначена для разработки. Для продакшн-среды используйте более надёжные серверные настройки и обеспечьте безопасность конфигураций.

---

Следуя этим шагам, вы сможете настроить Django-проект на другом ПК и получить к нему доступ с телефона.
