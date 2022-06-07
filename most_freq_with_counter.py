#https://habr.com/ru/company/yandex/blog/488682/

from collections import Counter
from random import random
 #a = [int(i) for i in input().split()] 
a = [int(random()*7) for i in range(15)]
print(a)


counter = Counter(a)

result = a[0]
max_count = counter[result]
for number, count in counter.items():
    if count > max_count or (count == max_count and number > result):
        result = number
        max_count = count

print(result) 