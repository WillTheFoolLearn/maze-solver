from graphics import Window, Point, Line
from cell import Cell
from maze import Maze


def main():
    

    win = Window(800, 600)
    num_rows = 30
    num_cols = 40

    maze = Maze(5, 5, num_rows, num_cols, (win.width - 10)/num_cols, (win.height - 10)/num_rows, win)

    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze.solve()
    
    win.wait_for_close()

if __name__ == "__main__":
    main()