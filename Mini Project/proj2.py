file = "highscore.txt"

score = 0
highscore = 0

def load_highscore():
    global highscore
    try:
        file = open("highscore.txt", "r")
        highscore = int(file.read())
        file.close()
    except:
        pass

def save_highscore():
    global score, highscore
    if score > highscore:
        highscore = score
        file = open("highscore.txt", "w")
        file.write(str(highscore))
        file.close()

def play_quiz():
    global score
    questions = ["5+4=??", "12-8=?", "3*3=?", "16/4=?"]
    answers = ["9", "4", "9", "4"]
    for i in range(len(questions)):
        print("\nQ.", questions[i])
        user_answer = input("Your answer: ")   # FIX 1
        if user_answer == answers[i]:
            score = score + 1
            print("Correct Answer!")
        else:
            print("Wrong Answer!")

# main program
def main():
    global highscore
    load_highscore()
    name = input("enter your name: ")
    play_quiz()
    print("\nYour Score is:", score)
    print("quiz over!!")
    if score > highscore:
        highscore = score
        save_highscore()
        print("Congratulations", name, "! You have the highest score.")
    else:
        print("The highest score is:", highscore)

main()
