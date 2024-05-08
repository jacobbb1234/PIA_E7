
import datetime

def save(data):
    date_time = datetime.datetime.now()
    time = date_time.strftime('%H-%M-%S')
    date = date_time.strftime('%d-%m-%y')
    
    name_file = f"Reportes de Consulta API/Consulta_{date}_{time}.txt"

    with open(name_file, "w") as f:
        f.write(data)
        print("Archivo guardado exitosamente")