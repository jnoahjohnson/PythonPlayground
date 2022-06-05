sTeam = "Rockies" 
bPlayoffs = False 
iWins = 20 

if (sTeam == "test") : 
    if (bPlayoffs == True):
        if (iWins >= 20): 
            print ("Go Rockies")
elif (sTeam == "Rockies"):
     if (bPlayoffs == False): 
         if (iWins >= 20):
              print ("Almost")
else: print ("Next Season")