import os

import pytest

from src.utils import get_financial_transactions


@pytest.fixture
def path():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return path_to_file


@pytest.fixture
def path_empty_list():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_1.json")
    return path_to_file


@pytest.fixture
def path_mistake_json():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_2.json")
    return path_to_file


@pytest.fixture
def trans():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
         "amount": "31957.58",
         "currency": {
          "name": "руб.",
          "code": "RUB"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


def test_financial_transactions_nofile():
    assert get_financial_transactions('nofile') == []


def test_financial_transactions(path):
    assert get_financial_transactions(path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
             "name": "руб.",
             "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


def test_financial_transactions_empty_list(path_empty_list):
    assert get_financial_transactions(path_empty_list) == []


def test_financial_transactions_mistake_json(path_mistake_json):
    assert get_financial_transactions(path_mistake_json) == []
