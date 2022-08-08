# --------------------------
def new_Game():
    guesses = []
    correct_Guesses = 0
    question_Num = 1

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_Num - 1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_Guesses += check_Answer(questions.get(key), guess)
        question_Num += 1

    display_Score(correct_Guesses, guesses)


# --------------------------
def check_Answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


# --------------------------
def display_Score(correct_Guesses, guesses):
    print("--------------------------")
    print("RESULTS")


    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    print("--------------------------")
    score = int((correct_Guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


# --------------------------
def play_Again():
    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


# --------------------------

questions = {"When was Google created?: ": "A",
             "When was YouTube created?: ": "B",
             "When was Amazon created?: ": "C",
             "When was Netflix created?: ": "A"
             }

options = [["A. 1998", "B. 1992", "C. 2001", "D. 2003"],
           ["A. 2006", "B. 2005", "C. 2003", "D. 2009"],
           ["A. 2003", "B. 1994", "C. 1997", "D. 1969"],
           ["A. 1997", "B. 2001", "C. 1993", "D. 1969"]]

new_Game()

while play_Again():
    new_Game()

print()
print("Thanks for playing! BYE!")