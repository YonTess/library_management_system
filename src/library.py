from book import Book
from member import Member

class Library:
    """Holds books (keyed by ISBN) and members (keyed by member ID)."""

    def __init__(self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

    # Reject duplicate ISBNs
    def add_book(self, book: Book):
        if book.isbn in self.books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists.")
        self.books[book.isbn] = book

    # Only books that exist and are not checked out can be removed
    def remove_book(self, isbn: str):
        if isbn not in self.books:
            raise ValueError(f"Book with ISBN {isbn} does not exist.")
        if not self.books[isbn].is_available():
            raise ValueError(f"Book with ISBN {isbn} is currently borrowed.")
        del self.books[isbn]

    # Reject duplicate member IDs
    def register_member(self, member: Member):
        if member.member_id in self.members:
            raise ValueError(f"Member with ID {member.member_id} already exists.")
        self.members[member.member_id] = member

    # Members with unreturned books cannot be removed
    def remove_member(self, member_id: str):
        if member_id not in self.members:
            raise ValueError(f"Member with ID {member_id} does not exist.")
        if self.members[member_id].get_borrowed_count() > 0:
            raise ValueError(f"Member with ID {member_id} has borrowed books.")
        del self.members[member_id]