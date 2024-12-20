#GUI WITH TKINTER
import tkinter as tk

window = tk.Tk()
window.title("Hello World")
window.geometry("500x500")

hello = tk.Label(text="Hello World!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()