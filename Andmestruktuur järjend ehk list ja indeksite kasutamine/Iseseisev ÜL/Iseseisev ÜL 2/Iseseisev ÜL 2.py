#  Alex Karu
import turtle


def juhendi_lugemine(kilpkonn):
    juhendid = []
    with open(kilpkonn, 'r') as f:
        for rida in f:
            cmd = rida.strip().split(' ')
            juhendid.append(cmd)
    return juhendid


def joonistamine(kujund, kilpkonn):
    for cmd in kujund:
        if cmd[0] == 'edasi':
            kilpkonn.forward(int(cmd[1]))
        elif cmd[0] == 'tagasi':
            kilpkonn.backward(int(cmd[1]))
        elif cmd[0] == 'paremale':
            kilpkonn.right(int(cmd[1]))
        elif cmd[0] == 'vasakule':
            kilpkonn.left(int(cmd[1]))


kordade_arv = int(input("Mitu korda kujund joonistada? "))
juhend = juhendi_lugemine('kilpkonn.txt')
a = input("Sisestage programmi pealkiri ")
b = input("Sisestage värv (inglise keeles) ")
turtle.bgcolor(b)
turtle.title(a)
aken = turtle.Screen()
k = turtle.Turtle()
k.speed(0)


for i in range(kordade_arv):
    joonistamine(juhend, k)
turtle.exitonclick()
