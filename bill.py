amount = 0
purches_list = []

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f"Ваш баланс {amount}")


    choise = input('Введите номер: ')
    if choise == '1':
        bill = int(input ("Введите сумму:"))
        amount += bill
    elif choise == '2':
        bill=int(input ("Введите сумму покупки:"))
        if bill > amount:
           print ("Пополните баланс")
        else:
            amount -= bill
            purchase =input ("Введите название покупки:")
            purches_list.append ([purchase,bill])
    elif choise == '3':
        print(purches_list)
    elif choise == '4':
        break
    else:
        print('Неверный пункт меню')
    f=open ("amount.txt","w")
    f.write (f"Ваш баланс {amount}")
    f=open("purches.txt",'w')
    result=purches_list
    f.writelines(str(result))
    f. close()

