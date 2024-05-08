
import requests

API_KEY = "f80b7e072a75bb46efc5fd711e3829fa"
URL_BASE = "https://superheroapi.com/api/"

def data_search_powerstats(range_hero_min, range_hero_max, powerstats_hero):

    heroes_list = []

    for hero_id in range (1, 25):
        url_search = f"{URL_BASE}{API_KEY}/{hero_id}/powerstats"
        response = requests.get(url_search)

        if response.status_code == 200:

            data = response.json()
            powerstats_value = data.get(powerstats_hero)
            
            if powerstats_value == "null":
                print(f" El personaje con ID {hero_id} no tiene valor de {powerstats_hero}")

            else: 
                powerstats_value = int(powerstats_value)
                if range_hero_min <= powerstats_value <= range_hero_max:
                    heroes_list.append(hero_id)
                else: 
                    None

        else:
            print(f"Error al obtener los datos del heroe {hero_id}: {response.status_code}")
                    
    return heroes_list

