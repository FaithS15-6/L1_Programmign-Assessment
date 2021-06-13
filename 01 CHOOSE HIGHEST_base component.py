import random

 # Functions go here 
 # List of valid player response
 # check rounds played
    # Fuctions go here
def check_rounds():
        while True:
            response = input("How many rounds: ")

            round_error = "Please type either <enter> or an " \
                        "integer that is more than 0\n"

            # If infinite mode not chosen, check response
            # Is an interger that is more than 0
            if response != "":
                try:
                    response = int(response)

                    # If response is too low, go back to start of loop

                    if response < 1:
                        print(round_error)
                        continue

                except ValueError:
                    print(round_error)
                    continue

        return response

 # check number entered is valid (true/false)

 # Functions go here
