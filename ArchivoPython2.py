# Segundo commit
import calendar

# Lista de nombres de los meses en español
meses_espanol = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Iterar sobre cada mes del año 2024
for mes in range(1, 13):
    # Obtener el número de días del mes usando calendar.monthrange()
    _, num_dias = calendar.monthrange(2024, mes)
    
    # Imprimir el nombre del mes y el número de días
    print(f"{meses_espanol[mes-1]}: {num_dias} días")