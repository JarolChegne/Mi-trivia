
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import random
puntaje = random.randint(0, 10)

import time
iniciar_trivia = True
intentos = 0

print("\033[34mBienvenido a mi trivia sobre cultura general")
print("Pondremos a prueba y desafiaremos tusconocimientos")
print("Descubre con esta trivia hasta donde llegan tus conocimientos. Comparte tu resultado y reta a tus amigos, ¡Expande tu cultura!\033[39m")
print(YELLOW + "En este momento tienes", puntaje, "puntos" + RESET)
time.sleep(2)


  
nombre = input(YELLOW + "Antes de comenzar ingresa tu nombre: " + RESET)
time.sleep(2)

print(YELLOW + "\n Hola", nombre,"responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+ RESET)

time.sleep(2)
 


print(CYAN + "1) ¿Cuál es la última letra del alfabeto griego?")
print("a) Alpha")
print("b) Omega")
print("c) Beta")
print("d) Zeta" + RESET)

respuesta_1 = input(BLUE + "\nCúal es tu respuesta: " + RESET)

while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_1 == "b":
    puntaje += 10
    print(
        GREEN +
        "\n¡Excelente!, buen trabajo, aunque solo estamos empezando no te vayas a confiar",
        nombre, "!" + RESET)
else:
    print(RED + "Incorrecto", nombre, "!" + RESET)

print(CYAN + nombre, "llevas", puntaje, "puntos" + RESET)
time.sleep(2)

print(CYAN + "\n2) ¿Como se le llama al conjunto de cerdos ?")
print("a) Bandada")
print("b) Cardumen")
print("c) Archipielago")
print("d) Piara" + RESET)

respuesta_2 = input(BLUE + "\nTu respuesta: " + RESET)

while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_2 == "a":
    print(RED + "Incorrecto!", nombre, "bandada es un conjuto de aves")

elif respuesta_2 == "b":
    print("Incorrecto!", nombre, "cardumen es un conjunto de peces")
elif respuesta_2 == "c":
    print("Incorrecto!", nombre,
          "archipielago es un conjunto de islas" + RESET)
else:
    puntaje += 10
    print(GREEN + "Muy bien", nombre, "!" + RESET)

print(CYAN + nombre, "llevas", puntaje, "puntos" + RESET)
time.sleep(2)

print(
    YELLOW +
    "\n Apartir de este momento se te restaran puntos si tu respuesta es incorrecta. Vamos aumentando el nivel ¡Buena suerte!\n"
    + RESET)
time.sleep(2)

print(CYAN + "\n3) ¿Quién es el dios romano de la guerra?")
print("a) Ares")
print("b) Jupiter")
print("c) Marte")
print("d) Belerofonte" + RESET)

respuesta_3 = input(BLUE + "\nTu respuesta: " + RESET)

while respuesta_3 not in ("a", "b", "c", "d"):
 respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_3 == "a":
    print(RED + "Totalmente incorrecto! ...")
    puntaje = puntaje - 5
elif respuesta_3 == "d":
    print("Totalmente incorrecto...")
    puntaje = puntaje - 5
elif respuesta_3 == "b":
    print("Totalmente incorrecto! ..." + RESET)
    puntaje = puntaje - 5
else:
    print(GREEN + "Correcto! ..." + RESET)
    puntaje = puntaje + 10
    print(CYAN + nombre, "llevas", puntaje, "puntos" + 
 RESET)

    time.sleep(2)

print(CYAN + "\n4) Según la leyenda ¿cómo murió el Papa Adriano IV en 1159?")
print("a) Tragándose una mosca")
print("b) Cayéndose de un balcón")
print("c) Chocandose contra una puerta")
print("d) Cayéndose de un caballo" + RESET)

respuesta_4 = input(BLUE + "\nTu respuesta: " + RESET)

while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_4 == "a":
    print(RED + "Totalmente incorrecto! ...")
    puntaje = puntaje - 5
elif respuesta_4 == "d":
    print("Totalmente incorrecto...")
    puntaje = puntaje - 5
elif respuesta_4 == "c":
    print("Totalmente incorrecto! ..." + RESET)
    puntaje = puntaje - 5
else:
    print(GREEN + "Correcto! ..." + RESET)
    puntaje = puntaje + 10
    print(CYAN + nombre, "llevas", puntaje, "puntos" + RESET)
    time.sleep(2)

print(CYAN +"\n5) Aproximadamente ¿qué porcentaje de la superficie de la tierra es agua?"
)
print("a) 10%")
print("b) 50%")
print("c) 70%")
print("d) 90%" + RESET)

respuesta_5 = input(BLUE + "\nTu respuesta: " + RESET)

while respuesta_5 not in ("a", "b", "c", "d"):
    respuesta_5 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_5 == "a":
    print(RED + "Totalmente incorrecto! ...")
    puntaje = puntaje - 5
elif respuesta_5 == "d":
    print("Totalmente incorrecto!...")
    puntaje = puntaje - 5
elif respuesta_5 == "b":
    print("Totalmente incorrecto! ..." + RESET)
    puntaje = puntaje - 5
else:
    print(GREEN + "Correcto! ..." + RESET)
    puntaje = puntaje + 10
    print(CYAN + nombre, "llevas", puntaje, "puntos" + RESET)
    time.sleep(2)

print(CYAN + "\n6) ¿Qué significa PALIMPSESTO?")
print("a) Un personaje que carece de seriedad.")
print(
    "b) Razonamientopor el que la verdad de una proposición se prueba demostrando la imposibilidad o absurdo de la proposición contraria."
)
print("c) Algo que sirve como ayuda auxiliar.")
print("d) Manuscrito cuya escritura ha sido eliminado con objeto de escribir otro texto encima."+ RESET)

respuesta_6 = input(BLUE + "\nTu respuesta: " + RESET)

while respuesta_6 not in ("a", "b", "c", "d"):
    respuesta_6 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_6 == "a":
    print(RED + "Totalmente incorrecto! ...")
    puntaje = puntaje - 5
elif respuesta_6 == "c":
    print("Totalmente incorrecto!...")
    puntaje = puntaje - 5
elif respuesta_6 == "b":
    print("Totalmente incorrecto! ..." + RESET)
    puntaje = puntaje - 5
else:
    print(GREEN + "Correcto! ..." + RESET)
    puntaje = puntaje + 10
    print(CYAN + nombre, "llevas", puntaje, "puntos" + RESET)
    time.sleep(2)

print(CYAN + "\n7) ¿En qué año murió Bob Marley?")
print("a) 1981.")
print("b) 1986.")
print("c) 1991.")
print("d) 2003." + RESET)

respuesta_7 = input(BLUE + "\nTu respuesta: " + RESET)

while respuesta_7 not in ("a", "b", "c", "d"):
    respuesta_7 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_7 == "b":
    print(RED + "Totalmente incorrecto! ...")
    puntaje = puntaje - 5
elif respuesta_7 == "c":
    print("Totalmente incorrecto!...")
    puntaje = puntaje - 5
elif respuesta_7 == "b":
    print("Totalmente incorrecto! ..." + RESET)
    puntaje = puntaje - 5
else:
    print(GREEN + "Correcto! ..." + RESET)
    puntaje = puntaje + 10
    print(CYAN + nombre, "llevas", puntaje, "puntos" + RESET)
    time.sleep(2)

print(CYAN +"\n8) ¿Cuál es el nombre de la herramienta necesaria para jugar al billar?")
print("a) Palo.")
print("b) Snooker.")
print("c) Bundigo.")
print("d) Taco." + RESET)

respuesta_8 = input(BLUE + "\nTu respuesta: " + RESET)

while respuesta_8 not in ("a", "b", "c", "d"):
    respuesta_8 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_8 == "a":
    print(RED + "Totalmente incorrecto! ...")
    puntaje = puntaje - 5
elif respuesta_8 == "b":
    print("Totalmente incorrecto!...")
    puntaje = puntaje - 5
elif respuesta_8 == "c":
    print("Totalmente incorrecto! ..." + RESET)
    puntaje = puntaje - 5
else:
    print(GREEN + "Correcto! ..." + RESET)
    puntaje = puntaje + 10
    print(CYAN + nombre, "llevas", puntaje, "puntos" + RESET)
    time.sleep(2)

print(CYAN +"\n9) ¿Cuál es el estado estadunidense más cercano a la antigua Unión Soviética?")
print("a) Alaska.")
print("b) California.")
print("c) Florida.")
print("d) Texas." + RESET)

respuesta_9 = input(BLUE + "\nTu respuesta: " + RESET)

while respuesta_9 not in ("a", "b", "c", "d"):
    respuesta_9 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_9 == "b":
    print(RED + "Totalmente incorrecto! ...")
    puntaje = puntaje - 5
elif respuesta_9 == "c":
    print("Totalmente incorrecto!...")
    puntaje = puntaje - 5
elif respuesta_9 == "b":
    print("Totalmente incorrecto! ..." + RESET)
    puntaje = puntaje - 5
else:
    print(GREEN + "Correcto! ..." + RESET)
    puntaje = puntaje + 10
    print(CYAN + nombre, "llevas", puntaje, "puntos" + RESET)
    time.sleep(2)

print(CYAN + "\n10) ¿Qué animal es la drosophila?")
print("a) Una rata.")
print("b) Una mosca.")
print("c) Un conejillo de Indias.")
print("d) Una cabra." + RESET)

respuesta_10 = input(BLUE + "\nTu respuesta: " + RESET)

while respuesta_10 not in ("a", "b", "c", "d"):
    respuesta_10 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_10 == "a":
    print(RED + "Totalmente incorrecto! ...")
    puntaje = puntaje - 5
elif respuesta_10 == "c":
    print("Totalmente incorrecto!...")
    puntaje = puntaje - 5
elif respuesta_10 == "b":
    print("Totalmente incorrecto! ..." + RESET)
    puntaje = puntaje - 5
else:
    print(GREEN + "Correcto! ..." + RESET)
    puntaje = puntaje + 10
    time.sleep(2)

print(BLUE + "\nGracias", nombre, "por jugar mi trivia, alcanzaste", puntaje,"puntos" + RESET)

