from random import randint
from sty import fg, bg, ef, rs, Rule
while True:
    Solo_MultiP = input("Escribe \"A\" para jugar contra la maquina.\nEscribe \"B\" para jugar contra otro jugador.(Al mejor de 3)\nEscribe \"C\" para cancelar y cerrar el programa.\n\n\n>")
    Texto_Introduce_Numero_single_P = "Introduce un número del 1 al 3, siendo: 1:Piedra, 2: Papel, 3: Tijeras\n> "
    if Solo_MultiP == "A" or Solo_MultiP == "a":
        while True:
            try:
                eleccion_maquina = randint(1,3)
                eleccion_jugador = int(input(Texto_Introduce_Numero_single_P))
                eleccion_jugador2 = eleccion_jugador
                eleccion_maquina2 = eleccion_jugador2
                if eleccion_maquina2 == 1:
                    eleccion_maquina2 = "piedra"
                elif eleccion_maquina2 == 2:
                    eleccion_maquina2 = "papel"
                elif eleccion_maquina2 == 3:
                    eleccion_maquina2 = "tijeras"

                if eleccion_jugador2 == 1:
                    eleccion_jugador2 = "piedra"
                elif eleccion_jugador2 == 2:
                    eleccion_jugador2 = "papel"
                elif eleccion_jugador2 == 3:
                    eleccion_jugador2 = "tijeras"

                Perdido_Single_P = "Has perdido! El jugador 1 ha sacado {0} y y el jugador 2 ha sacado {1} \n\n".format(eleccion_jugador2,eleccion_maquina2)
                Ganador_Single_P = "Has Ganado! El jugador 1 ha sacado {0} y el jugador 2 ha sacado {1} \n\n".format (eleccion_jugador2,eleccion_maquina2)
                if eleccion_jugador > 3:
                    print("\nERROR: Escribe un número en el rango especificado\n")
                    break
                elif eleccion_jugador == eleccion_maquina:
                    
                    print("Habeis empatado! Ambos habeis sacado {0} \n\n".format(eleccion_jugador))
                elif eleccion_jugador == 1 and eleccion_maquina == 2:
                    
                    print(Perdido_Single_P)
                elif eleccion_jugador == 1 and eleccion_maquina == 3:
                    
                    print(Ganador_Single_P)
                elif eleccion_jugador == 2 and eleccion_maquina == 1:
                    print(Ganador_Single_P)
                elif eleccion_jugador == 2 and eleccion_maquina == 3:
                    print(Perdido_Single_P)
                elif eleccion_jugador == 3 and eleccion_maquina == 1:
                    print(Perdido_Single_P)
                elif eleccion_jugador == 3 and eleccion_maquina == 2:
                    print(Ganador_Single_P)
                elif eleccion_jugador == "C":
                    print("Saliendo...")
                    break
            except ValueError:
                print("\nERROR: Escribe un número en el rango especificado\n")
                break    
    elif Solo_MultiP == "B" or Solo_MultiP == "b":
        print("No implementado")
        for i in range(3):
            try:
                eleccionJugador_A = int(input("Jugador 1:" + Texto_Introduce_Numero_single_P))
                eleccionJugador_A_2 = eleccionJugador_A

                if eleccionJugador_A_2 == 1:
                    eleccionJugador_A_2 = "piedra"
                elif eleccionJugador_A_2 == 2:
                    eleccionJugador_A_2 = "papel"
                elif eleccionJugador_A_2 == 3:
                    eleccionJugador_A_2 = "tijeras"

                eleccionJugador_B = int(input("Jugador 2:" + Texto_Introduce_Numero_single_P))
                eleccionJugador_B_2 = eleccionJugador_B

                if eleccionJugador_B_2 == 1:
                    eleccionJugador_B_2 = "piedra"
                elif eleccionJugador_B_2 == 2:
                    eleccionJugador_B_2 = "papel"
                elif eleccionJugador_B_2 == 3:
                    eleccionJugador_B_2 = "tijeras"

                Perdido_Single_P = "¡Gana el jugador 2! El jugador 1 ha sacado {0} y el jugador 2 ha sacado {1} \n\n".format(eleccionJugador_A_2,eleccionJugador_B_2)
                Ganador_Single_P = "¡Gana el jugador 1! El jugador 1 ha sacado {0} y el jugador 2 ha sacado {1} \n\n".format (eleccionJugador_A_2,eleccionJugador_B_2)
                if eleccionJugador_A > 3:
                    print("\nERROR: Escribe un número en el rango especificado\n")
                    break
                elif eleccionJugador_A == eleccionJugador_B:                 
                    print("Habeis empatado! Ambos habeis sacado {0} \n\n".format(eleccionJugador_A))
                elif eleccionJugador_A == 1 and eleccionJugador_B == 2:                
                    print(Perdido_Single_P)
                elif eleccionJugador_A == 1 and eleccionJugador_B == 3:                    
                    print(Ganador_Single_P)
                elif eleccionJugador_A == 2 and eleccionJugador_B == 1:
                    print(Ganador_Single_P)
                elif eleccionJugador_A == 2 and eleccionJugador_B == 3:
                    print(Perdido_Single_P)
                elif eleccionJugador_A == 3 and eleccionJugador_B == 1:
                    print(Perdido_Single_P)
                elif eleccionJugador_A == 3 and eleccionJugador_B == 2:
                    print(Ganador_Single_P)
                elif eleccionJugador_A == "C":
                    print("Saliendo...")
                    break
            except ValueError:
                print("\nERROR: Escribe un número en el rango especificado\n")
                break    
    elif Solo_MultiP == "C" or Solo_MultiP == "c":
        break 
        break
        exit(0)
    else:
        print("\nERROR: Valor Incorrecto \n")
        
