choices = "1. Добавить покупателя\n2. Обслужить покупателя\n3. Посмотреть очередь\n4. Выйти"
print("Добро пожаловать.")
full_queue = []
queue = ()
print('Примечание: Не  обслуживайте пустую очередь!')
my_choice = 0
while True:
    print('\n'+choices)
    my_choice = int(input('Выберите действие (1-4): '))
    if my_choice == 1:
        name = input('Введите имя покупателя: ')
        products = int(input('Введите количество продуктов: '))
        queue += (name,)
        queue += (products,)
        full_queue.append(queue)
        print('Покупатель добавлен')
        queue = ()
        continue
    elif my_choice == 2:
        print(full_queue[0][0], 'обслужен')
        full_queue.remove(full_queue[0])
    elif my_choice == 3:
        for i in range(len(full_queue)):
            print(f'{i+1}. {full_queue[i][0]} ({full_queue[i][1]} товаров)')
    elif my_choice == 4:
        exit('Вы вышли.')