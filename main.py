import requests

def currency_converter():
    print("=== Конвертер валют ===")
    base_currency = input("Введіть базову валюту (наприклад, USD): ").upper()
    target_currency = input("Введіть валюту для конвертації (наприклад, EUR): ").upper()
    amount = float(input("Введіть суму для конвертації: "))

    url = f"https://api.exchangerate.host/convert?from={base_currency}&to={target_currency}&amount={amount}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and "result" in data:
            result = data["result"]
            print(f"{amount} {base_currency} = {result:.2f} {target_currency}")
        else:
            print("Помилка при отриманні даних. Перевірте валюту та спробуйте знову.")
    except Exception as e:
        print("Помилка з'єднання:", e)

if __name__ == "__main__":
    currency_converter()
