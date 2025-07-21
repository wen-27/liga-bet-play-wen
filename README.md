# ⚽ Liga Bet Play - Sistema de Gestión de Torneos ⚽

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Activo-brightgreen.svg)

**Desarrollado con ❤️ por [Wendy](https://github.com/wen-27)**

</div>

---

## 📋 Descripción

**Liga Bet Play** es un sistema completo de gestión de torneos de fútbol desarrollado en Python. Permite administrar equipos, programar partidos, registrar marcadores y generar estadísticas en tiempo real.

### 🌟 Características Principales

- ⚽ **Gestión de Equipos**: Registro y administración de equipos participantes
- 📅 **Programación de Partidos**: Sistema de fechas y horarios para encuentros
- 📊 **Registro de Marcadores**: Captura de resultados en tiempo real
- 🏆 **Estadísticas Automáticas**: Cálculo automático de puntos, goles y posiciones
- 👥 **Gestión de Planteles**: Registro de jugadores y cuerpo técnico
- 📈 **Reportes y Análisis**: Visualización de datos y estadísticas del torneo

---

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/wen-27/liga-bet-play.git
   cd liga-bet-play
   ```

2. **Instalar dependencias**
   ```bash
   pip install tabulate
   ```

3. **Ejecutar el programa**
   ```bash
   python main.py
   ```

---

## 🎮 Cómo Usar el Sistema

### 1. Registro de Equipos
- Selecciona la opción **"Registrar nuevo equipo"**
- Ingresa el nombre del equipo (solo letras y espacios)
- El sistema validará que el equipo no esté duplicado

### 2. Programación de Partidos
- Selecciona **"Programar fecha del torneo"**
- Elige los equipos local y visitante
- Ingresa la fecha del partido (día, mes, año)
- El sistema validará fechas futuras

### 3. Registro de Marcadores
- Selecciona **"Registrar marcador de partidos"**
- Elige el partido programado que se jugó
- Ingresa los goles de cada equipo
- El sistema actualizará automáticamente las estadísticas

### 4. Consulta de Estadísticas
- **"Equipo con más goles en contra"**: Muestra el equipo más vulnerable
- **"Equipo con más goles a favor"**: Muestra el equipo más ofensivo
- **"Ver equipos inscritos"**: Tabla completa con todas las estadísticas

### 5. Gestión de Planteles
- Selecciona **"Registrar plantel de jugadoras"**
- Elige el equipo
- Registra jugadores y cuerpo técnico con sus posiciones/cargos

---

## 📊 Estructura de Datos

### Equipos
```python
# [nombre, partidos_jugados, victorias, empates, derrotas, goles_favor, goles_contra, puntos]
equipo = ["Barcelona", 5, 3, 1, 1, 12, 5, 10]
```

### Partidos Programados
```python
# [equipo_local, equipo_visitante, fecha_formateada]
partido = ["Barcelona", "Real Madrid", "15/12/2024"]
```

### Planteles
```python
# [tipo, nombre, posicion/cargo]
jugador = ["jugador", "María González", "Delantera"]
tecnico = ["cuerpo_tecnico", "Carlos López", "Entrenador"]
```

---

## 🎨 Características Técnicas

### Validaciones Implementadas
- ✅ Nombres de equipos únicos
- ✅ Fechas futuras para partidos
- ✅ Goles no negativos
- ✅ Equipos diferentes en un partido
- ✅ Campos obligatorios completos

### Funciones Principales
- `registrar_equipo()`: Gestión de equipos
- `programar_fecha()`: Programación de partidos
- `registrar_marcador()`: Captura de resultados
- `mas_goles_contra()`: Estadísticas defensivas
- `mas_goles_favor()`: Estadísticas ofensivas
- `registro_plantel()`: Gestión de planteles

---

## 🖥️ Interfaz de Usuario

El sistema cuenta con una interfaz de consola intuitiva que incluye:

- 🎨 **ASCII Art**: Diseños atractivos en cada menú
- 📋 **Tablas Formateadas**: Información clara y organizada
- 🎯 **Navegación Simple**: Menús numerados fáciles de usar
- ⚠️ **Mensajes de Error**: Validaciones claras y útiles
- ✅ **Confirmaciones**: Feedback inmediato de acciones

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje principal
- **tabulate**: Librería para formateo de tablas
- **datetime**: Manejo de fechas y horarios
- **os/sys**: Funciones del sistema operativo

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👩‍💻 Desarrolladora

**Wendy** - [@wen-27](https://github.com/wen-27)

- 🌟 Desarrolladora Full Stack
- ⚽ Apasionada por el fútbol y la tecnología
- 💻 Especializada en Python y desarrollo web
- 🎯 Comprometida con la excelencia en el código

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📞 Contacto

- **GitHub**: [@wen-27](https://github.com/wen-27)
- **Email**: [Tu email aquí]
- **LinkedIn**: [Tu LinkedIn aquí]

---

<div align="center">

### ⚽ ¡Gracias por usar Liga Bet Play! ⚽

**Desarrollado con pasión por el fútbol y la programación**

![Footer](https://img.shields.io/badge/Made%20with-Python-red.svg)
![Footer](https://img.shields.io/badge/Version-1.0.0-blue.svg)

</div> 