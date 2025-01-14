from django.shortcuts import render, redirect
from .utils import get_weather
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomAuthenticationForm

User = get_user_model()

def index(request):
    return render(request, 'index.html')

def home(request):
    lat = request.GET.get('lat', 55.45)
    lon = request.GET.get('lon', 37.36)

    weather_data = get_weather(lat, lon)

    if 'weather' in weather_data and len(weather_data['weather']) > 0:
        weather_data['weather'][0]['description'] = weather_data['weather'][0]['description'].capitalize()

    if 'main' in weather_data:
        weather_data['main']['temp'] = round(weather_data['main']['temp'])
        weather_data['main']['feels_like'] = round(weather_data['main']['feels_like'])

    if 'wind' in weather_data:
        weather_data['wind']['speed'] = round(weather_data['wind']['speed'])

    message = "Зарегистрируйтесь, чтобы получать уведомления."
    if request.user.is_authenticated:
        rain_status = weather_data.get('rain', {}).get('1h', 0)
        if rain_status > 0:
            message = "Возьмите зонтик!"
        else:
            message = "Сегодня зонт не нужен!"
    return render(request, 'weather/home.html', {'weather': weather_data, 'message': message})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'weather/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'weather/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def toggle_notifications(request):
    user = request.user
    user.notifications_enabled = not user.notifications_enabled
    user.save()
    return redirect('home')
