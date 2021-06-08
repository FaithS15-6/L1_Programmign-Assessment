import random

ch_list = ["true", "false"]
rps_list = ["1", "50"]

def true_false(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "true" or response == "t":
            response = "true"
            return response

        elif response == "false" or response == "f":
            response = "f"
            return response

        else:
            print("please answer true/false")