#!/usr/bin/python3

result = []

for num in range(2000, 3601):
    if num % 7 == 0 and num % 5 != 0:
        result.append(num)


print(*result, sep=",")  # * used to unpack list
