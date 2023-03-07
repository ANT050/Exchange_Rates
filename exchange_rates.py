import requests

api_key = "YOUR_API_KEY"
symbols = "USD,RUB,EUR,CNY,TRY,GBP,CHF,JPY,AED,HKD,SGD"

#Функция получения курса валют
def get_exchange_rates(api_key: str, symbols: str):
  
    # Формирование URL для получения котировок
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&symbols={symbols}"

    try:
        # Выполнение запроса к API
        request = requests.get(url)

        # Проверка корректности ответа
        if request.status_code == 200 and request.content:
          
            # Получение ответа в формате JSON
            received_response = request.json()

            # Извлечение нужных котировок и вывод на экран
            for currency in ["USD", "EUR", "CNY", "TRY", "GBP", "CHF", "JPY", "AED", "HKD", "SGD"]:
                try:
                    exchange_rate = received_response["rates"]["RUB"] / received_response["rates"][currency]
                    print(f"{currency}/RUB: {exchange_rate:.4f}")
                except KeyError:
                    print(f"{currency}/RUB: котировка отсутствует")

            print()

            for currency in ["EUR", "GBP"]:
                try:
                    exchange_rate = received_response["rates"]["USD"] / received_response["rates"][currency]
                    print(f"{currency}/USD: {exchange_rate:.4f}")
                except KeyError:
                    print(f"{currency}/RUB: котировка отсутствует")

            for currency in ["CHF", "CNY", "TRY", "JPY", "HKD", "SGD", "AED"]:
                try:
                    exchange_rate = received_response["rates"][currency] / received_response["rates"]["USD"]
                    print(f"USD/{currency}: {exchange_rate:.4f}")
                except KeyError:
                    print(f"{currency}/RUB: котировка отсутствует")

        else:
            print("\nОшибка при получении котировок")

    except requests.exceptions.ConnectionError:
        print("Отсутствует связь с сервисом по предоставлению валютных котировок")

get_exchange_rates(api_key, symbols)