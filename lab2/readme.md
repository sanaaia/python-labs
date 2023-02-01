# Телеграм-бот

Телеграм-бот имеет следующие команды:

* `/hello` — приветствует пользователя по имени
```
/hello
Привет @User
```
* `/time` — возвращает текущую дату и время в удобном формате
```
/time
Сейчас 15:25, 7 марта 2022 года
```
* `/binom <N> <K>` — вычисляет биномиальный коэффициент для N по K
```
/binom 4 2
Binom(4,2) = 6
```
* `/cat` — показывает картинку случайного кода ошибки HTTP с сайта https://http.cat/
* `/weather <latitude> <longitude>` — дает данные о текущей погоде (только в США) с сайта https://www.weather.gov/documentation/services-web-api
```
/weather 40.730610 -73.935242
Сейчас: Mostly sunny (49°F)
```

## Запуск

1. Запросите бота [@botfather](https://t.me/botfather) о создании бота, сохраните 
токен вашего бота в файле `token`

```
echo <my-token> >> token
```
2. Создайте и активируйте виртуальное окружение, установите зависимости:
```
python -m venv venv
venv\scripts\activate.bat
pip install -r requirements.txt
```
3. Запустите телеграм-бота
```
python bot.py
```