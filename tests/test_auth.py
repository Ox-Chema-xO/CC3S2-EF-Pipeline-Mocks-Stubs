import pytest
from unittest.mock import Mock

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

@pytest.mark.xfail(reason="Fallara porque aun no se implementa el acceso por token")
def test_authenticated_user_token(user_fixture):
    acceso = False
    mock_user = Mock()
    mock_user.return_value
    mock_user.user = user_fixture
    mock_user.user.token = True
    #Como aun no se implementa el acceso por token esto fallara
    assert acceso == True
