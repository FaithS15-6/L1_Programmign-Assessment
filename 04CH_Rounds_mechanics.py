# Functions used to check input is valid

def check_rounds():
   
    while True:
        response = input("How many rounds: ")
        round_error = "Please type either <enter> or an interger that is more than zero"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response

# Main Routine goes here...

rounds_played = 0
choose_instructions = "please the highest numer from the list"

# Ask user for number of rounds. <enter> for infinite mode
rounds = check_rounds()
end_game = "no"
while end_game == "no":
    
    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continues Mode : Round {}".format(rounds_played + 1)
        print(heading)
        
        choose = input("{} or 'xxx' to end: ".format(choose_instructions))
        if choose == "xxx":
            break

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        choose = input(choose_instructions)
        if rounds_played == -1:
            end_game = "yes"

    # extra loop
    print("You chose {}".format(choose))

    rounds_played += 1
print("Thanks for playing")

