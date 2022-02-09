from tkinter import Button
import random
import settings
from utils import *
import ctypes


class Cell:

    def __init__(self, x, y, game):
        self.ismine = False
        self.value = 0
        self.button = None
        self.coords = (x, y)
        self.flagged = False
        self.covered = True
        self.game=game

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
        if self.game.is_game_over or self.flagged:
            return

        if not self.game.started:
            self.game.randomize(self)
            self.game.started = True

        if (self.ismine):
            self.button.config(bg='magenta', text='!')
            self.game.game_over()
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
            print(self.value)
            self.button.config(text=f'{number_coding[self.value]}', fg=f'{color_coding[self.value]}', bg='white')

    def get_neighbors(self):
        neighbors = []
        for direction in settings.directions:
            coords = add_coords(self.coords, direction)
            if valid(coords):
                neighbors.append(self.game.get_cell(coords))
                #print(f'what get_neighbors receives:{neighbors[-1].coords}')
        return neighbors