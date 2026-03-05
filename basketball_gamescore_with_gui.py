from tkinter import *

CALCULATOR_WINDOW = Tk()
CALCULATOR_WINDOW.title('Basketball Gamescore Calculator')

CALCULATOR_WINDOW.config(background='orange')

ICON = PhotoImage(file='C:\\Users\\azale\\Desktop\\python_projects\\ball_icon.png')
CALCULATOR_WINDOW.iconphoto(True, ICON)

LABEL = Label(CALCULATOR_WINDOW, text='Basketball Gamescore Calculator', font=('Comic Sans MS', 40, 'bold'))
LABEL.pack()

CALCULATOR_WINDOW.mainloop()