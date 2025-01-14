# weather/notification/utils.py
from firebase_admin import messaging
from weather.utils import get_weather
from weather.models import User

def send_push_notification(token, title, body):
    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            token=token,
        )
        response = messaging.send(message)
        print(f"Уведомление отправлено: {response}")
    except Exception as e:
        print(f"Ошибка при отправке уведомления: {e}")

def notify_users():
    users = User.objects.filter(fcm_token__isnull=False, notifications_enabled=True)  # Выбираем пользователей с токеном и включенными уведомлениями
    for user in users:
        weather = get_weather(user.location)  # Получаем погоду для местоположения пользователя
        if weather.get("rain"):
            send_push_notification(
                token=user.fcm_token,
                title="Погода",
                body="Возьми зонтик!",
            )
