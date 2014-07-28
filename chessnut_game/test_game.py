import unittest
from game import ChessnutGame


def build_forward_diagonal(_file, rank):
    """Determine all the spaces in a forward diagonal beginning at
    the specified cell.
    """
    while 0 <= rank <= 7 and 0 <= _file <= 7:
        yield (_file, rank)
        _file += 1
        rank += 1


def build_backward_diagonal(_file, rank):
    """Determine all the spaces in a backward diagonal beginning at
    the specified cell.
    """
    while 0 <= rank <= 7 and 0 <= _file <= 7:
        yield (_file, rank)
        _file -= 1
        rank += 1


class TestCoordinatesToDiagonals(unittest.TestCase):
    """Test the _coordinates_to_forward_diagonal and
    _coordinates_to_backward_diagonal methods.
    """
    def setUp(self):
        self.c = ChessnutGame()

    def test_coordinates_to_forward_diagonal(self):
        """Assert that all spaces are assigned to their correct forward
        diagonal.
        """
        diagonals = [
            (0, 7),
            (0, 6),
            (0, 5),
            (0, 4),
            (0, 3),
            (0, 2),
            (0, 1),
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (6, 0),
            (7, 0),
        ]

        for _file, rank in diagonals:
            for difile, dirank in build_forward_diagonal(_file, rank):
                self.assertEqual(
                    (_file, rank),
                    self.c._coordinates_to_forward_diagonal(difile, dirank)
                )

    def test_coordinates_to_backward_diagonal(self):
        """Assert that all spaces are assigned to their correct backward
        diagonal.
        """
        diagonals = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (6, 0),
            (7, 0),
            (7, 1),
            (7, 2),
            (7, 3),
            (7, 4),
            (7, 5),
            (7, 6),
            (7, 7),
        ]

        for _file, rank in diagonals:
            for difile, dirank in build_backward_diagonal(_file, rank):
                self.assertEqual(
                    (_file, rank),
                    self.c._coordinates_to_backward_diagonal(difile, dirank)
                )


class TestGenerateDiagonals(unittest.TestCase):
    """Test the _generate_forward_diagonals and _generate_backward_diagonals
    methods.
    """
    def setUp(self):
        self.c = ChessnutGame()

    def test_generate_forward_diagonal(self):
        """Test the _generate_forward_diagonal method."""

    def test_generate_backward_diagonal(self):
        """Test the _generate_backward_diagonal method."""


class TestFirstBlockedMoveFrom(unittest.TestCase):
    """Test the first_blocked_move_from method of the game class."""
    def setUp(self):
        self.c = ChessnutGame()

    def circle_piece(_file, rank, radius):
        """Create a circle of Pawns around the the given file and rank."""

    def test_empty_board(self):
        """Assert that the method returns (None, None) in every direction
        for an empty board.
        """

    def test_all_directions(self):
        """Assert that the method returns the expected space in each direction.
        """

    def test_all_directions_layered(self):
        """Assert that the method returns the expected value for multiple
        blocked spaces in a row.
        """


if __name__ == '__main__':
    unittest.main()
