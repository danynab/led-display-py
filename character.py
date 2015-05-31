__author__ = 'Dani'


class Character:
    def __init__(self, char):
        self.min_rows = 5
        self.min_columns = 4
        self.columns = self.min_columns
        self.rows = self.min_rows
        self.matrix = []
        self._draw_char(char)

    def _init_matrix(self):
        for i in range(0, self.rows):
            row = []
            for y in range(0, self.columns):
                row.append(0)
            self.matrix.append(row)

    def _draw_char(self, char):
        if char == '0':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 3)
            self._mark_section_horizontal(2, 5, 3)
            self._mark_section_vertical(1, 2, 4)
            self._mark_section_vertical(4, 2, 4)
        elif char == '1':
            self.columns = 3
            self._init_matrix()
            self._mark_point(1, 2)
            self._mark_section_horizontal(2, 1, 3)
            self._mark_section_vertical(3, 2, 5)
        elif char == '2':
            self._init_matrix()
            self._mark_section_horizontal(1, 1, 4)
            self._mark_section_horizontal(1, 3, 4)
            self._mark_section_horizontal(1, 5, 4)
            self._mark_point(4, 2)
            self._mark_point(1, 4)
        elif char == '3':
            self._init_matrix()
            self._mark_section_horizontal(1, 1, 3)
            self._mark_section_horizontal(2, 3, 3)
            self._mark_section_horizontal(1, 5, 3)
            self._mark_point(4, 2)
            self._mark_point(4, 4)
        elif char == '4':
            self._init_matrix()
            self._mark_section_horizontal(2, 3, 3)
            self._mark_section_vertical(4, 1, 5)
            self._mark_section_vertical(1, 1, 3)
        elif char == '5':
            self._init_matrix()
            self._mark_section_horizontal(1, 1, 4)
            self._mark_section_horizontal(1, 3, 4)
            self._mark_section_horizontal(1, 5, 4)
            self._mark_point(1, 2)
            self._mark_point(4, 4)
        elif char == '6':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 4)
            self._mark_section_horizontal(1, 3, 4)
            self._mark_section_horizontal(2, 5, 3)
            self._mark_section_vertical(1, 2, 4)
            self._mark_point(4, 4)
        elif char == '7':
            self._init_matrix()
            self._mark_section_horizontal(1, 1, 4)
            self._mark_point(1, 5)
            self._mark_point(2, 4)
            self._mark_point(3, 3)
            self._mark_point(4, 2)
        elif char == '8':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 3)
            self._mark_section_horizontal(2, 3, 3)
            self._mark_section_horizontal(2, 5, 3)
            self._mark_point(1, 2)
            self._mark_point(1, 4)
            self._mark_point(4, 2)
            self._mark_point(4, 4)
        elif char == '9':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 3)
            self._mark_section_horizontal(2, 3, 3)
            self._mark_section_horizontal(1, 5, 3)
            self._mark_section_vertical(1, 2, 3)
            self._mark_section_vertical(4, 2, 4)
        elif char.lower() == 'a':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 3)
            self._mark_section_horizontal(2, 3, 3)
            self._mark_section_vertical(1, 2, 5)
            self._mark_section_vertical(4, 2, 5)
        elif char.lower() == 'b':
            self._init_matrix()
            self._mark_section_horizontal(1, 1, 3)
            self._mark_section_horizontal(1, 5, 3)
            self._mark_section_vertical(2, 2, 4)
            self._mark_point(3, 3)
            self._mark_point(4, 2)
            self._mark_point(4, 4)
        elif char.lower() == 'c':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 4)
            self._mark_section_horizontal(2, 5, 4)
            self._mark_section_vertical(1, 2, 4)
        elif char.lower() == 'd':
            self._init_matrix()
            self._mark_section_horizontal(1, 1, 3)
            self._mark_section_horizontal(1, 5, 3)
            self._mark_section_vertical(2, 2, 4)
            self._mark_section_vertical(4, 2, 4)
        elif char.lower() == 'e':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 4)
            self._mark_section_horizontal(2, 3, 3)
            self._mark_section_horizontal(2, 5, 4)
            self._mark_section_vertical(1, 1, 5)
        elif char.lower() == 'f':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 4)
            self._mark_section_horizontal(2, 3, 3)
            self._mark_section_vertical(1, 1, 5)
        elif char.lower() == 'g':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 4)
            self._mark_section_horizontal(3, 3, 4)
            self._mark_section_horizontal(2, 5, 4)
            self._mark_section_vertical(1, 2, 4)
            self._mark_section_vertical(4, 3, 4)
        elif char.lower() == 'h':
            self._init_matrix()
            self._mark_section_horizontal(2, 3, 3)
            self._mark_section_vertical(1, 1, 5)
            self._mark_section_vertical(4, 1, 5)
        elif char.lower() == 'i':
            self.columns = 3
            self._init_matrix()
            self._mark_section_horizontal(1, 1, 3)
            self._mark_section_horizontal(1, 5, 3)
            self._mark_section_vertical(2, 2, 4)
        elif char.lower() == 'j':
            self._init_matrix()
            self._mark_section_horizontal(2, 5, 3)
            self._mark_section_vertical(4, 1, 4)
            self._mark_point(1, 4)
        elif char.lower() == 'k':
            self._init_matrix()
            self._mark_section_vertical(1, 1, 5)
            self._mark_point(2, 3)
            self._mark_point(3, 2)
            self._mark_point(3, 4)
            self._mark_point(4, 1)
            self._mark_point(4, 5)
        elif char.lower() == 'l':
            self._init_matrix()
            self._mark_section_horizontal(1, 5, 4)
            self._mark_section_vertical(1, 1, 4)
        elif char.lower() == 'm':
            self._init_matrix()
            self._mark_section_vertical(1, 2, 5)
            self._mark_section_vertical(2, 1, 2)
            self._mark_section_vertical(3, 1, 2)
            self._mark_section_vertical(4, 2, 5)
        elif char.lower() == 'n':
            self._init_matrix()
            self._mark_section_vertical(1, 1, 5)
            self._mark_section_vertical(4, 1, 5)
            self._mark_section_vertical(2, 2, 3)
            self._mark_section_vertical(3, 3, 4)
        elif char.lower() == 'n^':
            self._init_matrix()
            self._mark_section_horizontal(1, 1, 4)
            self._mark_section_vertical(1, 3, 5)
            self._mark_section_vertical(4, 3, 5)
            self._mark_point(2, 4)
            self._mark_point(3, 5)
        elif char.lower() == 'o':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 3)
            self._mark_section_horizontal(2, 5, 3)
            self._mark_section_vertical(1, 2, 4)
            self._mark_section_vertical(4, 2, 4)
        elif char.lower() == 'p':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 3)
            self._mark_section_horizontal(2, 3, 3)
            self._mark_section_vertical(1, 1, 5)
            self._mark_point(4, 2)
        elif char.lower() == 'q':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 3)
            self._mark_section_horizontal(2, 5, 4)
            self._mark_section_vertical(1, 2, 4)
            self._mark_section_vertical(4, 2, 4)
            self._mark_point(3, 4)
        elif char.lower() == 'r':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 3)
            self._mark_section_horizontal(2, 3, 3)
            self._mark_section_vertical(1, 1, 5)
            self._mark_point(4, 2)
            self._mark_point(3, 4)
            self._mark_point(4, 5)
        elif char.lower() == 's':
            self._init_matrix()
            self._mark_section_horizontal(2, 1, 4)
            self._mark_section_horizontal(2, 3, 3)
            self._mark_section_horizontal(1, 5, 3)
            self._mark_point(1, 2)
            self._mark_point(4, 4)
        elif char.lower() == 't':
            self._init_matrix()
            self._mark_section_horizontal(1, 1, 4)
            self._mark_section_vertical(2, 2, 5)
            self._mark_section_vertical(3, 2, 5)
        elif char.lower() == 'u':
            self._init_matrix()
            self._mark_section_horizontal(2, 5, 3)
            self._mark_section_vertical(1, 1, 4)
            self._mark_section_vertical(4, 1, 4)
        elif char.lower() == 'v':
            self._init_matrix()
            self._mark_section_vertical(1, 1, 5)
            self._mark_section_vertical(4, 1, 2)
            self._mark_point(2, 4)
            self._mark_point(3, 3)
        elif char.lower() == 'w':
            self._init_matrix()
            self._mark_section_vertical(1, 1, 4)
            self._mark_section_vertical(2, 3, 5)
            self._mark_section_vertical(3, 3, 5)
            self._mark_section_vertical(4, 1, 4)
        elif char.lower() == 'x':
            self._init_matrix()
            self._mark_section_vertical(1, 1, 2)
            self._mark_section_vertical(4, 1, 2)
            self._mark_section_vertical(1, 4, 5)
            self._mark_section_vertical(4, 4, 5)
            self._mark_section_horizontal(2, 3, 3)
        elif char.lower() == 'y':
            self._init_matrix()
            self._mark_section_vertical(1, 1, 3)
            self._mark_section_vertical(4, 1, 5)
            self._mark_section_horizontal(2, 3, 3)
            self._mark_section_horizontal(1, 5, 3)
        elif char.lower() == 'z':
            self._init_matrix()
            self._mark_section_horizontal(1, 1, 4)
            self._mark_section_horizontal(1, 5, 4)
            self._mark_section_horizontal(2, 3, 3)
            self._mark_point(1, 4)
            self._mark_point(4, 2)
        else:
            self._init_matrix()

    def _mark_section_horizontal(self, x_initial, y, x_final):
        x_set = range(x_initial, x_final + 1)
        for x in x_set:
            self._mark_point(x, y)

    def _mark_section_vertical(self, x, y_initial, y_final):
        y_set = range(y_initial, y_final + 1)
        for y in y_set:
            self._mark_point(x, y)

    def _mark_point(self, x, y):
        if 0 < x < self.columns + 1 and 0 < y < self.rows + 1:
            self.matrix[y - 1][x - 1] = 1
