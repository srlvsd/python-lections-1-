def button_check():
    print("все работает хорошо!")
import tkinter
from tkinter import ttk
root = tkinter.Tk()
button = ttk.Button(root, text ="Это кнопка", command=button_check)
button.pack()
root.mainloop()
