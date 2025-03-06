import tkinter as tk
import sys
import persons_pandas_lib as persons
from PIL import Image, ImageTk


class App:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("WCA")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)

        self.create_gui()

    def quit(self) -> None:
        self.root.quit()
        self.root.destroy()

    def generate_image(self, image_path: str) -> None:
        bilde = Image.open(image_path)
        bilde = bilde.resize((600, 450))
        bilde = ImageTk.PhotoImage(bilde)
        label = tk.Label(self.frame, image=bilde)
        label.image = bilde
        label.pack()

    def create_scroll(self) -> None:
        scrollbar = tk.Scrollbar(self.root, command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.frame.bind(
            "<Configure>",  # on resize
            lambda _: self.canvas.config(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.config(yscrollcommand=scrollbar.set)

        self.canvas.bind_all(
            "<Button-4>", lambda _: self.canvas.yview_scroll(-1, "units")
        )
        self.canvas.bind_all(
            "<Button-5>", lambda _: self.canvas.yview_scroll(1, "units")
        )

    def create_gui(self) -> None:
        self.canvas = tk.Canvas()
        self.frame = tk.Frame()

        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.frame)

        self.create_scroll()

        self.generate_image(persons.gender_names())
        self.generate_image(persons.countries())
        self.generate_image(persons.changes())
        self.generate_image(persons.first_names())
        self.generate_image(persons.last_names())
        self.generate_image(persons.unigue_names())
        self.generate_image(persons.name_lengths())


if __name__ == "__main__" and not sys.flags.interactive:
    root = tk.Tk()
    app = App(root)
    tk.mainloop()
