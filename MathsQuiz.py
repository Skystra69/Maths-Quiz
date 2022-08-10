import random
import time
import os

loopCode = True

while loopCode == True:

    i = 0
    playerScore = 0
    print("Welcome to the Basic Maths Quiz!")
    print("Version 1.1")
    print("")
    #introduction

    print("Please enter a difficulty from 1 to 3")
    print("1: Beginner")
    print("2: Advanced")
    print("3: Master")
    print("4: Legend")
    print("5: Mythical")
    print("")
    difficultyLevelInt = int(input())
    #difficulty decision

    if difficultyLevelInt == 1:
        difficultyLevelStr = ("Beginner")
    elif difficultyLevelInt == 2:
        difficultyLevelStr = ("Advanced")
    elif difficultyLevelInt == 3:
        difficultyLevelStr = ("Master")
    elif difficultyLevelInt == 4:
        difficultyLevelStr = ("Legend")
    elif difficultyLevelInt == 5:
        difficultyLevelStr = ("Mythical")
    else:
        difficultyLevelStr = ("Beginner")
    #if/else case to cycle through decision

    print("")
    print("You have selected " + difficultyLevelStr + " level!")
    print("You will receive 5 questions. At the end you will receive a score.")
    print("")
    #output to show selected difficulty

    if difficultyLevelStr == "Beginner":
        while i<5:
            
            x = random.randint(0,5)
            y = random.randint(0,5)
            z = (x + y)
            
            equation = "What is {} + {}?"
            print(equation.format(x, y))
            userAnswer = int(input())

            if userAnswer == (z):
                playerScore +=1
                
            i += 1
            
    elif difficultyLevelStr == "Advanced":
        while i<5:
            
            x = random.randint(0,20)
            y = random.randint(0,20)
            z = (x + y)
            
            equation = "What is {} + {}?"
            print(equation.format(x, y))
            userAnswer = int(input())

            if userAnswer == (z):
                playerScore +=1
                
            i += 1

    elif difficultyLevelStr == "Master":
        while i<5:
            
            x = random.randint(-20,20)
            y = random.randint(0,20)
            z = (x - y)
            
            equation = "What is {} - {}?"
            print(equation.format(x, y))
            userAnswer = int(input())

            if userAnswer == (z):
                playerScore +=1
                
            i += 1

    elif difficultyLevelStr == "Legend":
        while i<5:
            
            x = random.randint(-100,100)
            y = random.randint(-100,100)
            z = (x - y)
            
            equation = "What is {} - {}?"
            print(equation.format(x, y))
            userAnswer = int(input())

            if userAnswer == (z):
                playerScore +=1
                
            i += 1
            
    else: #this bit of code applies to the highest level by default
        while i<5:
            
            x = random.randint(0,15)
            y = random.randint(2,3)
            z = (x ** y)
            
            equation = "What is {} ^ {}?"
            print(equation.format(x, y))
            userAnswer = int(input())

            if userAnswer == (z):
                playerScore +=1
                
            i += 1

    print("")
    print("Difficulty: " + difficultyLevelStr)
    print("Score: " + str(playerScore))

    if playerScore == 0:
        print("Disappointing.")
    elif playerScore == 1 or playerScore == 2:
        print("Maybe you need more practice.")
    elif playerScore == 3 or playerScore == 4:
        print("Good effort.")
    else:
        print("Great effort!")
    print("")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
