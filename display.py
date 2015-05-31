from queue import Queue
import time

from character import Character
import port_adapter

__author__ = 'Dani'


class Display:
    def __init__(self, rows, columns, ports=None):
        self.matrix = []
        self.ports = ports
        self.rows = rows
        self.columns = columns
        for column in range(0, self.columns):
            column = []
            for row in range(0, self.rows):
                column.append(0)
            self.matrix.append(column)
        self.buffer = Queue()
        self.separator = [0 for _ in range(0, self.rows)]

    def write(self, text):
        for char in text:
            if not self.buffer.empty():
                self.buffer.put(self.separator)
            character = Character(char)
            matrix = character.matrix
            columns = len(matrix[0])
            rows = len(matrix)
            for column_index in range(0, columns):
                column = []
                for row_index in range(rows, 0, -1):
                    column.append(matrix[row_index - 1][column_index])
                self.buffer.put(column)
        for _ in range(0, self.columns):
            self.buffer.put(self.separator)

    def print_current_buffer(self):
        while not self.buffer.empty():
            column = self.buffer.get()
            for item in column:
                print('{}'.format(item), end=' ')
                time.sleep(0.05)
            print()

    def show(self):
        if self.ports:
            port_adapter.setup(self.ports)
        while not self.buffer.empty():
            column = self.buffer.get()
            for pos in range(1, self.columns):
                self.matrix[pos - 1] = self.matrix[pos]
            self.matrix[self.columns - 1] = column
            if self.ports:
                for column_index in range(0, self.columns):
                    for row_index in range(0, self.rows):
                        item = self.matrix[column_index][row_index]
                        port = self.ports[column_index][row_index]
                        port_adapter.output(port, item)
            for item in column:
                print('{}'.format(item), end=' ')
            print()
            time.sleep(0.2)
