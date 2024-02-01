from src import function



user_input = int(input('введите нужное количество транзакций: '))


count_transaction = 0
while count_transaction < user_input:
    function.print_display_to_user(user_input, count_transaction)
    print()
    count_transaction += 1
