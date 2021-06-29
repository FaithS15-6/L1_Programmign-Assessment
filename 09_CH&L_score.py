# CH&L componet 6 - scring system 

# correct answers will be calculated (total - correct - wrong)
question_answered = 0
question_wrong = 0
question_correct = 0

# results for testing puposes
test_results = ["correct", "correct", "wrong", "wrong"]

#play game
for item in test_results:
    question_answered += 1
    print("Question {}: {} ".format(question_answered, item))

print()
# quick calculations (stats)
question_correct = question_answered - question_wrong 

# end of game Statistics
print()
print('*End Game Summary*')
print("Correct Answers: {} \t|\t Wrong Answers: {}".format(question_correct, question_wrong))
print()
print("Thanks 4 playing*")