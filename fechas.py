from datetime import datetime
from datetime import timedelta

"""Mostrar la cantidad de meses transcurridos desde la fecha de nacimiento del usuario"""

fecha = datetime(int(input("anio: ")), int(input("mes: ")), int(input("dia: ")))
now = datetime.now()
new_date = now - fecha
print('\ntienes', int(new_date.days / 365), 'anios')
print('\nhan pasado', int((new_date.days / 365) * 12), 'meses desde tu nacimiento')

format = now.strftime('\nfecha actual: Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
format_fecha = fecha.strftime('fecha usuario: %d, %m, %Y')

print(format)
print(format_fecha)
