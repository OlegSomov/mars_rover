# Rover tests
from src.rover import MarsRover, Rover
from math import pi


def test_rover_init(mars_plateau):
    # test the rover init
    rover = mars_plateau.deploy_rover("1 2 N")
    assert rover.id == '1'
    assert rover.x == 1
    assert rover.y == 2
    assert rover.direction == pi / 2


def test_rover_moves(mars_plateau):
    rover = mars_plateau.deploy_rover("1 2 N")
    rover.rotate_left()
    assert rover.get_direction() == "W"
    rover.rotate_right()
    assert rover.get_direction() == "N"
    rover.move()
    assert rover.x == 1
    assert rover.y == 3


def test_conversion():
    result = MarsRover._convert_to_compas(0)
    assert result == "E"
    result = MarsRover._convert_to_compas(pi / 2)
    assert result == "N"
    result = MarsRover._convert_to_compas(pi)
    assert result == "W"
    result = MarsRover._convert_to_compas((3 * pi) / 2)
    assert result == "S"
    result = MarsRover._convert_to_compas(-pi / 2)
    assert result == "S"
    result = MarsRover._convert_to_compas(-pi)
    assert result == "W"
    result = MarsRover._convert_to_compas((3 * -pi) / 2)
    assert result == "N"


def test_command_parse(mars_plateau):
    rover = mars_plateau.deploy_rover("1 2 N")
    rover.parse_commands("LMLMLMLMM")
    assert rover.x == 1
    assert rover.y == 3
    assert rover.get_direction() == "N"


def test_basic_methods():
    # for future
    rover = Rover()
    rover.rotate_left()
    rover.rotate_right()
    rover.move()
    rover.parse_commands("LLMM")
    rover.get_location()
    rover.get_direction()
