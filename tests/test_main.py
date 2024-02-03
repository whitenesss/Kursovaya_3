from src.function import data_cek, transaction_data, checking_cards_from, checking_cards_to, print_display_to_user
import json


def test_data_cek():
    assert data_cek(1) == ['2019-12-08T22:46:21.935582']
    assert data_cek(2) == ['2019-12-08T22:46:21.935582', '2019-12-07T06:17:14.634890']


def test_transaction_data():
    assert transaction_data() == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
                                   'operationAmount': {'amount': '41096.24',
                                                       'currency': {'name': 'USD', 'code': 'USD'}},
                                   'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
                                  {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725',
                                   'operationAmount': {'amount': '21344.35',
                                                       'currency': {'name': 'руб.', 'code': 'RUB'}},
                                   'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'},
                                  {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
                                   'operationAmount': {'amount': '30153.72',
                                                       'currency': {'name': 'руб.', 'code': 'RUB'}},
                                   'description': 'Перевод организации', 'from': 'Maestro 7810846596785568',
                                   'to': 'Счет 43241152692663622869'},
                                  {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
                                   'operationAmount': {'amount': '48150.39',
                                                       'currency': {'name': 'USD', 'code': 'USD'}},
                                   'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
                                   'to': 'Счет 35158586384610753655'},
                                  {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
                                   'operationAmount': {'amount': '62814.53',
                                                       'currency': {'name': 'руб.', 'code': 'RUB'}},
                                   'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794',
                                   'to': 'Счет 46765464282437878125'}]


def test_checking_cards_from():
    assert checking_cards_from(transaction_data(5)[4]) == ('Счет', '38611 4**** ***** *9794')
    assert checking_cards_from(transaction_data(5)[1]) == 'отсутствует'
    assert checking_cards_from(transaction_data(5)[2]) == ('Maestro', '7810 84** **** 5568')
    assert checking_cards_from(transaction_data(5)[3]) == ('Visa', 'Classic', '2842 87** **** 9012')


def test_checking_cards_to():
    assert checking_cards_to(transaction_data(10)[6]) == ('МИР', '**7301')
    assert checking_cards_to(transaction_data(5)[3]) == ('Счет', '**3655')
