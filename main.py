import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for (index, row) in file.iterrows()}

on = True
while on:
    word = input("Enter a word: ")
    try:
        codes = [nato[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters are accepted")
    else:
        print(codes)
        on = False
