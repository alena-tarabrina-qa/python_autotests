import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a365ea1eced6e894ee95f6886e9c809f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "alen.tarabrina@yandex.ru",
    "password": "Iloveqa111"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_name = {
    "pokemon_id": "72097",
    "name": "Моника",
    "photo_id": 1
}
body_pokeball = {
    "pokemon_id": "72097"
}
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email' , headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text) 