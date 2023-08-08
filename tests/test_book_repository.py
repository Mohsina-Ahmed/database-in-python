from lib.book_repository import *
from lib.book_store import *
'''
when I call #all on the book_store
I get all the books back in the list
'''
def test_list_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = Book_Repository(db_connection)
    result = repository.all()
    assert result == [
        Book_Store(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book_Store(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book_Store(3, 'Emma', 'Jane Austen'),
        Book_Store(4, 'Dracula', 'Bram Stoker'),
        Book_Store(5, 'The Age of Innocence', 'Edith Wharton')
    ]