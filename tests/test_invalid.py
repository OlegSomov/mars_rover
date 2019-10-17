from math import pi
import pytest
from src.rover import CollisionError, OutOfPlateauError
from src.plateau import Mars


def test_rover_init_invalid(mars_plateau):
    # test the rover init
    rover = mars_plateau.deploy_rover("1 2 N")
    assert rover.id == '1'
    assert rover.x == 1
    assert rover.y == 2
    assert rover.direction == pi / 2

    # the second rover should not be deployed to the same location
    with pytest.raises(CollisionError) as e:
        rover = mars_plateau.deploy_rover("1 2 N")
    assert str(e.value) == "the initial location of a rover is not available"


def test_rover_out_of_range(mars_plateau):
    rover = mars_plateau.deploy_rover("1 2 N")
    with pytest.raises(OutOfPlateauError) as e:
        for i in range(20):
            rover.move()
    assert str(e.value) == "Next move is out of a plateau range"


def test_collision(mars_plateau):
    mars_plateau.deploy_rover("1 2 N")

    rover2 = mars_plateau.deploy_rover("1 1 N")
    with pytest.raises(CollisionError) as e:
        rover2.move()

    assert str(e.value) == "Next move will collide with other rover"


def test_wrong_command(mars_plateau):
    rover = mars_plateau.deploy_rover("1 2 N")
    with pytest.raises(TypeError) as e:
        rover.parse_commands(123)
    assert str(e.value) == "The commands must be str"


def test_plateau_init_invalid():
    with pytest.raises(ValueError) as e:
        Mars.from_string("123")
    assert str(e.value) == "not enough values to unpack (expected 2, got 1)"