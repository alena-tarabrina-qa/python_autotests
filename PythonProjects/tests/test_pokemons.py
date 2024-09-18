import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a365ea1eced6e894ee95f6886e9c809f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '5281'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200 

def test_part_of_response():
        response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
        assert response_get.json()["data"][0]["name"] == 'Моника' 


@pytest.mark.parametrize('key, value', [('name', 'Моника'), ('trainer_id', TRAINER_ID), ('pokemon_id, 72097')])
def test_parametrize(key, value):
      response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
      assert response_parametrize.json()["data"][0][key] == value