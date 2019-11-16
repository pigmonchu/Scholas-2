import turtle

t = turtle.Turtle ()

tipo = input ("¿Petalos cuadrados (C), circulos (CI), o triangulos (T)?: ")

x = int(input ("¿Cuantos petalos quieres?: "))

t.speed(-1)
t.color ("green")
t.right(90)
t.forward(100)
t.right(180)
t.forward(100)
t.right(90)
t.circle(50)
t.penup()
t.left(90)
t.forward(50)
t.pendown()

t.right(180-((360/x)/2))

if tipo == "CI":
    t.color("blue")
    if x<=5:
        s=35
    elif x>5:
        s=(200/x)
    for n in range(x):
        t.penup()
        t.forward(50)
        t.right(90)
        t.pendown()
        t.circle(s)
        t.right(90)
        t.penup()
        t.forward(50)
        t.right(180-(360/x))
        
elif tipo == "C":
    t.color("red")
    if x<=5:
        s=50
    elif x>5:
        s=(350/x)    
    for n in range(x):
        t.penup()
        t.forward(50)
        t.right(90)
        t.pendown()
        t.forward(s/2)
        for r in range (3):
            t.left(90)
            t.forward(s)
        t.left(90)
        t.forward(s/2)
        t.right(90)
        t.penup()
        t.forward(50)
        t.right(180-(360/x))

elif tipo == "T":
    t.color("yellow")
    if x<=5:
        s=50
    elif x>5:
        s=(350/x)    
    for n in range(x):
        t.penup()
        t.forward(50)
        t.right(90)
        t.pendown()
        t.forward(s/2)
        for r in range (2):
            t.left(120)
            t.forward(s)
        t.left(120)
        t.forward(s/2)
        t.right(90)
        t.penup()
        t.forward(50)
        t.right(180-(360/x))
        
        
else:
    print("Respuesta incorrecta")
      