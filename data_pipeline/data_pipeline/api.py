import requests

def get_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=1118'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Retorna os dados em formato JSON
    else:
        return None
