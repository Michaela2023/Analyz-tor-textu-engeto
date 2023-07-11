"""
projekt_1.py: první projekt do Engeto Online Python Akademie-Textový analyzátor
author: Michaela Řežábková
email: rezabkova.michaela@seznam.cz
discord:Míša Ř#8858 """

"""
"""



import re
import matplotlib.pyplot as plt

registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

jmeno = input("Zadejte přihlašovací jméno: ")
heslo = input("Zadejte heslo: ")

if jmeno in registrovani_uzivatele and registrovani_uzivatele[jmeno] == heslo:
    print("Vítejte, " + jmeno + "! Můžete začít analyzovat texty. Vyberte prosím text v rozmezí od 1-3")
else:
    print("Přihlašovací údaje nejsou správné. Program bude ukončen.")

TEXTS = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley. 
    ''',
    '''
    At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.
    ''',
    '''
    The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.
    '''
]

def analyze_text(text):
    word_lengths = []
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        word_lengths.append(len(word))

    print("Počet slov:", len(words))
    print("Počet slov začínajících velkým písmenem:", len(re.findall(r'\b[A-Z][a-zA-Z]*\b', text)))
    print("Počet slov psaných velkými písmeny:", len(re.findall(r'\b[A-Z]+\b', text)))
    print("Počet slov psaných malými písmeny:", len(re.findall(r'\b[a-z]+\b', text)))
    print("Počet čísel:", len(re.findall(r'\b[0-9]+\b', text)))
    print("Součet všech čísel v textu:", sum(int(num) for num in re.findall(r'\b[0-9]+\b', text)))

    # Vytvoření histogramu
    plt.hist(word_lengths, bins=range(min(word_lengths), max(word_lengths) + 2, 1), edgecolor='black')
    plt.xlabel('Délka slova')
    plt.ylabel('Četnost')
    plt.title('Četnost délky slov')
    plt.xticks(range(min(word_lengths), max(word_lengths) + 1))
    plt.show()

text_number = int(input("Zadejte číslo textu (1-3): "))

if text_number >= 1 and text_number <= 3:
    text = TEXTS[text_number - 1]
    analyze_text(text)
else:
    print("Neplatné číslo textu. Zadejte číslo od 1 do 3.")
