def flor(tortuga, tipo, lado):
    for nr in range (18):
        if tipo == 'Cu':
            cuadrado(tortuga, lado)
        elif tipo == 'C':
            tortuga. circle (40)
        elif tipo == 'T':
            triangulo(tortuga)
        tortuga. left (20)
    tallo(tortuga, 200)
 

def tallo(s,longitud):
    s.right (90)
    s.forward (longitud)


def triangulo(nose):
    for nr in range (3):
        nose.forward (200)
        nose.left (120)


def cuadrado(t, lado):
    for nr in range (4):
        t.forward (lado)
        t.left (90)
