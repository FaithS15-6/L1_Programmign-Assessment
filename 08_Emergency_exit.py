rounds = input("Rounds? ")
rounds_played = 0

again = ""


end_game = "no"
while end_game == "no":

    rounds_played += 1

    if rounds != "" and rounds_played >= int(rounds) + 1:
        break




    print("{} hello".format(rounds_played))
    again = input("press enter / xxx: ")

    if again == "xxx":
        break
