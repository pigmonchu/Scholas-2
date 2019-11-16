import turtle
import flors

tortu = turtle.Turtle ()

tortu.shape ("turtle")
tortu.speed(-1)


eleccion = input("¿Cómo quieres dibujar tu flor: con C (circulos), con T (triángulos) o con Cu (Cuadrados)?")
lado = input("Tamaño de pétalo: ")
lado_num = int(lado)

if eleccion in ['Cu', 'C', 'T']:

    if eleccion == "Cu":
        tortu.color ("red")
        
    elif eleccion == "T":
        tortu.color ("green")
        
    elif eleccion == "C":
        tortu.color ("blue")

    flors.flor(tortu, eleccion, lado_num)
else:
    print("Elige lo que toca")



    


'''    
else:
    print ("Has escrito la respuesta incorrecta")
'''



