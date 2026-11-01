class Member:
    """A library member who tracks the ISBNs of books they have borrowed."""

    def __init__(self, member_id: str, name: str, borrowed_isbns: list[str] | None = None):
        self.member_id = member_id
        self.name = name
        self.borrowed_isbns = borrowed_isbns if borrowed_isbns is not None else []

    # Record a borrowed book
    def add_borrowed_book(self, isbn: str):
        self.borrowed_isbns.append(isbn)

    # Forget a returned book; ignores ISBNs not on the list
    def remove_borrowed_book(self, isbn: str):
        if isbn in self.borrowed_isbns:
            self.borrowed_isbns.remove(isbn)

    # Number of books currently borrowed
    def get_borrowed_count(self):
        return len(self.borrowed_isbns)
    

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"