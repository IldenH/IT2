import tkinter as tk
from tkinter import font
import sys
from PIL import Image, ImageTk


class App:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Hello, world!")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)

        self.create_gui()

    def quit(self) -> None:
        self.root.quit()
        self.root.destroy()

    def skriv_ut(self) -> None:
        self.hilsen.configure(text=f"Hallo {self.navn.get()}!")

    def generate_image(self) -> str:
        return "image.png"

    def create_gui(self) -> None:
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="JetBrainsMono Nerd Font", size=20)

        frame = tk.Frame(self.root)
        frame.grid(row=0, column=1)

        bilde = Image.open(self.generate_image())
        bilde = bilde.resize((150, 150))
        bilde = ImageTk.PhotoImage(bilde)
        label = tk.Label(self.root, image=bilde)
        label.image = bilde
        label.grid(row=0, column=0)

        tk.Label(self.root, text="Hva heter du?").grid(row=0, column=1)

        self.navn = tk.Entry(root)
        self.navn.grid(row=1, column=1)

        submit_button = tk.Button(self.root, text="Submit", command=self.skriv_ut)
        submit_button.grid(row=2, column=1)

        self.hilsen = tk.Label(root)
        self.hilsen.grid(row=3, column=0)


if __name__ == "__main__" and not sys.flags.interactive:
    root = tk.Tk()
    app = App(root)
    root.mainloop()
