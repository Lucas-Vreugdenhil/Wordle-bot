import os
import time as t

#DISCLAIMER: My 5 letter words text file might not contain every single 5 letter word.

file = open('5 Letter Words.txt', 'r')
words = file.readlines()

def removeWrong(firstGuess,firstResult,words):
    removeThese = []
    
    # Get all wrong words -------------------------------
    for i in range (0,5):
        if(firstResult[i] == "0"):
            for j in range (0, len(words)):
                if(words[j].find(firstGuess[i]) != -1):
                    removeThese.append(j)
        if(firstResult[i] == "1"):
            for j in range(0, len(words)):
                if(words[j][i] == firstGuess[i] or words[j].find(firstGuess[i]) == -1):
                    removeThese.append(j)

        if(firstResult[i] == "2"):
            for j in range(0, len(words)):
                if(words[j][i] != firstGuess[i]):
                    removeThese.append(j) 
    # ---------------------------------------------------
    
    # Remove all wrong words 
    removeThese = sorted(set(removeThese))
    a = 0

    for i in range (0, len(removeThese)):
        words.pop((removeThese[i] - a))
        a = a + 1


iteration = 1

while(True):
    print("Guess: " + str(iteration) + ". type 'new game' to restart.")
    t.sleep(.1)
    guess = input()
    if(guess.lower() == "new game" or guess.lower() == "newgame"):
        file = open('5 Letter Words.txt', 'r')
        words = file.readlines()
        print("Guess: 1. type 'new game' to restart.")
        guess = input()
        iteration = 1
    print("Result. Green 2, Yellow 1, Gray 0. For example 02012")
    result = str(input())
    print("\n")
    removeWrong(guess, result, words)
    print("Possible words: " + str(len(words)))
    for line in words:
        print(line)
    iteration+= 1
