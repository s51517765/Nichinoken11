# -*- coding: utf-8 -*-
import math

max = 654321
min = 123456
d1, d2, d3, d4, d5, d6 = 0, 0, 0, 0, 0, 0

for i in range(min, max+1):
    for j in range(1,7):
        if i < j * pow(10, 5):
            break
        d1 = j

    for j in range(1,7):
        if i - d1 * pow(10, 5) < j * pow(10, 4):
            break
        d2 = j

    for j in range(1,7):
        if i - d1 * pow(10, 5) - d2 * pow(10, 4) < j * pow(10, 3):
            break
        d3 = j

    for j in range(1,7):
        if i - d1 * pow(10, 5) - d2 * pow(10, 4) - d3 * pow(10, 3) < j * pow(10, 2):
            break
        d4 = j

    for j in range(1,7):
        if i - d1 * pow(10, 5) - d2 * pow(10, 4) - d3 * pow(10, 3) - d4 * pow(10, 2) < j * pow(10, 1):
            break
        d5 = j

    for j in range(1,7):
        if i - d1 * pow(10, 5) - d2 * pow(10, 4) - d3 * pow(10, 3) - d4 * pow(10, 2) - d5 * pow(10, 1) < j * pow(10, 0):
            break
        d6 = j

    list = [] #リストの初期化
    list.append(d1)
    if d2 not in list: #d2がリストになければ
        list.append(d2)
        if d3 not in list: #d3がリストになければ（以下同）
            list.append(d3)
            if d4 not in list:
                list.append(d4)
                if d5 not in list:
                    list.append(d5)
                    if d6 not in list:
                        list.append(d6)

                        if (d1 * pow(10, 1) + d2 * pow(10, 0)) % 2 == 0: #最初の2桁が2の倍数
                            if (d1 * pow(10, 2) + d2 * pow(10, 1) + d3 * pow(10, 0)) % 3 == 0: #最初の3桁が3の倍数（以下同）
                                if (d1 * pow(10, 3) + d2 * pow(10, 2) + d3 * pow(10, 1) + d4 * pow(10, 0)) % 4 == 0:
                                    if (d1 * pow(10, 4) + d2 * pow(10, 3) + d3 * pow(10, 2) + d4 * pow(10, 1) + d5 * pow(10, 0)) % 5 == 0:
                                        if (d1 * pow(10, 5) + d2 * pow(10, 4) + d3 * pow(10, 3) + d4 * pow(10, 2) + d5 * pow(10, 1) + d6 * pow(10, 0)) % 6 == 0:
                                            print(i)

