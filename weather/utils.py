import requests

def get_weather(lat, lon):
    api_key = '7cf04ab4aae387708bf059e52db99cf8'
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=ru"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Ответ от OpenWeather:", data) 
        rain_status = data.get('rain', {}).get('1h', 0) 
        snow_status = data.get('snow', {}).get('1h', 0)
        
        data['rain_status'] = rain_status
        data['snow_status'] = snow_status
        
        return data
    else:
        return {"error": f"Не удалось получить данные о погоде. Код ошибки: {response.status_code}"}
