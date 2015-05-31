from pip._vendor.distlib.compat import raw_input

from display import Display

__author__ = 'Dani'

if __name__ == "__main__":
    column1 = [2, 3, 4, 17, 27]
    column2 = [26, 19, 13, 6, 5]
    ports = [column1, column2]
    display = Display(5, 2, ports)
    text = raw_input('Text: ')
    display.write(text)
    display.show()
