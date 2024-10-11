from cell import Cell
import time
from graphics import Window
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win:Window | None = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)

        self._create_cells()

    def _create_cells(self):

        if self.num_rows < 1 or self.num_cols < 1:
            raise Exception("You need a bigger number, doofus!")
        
        for i in range(self.num_cols):
            self._cells_col = []
            for j in range(self.num_rows):
                cell = Cell(self.x1 + self.cell_size_x * i,
                            self.y1 + self.cell_size_y * j,
                            self.x1 + self.cell_size_x * (i + 1), 
                            self.y1 + self.cell_size_y * (j + 1), 
                            self.win)
                self._cells_col.append(cell)
            self._cells.append(self._cells_col)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        time.sleep(0.005)
        self.win.redraw()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            cells_to_visit = []
            if i-1 >= 0:
                if self._cells[i-1][j].visited == False:
                    cells_to_visit.append((i-1, j))
            if i+1 < self.num_cols:
                if self._cells[i+1][j].visited == False:
                    cells_to_visit.append((i+1, j))
            if j-1 >= 0:
                if self._cells[i][j-1].visited == False:
                    cells_to_visit.append((i, j-1))
            if j+1 < self.num_rows:
                if self._cells[i][j+1].visited == False:
                    cells_to_visit.append((i, j+1))

            if not cells_to_visit:
                self._draw_cell(i, j)
                return
            else:
                x2, y2 = random.choice(cells_to_visit)
                if i < x2 <= self.num_cols-1:
                    self._cells[x2][y2].has_left_wall = False
                    self._cells[i][j].has_right_wall = False
                if i > x2 >= 0:
                    self._cells[x2][y2].has_right_wall = False
                    self._cells[i][j].has_left_wall = False
                if j < y2 <= self.num_rows-1:
                    self._cells[x2][y2].has_top_wall = False
                    self._cells[i][j].has_bottom_wall = False
                if j > y2 >= 0:
                    self._cells[x2][y2].has_bottom_wall = False
                    self._cells[i][j].has_top_wall = False

                self._break_walls_r(x2, y2)
    
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        return self._solve_r(i=0, j=0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        if i-1 >= 0:
            if self._cells[i-1][j].visited == False and self._cells[i][j].has_left_wall == False:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                if self._solve_r(i-1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i-1][j], True)
        if i+1 < self.num_cols:
            if self._cells[i+1][j].visited == False and self._cells[i][j].has_right_wall == False:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                if self._solve_r(i+1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i+1][j], True)
        if j-1 >= 0:
            if self._cells[i][j-1].visited == False and self._cells[i][j].has_top_wall == False:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                if self._solve_r(i, j-1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j-1], True)
        if j+1 < self.num_rows:
            if self._cells[i][j+1].visited == False and self._cells[i][j].has_bottom_wall == False:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._solve_r(i, j+1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j+1], True)

        return False
