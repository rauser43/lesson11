import os

print ("1. Создать папку")
print("2. Удалить (файл/папку)")
print ("3. Копировать (файл/папку)")
print ("4. Просмотр содержимого рабочей директории")
print ("5. Посмотреть только папки")
print ("6. Посмотреть только файлы")
print ("7. Просмотр информации об операционной системе")
print ("8. Создатель программы")
print ("9. Играть в викторину")
print ("10. Мой банковский счет")
print ("11. Смена рабочей директории")
print ("12. Выход")

choice = input('Выберите пункт меню:')
if choice == '1':
    input("Введите название папки:")
if not os.path.isdir ("newstep"):
    os.mkdir ("newstep")
elif choice == '2':
    input("Введите название папки:")
if os.path.isdir("newstep"):
    os.rmdir("newstep")
elif choice == '3':
    shutill.copy ("newstep.py","newstep.copy.py")
elif choice == '4':
    print("Содержимое рабочей директории:", os.getcwd())
elif choice == '5':
    os.listdir()
    #for dirname in dirnames:
        #print("Каталог:", os.path.join(dirpath, dirname))
    print ()
elif choice == '6':
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))
        os.walk()
elif choice == '7':
    print(sys.platform)
elif choice == '8':
    print(sys.executable)
elif choice == '9':
    def get_random_person():

        FAMOUS_PEOPLE = {'Александр Сергеевич Пушнин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                         'Сергей Александрович Есенин': '03.10.1895', 'Владимир Семенович Высоцкий': '25.01.1938',
                         'Виктор Робертович Цой': '21.06.1962', 'Константин Эдуардович Циолковский': '17.09.1857',
                         'Сергей Павлович Королев': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908',
                         'Андрей Николаевич Туполев': '29.10.1888', 'Юрий Алексеевич Гагарин': '09.03.1934'}

        name, date = random.choice(list(FAMOUS_PEOPLE.items()))
        return name, date

elif choice == '10':
    amount = 0
    purches_list = []
while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f"Ваш баланс {amount}")

try = input ('Выберите пункт меню:')
if try == '1':
    bill = int(input ("Введите сумму:"))
    amount += bill
    elif try == '2':
        bill = int(input ("Введите сумму покупки:"))
        if bill>amount:
            print ("Пополните баланс")
        else:
            amount -= bill
            purchase=input ("Введите название покупки:")
            purches_list.append ([purchase,bill])
    elif try == '3':
        print(purches_list)
    elif try == '4':
        break
    else:
        print('Неверный пункт меню')
elif choice == '11':
    print ("Выход")


