import turtle
import flors

tortu = turtle.Turtle ()

tortu.shape ("turtle")
tortu.speed(-1)


eleccion = input("¿Cómo quieres dibujar tu flor: con C (circulos), con T (triángulos) o con Cu (Cuadrados)?")

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



