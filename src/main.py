from src.function import print_display_to_user

user_input = int(input('введите нужное количество транзакций: '))

count_transaction = 0
while count_transaction < user_input:
    print_display_to_user(user_input, count_transaction)
    print()
    count_transaction += 1
