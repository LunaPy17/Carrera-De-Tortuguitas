import turtle
import random

# Configuración inicial de la ventana
ventana = turtle.Screen()
ventana.title("Carrera de tortugas")
ventana.bgcolor("lightgreen")
ventana.setup(720, 500)

# Línea de inicio
linea_inicio = turtle.Turtle()
linea_inicio.penup()
linea_inicio.goto(-280, 170)
linea_inicio.pendown()
linea_inicio.goto(-280, -170)

# Línea de meta
linea_meta = turtle.Turtle()
linea_meta.penup()
linea_meta.goto(280, 170)
linea_meta.pendown()
linea_meta.goto(280, -170)

# Tortugas
tortugas = []
colores = ["red", "orange", "blue", "green"]
for i in range(4):
    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.color(colores[i])
    tortuga.penup()
    tortuga.goto(-320, 150 - i * 100)
    tortuga.pendown()
    tortugas.append(tortuga)

# Controles del juego
controles = turtle.Turtle()
controles.hideturtle()
controles.penup()
controles.goto(-270, -240)
controles.write("Controles:\nReiniciar >>> R\nIniciar >>> Espacio", font=("Arial", 16, "normal"))

# Función para avanzar las tortugas
def avanzar():
    ganador = None
    for tortuga in tortugas:
        if ganador is None:
            # Avanzar la tortuga de forma aleatoria
            avance = random.randint(1, 20)
            tortuga.forward(avance)

            # Verificar si la tortuga ha llegado a la meta
            if tortuga.xcor() >= 300:
                ganador = tortuga
                color_original = ganador.color()[0]
                ganador.color("black")

                for i in range(10):
                    ganador.forward(5)
                    ganador.backward(5)

                ganador.color(color_original)
                controles.clear()
                controles.write("¡La tortuga " + color_original + " ha ganado!", font=("Arial", 16, "normal"))
                ventana.onkey(reiniciar, "r")
        else:
            ":("

    if ganador is None:
        # Programar la siguiente llamada a la función avanzar
        ventana.ontimer(avanzar, 100)

# Función para reiniciar la carrera
def reiniciar():
    global ganador
    # Borrar todo y dibujar de nuevo las tortugas y la línea de meta
    for tortuga in tortugas:
        tortuga.hideturtle()
    tortugas.clear()
    linea_meta.clear()
    linea_inicio.clear()
    # Eliminar las tortugas anteriores y crear nuevas tortugas
    for tortuga in tortugas:
        tortuga.clear()

    # Desactivar los controles
    ventana.onkey(None, "space")
    ventana.onkey(None, "r")

    # Dibujar de nuevo la línea de inicio y la línea de meta
    linea_inicio.penup()
    linea_inicio.goto(-280, 170)
    linea_inicio.pendown()
    linea_inicio.goto(-280, -170)
    linea_meta.penup()
    linea_meta.goto(280, 170)
    linea_meta.pendown()
    linea_meta.goto(280, -170)

    # Crear las tortugas de nuevo
    for i in range(4):
        tortuga = turtle.Turtle()
        tortuga.shape("turtle")
        tortuga.color(colores[i])
        tortuga.penup()
        tortuga.goto(-320, 150 - i * 100)
        tortuga.pendown()
        tortugas.append(tortuga)

    # Configurar los controles del juego
    ganador = None
    ventana.onkey(reiniciar, "r")
    ventana.onkeypress(avanzar, "space")
    ventana.listen()

    # Mostrar los controles de nuevo
    controles.clear()
    controles.goto(-270, -240)
    controles.write("Controles:\nReiniciar >>> R\nIniciar >>> Espacio", font=("Arial", 16, "normal"))

ventana.onkeypress(avanzar, "space")
ventana.onkey(reiniciar, "r")
ventana.listen()

turtle.mainloop()