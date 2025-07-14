# Desafio
# Se puede colocar el nombre en la segunda solicitud. No pense que haria falta 
# Lo ingresado por el usuario sea lowerCase de tal forma de comparar minuscula con minuscula. Hecho
# Más de un turno con el bucle while. Hecho

nombre1 = input("Como se llamara el jugador 1?: ")
nombre2 = input("Como se llamara el jugador 2?: ")

ganadas_jugador1 = 0
ganadas_jugador2 = 0

while ganadas_jugador1 < 3 and ganadas_jugador2 < 3:
    jugador1 = input(f"Hola {nombre1}! Que eliges? Piedra, papel o tijeras?: ").strip().lower()
    jugador2 = input(f"Hola {nombre2}! Que eliges? Piedra, papel o tijeras?: ").strip().lower()
    condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijeras" and jugador2 == "papel"
    condicion4 = jugador2 == "piedra" and jugador1 == "tijeras"
    condicion5 = jugador2 == "papel" and jugador1 == "piedra"
    condicion6 = jugador2 == "tijeras" and jugador1 == "papel"
    if condicion1 or condicion2 or condicion3:
        print("Ha ganado:", nombre1)
        ganadas_jugador1 += 1
    elif condicion4 or condicion5 or condicion6:
        print("Ha ganado:", nombre2)
        ganadas_jugador2 += 1
    else:
        print("Ha sido un empate")

if ganadas_jugador1 == 3:
    print(f"Felicidades {nombre1}, has ganado la partida!") 
else:
    print(f"Felicidades {nombre2}, has ganado la partida!") 


#if jugador1 == jugador2:
#    print("Ha sido un empate!")
#elif condicion1 or condicion2 or condicion3:
#    print("Ha ganado:", nombre1)
#else:
#    print("Ha ganado:", nombre2)