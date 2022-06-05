import random
# Class: Person
# Attri: first_name, last_name
# Init: props(first_name, last_name)

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Contestant(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.number_of_games = 0
        self.games_played = []
    
    def show_results(self):
        if (len(self.games_played) == 0):
            return self.first_name + " has not played a game."
        
        total = 0
        for iCount in range(0, len(self.games_played)):
            total += self.games_played[iCount].guess_count

        return (self.first_name + " has played " + str(len(self.games_played))) + " games and used a total of " + str(total) + " guesses"

class Game():
    def __init__(self, iGuessCount):
        self.guess_count = iGuessCount

listSongs = ["rocklobster", "peoplearepeople", "onceinalifetime", "sweetdreams", "missionaryman", "safetydance", "cars", "whipit"]

sFirst = ""
sLast = ""

while (sFirst == ""):
    sFirst = input("What is your first name? ")

while (sLast == ""):
    sLast = input("What is your last name? ")

oContestant = Contestant(sFirst, sLast)

sAnswer = "Y"

while (sAnswer.upper() == "Y"):
    dictAlphabet = {
        'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0,
        'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0,
        's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0
    }

    sSong = random.choice(listSongs)

    sGuessSong = ""

    for iCount in range(0, len(sSong)):
        sGuessSong = sGuessSong + "_"

    iGuessCount = 0

    while (iGuessCount < 20):
        sInput = input("Guess? ")

        while dictAlphabet[sInput.lower()] == 1:
            print("This letter has been used")
            sInput("Guess? ")
        
        dictAlphabet[sInput.lower()] = 1

        iGuessCount += 1

        sNewSong = ""
 
        for iCount in range(0, len(sSong)):
            if (sGuessSong[iCount] == "_"):
                if (sSong[iCount] == sInput.lower()):
                    sNewSong += sSong[iCount]
                else:
                    sNewSong += "_"
            else:
                sNewSong += sGuessSong[iCount]
        
        sGuessSong = sNewSong

        print(sGuessSong)

        if (sNewSong == sSong):
            print("Correct! You used " + str(iGuessCount) + " guesses")
            oContestant.games_played.append(Game(iGuessCount))
            iGuessCount = 30
            print("The song was " + sSong)
        elif (iGuessCount >= 20) :
            print("you took too many guesses!")
            oContestant.games_played.append(Game(iGuessCount))
            print("The song was " + sSong)

    # Check if player want to play again
    sAnswer = input("Do you want to play again (Y/N)? ")
        
print(oContestant.show_results())