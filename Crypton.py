# Name: Crypton
# Date: 4/8/2017
# Purpose of this program is to source input from the user and either encrypt or decrypt it based on the user's choice.


Text = input("Please enter your text")  # The user writes the text he/she wants to encrypt or decrypt.
choice = input("Type 'e' to encrypt 'd' to decrypt or 'q' to quit")  # The user chooses whether to encrypt or decrypt
result = ""  # The string in which the final encryption or decryption would be stored

# always remember the double equal to sign
# check if the user wants to encrypt or decrypt
if choice == "e":  # If the user wants to encrypt
    for EachLetter in Text:
        if EachLetter == "a":  # If there's an a in the text, it adds "Wr" to the final result.
            result += "Wr"
        elif EachLetter == "b":
            result += "x4"
        elif EachLetter == "c":
            result += "Sl"
        elif EachLetter == "d":
            result += "s6"
        elif EachLetter == "e":
            result += "N0"
        elif EachLetter == "f":
            result += "mC"
        elif EachLetter == "g":
            result += "iA"
        elif EachLetter == "h":
            result += "Fx"
        elif EachLetter == "i":
            result += "Y1"
        elif EachLetter == "j":
            result += "PL"
        elif EachLetter == "k":
            result += "bR"
        elif EachLetter == "l":
            result += "Zf"
        elif EachLetter == "m":
            result += "VD"
        elif EachLetter == "n":
            result += "L5"
        elif EachLetter == "o":
            result += "U9"
        elif EachLetter == "p":
            result += "ye"
        elif EachLetter == "q":
            result += "8b"
        elif EachLetter == "r":
            result += "aH"
        elif EachLetter == "s":
            result += "K7"
        elif EachLetter == "t":
            result += "gi"
        elif EachLetter == "u":
            result += "T6"
        elif EachLetter == "v":
            result += "r0"
        elif EachLetter == "w":
            result += "Ov"  # UpperCase Letter O
        elif EachLetter == "x":
            result += "EJ"
        elif EachLetter == "y":
            result += "n4"
        elif EachLetter == "z":
            result += "hQ"
        elif EachLetter == "A":
            result += "X6"
        elif EachLetter == "B":
            result += "vW"
        elif EachLetter == "C":
            result += "7d"
        elif EachLetter == "D":
            result += "Rt"
        elif EachLetter == "E":
            result += "o3"
        elif EachLetter == "F":
            result += "5m"
        elif EachLetter == "G":
            result += "Ds"
        elif EachLetter == "H":
            result += "wI"
        elif EachLetter == "I":
            result += "3z"
        elif EachLetter == "J":
            result += "G8"
        elif EachLetter == "K":
            result += "uj"
        elif EachLetter == "L":
            result += "1N"
        elif EachLetter == "M":
            result += "Ck"
        elif EachLetter == "N":
            result += "e0"
        elif EachLetter == "O":
            result += "9c"
        elif EachLetter == "P":
            result += "HG"
        elif EachLetter == "Q":
            result += "jx"
        elif EachLetter == "R":
            result += "6K"
        elif EachLetter == "S":
            result += "Mt"
        elif EachLetter == "T":
            result += "q7"
        elif EachLetter == "U":
            result += "2n"
        elif EachLetter == "V":
            result += "B3"
        elif EachLetter == "W":
            result += "fS"
        elif EachLetter == "X":
            result += "45"
        elif EachLetter == "Y":
            result += "Ip"
        elif EachLetter == "Z":
            result += "c9"
        elif EachLetter == "0":
            result += "d9"
        elif EachLetter == "1":
            result += "Qj"
        elif EachLetter == "2":
            result += "kZ"
        elif EachLetter == "3":
            result += "0Q"
        elif EachLetter == "4":
            result += "tM"
        elif EachLetter == "5":
            result += "Je"
        elif EachLetter == "6":
            result += "A5"
        elif EachLetter == "7":
            result += "zU"
        elif EachLetter == "8":
            result += "L2"
        elif EachLetter == "9":
            result += "pX"
# Check if the character is a space
        elif EachLetter == " ":
            result += "  "
# Check if the character is a full stop
        elif EachLetter == ".":
            result += ". "
# Check if the character is a comma
        elif EachLetter == ",":
            result += ", "
    print(result)  # Prints out the final encryption to the user

elif choice == "d":  # If the user decides to decrypt.
    currentIndex = 0
    lengthText = len(Text)  # The total number of letters the word has
    while currentIndex < lengthText:
        EachLetter = Text[currentIndex: currentIndex + 2]
        currentIndex += 2  # This adds 2 to the currentIndex variable until it exceeds the length of the text

        if EachLetter == "Wr":  # If "Wr" is seem in the text, it should be replaced by "a"
            result += "a"
        elif EachLetter == "x4":
            result += "b"
        elif EachLetter == "Sl":
            result += "c"
        elif EachLetter == "s6":
            result += "d"
        elif EachLetter == "N0":
            result += "e"
        elif EachLetter == "mC":
            result += "f"
        elif EachLetter == "iA":
            result += "g"
        elif EachLetter == "Fx":
            result += "h"
        elif EachLetter == "Y1":
            result += "i"
        elif EachLetter == "PL":
            result += "j"
        elif EachLetter == "bR":
            result += "k"
        elif EachLetter == "Zf":
            result += "l"
        elif EachLetter == "VD":
            result += "m"
        elif EachLetter == "L5":
            result += "n"
        elif EachLetter == "U9":
            result += "o"
        elif EachLetter == "ye":
            result += "p"
        elif EachLetter == "8b":
            result += "q"
        elif EachLetter == "aH":
            result += "r"
        elif EachLetter == "K7":
            result += "s"
        elif EachLetter == "gi":
            result += "t"
        elif EachLetter == "T6":
            result += "u"
        elif EachLetter == "r0":
            result += "v"
        elif EachLetter == "Ov":  # UpperCase Letter O
            result += "w"
        elif EachLetter == "EJ":
            result += "x"
        elif EachLetter == "n4":
            result += "y"
        elif EachLetter == "hQ":
            result += "z"
        elif EachLetter == "X6":
            result += "A"
        elif EachLetter == "vW":
            result += "B"
        elif EachLetter == "7d":
            result += "C"
        elif EachLetter == "Rt":
            result += "D"
        elif EachLetter == "o3":
            result += "E"
        elif EachLetter == "5m":
            result += "F"
        elif EachLetter == "Ds":
            result += "G"
        elif EachLetter == "wI":
            result += "H"
        elif EachLetter == "3z":
            result += "I"
        elif EachLetter == "G8":
            result += "J"
        elif EachLetter == "uj":
            result += "K"
        elif EachLetter == "1N":
            result += "L"
        elif EachLetter == "Ck":
            result += "M"
        elif EachLetter == "e0":
            result += "N"
        elif EachLetter == "9c":
            result += "O"
        elif EachLetter == "HG":
            result += "P"
        elif EachLetter == "jx":
            result += "Q"
        elif EachLetter == "6K":
            result += "R"
        elif EachLetter == "Mt":
            result += "S"
        elif EachLetter == "q7":
            result += "T"
        elif EachLetter == "2n":
            result += "U"
        elif EachLetter == "B3":
            result += "V"
        elif EachLetter == "fS":
            result += "W"
        elif EachLetter == "45":
            result += "X"
        elif EachLetter == "Ip":
            result += "Y"
        elif EachLetter == "c9":
            result += "Z"
        elif EachLetter == "d9":
            result += "0"
        elif EachLetter == "Qj":
            result += "1"
        elif EachLetter == "kZ":
            result += "2"
        elif EachLetter == "0Q":
            result += "3"
        elif EachLetter == "tM":
            result += "4"
        elif EachLetter == "Je":
            result += "5"
        elif EachLetter == "A5":
            result += "6"
        elif EachLetter == "zU":
            result += "7"
        elif EachLetter == "L2":
            result += "8"
        elif EachLetter == "pX":
            result += "9"
# Check if the character is a space
        elif EachLetter == "  ":
            result += " "
# Check if the character is a full stop
        elif EachLetter == ". ":
            result += "."
# Check if the character is a comma
        elif EachLetter == ", ":
            result += ","

    print(result)  # This prints out the final decrypted message for the user to see.

elif choice == "q":
    import sys
    sys.exit()
