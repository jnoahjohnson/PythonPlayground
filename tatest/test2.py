# author - Josh Moody
# description - this is a game of hangman for 80's songs

import random

#This list contains the songs with spaces removed
listSongs = ["rocklobster", "peoplearepeople", "onceinalifetime", "sweetdreams", "missionaryman", 
"safetydance", "cars", "whipit"]

class Person():

    def __init__(self, sFirstName, sLastName):
        self.first_name = sFirstName
        self.last_name = sLastName
    
class Game():

    def __init__(self, iGuessCount):
        self.guess_count = iGuessCount
    
class Contestant(Person):

    def __init__(self, sFirstName, sLastName):
        super().__init__(sFirstName, sLastName)
        # number_of_games is a redundant attribute
        # I'm going to use len(self.games_played) instead
        # but I'm including the attribute to stay in line with the instructions
        self.number_of_games = 0
        self.games_played = []

    def show_results(self):
        iSumGuesses = 0
        # sum up the guesses in all the games this contestant has played
        for iCount in range(0, len(self.games_played)):
            iSumGuesses += self.games_played[iCount].guess_count
        print(f"{self.first_name} {self.last_name} has played {len(self.games_played)} games and used a total of {iSumGuesses} guesses")

# prompt user for name until they enter something
sFirstName = ""
sLastName = ""
while(sFirstName == ""):
    sFirstName = input("Enter the player's first name: ")
while(sLastName == ""):
    sLastName = input("Enter the player's last name: ")

oContestant = Contestant(sFirstName, sLastName)

# tracks whether the player wants to play a game
bWantsToPlay = True

while(bWantsToPlay):

    # initialize the dictionary of guesses
    # I would have preferred to use a set but this works too I guess
    dictAlphabet = { 
    'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 
    'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 
    's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0
    }

    # select a random song from the list
    sRandomSong = random.choice(listSongs)

    # create a string of equal length to the song, but only underscores
    sGuess = "_" * len(sRandomSong)
    iGuessCount = 0

    while(sGuess != sRandomSong):
        print("You have made " + str(iGuessCount) + " guesses so far.")
        print(sGuess)
        # cGuess (not to be confused with sGuess) holds a single character
        cGuess = input("Enter a letter to guess: ").lower()
        # make sure the guess character matches a value in the dictionary
        if cGuess not in dictAlphabet:
            print("Error: invalid input. Only letters in the alphabet are accepted")
            continue

        if(dictAlphabet[cGuess] != 0):
            print("You already guessed that letter. Try a different one.")
            continue

        # if the loop reaches this point, the guess attempt was valid
        iGuessCount += 1
        
        dictAlphabet[cGuess] = 1

        # very annoying that strings are immutable in python
        # this loop reveals the correctly guessed characters in the guess string
        # by created a new string and adding the correctly guessed characters to it
        sUpdatedGuess = ""
        for iCount in range(0, len(sGuess)):
            if(sRandomSong[iCount] == cGuess):
                sUpdatedGuess += cGuess
            else:
                sUpdatedGuess += sGuess[iCount]

        # replace the old guess with the new one
        sGuess = sUpdatedGuess

        # win condition
        if(sGuess == sRandomSong):
            print("Correct! You used " + str(iGuessCount) + " guesses")
            print("The song was " + sRandomSong)
            break

        # lose condition
        elif(iGuessCount >= 20):
            print("You took too many guesses!")
            break
    
    # after the game is finished (win or lose)
    # add finished game to list of played games
    oGame = Game(iGuessCount)
    oContestant.games_played.append(oGame)

    # determine whether to play again
    sPlayAgain = ""
    while(sPlayAgain != "y" and sPlayAgain != "n"):
        sPlayAgain =  input("Play again? (y/n): ").lower()
    if(sPlayAgain == "y"): bWantsToPlay = True
    else: bWantsToPlay = False

# after the player has decided to stop playing, show results
oContestant.show_results()