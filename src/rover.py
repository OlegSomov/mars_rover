from math import pi, sin, cos
import logging as log


class OutOfPlateauError(Exception):
    pass


class CollisionError(Exception):
    pass


class Rover(object):
    """
    The class represent the rover interface.
    Can be extended by defining general rover characteristicts e.g. number of wheels
    """

    def __init__(self):
        pass

    def rotate_left(self):
        """Method to rotate the rover right"""
        pass

    def rotate_right(self):
        """Method to rotate the rover right"""
        pass

    def move(self):
        """Method to move the rover in the set direction"""
        pass

    def parse_commands(self, commands):
        """Command parset method can be extended by override"""
        pass

    def get_location(self):
        """Method that returns the location of the rover in form of tuple"""
        pass

    def get_direction(self):
        """Return the direction of the rover"""
        pass


class MarsRover(Rover):
    """A model of the mars rover 1.0. The mode defines basic functionality of the rover.
    The commands defined to contrl the rover are:
    * L - to rotate rover left 90 degrees
    * R - to rotate rover right 90 degrees
    * M - to move rover in the direction it's currently set

    Raises
    ------
    OutOfPlateauError
            The error is raised when the initial location is out of the plateau range
    CollisionError
        The error is raised when the location of a rover is not available. e.g. taken by other rover
    TypeError
        When the command to control rover is not string. This model supports only str commands, with content (L || R || M)
    """

    def __init__(self, rover_id, x, y, direction, plateau):
        super().__init__()
        self.id = rover_id
        self.x = x
        self.y = y
        self.direction = direction
        self.plateau = plateau
        log.debug("Initialized MarsRover x,y,direction = {},{},{}".format(self.x, self.y, self.get_direction()))

    def rotate_left(self):
        """Method to rotate the rover left 90 degrees"""
        self.direction += pi / 2
        log.debug("Rotated left. Now {}".format(self.get_direction()))

    def rotate_right(self):
        """Method to rotate the rover right 90 degrees"""
        self.direction += -pi / 2
        log.debug("Rotated right. Now {}".format(self.get_direction()))

    def move(self):
        """Method to move the rover by 1 position in the direction it is set
        May return:
        * OutOfPlateauError
        * CollisionError
        """
        next_x = self.x + round(cos(self.direction))
        next_y = self.y + round(sin(self.direction))
        if not self.plateau.is_in_range(next_x, next_y):
            log.error("The Next move is out of a plateau range. Next move would be {},{}".format(next_x, next_y))
            raise OutOfPlateauError("Next move is out of a plateau range")
        if not self.plateau.is_position_available(next_x, next_y):
            log.error("The Next move will collide with other rover. Next move would be {},{}".format(next_x, next_y))
            raise CollisionError("Next move will collide with other rover")
        self.x = next_x
        self.y = next_y
        log.debug("Moved x,y = {}, {} Now {},{}".format(round(cos(self.direction)), round(sin(self.direction)), self.x, self.y))

    def parse_commands(self, commands):
        log.debug("Parsing rover commands")
        if type(commands) is not str:
            log.error("The commands is not str type. Received {}".format(type(commands)))
            raise TypeError("The commands must be str")
        commands = commands.upper()
        instructions = {
            "L": self.rotate_left,
            "R": self.rotate_right,
            "M": self.move
        }
        for command in commands:
            log.debug("Comand received {}".format(command))
            instructions[command]()

    def get_location(self):
        """Returns a tuple of the rover location"""
        return (self.x, self.y)

    def get_direction(self):
        "Return currect cardinal compas direction of the rover."
        return self._convert_to_compas(self.direction)

    @staticmethod
    def _convert_to_compas(radians):
        """Convenience method to convert the radians to the cardinal compass points

        Parameters
        ----------
        radians : float
            Radians to convert

        Returns
        -------
        str
            Cardinal compass points
        """
        if radians < 0:
            convert_direction = {-3 * pi / 2: 'N', -pi / 2: 'S', 0.0: 'E', -pi: 'W'}
            return convert_direction[radians % (2 * -pi)]
        else:
            convert_direction = {pi / 2: 'N', 3 * pi / 2: 'S', 0.0: 'E', pi: 'W'}
            return convert_direction[radians % (2 * pi)]
