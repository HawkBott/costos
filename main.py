import pandas as pd

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


print ("Salario Diario MXN: ",salario_diario)
print ("Horas laborales diarias", horas_laborales_diarias)
print ("Dias labores por mes: ", dias_laborales_por_mes)



print(tabla)






