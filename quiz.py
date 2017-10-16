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
    with open("quiz.txt", "r") as infile:

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


    #Split line1 at the semicolon
    #Store the first position in question1
    line1 = line1.split("?")
    question1 = line1.pop(0) + "?"
    answers1 = ",".join(line1)
    correctAnswer1 = 'A'
    problem1 = (question1, answers1, correctAnswer1)


    #Split line2 at the semicolon
    #Store the first position in question2
    line2 = line2.split("?")
    question2 = line2.pop(0) + "?"
    answers2 = ",".join(line2)
    correctAnswer2 = 'C'
    problem2 = (question2, answers2, correctAnswer2)

    #Split line3 at the semicolon
    #Store the first position in question3
    line3 = line3.split("?")
    question3 = line3.pop(0) + "?"
    answers3 = ",".join(line3)
    correctAnswer3 = 'D'
    problem3 = (question3, answers3, correctAnswer3)

    #Split line4 at the semicolon
    #Store the first position in question4
    line4 = line4.split("?")
    question4 = line4.pop(0) + "?"
    answers4 = ",".join(line4)
    correctAnswer4 = 'A'
    problem4 = (question4, answers4, correctAnswer4)

    #Split line5 at the semicolon
    #Store the first position in question5
    line5 = line5.split("?")
    question5 = line5.pop(0) + "?"
    answers5 = ",".join(line5)
    correctAnswer5 = 'B'
    problem5 = (question5, answers5, correctAnswer5)

    #Create a tuple from all of the problemsets
    problems = (problem1, problem2, problem3, problem4, problem5)
    

    #Display introduction
    print()
    print("Let's play COSMOS!!!")
    print("This is a quiz game to test your knowledge of the cosmos\n")

    print("Before we start, would you mind telling me your name?")
    firstName = input("> ").strip().title()
    userName = firstName[1:]+firstName[0]+"ay"
    userName = userName.title()
    print()

    print("{} seems like a nice name, but that won't do.".format(firstName))
    print("For the rest of the game, I will now call you {} \n".format(userName))
    


    #Loop through the problem tuple and keep track of the questions, the answers, and the correct answer
    for questions, answers, correctAnswer  in problems:
        print(questions, end='\n')
        print(answers)
        print()

        print("Type in the letter represnting your choice below")
        answer = input("> ").strip().upper()

        if answer == correctAnswer:
            print("You guessed correctly\n")
            score +=1
        else:
            print("You guessed incorrectly\n")
    if score == PERFECTSCORE:
        print("{}, you must be Neil deGrasse Tyson, because you scored a perfect score.".format(userName))
    elif score == PERFECTSCORE - 1:
        print(score)
    elif score == PERFECTSCORE - 2:
        print(score)
    elif score == PERFECTSCORE - 3:
        print(score)
    elif score == PERFECTSCORE - 4:
        print(score)
    else:
        print(score)
if __name__ == "__main__":
    main()
