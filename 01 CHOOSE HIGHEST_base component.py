import random

# Functions go here 
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
# Checks number of rounds

  # develop random numbers players can***  
# 
num_1 = random.randrange(1, 50)
num_2 = num_1 * 15
num_3 = num_2 + 4
num_4 = num_3 / -10 +2
num_5 = num_2 + 3
num_6 = num_5 +num_3

list1 = [num_1, num_2, num_3, num_4, num_5, num_6 ]

print(*list1, sep= ", ")


print()


# Main routine goes here

# ask user for answer and check that it is correct.

user_choice = intcheck("Choose the highest number from the list ")
# Number list, 
correct = max(list1)

# Prints out correct answers (Highest and Lowest when player is done)
print ("Max value element :", max(list1))
print ("Min value element :", min(list1))



    # Fuctions go here