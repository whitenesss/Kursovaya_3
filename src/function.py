import datetime
import json
import os
import sys

with open(os.path.join('operations.json'), 'r', encoding="utf-8") as jsonfile:
    templates = json.load(jsonfile)  # read the file json



def data_cek(namber=5):
    '''
    getting date sorted
    '''
    data = []
    for day_namber in templates:
        if day_namber == {}:
            continue
        if day_namber['state'] == 'EXECUTED':
            data.append(day_namber['date'])
            data1 = sorted(data, reverse=True)
    return data1[:namber]


def transaction_data(kol_vo=5):
    '''
    collection of transaction data of the selected amount
    '''
    tran = []
    count_itereit = 0
    for transaction_data in templates:
        if transaction_data == {}:
            continue
        if transaction_data['date'] in data_cek(kol_vo):
            count_itereit += 1
            tran.append(transaction_data)
    return tran


def checking_cards_from(kol_v):
    '''
    We collect the sender's data, card, account, bank name and encrypt
    '''
    if 'from' in kol_v:
        card = kol_v['from']
        card_1 = card.split()
        card_number = card_1[-1]
        if len(card_1) == 3:
            card_name = card_1[0:2]
        elif len(card_1) == 2:
            card_name = card_1[0:1]

        if 16 == len(card_number):
            private_number1 = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
            chunks, chunk_size = len(private_number1), len(private_number1) // 4
            private_number = " ".join([private_number1[i:i + chunk_size] for i in range(0, chunks, chunk_size)])
            return *card_name, private_number
        elif 20 == len(card_number):
            private_number1 = card_number[:10] + (len(card_number[10:-4]) * '*') + card_number[-4:]
            chunks, chunk_size = len(private_number1), len(private_number1) // 5
            private_number = " ".join([private_number1[namber:namber + chunk_size] for namber in range(0, chunks, chunk_size)])
            return *card_name, private_number
    return "отсутствует"


def checking_cards_to(kol_v):
    '''
    We collect the recipient's data and encrypt it
    '''
    if 'to' in kol_v:

        card = kol_v['to']
        card_1 = card.split()
        card_number = card_1[-1]
        if len(card_1) == 3:
            card_name = card_1[0:2]
        elif len(card_1) == 2:
            card_name = card_1[0:1]
        if 16 == len(card_number):
            private_number1 = '**' + card_number[-4:]
            return *card_name, private_number1
        elif 20 == len(card_number):
            private_number1 = '**' + card_number[-4:]
            return *card_name, private_number1
    return "отсутствует"


def print_display_to_user(kolvo=5, iter=None):
    '''
    beautiful output of all information about the transaction
    '''
    dat = transaction_data(kolvo)[iter]['date']
    translation_description = transaction_data(kolvo)[iter]['description']
    dat = dat[0:10].split("-")
    print(f'{dat[2]}.{dat[1]}.{dat[0]} {translation_description}')
    print(*checking_cards_from(transaction_data(kolvo)[iter]), '->', *checking_cards_to(transaction_data(kolvo)[iter]))
    print(f"{transaction_data(kolvo)[iter]['operationAmount']['amount']}"
          f"{transaction_data(kolvo)[iter]['operationAmount']['currency']['name']}")
