import os

liga = []
fecha_partido = []

def registrar_equipo():

    print("--- REGISTRO DE EQUIPOS ---")

    nombre_local = input("Ingresa el nombre del equipo local: ")
    nombre_visitante = input("Ingresa el nombre del equipo visitante: ")
                                        # PJ, PG, PE, PP, GF, GC, TP
    equipo_local = [nombre_local, [], [],0, 0, 0, 0, 0, 0, 0]
    equipo_visitante = [nombre_visitante, [], [], 0, 0, 0, 0, 0, 0, 0]

    liga.append(equipo_local)
    liga.append(equipo_visitante)

    print(f"\n¡Partido configurado con éxito!")
    print(f"Local: {liga[0][0]}")
    print(f"Visitante: {liga[1][0]}")
    print("\nEstructuras de datos creadas. Ahora puede registrar jugadores y cuerpo técnico.")

def programar_fecha():

    print("-- PROGRAMAR FECHA DEL PARTIDO --")

    fecha = input("Ingresa la fecha del partido (ej: DD/MM/AAAA): ")
    hora = input("Ingresa la hora del partido (ej: HH:MM): ")

    fecha_partido.append(fecha)
    fecha_partido.append(hora)

    print("\n¡Fecha programada con éxito!")
    print(f"El partido {liga[0][0]} vs {liga[1][0]} se jugará el {fecha} a las {hora}")

def registrar_marcador():
    print("--- REGISTRAR MARCADOR DEL PARTIDO ---")

    equipo_local = liga[0]
    equipo_visitante = liga[1]

    print(f"Partido: {equipo_local[0]} vs {equipo_visitante[0]}")

    goles_local = int(input(f"Goles de {equipo_local[0]}: "))
    goles_visitante = int(input(f"Goles de {equipo_visitante[0]}: "))

    equipo_local[3] += 1
    equipo_visitante[3] += 1

    equipo_local[7] += goles_local
    equipo_local[8] += goles_visitante
    equipo_visitante[7] += goles_visitante
    equipo_visitante[8] += goles_local

    if goles_local > goles_visitante:
        equipo_local[4] += 1     # Gana Local
        equipo_local[9] += 3
        equipo_visitante[6] += 1 # Pierde Visitante
    elif goles_visitante > goles_local:
        equipo_visitante[4] += 1 # Gana Visitante
        equipo_visitante[9] += 3
        equipo_local[6] += 1     # Pierde Local
    else:
        equipo_local[5] += 1     # Empate
        equipo_local[9] += 1
        equipo_visitante[5] += 1 # Empate
        equipo_visitante[9] += 1

    print("\n¡Marcador registrado y estadísticas actualizadas!")
    print(f"Resultado final: {equipo_local[0]} {goles_local} - {goles_visitante} {equipo_visitante[0]}")

def mas_goles_contra():
    print("--- EQUIPO CON MÁS GOLES EN CONTRA ---")
    
    equipo_local = liga[0]
    equipo_visitante = liga[1]

    contra_local = equipo_local[8]
    contra_visitante = equipo_visitante[8]

    print  (f'analisis de goles en conta: ')
    print (f'-{equipo_local[0]}: {contra_local} goles recibidos')
    print (f'- {equipo_visitante[0]}: {contra_visitante} goles recibidos')
    
    if contra_local > contra_visitante:
        print(f"\nResultado: El equipo con más goles en contra es {equipo_local[0]}.")
    elif contra_visitante > contra_local:
        print(f"\nResultado: El equipo con más goles en contra es {equipo_visitante[0]}.")
    else:
        print(f"\nResultado: Ambos equipos han recibido la misma cantidad de goles ({contra_local}).")

def mas_goles_favor():
    print ('--- EQUIPO CON MAS GOLES A FAVOR---')

    equipo_local = liga[0]
    equipo_visitante =liga [1]

    favor_local = [7] 
    favor_visitante = [7]

    print(f' analisis de goles a favor')
    print(f'-{equipo_local[0]}:{favor_local} goles recibidos')
    print(f'-{equipo_visitante[0]}:{favor_visitante} goles recibidos')

    if favor_local > favor_visitante:
        print(f"\nResultado: El equipo con más goles a favor es {equipo_local[0]}.")
    elif favor_visitante > favor_local:
        print(f"\nResultado: El equipo con más goles a favor es {equipo_visitante[0]}.")
    else:
        print('ambos equipos tienen la misma cantidad de goles a favor')
    

def registro_plantel(liga):
    print('---REGISTRO PLANTEL---')

    for i, liga in enumerate (liga,start=1):
        print (f'{i}. {liga}')

    opcion = int(input('selecciona un numero de equipo: '))

    equipo_seleccionado = liga[opcion - 1]

    equipo_seleccionado[1] = input("Ingrese el cargo del cuerpo tecnico: ")

    


MAIN_MENU = """
MENU PRINCIPAL
1. REGISTRAR EQUIPO
2. PROGRAMAR FECHA
3. REGISTRAR MARCADOR
4. EQUIPO CON MAS GOLES EN CONTRA
5. EQUIPO CON MAS GOLES A FAVOR
6. REGISTRO PLANTEL
7. VER EQUIPOS
8. SALIR
"""

def main():
    os.system("clear")
    while True:
        print(MAIN_MENU)
        opc = input(" = ")
        match opc:
            case "1":
                os.system("clear")
                registrar_equipo()
                x = input("Presione una tecla para continuar... ")
            case "2":
                os.system("clear")
                programar_fecha()
                x = input("Presione una tecla para continuar... ")
            case "3":
                os.system("clear")
                registrar_marcador()
                x = input("Presione una tecla para continuar... ")
            case "4":
                os.system("clear")
                mas_goles_contra()
                x = input("Presione una tecla para continuar... ")
            case "5":
                os.system("clear")
                mas_goles_favor()
                x = input("Presione una tecla para continuar... ")
            case "6":
                os.system("clear")
                registro_plantel()
                x = input("Presione una tecla para continuar... ")
            case "7":
                print(liga)
                x = input("Presione una tecla para continuar... ")
            case "8":
                break
            case _:
                print("ERROR...")
                x = input("Presione una tecla para continuar... ")

if __name__ == "__main__":
    main()