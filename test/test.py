#Author: Bethany Ward
#Program Description:The purpose of the game is to randomly choose a song from a pre-defined list of 1980's songs (like hangman). 

import random 

#person class
class Person() :
    def __init__(self, first_name, last_name) : 
        self.first_name = first_name
        self.last_name = last_name

#GAMES class
class Games() :
    def __init__(self, guess_count) : 
        self.guess_count = guess_count
        
#CONTESTANT class
class Contestant(Person) :
    def __init__(self, first_name, last_name) : 
        super().__init__(first_name, last_name)
        self.num_games = 0
        self.games_played = [] 

    def show_results(self, first_name, last_name, num_games) :
        if num_games == 0 :
            print(first_name + " " + last_name + " has not played a game") 
        else :
            print(first_name + " " + last_name + " has played " + str(num_games) + " and used a total of " + guesses + "guesses")

#list of songs
listofSongs = ["rocklobster", "peoplearepeople", "onceinalifetime", "sweetdreams", "missionaryman","safetydance", "cars", "whipit"]

#Use a dictionary to keep track of the letters used. Here is the dictionary:
dictAlphabet = {
'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0,
'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0,
's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0
 } 

#Get the player's first name and last name from prompts and create a new contestant object. They
#MUST enter a first name and a last name. Do not let them out of the prompt unless there is a value.
fName = ""
lName = ""
while (fName == "" and lName == "") :
    fName = input("Enter the player's first name: ")
    lName = input("Enter the player's last name: ")

oContestant = Contestant(fName, lName)

#See if they want to play again
playAgain = True
while playAgain == True :
    #Get the random song title from the list of songs to solve for the current player
    iRandIndex = random.randint(0, len(listofSongs)-1)
    theSong = listofSongs[iRandIndex] #theSong = 'nameofsong'

    #turning the song name into a list to be able to search through
    lstTheSong = []
    for iCount in range(0, len(theSong)):
        lstTheSong = list(theSong) #lstTheSong = ['n','a','m','e','o','f','s','o','n','g']

    #Use the song title to create underscores in the place of characters 
    lstGuessSong = [] 
    for iCount in range(0, len(theSong)):
        lstGuessSong.append("_") #lstGuessSong = ['_', '_', '_', '_']

    #As the user guesses letters you will update the display (i.e. mi__io____m__)
    guess_count = 0
    allRight = False
    underscoreCount = 0
    if guess_count <= 20 : 
         while (allRight == False) :
            guessletter = input("Guess a letter: ")
            #See if guessed letter is already used or not and then update
            if dictAlphabet[guessletter] == 1 :
                print("That letter has already been guessed! ") 
            else :
                dictAlphabet['guessletter'] = 1
                guess_count += 1
                #for loop to look for letter in song
                for iCounter in range (0, len(lstTheSong)) :
                    if lstTheSong[iCounter] == guessletter :
                        lstGuessSong[iCounter] = guessletter
            #printing the guess string
                lstGuessSongX = "".join(lstGuessSong)
                print(lstGuessSongX)
            #checking to see if all letters have been guessed
            for count in range (0,len(lstGuessSong)):
                if lstGuessSong[count] == '_' :
                    underscoreCount += 1
            if underscoreCount >= 1 :
                allRight = False
            else:
                allRight = True 
                print("Correct! You used " + str(guess_count) + " guesses.")
                print("The song was " + lstGuessSongX)

            oGame = Games(guess_count)
            oContestant.games_played.append(oGame)

    #outside while loop, if guesses are more than 20
    elif guess_count > 20 :
        print("You took too many guessses!")
    else:
        #checking to see if they want to play again
        again = input("Would you like to play again? (Y/N)") 
        if again.upper() == "Y" :
            playAgain = True
        else :
            playAgain = False
            #Once they have decided to stop, call the show_results() method to display the results of the game for the contestant.
            oContestant.showResults()