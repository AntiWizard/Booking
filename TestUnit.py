import unittest
from booking import *

class TestBookHotel(unittest.TestCase):
    room1 = Room(12,3,250000)
    hotel = Hotel("aras baran", "tabriz, el goli", (10,10), "04134773050")
    def test_defineHotel(self):
        # self.room1 = Room(12,3,250000)
        # self.hotel = Hotel("aras baran", "tabriz, el goli", (10,10), "04134773050")
        self.bookee = Bookee("hotel")

        self.hotel.addRoom(self.room1)
        self.bookee.addBookee(self.hotel)
        print(1)
        self.assertEqual(self.bookee.inventory[0].rooms[0], self.room1)

    def test_bookRoom(self):

        user = User("vali","04144422225")
        book = Book(200,202,self.room1, user)
        print(2)
        print (book.calculateCost())


    def test_bookee(self):
        pass

    def test_book(self):
        pass

    def test_user(self):
        pass