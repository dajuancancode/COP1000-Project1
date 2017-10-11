#Define main function
def main():
    #Declare constant for PERFECTSCORE as 5
    PERFECTSCORE = 5
    #Declare variable for score as a whole number
    score = 0
    #Declare vaiable for firsName as a string
    firstName = ""
    #Declare variable for userName as a string
    userName = ""
    #Declare variable for answer as a string
    answer = ""

    #Read in file with questions
    infile = open("quiz.txt", "r")

    #Store the first line as the variable line1
    line1 = infile.readline()
    #Store the second line as the variable line2
    line2 = infile.readline()
    #Store the third line as the variable line3
    line3 = infile.readline()
    #Store the fourth line as the variable line4
    line4 = infile.readline()
    #Store the fifth line as the variable line5
    line5 = infile.readline()

    #Close the file
    infile.close()

    #Split line1 at the semicolon
    #Store the first position in question1
    line1 = line1.split("?")
    question1 = line1.pop(0) + "?"
    answers1 = ",".join(line1)
    problem1 = {question1: answers1}

    #Split line2 at the semicolon
    #Store the first position in question2
    line2 = line2.split("?")
    question2 = line2.pop(0) + "?"
    answers2 = ",".join(line2)
    problem2 = {question2: answers2}

    #Split line3 at the semicolon
    #Store the first position in question3
    line3 = line3.split("?")
    question3 = line3.pop(0) + "?"
    answers3 = ",".join(line3)
    problem3 = {question3: answers3}

    #Split line4 at the semicolon
    #Store the first position in question4
    line4 = line4.split("?")
    question4 = line4.pop(0) + "?"
    answers4 = ",".join(line4)
    problem4 = {question4: answers4}

    #Split line5 at the semicolon
    #Store the first position in question5
    line5 = line5.split("?")
    question5 = line5.pop(0) + "?"
    answers5 = ",".join(line5)
    problem5 = {question5: answers5}

    for questions, answers in problem1.items():
        print(questions)
        print(answers[1:])
        
        print("Type in the letter represnting your choice below")
        answer = input("> ").strip().upper()
        print()

        if answer == "A":
            print("You guessed correctly\n")
            score += 1
            
        else:
            print("You guessed incorrectly")
            print("The correct answer was: 92.96 million mi\n")
    
    for questions, answers in problem2.items():
        print(questions)
        print(answers[1:])
        
        print("Type in the letter represnting your choice below")
        answer = input("> ").strip().upper()
        print()

        if answer == "C":
            print("You guessed correctly\n")
            score += 1
        else:
            print("You guessed incorrectly")
            print("The correct answer was: Andromeda\n")
    
    for questions, answers in problem3.items():
        print(questions)
        print(answers[1:])
        
        print("Type in the letter represnting your choice below")
        answer = input("> ").strip().upper()
        print()

        if answer == "D":
            print("You guessed correctly\n")
            score += 1
        else:
            print("You guessed incorrectly")
            print("The correct answer was: 187 years\n")
    
    for questions, answers in problem4.items():
        print(questions)
        print(answers[1:])
        
        print("Type in the letter represnting your choice below")
        answer = input("> ").strip().upper()
        print()
        
        if answer == "A":
            print("You guessed correctly\n")
            score += 1
        else:
           print("You guessed incorrectly")
           print("The correct answer was: Voyager 2\n")
    
    for questions, answers in problem5.items():
        print(questions)
        print(answers[1:])
        
        
        print("Type in the letter represnting your choice below")
        answer = input("> ").strip().upper()
        print()

        if answer == "B":
            print("You guessed correctly\n")
            score += 1
        else:
            print("You guessed incorrectly")
            print("The Answer was: No\n")
    
    if score == PERFECTSCORE:
        print("Congratulations! You recieved a perfect score")
        print(score)
    elif score == PERFECTSCORE - 1:
        print("You were only one point away from a perfect score")
        print(score)
    elif score == PERFECTSCORE - 2:
        print("You were two points away from a perfect score")
        print(score)
    elif score == PERFECTSCORE - 3:
        print("You were three points away from a perfect score")
        print(score)
    elif score == PERFECTSCORE - 4:
        print("You were four points away from a perfect score")
        print(score)
    else:
        print("You missed every single question")
        print(score)
    #Display introduction
if __name__ == "__main__":
    main()
