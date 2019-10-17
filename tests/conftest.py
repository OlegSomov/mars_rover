import pytest
from src.plateau import Mars


@pytest.fixture
def mars_plateau():
    pl = Mars(10, 10)
    return pl
