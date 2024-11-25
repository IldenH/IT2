class Book:
    def __init__(
        self,
        tittel: str,
        forfattere: list,
        isbn: int,
        utgivelsesår: int,
        forlag: str = "",
    ) -> None:
        self.tittel = tittel
        self.forfattere = forfattere
        self.isbn = isbn
        self.utgivelsesår = utgivelsesår
        self.forlag = forlag

    def list_info(self) -> str:
        return f"""{self.tittel} ({self.utgivelsesår}):
    Skrevet av: {self.list_forfattere()}{f"\n    Forlag: {self.forlag}" if self.forlag != "" else ""}
    ISBN: {self.isbn}"""

    def list_forfattere(self) -> str:
        forfattere = ""

        if len(self.forfattere) == 1:
            return self.forfattere[0]

        for i in range(len(self.forfattere)):
            if i == len(self.forfattere) - 1:
                forfattere += " og "
            elif i > 0:
                forfattere += ", "
            forfattere += str(self.forfattere[i])

        return forfattere


class Bibliotek:
    def __init__(self, bøker: dict = {}) -> None:
        self.bøker = bøker

    def add_book(self, book: Book) -> None:
        self.bøker[book.tittel] = book

    def list_books(self) -> None:
        for book in self.bøker.values():
            print(book.list_info())


if __name__ == "__main__":
    bibliotek = Bibliotek()
    bibliotek.add_book(Book("Dune", ["Frank Herbert"], 9780340960196, 2015))
    bibliotek.add_book(
        Book(
            "intertekst",
            ["Eriksen, H.", "Garthus, K. M. K.", "Schulze, A.-M."],
            9788211031082,
            2020,
            "Fagbokforlaget",
        )
    )
    bibliotek.list_books()
