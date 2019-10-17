from src.plateau import Mars
import logging as log
import sys
import os

log.basicConfig(level=log.DEBUG)

if sys.version_info.major < 3:
    print("The program support only python3 and higher. Python2 will be dead starting 2020 :(")
    exit(1)


def user_input():
    "Method to execute using user input"
    plateau_corner = input("Input the plateau upper-left corner location as X and Y coordinates separated by space. Example: 13 15\n")
    plateau = Mars.from_string(plateau_corner)  # init plateau

    while(True):
        print("Please enter the rover initial location for the deployment. The format is X Y D. Where:")
        print("X and Y are coordinates of the rover as int")
        print("D - is the cardinal compass points direction. E.g. one of the 'NSEW' letters.")
        rover_location = input()
        rover = plateau.deploy_rover(rover_location)  # deploy rover

        print("Input the commands string for the rover. Currently Mars rover supports next commands:")
        print("L - rotate left 90 degrees")
        print("R - rotate right 90 degrees")
        print("M - move one point into the set direction")
        commands = input()
        rover.parse_commands(commands)

        more = input("Do you wish to add more rovers? yes continues or anything else to print final locations and exit\n")
        if more.lower() != "yes":
            break

    # print rover locations
    for rover in plateau.rovers.values():
        log.info("Rover ID: {} Location: {} Heading: {}\n".format(rover.id, rover.get_location(), rover.get_direction()))
        print("{} {} {}\n".format(rover.x, rover.y, rover.get_direction()))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fn = sys.argv[1]
        if os.path.exists(fn):
            # execute file commands
            with open(fn, 'r') as f:
                plateau = Mars.from_string(f.readline().rstrip('\n'))  # init plateau
                for line in f:
                    rover = plateau.deploy_rover(line.rstrip('\n'))  # deploy rover
                    rover.parse_commands(f.readline().rstrip('\n'))  # control the rover
                for rover in plateau.rovers.values():
                    log.info("Rover ID: {} Location: {} Heading: {}\n".format(rover.id, rover.get_location(), rover.get_direction()))
                    print("{} {} {}\n".format(rover.x, rover.y, rover.get_direction()))
            exit(0)
        else:
            log.error("Specified file not found!")
    log.info("Maual entry")
    user_input()
