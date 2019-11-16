import turtle
tortu = turtle.Turtle ()

tortu.shape ("turtle")


def cuadrado:
    for nr in range (4):
        tortu.forward (200)
        tortu.left (90)

print ("¿Cómo quieres dibujar tu flor: con C (circulos), con T (triángulos) o con Cu (Cuadrados)?")
eleccion = input ()

if eleccion == "Cu":
    tortu.color ("red")
    for nr in range (18):
        cuadrado()
        tortu. left (20)
    tortu.right (90)
    tortu.forward (500)
    
elif eleccion == "T":
    tortu.color ("green")
    for nr in range (18):
        for nr in range (3):
            tortu.forward (200)
            tortu.left (120)
        tortu.left (20)
    tortu.right (90)
    tortu.forward (500)
        
elif eleccion == "C":
    tortu.color ("blue")
    for nr in range (18):
        tortu. circle (40)
        tortu.left (20)
    tortu.right (90)
    tortu.forward (500)
    
else:
    print ("Has escrito la respuesta incorrecta")
    



    






