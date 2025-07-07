import pytest
from unittest.mock import Mock
from fastapi.testclient import TestClient

@pytest.fixture
def user_fixture():
    """
    Fixture que devuelve informacion basica de un usuario
    activo o no de la uni
    """
    return {
        "cod_uni": 1,
        "username": "chema",
        "email": "chema@uni.pe",
        "name": "Diego",
        "es_activo": True
    }

@pytest.fixture
def authenticated_client_fixture(user_fixture):
    """
    Fixture que devuelve un cliente autenticado(usuario) simulado
    """
    mock_client = Mock()
    mock_client.user = user_fixture
    #Simulamos autenticado
    mock_client.is_authenticated = True
    return mock_client
