from datetime import date
from models import Book, Magazine

book = Book(1, "Dune", "Frank Herbert")
book.check_out("Amina", today=date(2026, 1, 1))
assert book.return_item(today=date(2026, 1, 22)) == 0.0

book.check_out("Amina", today=date(2026, 1, 1))
assert book.return_item(today=date(2026, 1, 26)) == 1.0

mag = Magazine(2, "Tech Monthly", "May")
mag.check_out("Joe", today=date(2026, 1, 10))
assert mag.return_item(today=date(2026, 1, 19)) == 1.0

print("All tests passed")

3