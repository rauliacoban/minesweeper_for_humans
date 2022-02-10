from cell import *
import random
import ctypes
from tkinter import *


class Game:
    def __init__(self, board_frame, mines_label, n_mines):
        self.board_frame = board_frame
        self.mines_label = mines_label
        self.n_mines = n_mines
        self.remaining_mines = n_mines
        self.cells = []
        self.started = False
        self.is_game_over = False

        for x in range(CELL_HEIGHT):
            for y in range(CELL_WIDTH):
                c = Cell(x, y, self)
                c.create_button(board_frame)
                c.button.grid(row=x, column=y)
                self.cells.append(c)

        self.update_mine_display(0)

    def update_mine_display(self, increment):
        self.remaining_mines += increment
        self.mines_label.config(text=f'{self.remaining_mines}')

    def get_cell(self, coords):
        for cell in self.cells:
            if cell.coords == coords:
                return cell

    def game_over(self):
        self.is_game_over = True
        print('Game over!')
        ctypes.windll.user32.MessageBoxW(0, 'Clicked on a mine!', 'Game Over', 0)
        for cell in self.cells:
            if cell.covered:
                if cell.ismine:
                    cell.button.config(text='!')
                else:
                    cell.button.config(text=f'{number_coding[cell.value]}')

    def randomize(self, start):
        valid_distribution = False

        while not valid_distribution:
            valid_distribution = True
            mines = [start]

            while start in mines:
                mines = random.sample(self.cells, self.n_mines)

            for neighbor in start.get_neighbors():
                if neighbor in mines:
                    valid_distribution = False
                    break
                for far_neighbor in neighbor.get_neighbors():
                    if far_neighbor in mines:
                        valid_distribution = False

        for cell in mines:
            cell.ismine = True
            for neighbor in cell.get_neighbors():
                if not neighbor.ismine:
                    neighbor.value += 1
