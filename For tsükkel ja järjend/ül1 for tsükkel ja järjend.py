# Alex Karu
list1 = ['Tartu', 'Tallin', 'Viljandi', 'Narva', 'Haapsalu', 'Paide', 'Valga']  # list Eesti linna nimedega
lisiti_pikkus = (len(list1))  # annab listi pikkuse
list1.sort()  # sorteerib listi tähestikulises järjekorras
for linnad in list1:  # tsükkel
    print('Järjendis on: ', lisiti_pikkus, ' linna')  # prindib, kui palju linnu on listis
    print(linnad)  # prindib ühe linna

