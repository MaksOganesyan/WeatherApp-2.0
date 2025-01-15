import os
import signal
import webbrowser
from threading import Timer
import subprocess
import time

# Функция для открытия браузера с вашим приложением
def open_browser():
    webbrowser.open("http://localhost:8000")

# Функция для остановки сервера
def stop_server(process):
    print("Stopping the server...")
    process.send_signal(signal.SIGINT)  # Отправляем сигнал SIGINT (для имитации Ctrl+C)

if __name__ == "__main__":
    # Запускаем сервер в отдельном процессе
    process = subprocess.Popen(["python", "manage.py", "runserver", "0.0.0.0:8000"])

    # Даем серверу немного времени для запуска, потом открываем браузер
    Timer(2, open_browser).start()

    try:
        # Ждем определенное время (например, 60 секунд) и затем останавливаем сервер
        time.sleep(10)  # Вы можете установить любое нужное вам время работы
        stop_server(process)  # Останавливаем сервер
    except KeyboardInterrupt:
        # Позволяет вручную остановить сервер с помощью Ctrl+C
        stop_server(process)
        print("\nServer stopped manually.")
