from itertools import count

for el in count(int(input(('Введите первое число списка: ')))) :
    print(el)





from itertools import cycle

my_list = [ 234, 'cool' , 23,  True ]
for el in cycle(my_list):
    print(el)

