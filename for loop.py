vowels = ["a", "e", "i", "o", "w"]

string = "The quick brown fox jump over the lazy dog"

for letter in string:
    if letter in vowels:
        print(f"{letter} is a vowel !")
    else:
        print(letter)