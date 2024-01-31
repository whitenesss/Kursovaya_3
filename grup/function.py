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




print(*transaction_data(2))
qwe = transaction_data(2)[0]['operationAmount']['amount']
print(qwe)



#
# # def print_display_to_user():
# print(transaction_data(2)[0]['date'])
# dat = transaction_data(2)[0]['date']
# translation_description = transaction_data(2)[0]['description']
#
# dat = dat[0:10].split("-")
# print(f'{dat[2]}.{dat[1]}.{dat[0]} {translation_description}')




