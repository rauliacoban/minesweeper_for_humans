from tkinter import *
from settings import *
from cell import *

root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Minesweeper')
root.resizable(False, False)
root.configure(bg='black')


top_frame = Frame(root,
                  bg='black',
                  width=WIDTH,
                  height=HEIGHT*TOP_RATIO)
top_frame.place(x=0, y=0)

left_bar = Frame(root,
                 bg='black',
                 width=WIDTH*LEFT_RATIO,
                 height=HEIGHT - HEIGHT*TOP_RATIO)
left_bar.place(x=0, y=HEIGHT*TOP_RATIO)

center_frame = Frame(root,
                     bg='black',
                     width=WIDTH - WIDTH*LEFT_RATIO,
                     height=HEIGHT - HEIGHT*TOP_RATIO)
center_frame.place(x=WIDTH*LEFT_RATIO, y=HEIGHT*TOP_RATIO)


for x in range(CELL_HEIGHT):
    for y in range(CELL_WIDTH):
        c = Cell(x, y)
        c.create_button(center_frame)
        c.button.grid(row=x, column=y)

root.mainloop()
