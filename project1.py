"""
projekt_1.py: první projekt do Engeto Online Python Akademie
"Textový analyzátor"

author: Jan Juřík
email: jurik.jan.2222@gmail.com
discord: jackobs1395
"""


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

amount_texts = len(TEXTS)

# přihlášení uživatele
user = input("Enter username: ")
password = input("Enter password: ")

# ověřit, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,

REG_USERS = dict(bob = "123", ann = "pass123", mike = "password123", liz = "pass123")

# pokud není registrovaný, upozorni jej a ukonči program.

if user not in REG_USERS or REG_USERS[user] != password:
    print(f"unregistered user, terminating the program..")
    exit()

# pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,

separator = "-" * 40

print(separator)
print(f"Welcome to the app, {user}")
print(f"You have {amount_texts} texts to be analyzed.")
print(separator)

choose_text = input(f"Enter a number btw. 1 and {amount_texts} to select: ")
print(separator)

# kontrola zadaného čísla

if not choose_text.isdigit():
    print("It is not a number.\n")
    exit()

text_Nr = int(choose_text) 

if text_Nr not in range(1, amount_texts + 1):
    print("Out of range.\n")
    exit()

# Analyza textu
# počet slov,
# počet slov začínajících velkým písmenem,
# počet slov psaných velkými písmeny,
# počet slov psaných malými písmeny,
# počet čísel (ne cifer),
# sumu všech čísel (ne cifer) v textu.


chosen_text = [word.strip(",.:;'") for word in TEXTS[text_Nr - 1].split()]

title_words = 0
uppercase_words = 0
lowercase_words = 0
numbers = 0
numbers_sum = 0
occurences_lenght = {}

pocet_slov = len(chosen_text)
for word in chosen_text:
    if word[0].istitle():
        title_words += 1
    if word.isupper():
        uppercase_words += 1
    if word.isalpha and word.islower():
        lowercase_words += 1
    if word.isnumeric():
        numbers += 1
        numbers_sum += int(word)
    
    lenght = len(word)
    if lenght in occurences_lenght:
        occurences_lenght[lenght] += 1
    else:
        occurences_lenght.update({lenght:1})
        
# výstup výsledků
        
print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {title_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {numbers} numeric strings.")
print(f"The sum of all the numbers is {numbers_sum}.")

column_name = ["LEN", "OCCURENCES", "NR."]
column_width = 15 
if max(occurences_lenght.values()) >= 15: column_width = max(occurences_lenght.values()) + 2 

print(separator)
print(f"{column_name[0]}|{column_name[1]: ^{column_width}}|{column_name[2]}")
print(separator)

for lenght in sorted(list(occurences_lenght.keys())):
    stars = "*" * occurences_lenght[lenght]
    print(f" {lenght: >2}|{stars: <{column_width}}|{occurences_lenght[lenght]}", sep="\n")
print(separator)