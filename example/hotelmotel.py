"""

***** Prove of Work *****

"""
from ..booking import *


class Room(AbstractBookable):
    def __init__(self, room_no, capacity):
        super().__init__()
        self.get_bookable_spec().add_property('type', 'room')
        self.get_bookable_spec().add_property('room_no', room_no)
        self.get_bookable_spec().add_property('capacity', capacity)

    def __str__(self):
        return "It's room number: " + str(self.get_bookable_spec().get_property('room_no'))


if __name__ == "__main__":
    user1 = User("hamze")
    room1 = Room(303, 3)
    book_obj = Book(room1, 100, 103)
    book_inv = BookInventory()
    book_inv.add_book(book_obj, user1)
