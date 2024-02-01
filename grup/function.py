import datetime
import json


def json_file_print():
    '''
    reading json file
    '''
    with open('operations.json', 'r', encoding="utf-8") as file:
        templates = json.load(file)
        return templates


def data_cek(a=5):
    '''
    getting date sorted
    '''
    data = []
    for day_namber in json_file_print():
        if day_namber == {}:
            continue
        if day_namber['state'] == 'EXECUTED':
            data.append(day_namber['date'])
    data = sorted(data, reverse=True)
    return data[:a]

def transaction_data(kol_vo=5):
    '''
    collection of transaction data of the selected amount
    '''
    tran = []
    b = 0
    for a in json_file_print():
        if a == {}:
            continue
        if a['date'] in data_cek(kol_vo):
            # print('нашли', a['date'], data_cek())
            b += 1
            tran.append(a)
    return tran




ewq = transaction_data(2)[0]
tre = transaction_data(2)[1]
#
# print(ewq)
# print(tre['from'])
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
            private_number1 = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
            chunks, chunk_size = len(private_number1), len(private_number1) // 4
            private_number = " ".join([private_number1[i:i + chunk_size] for i in range(0, chunks, chunk_size)])
            return *card_name, private_number
    return "отсутствует"

def checking_cards_to(kol_v):

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
    dat = transaction_data(kolvo)[iter]['date']
    translation_description = transaction_data(kolvo)[iter]['description']

    dat = dat[0:10].split("-")
    print(f'{dat[2]}.{dat[1]}.{dat[0]} {translation_description}')
    print(*checking_cards_from(transaction_data(kolvo)[iter]), '->', *checking_cards_to(transaction_data(kolvo)[iter]))
    print(f"{transaction_data(kolvo)[iter]['operationAmount']['amount']}"
          f"{transaction_data(kolvo)[iter]['operationAmount']['currency']['name']}")


