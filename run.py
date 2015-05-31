from display import Display

__author__ = 'Dani'

if __name__ == "__main__":
    column1 = [18, 23, 4, 17, 27]
    column2 = [26, 19, 13, 6, 5]
    ports = [column1, column2]
    display = Display(5, 2, ports)
    text = input('Text: ')
    display.write(text)
    display.show()
