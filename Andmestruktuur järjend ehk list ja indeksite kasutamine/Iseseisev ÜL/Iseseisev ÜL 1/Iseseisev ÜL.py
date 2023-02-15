# Alex Karu

# Loab Sammud.txt failis olevad andmed
nimekiri = []
f = open('Sammud.txt', encoding='utf-8')
for rida in f:
    nimekiri.append(rida.strip())
f.close()
print(nimekiri)

# Teeb nimekiri listi milles on string väärtused numbrid listiks milles on int väärtused
numbrid = list(map(int, nimekiri))


def arvude_jarjend(arv):  # funktsioon, mis lisab järjendis aru prindib selle välja nii kaua, kui järjendis on arve
    summa = 0
    for n in arv:  # tsükkel
        summa += n  # inkremendib summa n võrra
        print(summa)  # prindib summa

    # Prindib päeva keskmise sammude arvu
    paeva_keskmine = summa / len(numbrid)
    print("Päeva keskmine sammude arv on: ",  paeva_keskmine)

    # Prindib nädala kõrgeim sammude arvu
    max_value = max(numbrid)
    print("Nädala kõrgeim sammude arv on: ", (max(numbrid)), ",", numbrid.index(max_value), "päeval")

    # Prindib nädala mdalaima sammude arvu
    min_valu = min(numbrid)
    print("Nädala madalaim sammude arv on: ", min(numbrid), ",", numbrid.index(min_valu), "päeval")


print(arvude_jarjend(numbrid))
