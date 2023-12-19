import random

def randomWordGenerate() -> str:
    wordList = ["alma","elkelkposztásítottalanítottátok","citrom","alma","barom","kys",]
    return random.choice(wordList)

wordTemplate = []
word = randomWordGenerate()
#print(word)
print()
#tip = input("Írjon be egy betűt")
for i in range(len(word)):
    wordTemplate.append("_")
print("".join(wordTemplate))
print("\nTaláld ki a gondolt szót! 10 lehetőséged van,hogy megadj betűket")
tip = input("Az ön tippje: ")


if tip not in word:
    print("Szar vagy!")
else:
    for i in range(len(word)):
        if word[i] == tip:
            wordTemplate[i] = tip
print("".join(wordTemplate))           