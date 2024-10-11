import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_2(self):
        num_cols = 5
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_3(self):
        num_cols = 100
        num_rows = 75
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_4(self):
        num_cols = 0
        num_rows = 10
        with self.assertRaises(Exception):
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    
    def test_maze_create_cells_5(self):
        num_cols = -5
        num_rows = 10
        with self.assertRaises(Exception):
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)



if __name__ == "__main__":
    unittest.main()