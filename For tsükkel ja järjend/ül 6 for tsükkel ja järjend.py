# Alex Karu

arvud = [10, 21, 4, 45, 66, 93, 1]

paaris = 0
paaritu = 0
for arv in arvud:
    if arv % 2 == 0:
        paaris += 1

    else:
        paaritu += 1

print('Paaris arve on: ', paaris)
print('Paarituid arve on: ', paaritu)
