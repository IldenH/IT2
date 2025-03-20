import tkinter as tk


"""

R0: rad 0
C0: column 0

O: Av/På
C: Temperatur current
I: increase øk
S: Sett
D: decrease
R: resultat

   C0 C1 C2 C3
R0  O        I
R1  O  C  C  S
R2  O  C  C  S
R3  O        D
R4  R  R  R  R
"""


class App:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Temperaturstyring")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)

        self.temperatur = 20.0
        self.currentTemperatur = self.temperatur

        self.create_gui()

    def quit(self) -> None:
        self.root.quit()
        self.root.destroy()

    def changeTemperature(self, value: float) -> None:
        self.currentTemperatur += value
        self.current.configure(text=f"Temperatur:\n{self.currentTemperatur}°C")

    def sett(self) -> None:
        self.temperatur = self.currentTemperatur
        self.result.configure(text=f"Temperatur satt til {self.temperatur}°C")

    def create_gui(self) -> None:
        self.increaseButton = tk.Button(
            self.root,
            text="⬆️",
            command=lambda: self.changeTemperature(0.5),
            bg="lightgreen",
            font="Arial 16",
            width=3,
        )
        self.increaseButton.grid(row=0, column=3, padx=5, pady=5)

        self.setButton = tk.Button(
            self.root,
            text="Sett",
            command=self.sett,
            bg="lightgreen",
            font="Arial 16",
        )
        self.setButton.grid(row=1, column=3, rowspan=2, sticky="NS", padx=5, pady=5)

        self.decreaseButton = tk.Button(
            self.root,
            text="⬇️",
            command=lambda: self.changeTemperature(-0.5),
            bg="lightgreen",
            font="Arial 16",
            width=3,
        )
        self.decreaseButton.grid(row=3, column=3, padx=5, pady=5)

        self.onOff = tk.Button(
            self.root,
            text="Av/På",
            bg="lightgreen",
            font="Arial 16",
        )
        self.onOff.grid(row=0, column=0, rowspan=4, padx=5, pady=5, sticky="NS")

        self.current = tk.Label(
            self.root,
            bg="white",
            text=f"Temperatur:\n{self.currentTemperatur}°C",
            font="Arial 16",
            borderwidth=1,
            relief="solid",
            padx=10,
            pady=10,
        )
        self.current.grid(
            row=1, column=1, columnspan=2, rowspan=2, padx=5, pady=5, sticky="EWNS"
        )

        self.result = tk.Label(
            self.root,
            bg="white",
            relief="sunken",
            font="Arial 16",
        )
        self.result.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="EW")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
