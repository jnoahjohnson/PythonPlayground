from math import fabs
import random

#This program should have a Person class that has a first_name and last_Name attribute. It should also have a
# constructor that receives 2 strings and assigns them to the first_name and last_name attributes.
class Person:
    def __init__(self, sFirstName, sLastName) :
        self.first_name = sFirstName
        self.last_name = sLastName
        
# The program should have the Games class which has the attribute guess_count which when the Games object
# is created, the constructor should receive the guess count and assign it to the guess_count attribute.
class Game:
    def __init__(self, iGuessCount) :
        self.guess_count = iGuessCount
# The program should also have a Contestant class that is inherited from the Person class. It has the
# number_of_games attribute. It also has a games_played attribute which will be an list of Game objects. The
# Contestant constructor receives the two strings for the contestant first and last names as parameters and
# populates those attributes based upon proper OOP that we have learned in our course. The number_of_games
# will initially have a 0 value and the games_played will be an empty list.
class Contestant(Person) :
    def __init__(self, sFName, sLName):
        super().__init__(sFName, sLName)
        self.number_of_games = 0
        self.games_played = []
# This class should also have a method called show_results that returns a message with the first and last names
# concatenated along with the number of guesses for all the games played. If they haven't played a game yet
# and there are no game objects, return the first and last names concatenated with " has not played a game".
# Otherwise if they have played a game, then the method returns a string like: 
    def show_results(self):
        if (self.number_of_games != 0) :
            self.total_guesses = 0
            for iCount in range(0, len(self.games_played)) :
                self.total_guesses += self.games_played[iCount].guess_count
            return self.first_name + " " + self.last_name + "has played " + str(self.number_of_games) + \
                    " and a total of " + str(self.total_guesses) + " guesses"
        else :
            return self.first_name + " " + self.last_name + " has not played a game"

listSongs = ["rocklobster", "peoplearepeople", "onceinalifetime", "sweetdreams", "missionaryman",
"safetydance", "cars", "whipit"]

# Get the player's first name and last name from prompts and create a new contestant object. 
# They MUST enter a first name and a last name. Do not let them out of the prompt unless there is a value.
sFirstName = ""
sLastName = ""

while (sFirstName == "") :
    sFirstName = input("Make sure you enter the first name: ")
while (sLastName == "") :
    sLastName = input("Make sure you enter the last name: ")

oContestant = Contestant(sFirstName, sLastName)

iGuessCount = 0
bOneMoreRound = True
#  Get the random song title from the list of songs to solve for the current player
while (bOneMoreRound == True) :
    sTitle = random.choice(listSongs)
    #  Use the song title to create underscores in the place of characters (i.e. _________ ) There are no spaces in the song title.
    lstAnswer = []
    lstCorrect = list(sTitle)

    for iCount in range(0, len(lstCorrect)):
        lstAnswer.append("_")
    #  As the user guesses letters you will update the display (i.e. mi__io____m__)

    for iCount in range(0, len(lstCorrect)) :
        # declaring the dictionary inside the loop to play the game so you don't have to continually reset the values
        dictAlphabet = {
            'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0,
            'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0,
            's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0
        }
        print("".join(lstAnswer))

        bStartGuess = True
        while (bStartGuess == True and iGuessCount < 20) :
            sLetter = input("What is the letter on your mind? ")
            print(dictAlphabet)
            if (sLetter != lstCorrect[iCount]) :
                if (dictAlphabet[sLetter] == 0) :
                    print("Try another one")
                    dictAlphabet[sLetter] = 1
                    iGuessCount += 1
                else :
                    print("Don't choose the same letter! It's wrong.")
            else :
                iGuessCount += 1
                lstAnswer[iCount] = sLetter
                bStartGuess = False

        if (iGuessCount == 20 and lstAnswer != lstCorrect) :
            break

    if (lstAnswer == lstCorrect) :
        oContestant.games_played.append(Game(iGuessCount))
        oContestant.number_of_games += 1
        print("Correct! You used " + str(oContestant.games_played[-1].guess_count) + " guesses")
        print("This song was " + sTitle)
            
    
    if (iGuessCount < 20):
        sAsk = input("Do you want one more round?(YES/NO) ").upper()
        if (sAsk == "NO") :
            bOneMoreRound = False
            
    else :
        print("You took too many guesses!")
        bOneMoreRound = False

print(oContestant.show_results())