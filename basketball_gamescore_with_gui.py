from tkinter import *

CALCULATOR_WINDOW = Tk()
CALCULATOR_WINDOW.title('Basketball Gamescore Calculator')

CALCULATOR_WINDOW.config(background='orange')

ICON = PhotoImage(file='C:\\Users\\azale\\Desktop\\python_projects\\ball_icon.png')
CALCULATOR_WINDOW.iconphoto(True, ICON)

header = Label(CALCULATOR_WINDOW, 
              text='Basketball Gamescore Calculator', 
              font=('Comic Sans MS', 40, 'bold'),
              foreground='black',
              background='white',
              relief=RAISED,
              border=10,
              padx=5)
header.pack()

calculate_button = Button(CALCULATOR_WINDOW, text='Calculate Gamescore')
calculate_button.config(font=('Arial', 25, 'bold'))
calculate_button.config(activebackground='blue')
calculate_button.pack()

CALCULATOR_WINDOW.mainloop()