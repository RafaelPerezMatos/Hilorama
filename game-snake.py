import turtle
import time
import random

posponer = 0.1

score = 0
high_score = 0

#Configuracion de la ventana
wn = turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor("black")
wn.setup(width= 600, height= 600)
wn.tracer(0)

#cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
