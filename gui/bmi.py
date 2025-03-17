import tkinter as tk
from PIL import Image, ImageTk

"""
   C0 C1 C2
R0  B L1 E1
R1  B L2 E2
R2  B  K  K
R3  R  R  R
R4  M  M  M
"""


class Fly:
    def __init__(self, root) -> None:
        self.root = root

        self.create_gui()

    def calculate(self) -> None:
        vekt = self.vekt.get().replace(",", ".")
        høyde = self.høyde.get().replace(",", ".")
        try:
            vekt = float(vekt)
            høyde = float(høyde)
        except ValueError:
            melding = "FEIL: oppgi heltall eller desimaltall"
            self.resultat.configure(bg="red")
            kommentar = ""
        else:
            bmi = vekt / høyde**2
            melding = bmi
            self.resultat.configure(bg="white")

            # https://learnyouahaskell.com/syntax-in-functions#guards-guards
            if bmi <= 18.5:
                kommentar = "You're underweight, you emo, you!"
            elif bmi <= 25.0:
                kommentar = "You're supposedly normal. Pffft, I bet you're ugly!"
            elif bmi <= 30.0:
                kommentar = "You're fat! Lose some weight, fatty!"
            else:
                kommentar = "You're a whale, congratulations!"

        self.resultat.configure(text=melding)
        self.kommentar.configure(text=kommentar)

    def create_gui(self) -> None:
        bilde = Image.open("image.png")
        bilde = bilde.resize((150, 150))
        bilde = ImageTk.PhotoImage(bilde)
        bildeLabel = tk.Label(self.root, image=bilde)
        bildeLabel.image = bilde
        bildeLabel.grid(row=0, column=0, rowspan=3, padx=5, pady=5)

        labelVekt = tk.Label(self.root, text="Vekt i kg: ", anchor="e", width=12)
        labelVekt.grid(row=0, column=1)

        labelHøyde = tk.Label(self.root, text="Høyde i meter: ", anchor="e", width=12)
        labelHøyde.grid(row=1, column=1)

        self.vekt = tk.Entry(self.root)
        self.vekt.grid(row=0, column=2)

        self.høyde = tk.Entry(self.root)
        self.høyde.grid(row=1, column=2)

        button = tk.Button(
            self.root, text="Regn ut BMI", bg="lightgreen", command=self.calculate
        )
        button.grid(row=2, column=1, columnspan=2, sticky="EW")

        self.resultat = tk.Label(self.root, bg="white", relief="sunken")
        self.resultat.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="EW")

        self.kommentar = tk.Label(self.root)
        self.kommentar.grid(row=4, column=0, columnspan=3, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    fly = Fly(root)
    root.mainloop()
