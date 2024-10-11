from graphics import Line, Point, Window

class Cell:
    def __init__(self, x1:int, y1:int, x2:int, y2:int, win:Window | None = None, has_left_wall = True, has_right_wall = True, has_top_wall = True , has_bottom_wall = True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._tl = Point(x1, y1)
        self._br = Point(x2, y2)
        self._bl = Point(x1, y2)
        self._tr = Point(x2, y1)
        self._win = win
        self.visited = False

    def draw(self, fill_color="black"):
        left_wall = Line(self._tl, self._bl)
        right_wall = Line(self._tr, self._br)
        top_wall = Line(self._tl, self._tr)
        bottom_wall = Line(self._bl, self._br)
        if self.has_left_wall:
            self._win.draw_line(left_wall, fill_color)
        else:
            self._win.draw_line(left_wall, "white")
        if self.has_right_wall:
            self._win.draw_line(right_wall, fill_color)
        else:
            self._win.draw_line(right_wall, "white")
        if self.has_top_wall:
            self._win.draw_line(top_wall, fill_color)
        else:
            self._win.draw_line(top_wall, "white")
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, fill_color)
        else:
            self._win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell: "Cell", undo=False):
        mid_1 = Point((self._tl.x + self._tr.x) // 2, (self._tr.y + self._br.y) // 2)
        mid_2 = Point((to_cell._tl.x + to_cell._tr.x) // 2, (to_cell._tr.y + to_cell._br.y) // 2)
        line = Line(mid_1, mid_2)

        if undo:
            self._win.draw_line(line, "gray")
        else:
            self._win.draw_line(line, "red")