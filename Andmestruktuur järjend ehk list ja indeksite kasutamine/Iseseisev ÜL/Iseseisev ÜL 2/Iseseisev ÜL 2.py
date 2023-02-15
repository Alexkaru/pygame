#  Alex Karu


jarjend = []
f = open("kilpkonn.txt")
for rida in f:
    jarjend.append(rida.strip())
f.close()
print(jarjend)
