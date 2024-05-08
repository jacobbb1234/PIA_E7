import requests

API_KEY = "f80b7e072a75bb46efc5fd711e3829fa"
URL_BASE = "https://superheroapi.com/api/"

def data_search (hero):
    url_search = f"{URL_BASE}{API_KEY}/search/{hero}"
    response = requests.get(url_search)

    if response.status_code == 200:
        data = response.json()
        n = len(data["results"])
        opcion=[]
        print(" opcion:  ID:    name: ")
        i = 0
        for i in range (n):
                _id= data["results"][i]["id"]
                name = data["results"][i]["name"]
                print(" "*3, i + 1, " "*3, _id, " "*3, name)
                opcion.append(_id)
                i += 1
        return opcion
    
    else:
        print("Error al obtener los datos del heroe:", response.status_code)
        return None


def data_get(id_hero):
    url_id = f"{URL_BASE}{API_KEY}/{id_hero}"
    response = requests.get(url_id)

    if response.status_code == 200:
        data = str(response.json())
        return data

    else:
        print("Error al obtener los datos del heroe:", response.status_code)
        return None
