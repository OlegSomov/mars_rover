from src.rover import OutOfPlateauError
from src.plateau import Mars, Plateau
import pytest


def test_plateau_init():
    pl = Mars.from_string("10 10")
    assert pl.x == 10
    assert pl.y == 10


def test_deploy_outsid():
    pl = Mars(1, 1)
    with pytest.raises(OutOfPlateauError) as e:
        pl.deploy_rover("3 3 N")
    assert str(e.value) == "The initial location of a rover is outside of range"


def test_basic_methods():
    pl = Plateau()
    pl.is_in_range(0, 0)
    pl.is_position_available()
