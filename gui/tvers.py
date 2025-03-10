import tkinter as tk
import sys


class Tvers:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Tvers")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)

        self.correct_word = "HELLO"

        self.boxes = []
        self.letter_labels = []
        self.letter_frames = []

        self.create_gui()

    def quit(self) -> None:
        self.root.quit()
        self.root.destroy()

    def draw_boxes(self, boxes: int, size: int, padding: int) -> None:
        padding = size + padding
        for i in range(boxes):
            offset = padding * i
            box = self.canvas.create_rectangle(
                size + offset, size, size * 2 + offset, size * 2, fill="white"
            )
            self.boxes.append(box)

    def draw_letters(self, letters: list[str], size: int, padding: int) -> None:
        padding = size + padding
        for i, letter in enumerate(letters):
            offset = padding * i
            frame = tk.Frame(self.root, width=size, height=size, bg="white")
            label = tk.Label(
                frame, text=letter, font=("JetBrainsMono Nerd Font", 24), bg="white"
            )
            label.place(relx=0.5, rely=0.5, anchor="center")
            frame.place(x=200 + offset, y=200)
            frame.bind("<Button-1>", self.on_drag_start)
            frame.bind("<B1-Motion>", self.on_drag_motion)
            frame.bind("<ButtonRelease-1>", self.on_drag_release)
            self.letter_labels.append(label)
            self.letter_frames.append(frame)

    def create_gui(self) -> None:
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()
        self.draw_boxes(len(self.correct_word), 80, 20)
        self.draw_letters(list(self.correct_word), 80, 20)

    def on_drag_start(self, event: tk.Event) -> None:
        widget = event.widget
        widget.lift()
        self._drag_data = (event.x, event.y)

    def on_drag_motion(self, event: tk.Event) -> None:
        widget = event.widget
        x = widget.winfo_x() - self._drag_data[0] + event.x
        y = widget.winfo_y() - self._drag_data[1] + event.y
        widget.place(x=x, y=y)

    def on_drag_release(self, event: tk.Event) -> None:
        widget = event.widget
        x, y = widget.winfo_x(), widget.winfo_y()
        for i, box in enumerate(self.boxes):
            coords = self.canvas.coords(box)
            if (coords[0] < x < coords[2]) and (coords[1] < y < coords[3]):
                for letter in self.letter_labels:
                    if self.correct_word[i] == letter.cget("text"):
                        self.canvas.itemconfig(box, fill="green")
                    else:
                        self.canvas.itemconfig(box, fill="red")
                widget.place(x=coords[0] + 80, y=coords[1])
                return
        widget.place(x=200 + self.letter_frames.index(widget) * 100, y=200)


if __name__ == "__main__" and not sys.flags.interactive:
    root = tk.Tk()
    tvers = Tvers(root)
    root.mainloop()
