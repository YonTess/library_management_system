from book import Book
from member import Member 
from library import Library

def main():
    # Member demo: track borrowed ISBNs
    member = Member(name="Alice Smith", member_id="M001")
    print(member)
    print(f"Books borrowed: {member.get_borrowed_count()}")

    member.add_borrowed_book("978-0547928227")
    print(f"Books borrowed: {member.get_borrowed_count()}")

    member.add_borrowed_book("978-0451524935")
    print(f"Books borrowed: {member.get_borrowed_count()}")
    print(f"Borrowed ISBNs: {member.borrowed_isbns}")

    member.remove_borrowed_book("978-0547928227")
    print(f"Books borrowed after return: {member.get_borrowed_count()}")
    print(f"Borrowed ISBNs: {member.borrowed_isbns}")

    # Library demo: add and remove books
    library = Library()
    library.add_book(Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227"))
    library.add_book(Book("1984", "George Orwell", "978-0451524935"))
    print(f"Books in library: {len(library.books)}")
    for book in library.books.values():
        print(f"  {book}")

    library.remove_book("978-0547928227")
    print(f"Books after removal: {len(library.books)}")

    # Library demo: register and remove members
    library.register_member(Member(name="Alice Smith", member_id="M001"))
    library.register_member(Member(name="Bob Jones", member_id="M002"))
    print(f"Members in library: {len(library.members)}")
    for m in library.members.values():
        print(f"  {m}")

    library.remove_member("M001")
    print(f"Members after removal: {len(library.members)}")


if __name__ == "__main__":
    main()
