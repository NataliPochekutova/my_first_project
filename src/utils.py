import json
from json import JSONDecodeError


def get_financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, encoding="utf-8") as file:
            try:
                transactions = json.load(file)
                return transactions
            except JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
