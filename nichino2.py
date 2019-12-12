# Like a bogosort

import random
import math

list = [1, 2, 3, 4, 5, 6]

count = 0
answer = []
while (True):
    count += 1
    random.shuffle(list)
    sum = 0
    for i in range(0, 6):
        sum += list[i] * pow(10, 5 - i)

    if sum % 6 == 0 and int(sum / 10) % 5 == 0 and int(sum / 100) % 4 == 0 and int(sum / 1000) % 3 == 0 and int(sum / 10000) % 2 == 0:
        if sum not in answer:
            answer.append(sum)
            count = 0
    if count > 100000:
        break
print(answer)
