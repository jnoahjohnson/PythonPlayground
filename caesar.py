alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

textFile = open("Research.txt", "r")

text = textFile.readlines()

finalText = ""

for line in text:
    for char in line:
        if char.upper() in alphabet:
            location = alphabet.index(char.upper())
            newLocation = location - 13
            if newLocation < 0:
                newLocation = newLocation + 26
            
            finalText += alphabet[newLocation]
        else:
            finalText += char

newFile = open("Decrypted.txt", "w")
newFile.write(finalText)

newFile.close()
textFile.close()