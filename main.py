import os
import sys
from datetime import datetime
from tabulate import tabulate

# Lista para guardar equipos
# [nombre, partidos_jugados, victorias, empates, derrotas, goles_favor, goles_contra, puntos]
liga = []

# Lista para guardar partidos programados
# [equipo_local, equipo_visitante, fecha_formateada]
fecha_partido = []

# Funcion para mostrar partidos programados
def mostrar_partidos_programados(fecha_partido):
    # Crear lista de partidos con números
    partidos_tabla = []
    for i, partido in enumerate(fecha_partido, 1):
        # [equipo_local, equipo_visitante, fecha_formateada]
        partidos_tabla.append([
            i,              # #
            partido[0],     # Equipo Local
            partido[1],     # Equipo Visitante
            partido[2]      # Fecha
        ])
    
    # Mostrar tabla usando tabulate
    print(tabulate(partidos_tabla, headers=["#", "Local", "Visitante", "Fecha"], tablefmt="grid"))

# Funcion para mostrar equipos
def mostrar_equipos(liga):
    # Crear lista de equipos con números
    equipos_tabla = []
    for i, equipo in enumerate(liga, 1):
        equipos_tabla.append([i, equipo[0]])
    
    # Mostrar tabla usando tabulate
    print(tabulate(equipos_tabla, headers=["#", "Equipo"], tablefmt="grid"))

def ver_equipos_inscritos(liga):
    """
    Función para mostrar todos los equipos inscritos con sus estadísticas
    """
    limpiar_pantalla()
    print("""

    
  .---.   .-./`)  .-_'''-.     ____             _______      .-''-.,---------.         .-------.  .---.       ____      ____     __  
  | ,_|   \ .-.')'_( )_   \  .'  __ `.         \  ____  \  .'_ _   \          \        \  _(`)_ \ | ,_|     .'  __ `.   \   \   /  / 
,-./  )   / `-' |(_ o _)|  '/   '  \  \        | |    \ | / ( ` )   `--.  ,---'        | (_ o._),-./  )    /   '  \  \   \  _. /  '  
\  '_ '`)  `-'`". (_,_)/___||___|  /  |        | |____/ /. (_ o _)  |  |   \           |  (_,_) \  '_ '`)  |___|  /  |    _( )_ .'   
 > (_)  )  .---.|  |  .-----.  _.-`   |        |   _ _ '.|  (_,_)___|  :_ _:           |   '-.-' > (_)  )     _.-`   |___(_ o _)'    
(  .  .-'  |   |'  \  '-   ..'   _    |        |  ( ' )  '  \   .---.  (_I_)           |   |    (  .  .-'  .'   _    |   |(_,_)'     
 `-'`-'|___|   | \  `-'`   ||  _( )_  |        | (_{;}_) |\  `-'    / (_(=)_)          |   |     `-'`-'|___|  _( )_  |   `-'  /      
  |        |   |  \        /\ (_ o _) /        |  (_,_)  / \       /   (_I_)           /   )      |        \ (_ o _) /\      /       
  `--------'---'   `'-...-'  '.(_,_).'         /_______.'   `'-..-'    '---'           `---'      `--------`'.(_,_).'  `-..-'        
                                                                                                                                     
    📋 Equipos Inscritos en el Torneo 📋
    """)

    # Verificar que hay equipos registrados
    if not validar_liga_vacia(liga):
        return

    # Crear tabla con estadísticas de equipos
    equipos_tabla = []
    for i, equipo in enumerate(liga, 1):
        # [nombre, partidos_jugados, victorias, empates, derrotas, goles_favor, goles_contra, puntos]
        equipos_tabla.append([
            i,                          # #
            equipo[0],                  # Equipo
            equipo[1],                  # PJ (Partidos Jugados)
            equipo[2],                  # V (Victorias)
            equipo[3],                  # E (Empates)
            equipo[4],                  # D (Derrotas)
            equipo[5],                  # GF (Goles Favor)
            equipo[6],                  # GC (Goles Contra)
            equipo[7]                   # Pts (Puntos)
        ])
    
    # Mostrar tabla usando tabulate
    print(tabulate(equipos_tabla, 
                   headers=["#", "Equipo", "PJ", "V", "E", "D", "GF", "GC", "Pts"], 
                   tablefmt="grid"))

# Funciones de validacion
def validar_campo_vacio(campo):
    if not campo:
        print("   ❌ El campo no puede estar vacío.")
        pausar_pantalla()
        return False
    return True

def validar_equipos_con_partidos(liga):
    equipos_con_partidos = [equipo for equipo in liga if equipo[1] > 0]
    if not equipos_con_partidos:
        print("\n❌ No hay equipos que hayan jugado partidos.")
        print("   Primero debes registrar marcadores de partidos.")
        pausar_pantalla()
        return False
    return True

def validar_liga_vacia(liga):
    if not liga:
        print("\n❌ No hay equipos registrados para analizar.")
        return False
    return True

def validar_ingreso_goles(equipo_nombre):
    while True:
        try:
            goles = int(input(f"   Goles de {equipo_nombre}: ")) 
            if goles >= 0:
                return goles
            else:
                print("   ❌ Los goles no pueden ser un número negativo.")
        except ValueError:
            print("   ❌ Debes ingresar un número válido.")

def buscar_equipos(equipo_local_nombre, equipo_visitante_nombre, liga):
    equipo_local = None
    equipo_visitante = None
    
    for equipo in liga:
        if equipo[0] == equipo_local_nombre:
            equipo_local = equipo
        elif equipo[0] == equipo_visitante_nombre:
            equipo_visitante = equipo

    if not equipo_local or not equipo_visitante:
        print("   ❌ Error: No se encontraron los equipos en la liga.")
        return False, False
    
    return equipo_local, equipo_visitante

def validar_numero_partido(idx_partido, fecha_partido):
    if idx_partido < 0 or idx_partido >= len(fecha_partido):
        print("   ❌ Número de partido no válido. Inténtalo de nuevo.")
        return False
    return True

def validar_partidos_programados(fecha_partido):
    if not fecha_partido:
        print("\n❌ No hay partidos programados para registrar marcadores.")
        print("   Primero debes programar fechas de partidos.")
        return False
    return True

def rango_fechas(dia, mes, año):
    if dia < 1 or dia > 31 or mes < 1 or mes > 12 or año < 2024:
        print("   ❌ Fecha fuera de rango válido. Inténtalo de nuevo.")
        return False
    return True

def validar_equipos_iguales(equipo_local, equipo_visitante):
    if equipo_local == equipo_visitante:
        print("   ❌ No puedes programar un partido entre el mismo equipo.")
        return False
    return True

def validar_seleccion(equipo, liga):
    if equipo < 0 or equipo >= len(liga):
        print("   ❌ Número de equipo no válido. Inténtalo de nuevo.")
        return False
    return True

def validar_enteros(mensaje):
    while True:
        try:
            x = int(input(mensaje))
            return x
        except ValueError:
            print("ERROR: VALOR INVALIDO")
            pausar_pantalla()

def validar_cantidad_equipos(liga):
    if len(liga) < 2:
        print("Error: Debes registrar al menos 2 equipos.")
        return False
    return True

def validar_equipo_registrado(nombre_equipo):
    """
    Valida si un equipo ya está registrado en la liga
    Retorna True si el equipo ya existe, False si no
    """
    for equipo_registrado in liga:
        if nombre_equipo == equipo_registrado[0]:  # Compara con el nombre (primer elemento)
            return True
    return False

def validar_registro_equipo(mensaje):
    while True:
        try:
            x = input(mensaje)
            # Verificar que solo contenga letras y espacios
            if x.replace(" ", "").isalpha():
                return x.capitalize()
            else:
                print("Error: El nombre del equipo solo puede contener letras y espacios.")
                continue
        except ValueError:
            print("Error inesperado: Ingrese un nombre valido.")
    
# Funciones de pantalla
def pausar_pantalla():
    if sys.platform=="linux" or sys.platform=="darwin":
        input('...')
    else:
        os.system('pause')
        
def limpiar_pantalla():
    if sys.platform=="linux" or sys.platform=="darwin":
        os.system('clear')
    else:
        os.system('cls')

# Funcion para registrar equipos
def registrar_equipo():
    while True:
        limpiar_pantalla()
        print("""

        
  .---.   .-./`)  .-_'''-.     ____             _______      .-''-.,---------.         .-------.  .---.       ____      ____     __  
  | ,_|   \ .-.')'_( )_   \  .'  __ `.         \  ____  \  .'_ _   \          \        \  _(`)_ \ | ,_|     .'  __ `.   \   \   /  / 
,-./  )   / `-' |(_ o _)|  '/   '  \  \        | |    \ | / ( ` )   `--.  ,---'        | (_ o._),-./  )    /   '  \  \   \  _. /  '  
\  '_ '`)  `-'`". (_,_)/___||___|  /  |        | |____/ /. (_ o _)  |  |   \           |  (_,_) \  '_ '`)  |___|  /  |    _( )_ .'   
 > (_)  )  .---.|  |  .-----.  _.-`   |        |   _ _ '.|  (_,_)___|  :_ _:           |   '-.-' > (_)  )     _.-`   |___(_ o _)'    
(  .  .-'  |   |'  \  '-   ..'   _    |        |  ( ' )  '  \   .---.  (_I_)           |   |    (  .  .-'  .'   _    |   |(_,_)'     
 `-'`-'|___|   | \  `-'`   ||  _( )_  |        | (_{;}_) |\  `-'    / (_(=)_)          |   |     `-'`-'|___|  _( )_  |   `-'  /      
  |        |   |  \        /\ (_ o _) /        |  (_,_)  / \       /   (_I_)           /   )      |        \ (_ o _) /\      /       
  `--------'---'   `'-...-'  '.(_,_).'         /_______.'   `'-..-'    '---'           `---'      `--------`'.(_,_).'  `-..-'        
                                                                                                                                                                                                                                                                          
    ⚽ Registro de equipos ⚽
              """)

        nombre_nuevo_equipo = validar_registro_equipo('Ingrese el nombre del equipo: ')

        if validar_equipo_registrado(nombre_nuevo_equipo):
            print(f"\n¡Error! El equipo '{nombre_nuevo_equipo}' ya está registrado. Ingrese un nombre diferente. ❌")
            pausar_pantalla()
            continue  

        liga.append([nombre_nuevo_equipo, 0, 0, 0, 0, 0, 0, 0]) 

        print(f"\n✅ ¡Equipo '{nombre_nuevo_equipo}' registrado con éxito!")
        break  

# Funcion para programar fechas de partidos
def programar_fecha(liga, fecha_partido):
    """
    Función para programar fechas de partidos entre equipos registrados
    """
    limpiar_pantalla()
    print("""

    
  .---.   .-./`)  .-_'''-.     ____             _______      .-''-.,---------.         .-------.  .---.       ____      ____     __  
  | ,_|   \ .-.')'_( )_   \  .'  __ `.         \  ____  \  .'_ _   \          \        \  _(`)_ \ | ,_|     .'  __ `.   \   \   /  / 
,-./  )   / `-' |(_ o _)|  '/   '  \  \        | |    \ | / ( ` )   `--.  ,---'        | (_ o._),-./  )    /   '  \  \   \  _. /  '  
\  '_ '`)  `-'`". (_,_)/___||___|  /  |        | |____/ /. (_ o _)  |  |   \           |  (_,_) \  '_ '`)  |___|  /  |    _( )_ .'   
 > (_)  )  .---.|  |  .-----.  _.-`   |        |   _ _ '.|  (_,_)___|  :_ _:           |   '-.-' > (_)  )     _.-`   |___(_ o _)'    
(  .  .-'  |   |'  \  '-   ..'   _    |        |  ( ' )  '  \   .---.  (_I_)           |   |    (  .  .-'  .'   _    |   |(_,_)'     
 `-'`-'|___|   | \  `-'`   ||  _( )_  |        | (_{;}_) |\  `-'    / (_(=)_)          |   |     `-'`-'|___|  _( )_  |   `-'  /      
  |        |   |  \        /\ (_ o _) /        |  (_,_)  / \       /   (_I_)           /   )      |        \ (_ o _) /\      /       
  `--------'---'   `'-...-'  '.(_,_).'         /_______.'   `'-..-'    '---'           `---'      `--------`'.(_,_).'  `-..-'        
                                                                                                                                     
    📅 Programar fecha de partido 📅
    """)

    # Verificar que hay al menos 2 equipos registrados
    if not validar_cantidad_equipos(liga):
        return

    # Mostrar equipos disponibles
    mostrar_equipos(liga)

    # Seleccionar equipos
    while True:
        try:
            print(f"\n🏠 Selecciona el equipo LOCAL:")
            idx_local = validar_enteros("   Número del equipo local: ") - 1
            
            if not validar_seleccion(idx_local, liga):
                continue
                
            print(f"\n✈️  Selecciona el equipo VISITANTE:")
            idx_visitante = validar_enteros("   Número del equipo visitante: ") - 1
            
            if not validar_seleccion(idx_visitante, liga):
                continue
                
            if not validar_equipos_iguales(liga[idx_local][0], liga[idx_visitante][0]):
                continue   
            break
            
        except ValueError:
            print("   ❌ Debes ingresar un número válido.")
            continue

    equipo_local = liga[idx_local][0]
    equipo_visitante = liga[idx_visitante][0]

    # Ingresar fecha
    while True:
        print(f"\n📅 Ingresa la fecha del partido {equipo_local} vs {equipo_visitante}:")
        
        try:
            dia = validar_enteros("   Día (1-31): ")
            mes = validar_enteros("   Mes (1-12): ")
            año = validar_enteros("   Año (ej: 2024): ")
            
            # Validar rango de fechas
            if not rango_fechas(dia, mes, año):
                continue
            
            # Crear objeto datetime para validar fecha
            fecha_partido_obj = datetime(año, mes, dia)
            
            # Verificar que la fecha no sea anterior a hoy
            fecha_actual = datetime.now()
            if fecha_partido_obj < fecha_actual:
                print("   ❌ No puedes programar partidos en fechas pasadas.")
                continue
                
            break
            
        except ValueError:
            print("   ❌ Fecha no válida. Asegúrate de ingresar números correctos.")
            continue

    # Formatear fecha para mostrar
    fecha_formateada = fecha_partido_obj.strftime("%d/%m/%Y")
    
    # Guardar la programación
    # [equipo_local, equipo_visitante, fecha_formateada]
    partido_programado = [equipo_local, equipo_visitante, fecha_formateada]
    
    # Agregar a la lista global de partidos programados
    fecha_partido.append(partido_programado)
    
    # Mostrar confirmación
    print(f"\n✅ ¡Partido programado con éxito!")
    print(f"   🏠 {equipo_local} vs {equipo_visitante}")
    print(f"   📅 Fecha: {fecha_formateada}")

# Funcion para registrar marcadores de partidos
def registrar_marcador(liga, fecha_partido):
    """
    Función para registrar marcadores de partidos jugados
    """
    limpiar_pantalla()
    print("""

    
  .---.   .-./`)  .-_'''-.     ____             _______      .-''-.,---------.         .-------.  .---.       ____      ____     __  
  | ,_|   \ .-.')'_( )_   \  .'  __ `.         \  ____  \  .'_ _   \          \        \  _(`)_ \ | ,_|     .'  __ `.   \   \   /  / 
,-./  )   / `-' |(_ o _)|  '/   '  \  \        | |    \ | / ( ` )   `--.  ,---'        | (_ o._),-./  )    /   '  \  \   \  _. /  '  
\  '_ '`)  `-'`". (_,_)/___||___|  /  |        | |____/ /. (_ o _)  |  |   \           |  (_,_) \  '_ '`)  |___|  /  |    _( )_ .'   
 > (_)  )  .---.|  |  .-----.  _.-`   |        |   _ _ '.|  (_,_)___|  :_ _:           |   '-.-' > (_)  )     _.-`   |___(_ o _)'    
(  .  .-'  |   |'  \  '-   ..'   _    |        |  ( ' )  '  \   .---.  (_I_)           |   |    (  .  .-'  .'   _    |   |(_,_)'     
 `-'`-'|___|   | \  `-'`   ||  _( )_  |        | (_{;}_) |\  `-'    / (_(=)_)          |   |     `-'`-'|___|  _( )_  |   `-'  /      
  |        |   |  \        /\ (_ o _) /        |  (_,_)  / \       /   (_I_)           /   )      |        \ (_ o _) /\      /       
  `--------'---'   `'-...-'  '.(_,_).'         /_______.'   `'-..-'    '---'           `---'      `--------`'.(_,_).'  `-..-'        
                                                                                                                                     
    📝 Registrar marcador de partido 📝
    """)

    # Verificar que hay al menos 2 equipos registrados
    if not validar_cantidad_equipos(liga):
        return

    # Verificar si hay partidos programados
    if not validar_partidos_programados(fecha_partido):
        return

    # Mostrar partidos programados
    print("\n📋 Partidos programados:")
    mostrar_partidos_programados(fecha_partido)

    # Seleccionar partido programado
    while True:
        try:
            print(f"\n⚽ Selecciona el partido que se jugó:")
            idx_partido = validar_enteros("   Número del partido: ") - 1
            
            if not validar_numero_partido(idx_partido, fecha_partido):
                continue
                
            break
            
        except ValueError:
            print("   ❌ Debes ingresar un número válido.")
            continue

    # Obtener información del partido seleccionado
    partido_seleccionado = fecha_partido[idx_partido] # [equipo_local, equipo_visitante, fecha_formateada]
    equipo_local_nombre = partido_seleccionado[0] # equipo_local
    equipo_visitante_nombre = partido_seleccionado[1] # equipo_visitante
    fecha_partido_str = partido_seleccionado[2] # fecha_formateada

    # Buscar los equipos en la liga
    resultado_busqueda = buscar_equipos(equipo_local_nombre, equipo_visitante_nombre, liga)
    if resultado_busqueda == (False, False):
        return
    
    equipo_local, equipo_visitante = resultado_busqueda

    print(f"\n⚽ Partido: {equipo_local[0]} vs {equipo_visitante[0]}")
    print(f"   📅 Fecha programada: {fecha_partido_str}")

    # Ingresar goles del equipo local
    goles_local = validar_ingreso_goles(equipo_local[0]) # Goles de equipo local

    # Ingresar goles del equipo visitante
    goles_visitante = validar_ingreso_goles(equipo_visitante[0]) # Goles de equipo visitante

    # Actualizar estadísticas
    #     0            1             2        3         4           5            6          7
    # [nombre, partidos_jugados, victorias, empates, derrotas, goles_favor, goles_contra, puntos]
    
    # Incrementar partidos jugados
    equipo_local[1] += 1 # Incrementar partidos jugados del equipo local
    equipo_visitante[1] += 1 # Incrementar partidos jugados del equipo visitante

    # Actualizar goles a favor y en contra
    equipo_local[5] += goles_local     # Goles a favor del equipo local
    equipo_local[6] += goles_visitante # Goles en contra del equipo local
    equipo_visitante[5] += goles_visitante # Goles a favor del equipo visitante
    equipo_visitante[6] += goles_local     # Goles en contra del equipo visitante

    # Determinar resultado y actualizar estadísticas
    if goles_local > goles_visitante:
        # Victoria local
        equipo_local[2] += 1  # Incrementar victorias del equipo local
        equipo_local[7] += 3  # Incrementar puntos del equipo local
        equipo_visitante[4] += 1 # Incrementar derrotas del equipo visitante
        resultado = f"🏆 Victoria de {equipo_local[0]}"
    elif goles_visitante > goles_local:
        # Victoria visitante
        equipo_visitante[2] += 1 # Incrementar victorias del equipo visitante
        equipo_visitante[7] += 3 # Incrementar puntos del equipo visitante
        equipo_local[4] += 1     # Incrementar derrotas del equipo local
        resultado = f"🏆 Victoria de {equipo_visitante[0]}"
    else:
        # Empate
        equipo_local[3] += 1     # Incrementar empates del equipo local
        equipo_local[7] += 1     # Incrementar puntos del equipo local
        equipo_visitante[3] += 1 # Incrementar empates del equipo visitante
        equipo_visitante[7] += 1 # Incrementar puntos del equipo visitante
        resultado = "🤝 Empate"

    # Remover el partido de la lista de programados (ya se jugó)
    fecha_partido.pop(idx_partido)

    # Mostrar resumen del partido
    print(f"\n✅ ¡Marcador registrado con éxito!")
    print(f"   🏠 {equipo_local[0]} {goles_local} - {goles_visitante} {equipo_visitante[0]} ✈️")
    print(f"   📅 Fecha: {fecha_partido_str}")
    print(f"   🏆 Resultado: {resultado}")

# Funcion para mostrar equipo con más goles en contra
def mas_goles_contra(liga):
    """
    Función para mostrar el equipo que ha recibido más goles en contra
    """
    limpiar_pantalla()
    print("""

    
  .---.   .-./`)  .-_'''-.     ____             _______      .-''-.,---------.         .-------.  .---.       ____      ____     __  
  | ,_|   \ .-.')'_( )_   \  .'  __ `.         \  ____  \  .'_ _   \          \        \  _(`)_ \ | ,_|     .'  __ `.   \   \   /  / 
,-./  )   / `-' |(_ o _)|  '/   '  \  \        | |    \ | / ( ` )   `--.  ,---'        | (_ o._),-./  )    /   '  \  \   \  _. /  '  
\  '_ '`)  `-'`". (_,_)/___||___|  /  |        | |____/ /. (_ o _)  |  |   \           |  (_,_) \  '_ '`)  |___|  /  |    _( )_ .'   
 > (_)  )  .---.|  |  .-----.  _.-`   |        |   _ _ '.|  (_,_)___|  :_ _:           |   '-.-' > (_)  )     _.-`   |___(_ o _)'    
(  .  .-'  |   |'  \  '-   ..'   _    |        |  ( ' )  '  \   .---.  (_I_)           |   |    (  .  .-'  .'   _    |   |(_,_)'     
 `-'`-'|___|   | \  `-'`   ||  _( )_  |        | (_{;}_) |\  `-'    / (_(=)_)          |   |     `-'`-'|___|  _( )_  |   `-'  /      
  |        |   |  \        /\ (_ o _) /        |  (_,_)  / \       /   (_I_)           /   )      |        \ (_ o _) /\      /       
  `--------'---'   `'-...-'  '.(_,_).'         /_______.'   `'-..-'    '---'           `---'      `--------`'.(_,_).'  `-..-'        
                                                                                                                                     
    🥅 Equipo con más goles en contra 🥅
    """)

    # Verificar que hay equipos registrados
    if not validar_liga_vacia(liga):
        return

    # Verificar que hay equipos que han jugado partidos
    if not validar_equipos_con_partidos(liga):
        return

    # Obtener equipos con partidos
    equipos_con_partidos = [equipo for equipo in liga if equipo[1] > 0]

    # Encontrar el equipo con más goles en contra
    equipo_con_mas_goles = equipos_con_partidos[0]
    
    for equipo_actual in equipos_con_partidos:
        if equipo_actual[6] > equipo_con_mas_goles[6]:  # goles_contra
            equipo_con_mas_goles = equipo_actual

    # Mostrar resultado
    print(f"\n🏆 El equipo que ha recibido más goles en contra es:")
    print(f"   📛 {equipo_con_mas_goles[0]}")
    print(f"   🥅 Ha recibido un total de {equipo_con_mas_goles[6]} goles.")

# Funcion para mostrar equipo con más goles a favor
def mas_goles_favor(liga):
    limpiar_pantalla()
    print("""

    
  .---.   .-./`)  .-_'''-.     ____             _______      .-''-.,---------.         .-------.  .---.       ____      ____     __  
  | ,_|   \ .-.')'_( )_   \  .'  __ `.         \  ____  \  .'_ _   \          \        \  _(`)_ \ | ,_|     .'  __ `.   \   \   /  / 
,-./  )   / `-' |(_ o _)|  '/   '  \  \        | |    \ | / ( ` )   `--.  ,---'        | (_ o._),-./  )    /   '  \  \   \  _. /  '  
\  '_ '`)  `-'`". (_,_)/___||___|  /  |        | |____/ /. (_ o _)  |  |   \           |  (_,_) \  '_ '`)  |___|  /  |    _( )_ .'   
 > (_)  )  .---.|  |  .-----.  _.-`   |        |   _ _ '.|  (_,_)___|  :_ _:           |   '-.-' > (_)  )     _.-`   |___(_ o _)'    
(  .  .-'  |   |'  \  '-   ..'   _    |        |  ( ' )  '  \   .---.  (_I_)           |   |    (  .  .-'  .'   _    |   |(_,_)'     
 `-'`-'|___|   | \  `-'`   ||  _( )_  |        | (_{;}_) |\  `-'    / (_(=)_)          |   |     `-'`-'|___|  _( )_  |   `-'  /      
  |        |   |  \        /\ (_ o _) /        |  (_,_)  / \       /   (_I_)           /   )      |        \ (_ o _) /\      /       
  `--------'---'   `'-...-'  '.(_,_).'         /_______.'   `'-..-'    '---'           `---'      `--------`'.(_,_).'  `-..-'        
                                                                                                                                     
          🥅 Equipo con más goles a favor 🥅
""")

    # Verificar que hay equipos registrados
    if not validar_liga_vacia(liga):
        return
    
    # Verificar que hay equipos que han jugado partidos
    if not validar_equipos_con_partidos(liga):
        return
    
    # Obtener equipos con partidos
    equipos_con_partidos = [equipo for equipo in liga if equipo[1] > 0]
    
    # Encontrar el equipo con más goles a favor
    equipo_con_mas_goles = equipos_con_partidos[0]
    
    for equipo_actual in equipos_con_partidos:
        if equipo_actual[5] > equipo_con_mas_goles[5]:  # goles_favor
            equipo_con_mas_goles = equipo_actual
    
    # Mostrar resultado
    print(f"\n🏆 El equipo que ha marcado más goles a favor es:")
    print(f"   📛 {equipo_con_mas_goles[0]}")
    print(f"   🥅 Ha marcado un total de {equipo_con_mas_goles[5]} goles.")
    
# Funcion para registrar plantel de jugadoras
def registro_plantel(liga):
    """
    Función para registrar plantel de jugadores y cuerpo técnico
    """
    limpiar_pantalla()
    print("""

    
  .---.   .-./`)  .-_'''-.     ____             _______      .-''-.,---------.         .-------.  .---.       ____      ____     __  
  | ,_|   \ .-.')'_( )_   \  .'  __ `.         \  ____  \  .'_ _   \          \        \  _(`)_ \ | ,_|     .'  __ `.   \   \   /  / 
,-./  )   / `-' |(_ o _)|  '/   '  \  \        | |    \ | / ( ` )   `--.  ,---'        | (_ o._),-./  )    /   '  \  \   \  _. /  '  
\  '_ '`)  `-'`". (_,_)/___||___|  /  |        | |____/ /. (_ o _)  |  |   \           |  (_,_) \  '_ '`)  |___|  /  |    _( )_ .'   
 > (_)  )  .---.|  |  .-----.  _.-`   |        |   _ _ '.|  (_,_)___|  :_ _:           |   '-.-' > (_)  )     _.-`   |___(_ o _)'    
(  .  .-'  |   |'  \  '-   ..'   _    |        |  ( ' )  '  \   .---.  (_I_)           |   |    (  .  .-'  .'   _    |   |(_,_)'     
 `-'`-'|___|   | \  `-'`   ||  _( )_  |        | (_{;}_) |\  `-'    / (_(=)_)          |   |     `-'`-'|___|  _( )_  |   `-'  /      
  |        |   |  \        /\ (_ o _) /        |  (_,_)  / \       /   (_I_)           /   )      |        \ (_ o _) /\      /       
  `--------'---'   `'-...-'  '.(_,_).'         /_______.'   `'-..-'    '---'           `---'      `--------`'.(_,_).'  `-..-'        
                                                                                                                                     
    👩 Registro del plantel 👩
    """)

    # Verificar que hay equipos registrados
    if not validar_liga_vacia(liga):
        return

    # Mostrar equipos disponibles
    print("\n📋 Equipos disponibles:")
    mostrar_equipos(liga)
    
    # Seleccionar equipo
    while True:
        try:
            print(f"\n⚽ Selecciona el equipo:")
            idx_equipo = validar_enteros("   Número del equipo: ") - 1
            
            if not validar_seleccion(idx_equipo, liga):
                continue
            break
        except ValueError:
            print("   ❌ Debes ingresar un número válido.")
            continue
        
    # Obtener información del equipo seleccionado
    equipo_seleccionado = liga[idx_equipo]
    nombre_equipo = equipo_seleccionado[0]
    
    # Submenú del plantel
    while True:
        limpiar_pantalla()
        print("""

    
  .---.   .-./`)  .-_'''-.     ____             _______      .-''-.,---------.         .-------.  .---.       ____      ____     __  
  | ,_|   \ .-.')'_( )_   \  .'  __ `.         \  ____  \  .'_ _   \          \        \  _(`)_ \ | ,_|     .'  __ `.   \   \   /  / 
,-./  )   / `-' |(_ o _)|  '/   '  \  \        | |    \ | / ( ` )   `--.  ,---'        | (_ o._),-./  )    /   '  \  \   \  _. /  '  
\  '_ '`)  `-'`". (_,_)/___||___|  /  |        | |____/ /. (_ o _)  |  |   \           |  (_,_) \  '_ '`)  |___|  /  |    _( )_ .'   
 > (_)  )  .---.|  |  .-----.  _.-`   |        |   _ _ '.|  (_,_)___|  :_ _:           |   '-.-' > (_)  )     _.-`   |___(_ o _)'    
(  .  .-'  |   |'  \  '-   ..'   _    |        |  ( ' )  '  \   .---.  (_I_)           |   |    (  .  .-'  .'   _    |   |(_,_)'     
 `-'`-'|___|   | \  `-'`   ||  _( )_  |        | (_{;}_) |\  `-'    / (_(=)_)          |   |     `-'`-'|___|  _( )_  |   `-'  /      
  |        |   |  \        /\ (_ o _) /        |  (_,_)  / \       /   (_I_)           /   )      |        \ (_ o _) /\      /       
  `--------'---'   `'-...-'  '.(_,_).'         /_______.'   `'-..-'    '---'           `---'      `--------`'.(_,_).'  `-..-'        
                                                                                                                                     
    👩 Registro del plantel - """ + nombre_equipo + """ 👩

1. ⚽ Registrar jugador
2. 👨‍💼 Registrar cuerpo técnico  
3. 🔙 Regresar al menú principal

Por favor, selecciona una opción:
        """)
        
        opc = input(" = ")
        
        match opc:
            case "1":
                registrar_jugador(equipo_seleccionado)
            case "2":
                registrar_cuerpo_tecnico(equipo_seleccionado)
            case "3":
                break
            case _:
                print("❌ Opción no válida.")
                pausar_pantalla()

def registrar_jugador(equipo_seleccionado):
    """
    Función para registrar un jugador en el equipo
    """
    limpiar_pantalla()
    print(f"\n⚽ Registrando jugador para {equipo_seleccionado[0]}")
    print("=" * 50)
    
    # Ingresar nombre del jugador
    nombre_jugador = input("   Nombre del jugador: ").strip().upper()
    if not validar_campo_vacio(nombre_jugador):
        return
    
    # Ingresar posición del jugador
    posicion_jugador = input("   Posición de juego: ").strip().upper()
    if not validar_campo_vacio(posicion_jugador):
        return
    
    # Crear el jugador usando lista
    # [tipo, nombre, posicion]
    jugador = ["jugador", nombre_jugador, posicion_jugador]
    
    # Agregar al plantel del equipo
    if len(equipo_seleccionado) < 9:
        equipo_seleccionado.append([])
    
    equipo_seleccionado[8].append(jugador)
    
    print(f"\n✅ ¡Jugador registrado con éxito!")
    print(f"   📛 {nombre_jugador}")
    print(f"   ⚽ Posición: {posicion_jugador}")
    pausar_pantalla()

def registrar_cuerpo_tecnico(equipo_seleccionado):
    """
    Función para registrar un miembro del cuerpo técnico
    """
    limpiar_pantalla()
    print(f"\n👨‍💼 Registrando cuerpo técnico para {equipo_seleccionado[0]}")
    print("=" * 50)
    
    # Ingresar nombre del miembro
    nombre_miembro = input("   Nombre del miembro: ").strip().upper()
    if not validar_campo_vacio(nombre_miembro):
        return
    
    # Ingresar cargo del miembro
    cargo_miembro = input("   Cargo: ").strip().upper()
    if not validar_campo_vacio(cargo_miembro):
        return
    
    # Crear el miembro del cuerpo técnico usando lista
    # [tipo, nombre, cargo]
    miembro = ["cuerpo_tecnico", nombre_miembro, cargo_miembro]
    
    # Agregar al plantel del equipo
    if len(equipo_seleccionado) < 9: # 9 es el tamaño de la lista de equipos
        equipo_seleccionado.append([])
    
    equipo_seleccionado[8].append(miembro)
    
    print(f"\n✅ ¡Miembro del cuerpo técnico registrado con éxito!")
    print(f"   📛 {nombre_miembro}")
    print(f"   👨‍💼 Cargo: {cargo_miembro}")
    pausar_pantalla()

# Variable para mostrar menu principal
MAIN_MENU = """


  .---.   .-./`)  .-_'''-.     ____             _______      .-''-.,---------.         .-------.  .---.       ____      ____     __  
  | ,_|   \ .-.')'_( )_   \  .'  __ `.         \  ____  \  .'_ _   \          \        \  _(`)_ \ | ,_|     .'  __ `.   \   \   /  / 
,-./  )   / `-' |(_ o _)|  '/   '  \  \        | |    \ | / ( ` )   `--.  ,---'        | (_ o._),-./  )    /   '  \  \   \  _. /  '  
\  '_ '`)  `-'`". (_,_)/___||___|  /  |        | |____/ /. (_ o _)  |  |   \           |  (_,_) \  '_ '`)  |___|  /  |    _( )_ .'   
 > (_)  )  .---.|  |  .-----.  _.-`   |        |   _ _ '.|  (_,_)___|  :_ _:           |   '-.-' > (_)  )     _.-`   |___(_ o _)'    
(  .  .-'  |   |'  \  '-   ..'   _    |        |  ( ' )  '  \   .---.  (_I_)           |   |    (  .  .-'  .'   _    |   |(_,_)'     
 `-'`-'|___|   | \  `-'`   ||  _( )_  |        | (_{;}_) |\  `-'    / (_(=)_)          |   |     `-'`-'|___|  _( )_  |   `-'  /      
  |        |   |  \        /\ (_ o _) /        |  (_,_)  / \       /   (_I_)           /   )      |        \ (_ o _) /\      /       
  `--------'---'   `'-...-'  '.(_,_).'         /_______.'   `'-..-'    '---'           `---'      `--------`'.(_,_).'  `-..-'        
                                                                                                                                        
✨🌸⚽  Bienvenidos al Menú del Torneo  ⚽🌸✨

1. 🌷 Registrar nuevo equipo
2. 📅 Programar fecha del torneo
3. 📝 Registrar marcador de partidos
4. 🥅 Equipo con más goles en contra
5. 🎉 Equipo con más goles a favor
6. 👩 Registrar plantel de jugadoras
7. 📋 Ver equipos inscritos
8. 🚪 Salir del menú

Por favor, selecciona una opción:
"""

# Funcion para mostrar menu principal
def main():
    while True:
        limpiar_pantalla()
        print(MAIN_MENU)
        opc = input(" = ")
        match opc:
            case "1":
                limpiar_pantalla()
                registrar_equipo()
                pausar_pantalla()
            case "2":
                limpiar_pantalla()
                programar_fecha(liga, fecha_partido)
                pausar_pantalla()
            case "3":
                limpiar_pantalla()
                registrar_marcador(liga, fecha_partido)
                pausar_pantalla()
            case "4":
                limpiar_pantalla()
                mas_goles_contra(liga)
                pausar_pantalla()
            case "5":
                limpiar_pantalla()
                mas_goles_favor(liga)
                pausar_pantalla()
            case "6":
                limpiar_pantalla()
                registro_plantel(liga)
                pausar_pantalla()
            case "7":
                limpiar_pantalla()
                ver_equipos_inscritos(liga)
                pausar_pantalla()
            case "8":
                break
            case _:
                print("ERROR...")
                pausar_pantalla()

# Funcion principal
if __name__ == "__main__":
    main()