import Modulo_Buscar
import Modulo_Guardar
import Modulo_Rango


hero = input("Ingresa el nombre del heroe que deseas buscar: ")
opcion = Modulo_Buscar.data_search(hero)

if opcion:
    select = int(input("Ingresa la opción de héroe para conocer sus datos: ")) - 1
    if 0 <= select < len(opcion):
        id_heroe = opcion[select]
        datos_heroe = Modulo_Buscar.data_get(id_heroe)
        if datos_heroe:
            print("Datos del héroe seleccionado:")
            print(datos_heroe)
            Modulo_Guardar.save(datos_heroe)
    else:
        print("Opción no válida.")


print("""Tomando en cuenta las siguientes opciones:
              1. Inteligencia
              2. Fuerza
              3. Velocidad""")
power = input("Selecciona alguna: """)
if power == "1":
    power = "inteligencia"
    power_ = "intelligence"
elif power == "2":
    power = "fuerza"
    power_ = "strength"
elif power == "3":
    power = "velocidad"
    power_ = "speed"
else:
    print("No es válida su respuesta")
min_ = int(input(f"Ingresa el valor mínimo que deseas conocer de la {power} entre los heroes: "))
max_ = int(input(f"Ingresa el valor máximo que deseas conocer de la {power} entre los heroes: "))
heroes_list = Modulo_Rango.data_search_powerstats(min_, max_, power_)
print(f"Los siguientes ID son de heroes que tiene una {power} en el rango {min_}-{max_}: {heroes_list} ")

