import os
import datetime
liga = []
fecha_partido = []

def registrar_equipo():
    print("\n--- REGISTRO DE EQUIPOS ---")
    nombre_nuevo_equipo = input('Ingrese el nombre del equipo: ').capitalize()

    if not nombre_nuevo_equipo:
        print("\n¡Error! El nombre del equipo no puede estar vacío.")
        return

    for equipo_registrado in liga:
        if nombre_nuevo_equipo == equipo_registrado[0]:
            print(f"\n¡Error! El equipo '{nombre_nuevo_equipo}' ya está registrado.")
            return

    liga.append([nombre_nuevo_equipo, 0, 0, 0, 0, 0, 0, 0]) 
    print(f"\n¡Éxito! El equipo '{nombre_nuevo_equipo}' ha sido registrado.")

def programar_fecha():

    print("-- PROGRAMAR FECHA DEL PARTIDO --")

    liga = [["Equipo Local"], ["Equipo Visitante"]]
    fecha_partido = []
    while True:
        print("\nIngresa los datos de la fecha:")
        dia_texto = input("Día (DD): ")
        mes_texto = input("Mes (MM): ")
        año_texto = input("Año (AAAA): ")

        try:
           
            dia_num = int(dia_texto)
            mes_num = int(mes_texto)
            año_num = int(año_texto)

            datetime.datetime(año_num, mes_num, dia_num)
            break

        except ValueError:
            print("\n¡Error! La fecha ingresada no es válida. Revisa los números e inténtalo de nuevo.")
  

        fecha_partido.append(fecha_partido)

        print("\n¡Fecha programada con éxito!")
        print(f"El partido {liga[0][0]} vs {liga[1][0]} ")

def registrar_marcador():
    print("--- REGISTRAR MARCADOR DEL PARTIDO ---")

    if len(liga) < 2:
        print("\n¡Error! Debes registrar al menos 2 equipos.")
        return

    print("\n¿Qué partido se jugó?")
    for i, equipo in enumerate(liga):
        print(f"{i + 1}. {equipo[0]}")
    
    try:
        idx_local = int(input("Elige el número del equipo local: ")) - 1
        idx_visitante = int(input("Elige el número del equipo visitante: ")) - 1
        
        equipo_local = liga[idx_local]
        equipo_visitante = liga[idx_visitante]
            
    except (ValueError, IndexError):
        print("\n¡Error! Selección de equipo no válida.")
        return
        
    print(f"\nPartido: {equipo_local[0]} vs {equipo_visitante[0]}")

    while True:
        try:
            goles_local = int(input(f"Goles de {equipo_local[0]}: "))
            if goles_local >= 0: 
                break
            else:
                print("¡Error! Los goles no pueden ser un número negativo.")
        except ValueError:
            print("¡Error! Debes ingresar un número.")
            
    while True:
        try:
            goles_visitante = int(input(f"Goles de {equipo_visitante[0]}: "))
            if goles_visitante >= 0:
                break
            else:
                print("¡Error! Los goles no pueden ser un número negativo.")
        except ValueError:
            print("¡Error! Debes ingresar un número.")

    equipo_local[1] += 1     
    equipo_visitante[1] += 1 

    equipo_local[5] += goles_local     
    equipo_local[6] += goles_visitante 
    equipo_visitante[5] += goles_visitante 
    equipo_visitante[6] += goles_local     

    if goles_local > goles_visitante:
        equipo_local[2] += 1  
        equipo_local[7] += 3
        equipo_visitante[4] += 1 
    elif goles_visitante > goles_local:
        equipo_visitante[2] += 1 
        equipo_visitante[7] += 3
        equipo_local[4] += 1     
    else:
        equipo_local[3] += 1     
        equipo_local[7] += 1    
        equipo_visitante[3] += 1 
        equipo_visitante[7] += 1 

    print("\n¡Marcador registrado y estadísticas actualizadas!")


def mas_goles_contra():
    print("--- EQUIPO CON MÁS GOLES EN CONTRA ---")

    if not liga:
        print("\nNo hay equipos registrados para analizar.")
        return 

    equipo_con_mas_goles = liga[0] 

    for equipo_actual in liga:
     
        if equipo_actual[6] > equipo_con_mas_goles[6]:
 
            equipo_con_mas_goles = equipo_actual

    print(f"\nEl equipo que ha recibido más goles en contra es: {equipo_con_mas_goles[0]}")
    print(f"Ha recibido un total de {equipo_con_mas_goles[6]} goles.")
def mas_goles_favor():
    print("\n--- EQUIPO CON MÁS GOLES A FAVOR (MÁS GOLEADOR) ---")

    if not liga:
        print("\nNo hay equipos registrados para analizar.")
        return

    equipo_mas_goleador = liga[0]

    for equipo_actual in liga:
     
        if equipo_actual[5] > equipo_mas_goleador[5]:
           
            equipo_mas_goleador = equipo_actual

    print(f"\nEl equipo más goleador es: {equipo_mas_goleador[0]}")
    print(f"Ha marcado un total de {equipo_mas_goleador[5]} goles.")
    

def registro_plantel(liga):
    print('\n--- REGISTRO DE PLANTEL ---')

    if not liga:
        print("No hay equipos registrados.")
        return

    print("Equipos disponibles:")
    for i, equipo_en_lista in enumerate(liga, start=1):
        print(f'{i}. {equipo_en_lista[0]}')

    try:
        opcion = int(input('\nSelecciona un número de equipo: '))
        equipo_seleccionado = liga[opcion - 1]
    except (ValueError, IndexError):
        print("¡Error! Selección no válida.")
        return

    if len(equipo_seleccionado) < 9:
        equipo_seleccionado.append([])

    print(f"\n--- Registrando miembro para {equipo_seleccionado[0]} ---")
    nombre_miembro = input("Ingrese el nombre del jugador/técnico: ").title()
    cargo_miembro = input("Ingrese el cargo (Ej: DT, Delantero, etc.): ").upper()

    nuevo_miembro = {"nombre": nombre_miembro, "cargo": cargo_miembro}

    equipo_seleccionado[8].append(nuevo_miembro)
    
    print(f"\n¡Éxito! Se ha añadido a {nombre_miembro} ({cargo_miembro}) al plantel.")
    print(f"\nPlantel actual de {equipo_seleccionado[0]}:")
    for miembro in equipo_seleccionado[8]:
        print(f'- {miembro["nombre"]} ({miembro["cargo"]})')

    


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
                registro_plantel(liga)
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