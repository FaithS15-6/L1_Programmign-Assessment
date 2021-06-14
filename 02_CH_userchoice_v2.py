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

user_choice = choice_checker("Choose one / two / three: ")


# print out choice for comparison purpose
