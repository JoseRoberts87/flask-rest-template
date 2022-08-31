import pytest
from src import create_app


@pytest.fixture(scope="session")
def app():
    return create_app("TestingConfig")
