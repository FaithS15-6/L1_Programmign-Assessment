import random

    # Functions go here 
    # List of valid player response
    
num_1 = random.randrange(1, 50)
num_2 = num_1 * 15
num_3 = num_1 + 4
num_4 = num_1 / -10 +2
num_5 = num_2 + 3
num_6 = num_2 +num_3

list1 = [num_1, num_2, num_3, num_4, num_5, num_6 ]
print ("Max value element :", max(list1))
print ("Min value element :", min(list1))

print("One")
print(num_1)
print()
print("Two")
print(num_2)
print()
print("Three")
print(num_3)
print()
print("Four")
print(num_4)
print()
print("Five")
print(num_5)
print()
print("Six")
print(num_6)

print()

    # check rounds played
    # Functions go here
def choice_checker (number):

    valid = False
    while not valid :

        # Ask user for choice
        response = input(number)

        if response == "true" or response == "t":
            return response

# Main routine goes here

# ask user for answer and check that it is correct.

user_choice = choice_checker("Choose the highest number from the list: one / two / three / four / five / six: ")


    # Fuctions go here