import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns
import os

# Definiciones de los costos y cálculos
salario_diario = 248.93  # Salario diario en pesos mexicanos
horas_laborales_diarias = 8  # Horas laborales por día
dias_laborales_por_mes = 26  # Días laborables por mes

# Cálculo de costo por hora
costo_por_hora = salario_diario / horas_laborales_diarias

# Cálculo de costo mensual por persona
costo_mensual_por_persona = costo_por_hora * horas_laborales_diarias * dias_laborales_por_mes

# Cálculo del costo total por persona en 4 meses
costo_total_por_persona_4_meses = costo_mensual_por_persona * 4

# Definición de los roles y la cantidad de personas para cada uno
roles = [
    "Diseñador UI/UX",
    "Desarrollador Frontend",
    "Desarrollador Backend",
    "Diseñador Gráfico",
    "Especialista en Marketing Digital"
]
cantidad_personas = [1] * len(roles)  # Todos los roles tienen 1 persona

# Calculando el costo total por cada rol
costo_total_por_rol = [costo_total_por_persona_4_meses * cantidad for cantidad in cantidad_personas]

# Costo total de todo el equipo en 4 meses
costo_total_equipo_4_meses = sum(costo_total_por_rol)

# Creación de la tabla final
tabla = pd.DataFrame({
    "Rol": roles,
    "Cantidad de Personas": cantidad_personas,
    "Costo por Hora (MXN)": [costo_por_hora] * len(roles),
    "Costo Mensual por Persona (MXN)": [costo_mensual_por_persona] * len(roles),
    "Costo Total por Persona en 4 Meses (MXN)": [costo_total_por_persona_4_meses] * len(roles),
    "Costo Total por Rol en 4 Meses (MXN)": costo_total_por_rol
})

# Agregando la fila de total al final de la tabla
total_row = pd.DataFrame({
    "Rol": ["Total"],
    "Cantidad de Personas": [""],
    "Costo por Hora (MXN)": [""],
    "Costo Mensual por Persona (MXN)": [""],
    "Costo Total por Persona en 4 Meses (MXN)": [""],
    "Costo Total por Rol en 4 Meses (MXN)": [costo_total_equipo_4_meses]
})
tabla = pd.concat([tabla, total_row], ignore_index=True)

# Crear una figura y un eje
fig, ax = plt.subplots(figsize=(12, 6))

# Ocultar los ejes
ax.axis('tight')
ax.axis('off')

# Crear la tabla
table = ax.table(cellText=tabla.values, colLabels=tabla.columns, loc='center', cellLoc='center')

# Ajustar el estilo de la tabla
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.2)

# Ajustar el ancho de las columnas
table.auto_set_column_width(col=list(range(len(tabla.columns))))

# Añadir un título
plt.title(f"Costos de Embalaje\nSalario Diario: {salario_diario} MXN \n,Horas laborales diarias: {horas_laborales_diarias} \n, Días laborales por mes: {dias_laborales_por_mes}",fontsize=12)

# Obtener la ruta completa del directorio de trabajo actual
directorio_actual = os.getcwd()

# Nombre del archivo
nombre_archivo = 'costos_embalaje.png'

# Ruta completa del archivo
ruta_completa = os.path.join(directorio_actual, nombre_archivo)

# Guardar la figura como PNG
plt.savefig(ruta_completa, dpi=300, bbox_inches='tight')

print(f"La tabla ha sido guardada como '{nombre_archivo}'")
print(f"Ruta completa del archivo: {ruta_completa}")

# Verificar si el archivo se creó correctamente
if os.path.exists(ruta_completa):
    print(f"El archivo se ha creado correctamente en la ruta especificada.")
else:
    print(f"Hubo un problema al crear el archivo. Por favor, verifica los permisos de escritura en el directorio.")