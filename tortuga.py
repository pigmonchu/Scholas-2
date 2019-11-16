import turtle
tortu = turtle.Turtle ()

tortu.shape ("turtle")
tortu.speed(-1)

def flor(tipo):
    for nr in range (18):
        if tipo == 'Cu':
            cuadrado()
        elif tipo == 'C':
            tortu. circle (40)
        elif tipo = 'T':
            triangulo()
        tortu. left (20)
    tallo(200)
 

def tallo():
    tortu.right (90)
    tortu.forward ()


def triangulo():
    for nr in range (3):
        tortu.forward (200)
        tortu.left (120)


def cuadrado():
    for nr in range (4):
        tortu.forward (200)
        tortu.left (90)

print ("¿Cómo quieres dibujar tu flor: con C (circulos), con T (triángulos) o con Cu (Cuadrados)?")
eleccion = input ()

if eleccion == "Cu":
    tortu.color ("red")
    
elif eleccion == "T":
    tortu.color ("green")
    
elif eleccion == "C":
    tortu.color ("blue")


flor(eleccion)



    


'''    
else:
    print ("Has escrito la respuesta incorrecta")
'''



