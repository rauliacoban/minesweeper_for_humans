from cell import *
#Game(location='center_frame', n_mines=MINES)

class Game:
    def __init__(self, location, n_mines):
        self.location = location
        self.n_mines = n_mines
        self.cells = []
        self.started = False
        self.is_game_over = False

        for x in range(CELL_HEIGHT):
            for y in range(CELL_WIDTH):
                c = Cell(x, y, self)
                c.create_button(location)
                c.button.grid(row=x, column=y)
                self.cells.append(c)

    def get_cell(self, coords):
        for cell in self.cells:
            if cell.coords == coords:
                #print(f'what get_cell sends:{cell.coords}')
                return cell

    def game_over(self):
        print('Game over!')
        ctypes.windll.user32.MessageBoxW(0, 'Clicked on a mine!', 'Game Over', 0)
        for cell in self.cells:
            if cell.covered:
                if cell.ismine:
                    cell.button.config(text='!')
                else:
                    cell.button.config(text=f'{number_coding[cell.value]}')
            cell.button.unbind('<Button-1>')
            cell.button.unbind('<Button-3>')

    def randomize(self, start):
        valid_distribution = False

        while not valid_distribution:
            valid_distribution = True
            mines = [start]

            while start in mines:
                mines = random.sample(self.cells, self.n_mines)

            for cell in mines:
                for neighbor in cell.get_neighbors():
                    if neighbor is start:
                        valid_distribution = False

        for cell in mines:
            cell.ismine = True
            for neighbor in cell.get_neighbors():
                if not neighbor.ismine:
                    neighbor.value += 1
