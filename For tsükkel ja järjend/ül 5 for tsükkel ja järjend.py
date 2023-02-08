# Alex Karu
arvud = [10, 61, 2, 14, 42, 24, 7, 5]  # list


def arvude_jarjend(arv):  # funktsioon, mis lisab järjendis aru prindib selle välja nii kaua, kui järjendis on arve
    summa = 0
    for n in arv:  # tsükkel
        summa += n  # inkremendib summa n võrra
        print(summa)  # prindib summa


if arvud == []:  # kui arvud on tühi list prindib null
    print(0)
print(arvude_jarjend(arvud))
