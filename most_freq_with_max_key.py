#x = set('set')
#print(x)
from random import random

# Заполнение списка случайными числами от 0 до 7.
# Количество элементов в списке = 15.
# Для заполнения используется генератор списков.
List = [int(random()*7) for i in range(15)]
print(List)

#List = [int(i) for i in input().split()] 
def most_frequent( List ):
	return max ( set ( List ), key = List .count)
	#В функциях min() и max() можно указать необязательный именной параметр key. Ему присваивается одноаргументная функция, которая выполняет какое-то предварительное действие над элементами списка.
#List = [ 2 , 1 , 2 , 2 , 1 , 3 ]

print (most_frequent( List ))

