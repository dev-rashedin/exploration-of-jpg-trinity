# Python Quiz Game


questions = ("How many letters are in the English alphabet?",
             "How many continents are there?",
             "What is the capital of France?",
             "What is the capital of Germany?",
             "What is the capital of Italy?",)
options = (
    ("a. 26", "b. 27", "c. 28", "d. 29"),
    ("a. 6", "b. 7", "c. 8", "d. 9"),
    ("a. Paris", "b. Dublin", "c. Rome", "d. Madrid"),
    ("a. Paris", "b. Berlin", "c. Rome", "d. Dhaka"),
    ("a. Vienna", "b. Frankfurt", "c. Rome", "d. Madrid"),
)

answers = ("a", "b", "a", "b", "c")
guesses = []
score = 0

question_num = 0


for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (a, b, c, d): ").lower()
    guesses.append(guess)

    if(guess == answers[question_num]):
        score += 1
        print('Correct Answer')
    else:
        print('Wrong Answer')
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1


print("-----------------")
print("     RESULT     ")
print("-----------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = (score / len(questions)) * 100
print(f"Your score is: {score}%")