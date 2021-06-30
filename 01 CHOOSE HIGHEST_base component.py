import random


# Functions go here...

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


def instructions():
    print()
    print("**** How to play ****")
    print()
    print("In order to play this game...")
    print()
    return ""



# Main Routine goes here...


answered_before = yes_no("Have you played the game before? ")

if answered_before == "no":
    instructions()
print()

# Checks number of question
question_answered = 0
question_wrong = 0
question_correct = 0

game_summary = []

chose_instructions = "please chose the highest and lowest from list"

# Ask user for number of question. <enter> for infinite mode 
question =intcheck ("How many questions?:")

end_game ="no"
while end_game == "no":

# loops while questions answered is more than questions requested

    # Start of game play loop
    question_answered +=1

    # Rounds Heading
    print()
    if question =="":
        heading = "Continues Mode :Question {}".format(question_answered)
    else:
        heading = "Question {} of Question {}".format(question_answered, question)

        print(heading)


 # End Game if exit code is typed
    if question_answered == "xxx":
        break

        # end game is round entered is finished.
            
# develop random numbers players choose

    num_1 = random.randrange(1, 100)
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

    # ask user for answer and check that it is correct.


    user_ans = intcheck("Choose the highest number from the list ")
    correct_answer = max(list1)

    if user_ans == correct_answer:
        print ("Well done")
    else:
        print("Oops")

    user_ans = intcheck("Choose the lowest number from the list")
    correct_answer = min(list1)

    if user_ans == correct_answer:
        print ("Correct!!")
    else:
        print("Damn It")
    # ways to win

    # Correct answer list (highest) 
    correct = max(list1)

    
    if question!= "" and question_answered >= question - 1:
        break

    # Prints out correct answers (Highest and Lowest when player is done)
    print ("Max value element :", max(list1))
    print ("Min value element :", min(list1))


