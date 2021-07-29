import random

num_list = [1, 3, 5, 31, 24, 3.4]

random.shuffle(num_list)


print(num_list)
user_ans = int(input("What is the highetst number in the  list above? "))
correct_answer = max(num_list)

if user_ans == correct_answer:
    print("Well done")
else: 
    print("Oops")


