def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides,statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""

# Main Routine goes here
statement_generator("Welcome to the Choose Highest and Lowest Number game", "*")

print()
statement_generator("Congratulations you answered correctly!", "!")