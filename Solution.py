import random

randomNumber = []
attempts = 0


def generateRandomNumber():
    for i in range(4):
        num = random.randrange(0, 9)
        randomNumber.append(num)

    if len(randomNumber) > len(set(randomNumber)):
        randomNumber.clear()
        generateRandomNumber()

    return randomNumber


def guessNumber():
    guess = input("Enter the 4 digit number : ")
    guessList = []
    for i in guess:
        guessList.append(int(i))

    cows = 0
    bulls = 0
    global attempts
    attempts += 1

    for i in range(4):
        if guessList[i] == randomNumber[i]:
            cows += 1

    for i in range(4):
        for j in range(4):
            if guessList[i] == randomNumber[j]:
                bulls += 1

    if cows == 4:
        print("You have won the game after ", attempts, " attempts!")
    else:
        print("cows :", cows, " & bulls :", bulls, "& attempts :", attempts)
        guessNumber()


print(generateRandomNumber())
guessNumber()
