import random

num_1 = random.randrange(1, 100)
num_2 = num_1 - 50
num_3 = num_1 + 4
num_4 = num_1 / -10 +2
num_5 = num_2 + 3
num_6 = num_2 + 2

numlist =[num_1, num_2, num_3, num_4, num_5, num_6]

print(num_1)
print(num_2)
print(num_3)
print(num_4)
print(num_5)
print(num_6)

if num_1 > num_3:
    print("")
if num_3 < num_1:
    print("")

print()
print("Chose the highest number of of the numbers given above")