from tkinter import Button
import random
import settings
from utils import *
import ctypes


class Cell:
    all = []
    started = False
    is_game_over = False

    def __init__(self, x, y, ismine=False):
        self.ismine = ismine
        self.value = 0
        self.button = None
        self.coords = (x, y)
        self.flagged = False
        self.covered = True
        Cell.all.append(self)

    def create_button(self, location):
        button = Button(location,
                        text='',
                        width=3,
                        height=1,
                        bg='grey',
                        font='sans 9 bold'
        )
        button.bind('<Button-1>', self.left_click)
        button.bind('<Button-3>', self.right_click)
        self.button = button

    def uncover_neighbors(self):
        flags = 0
        neighbors = self.get_neighbors()
        for neighbor in neighbors:
            if neighbor.flagged:
                flags += 1
        if flags == self.value:
            for neighbor in neighbors:
                if not neighbor.flagged:
                    neighbor.left_click(False)

    def left_click(self, event):
        if Cell.is_game_over or self.flagged:
            return

        if not Cell.started:
            Cell.randomize(self)
            Cell.started = True

        if (self.ismine):
            self.button.config(bg='magenta', text='!')
            Cell.game_over()
            return
        self.setText()

        if (self.covered and self.value == 0) or (not self.covered and event):
            self.covered = False
            self.uncover_neighbors()
        if self.covered:
            self.covered = False


    def right_click(self, event):
        if not self.covered:
            return

        if(self.flagged):
            self.button.config(bg='grey')
        else:
            self.button.config(bg='black')
        self.flagged = not self.flagged

    def setText(self):
        if self.ismine:
            self.button.config(text='!', bg='white')
        else:
            self.button.config(text=f'{number_coding[self.value]}', fg=f'{color_coding[self.value]}', bg='white')

    def get_neighbors(self):
        neighbors = []
        for direction in settings.directions:
            coords = add_coords(self.coords, direction)
            if valid(coords):
                neighbors.append(Cell.get_cell(coords))
        return neighbors

    @staticmethod
    def randomize(start):
        mines = [start]
        while start in mines:
            mines = random.sample(Cell.all, MINES)

        for cell in mines:
            for neighbor in cell.get_neighbors():
                if neighbor is start:
                    Cell.randomize(start)
                    return

        for cell in mines:
            cell.ismine = True
            for neighbor in cell.get_neighbors():
                if not neighbor.ismine:
                    neighbor.value += 1

    @staticmethod
    def get_cell(coords):
        for cell in Cell.all:
            if cell.coords == coords:
                return cell

    @staticmethod
    def game_over():
        print('Game over!')
        ctypes.windll.user32.MessageBoxW(0, 'Clicked on a mine!', 'Game Over', 0)
        for cell in Cell.all:
            if cell.covered:
                if cell.ismine:
                    cell.button.config(text='!')
                else:
                    cell.button.config(text=f'{number_coding[cell.value]}')
            cell.button.unbind('<Button-1>')
            cell.button.unbind('<Button-3>')