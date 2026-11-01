class Book:
    """A library book; borrowed_by holds the member ID, or None if available."""

    def __init__(self, title: str, author: str, isbn: str, borrowed_by: str | None = None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed_by = borrowed_by

    def is_available(self):
        # Available means nobody currently has it
        return self.borrowed_by is None

    # Overridden by the second borrow() below, which is the one in effect
    def borrow(self, member_id: int):
        if self.is_available():
            self.borrowed_by = member_id
        else:
            raise ValueError("can't borrow what's not available!")

    def return_book(self):
        self.borrowed_by = None

    # Returns True on success, False if already borrowed
    def borrow(self, member_id):
        if not self.is_available():
            return False
        self.borrowed_by = member_id
        return True

    def return_book(self):
        self.borrowed_by = None

    # Human-readable form used by print()
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

