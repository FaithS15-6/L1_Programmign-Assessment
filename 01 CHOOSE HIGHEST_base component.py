import random


# Functions go here...

# checks that users answer yes/no to a question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")

# Checks that users enter a number a number between two end points
def intcheck(question):
    while True:
        response = input(question)

        round_error = "Please type either <enter> or an " \
                      "integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # Is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to start of loop

            except ValueError:
                print(round_error)
                continue

        return response    
# Ask user if they have played before
# Game instructions on how to play
def instructions():
    print()
    print("**** How to play ****")
    print()
    print("In order to play this game...")
    print()
    return ""

# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print()

# Checks number of rounds

# develop random numbers players can***
# 
num_1 = random.randrange(1, 50)
num_2 = num_1 * 15
num_3 = num_2 + 4
num_4 = num_3 +2
num_5 = num_2 + 3
num_6 = num_5 +num_3

list1 = [num_1, num_2, num_3, num_4, num_5, num_6] 

# shuffle numbers in list.
random.shuffle(list1)
print(list1)


print()


# Main routine goes here

# ask user for answer and check that it is correct.

user_choice = intcheck("Choose the highest number from the list ")
user_choice = intcheck("Choose the lowest number from the list")
# ways to win

# Number list, 
correct = max(list1)

# Prints out correct answers (Highest and Lowest when player is done)
print ("Max value element :", max(list1))
print ("Min value element :", min(list1))

# Functions go here
