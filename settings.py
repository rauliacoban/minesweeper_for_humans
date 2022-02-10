WIDTH = 1200
HEIGHT = 600
TOP_RATIO = 0.15
LEFT_RATIO = 0.15

CELL_WIDTH = 31
CELL_HEIGHT = 16
MINES = 99
FREE_CELLS = CELL_WIDTH * CELL_HEIGHT - MINES

directions = ((-1, -1), (-1, 0), (-1, 1), (0, 1),
              (1, 1), (1, 0), (1, -1), (0, -1))

color_coding = {
    0: 'white',
    1: 'blue',
    2: 'green',
    3: 'red',
    4: '#f0c818',
    5: 'cyan',
    6: 'magenta',
    7: 'magenta',
    8: 'magenta'
}

number_coding = {
    0: '',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    '': '&'
}
