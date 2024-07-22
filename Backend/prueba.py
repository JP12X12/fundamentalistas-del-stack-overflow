from datetime import datetime, timedelta

# Suponiendo que ya tienes estas variables
cant_dias = 5  # Número de días
horario_ingreso_str = "2024-07-22 14:00:00"  # Fecha y hora de ingreso en formato string

# Convertir la fecha y hora de ingreso de string a un objeto datetime
horario_ingreso = datetime.strptime(horario_ingreso_str, "%Y-%m-%d %H:%M:%S")

# Calcular la fecha de salida sumando la cantidad de días
dia_salida = horario_ingreso + timedelta(days=cant_dias)

print("Fecha y hora de ingreso:", horario_ingreso)
print("Día de salida:", dia_salida)
