import pytest
import requests
from unittest.mock import patch
from data_pipeline.api import get_pokemon

# Teste para verificar se a função retorna os dados corretamente quando a resposta é 200
@patch('data_pipeline.api.requests.get')
def test_get_pokemon_success(mock_get):
    # Simula uma resposta bem-sucedida da API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "count": 1118,
        "results": [{"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"}]
    }

    response = get_pokemon()

    assert response is not None
    assert response['count'] == 1118
    assert response['results'][0]['name'] == "bulbasaur"

# Teste para verificar se a função retorna None quando a resposta não é 200
@patch('data_pipeline.api.requests.get')
def test_get_pokemon_failure(mock_get):
    # Simula uma resposta falhada da API
    mock_get.return_value.status_code = 404

    response = get_pokemon()

    assert response is None