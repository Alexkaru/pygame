# Alex Karu

arvud = [10, 21, 4, 45, 66, 93, 1]  # list

paaris = 0  # paris arvud
paaritu = 0  # paaritud arvud
for arv in arvud:  # tsükkel, mis kontrollib, kas arv on paaris või paaritu
    if arv % 2 == 0:  # kui arvu kahega jagamisel on jääk 0 siis
        paaris += 1  # lisab paaris arvudele 1

    else: # muul juhul
        paaritu += 1  # lisab paaritutele arvudele 1

print('Paaris arve on: ', paaris)  # prindib paaris arvud
print('Paarituid arve on: ', paaritu)  # prindib paaritud arvud
