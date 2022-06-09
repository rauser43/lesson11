numbers= [2, 4, 6, 8, 7,10]
result = [1 if number %2 else 0 for number in numbers]
print (result)


try:
    list_1= [2, 4, 6, 8, 7,10]
    input ("Введите чило:", int(x))
    list_2= [x**3 for x in list_1]
    print (list_2)
except:
    print('Вы ввели не число')

list_1= [2, 4, 6, 8, 7,10]
list_2= [x**3 for x in list_1 if x%5 and x>5]
print (list_2)

names = ['Cris', 'Mary', 'Pit','Jonny']
len_names= [len(i) for i in names]
print(len_names)

