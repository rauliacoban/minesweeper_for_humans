from tkinter import *
from game import *

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

mines_label = Label(root,
                   bg='red',
                   width=5,
                   height=1)
mines_label.place(x=WIDTH/2 + 50, y=50)

cells_label = Label(root,
                   bg='blue',
                   width=5,
                   height=1)
cells_label.place(x=WIDTH/2 - 50, y=50)

def reset(event):
    game = Game(center_frame, mines_label, cells_label)

restart_btn = Button(text='restart', bg='yellow')
restart_btn.place(x=WIDTH/2, y=50)
restart_btn.bind('<Button-1>', reset)









reset(0)
root.mainloop()
