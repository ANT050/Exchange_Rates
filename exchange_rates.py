import requests

# Получение API ключа
api_key = "YOUR_API_KEY"

# Формирование URL для получения котировок
url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&symbols=USD,RUB,EUR,CNY,TRY,GBP,CHF,JPY,AED,HKD,SGD"

# Выполнение запроса к API
request = requests.get(url)

# Получение ответа в формате JSON
received_response = request.json()

# Извлечение нужных котировок и вывод на экран
for currency in ["USD", "EUR", "CNY", "TRY", "GBP", "CHF", "JPY", "AED", "HKD", "SGD"]:
    exchange_rate = received_response["rates"]["RUB"] / received_response["rates"][currency]
    print(f"{currency}/RUB: {exchange_rate:.4f}")