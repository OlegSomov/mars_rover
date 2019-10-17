from src.plateau import Mars


def test_integrated_file():
    with open("tests/test.txt", 'r') as f:
        plateau = Mars.from_string(f.readline().rstrip('\n'))  # init plateau
        assert plateau.x == 5
        assert plateau.y == 5
        for line in f:
            rover = plateau.deploy_rover(line.rstrip('\n'))  # deploy rover
            rover.parse_commands(f.readline().rstrip('\n'))  # control the rover

        assert len(plateau.rovers) == 2
        assert plateau.rovers["1"].x == 1
        assert plateau.rovers["1"].y == 3
        assert plateau.rovers["1"].get_direction() == "N"

        assert plateau.rovers["2"].x == 5
        assert plateau.rovers["2"].y == 1
        assert plateau.rovers["2"].get_direction() == "E"
