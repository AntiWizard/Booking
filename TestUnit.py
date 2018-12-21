import unittest
from booking import *


class TestBookHotel(unittest.TestCase):

    def test_new_hotel_room(self):
        """
        create hotel and add some rooms to it
        """
        # init
        hotel1 = Hotel("Aras Baran", "El goli, Tabriz", (10,10), "04134443050")
        room1 = Room(101,5,2560000)
        room2 = Room(303,3,3060000)
        hotel_room = Bookee()
        hotel_room.add_bookee(hotel1, room1)
        hotel_room.add_bookee(hotel1, room2)
        # assert
        self.assertEqual(hotel_room.get_rooms_by_hotel(hotel1), [room1,room2])

    def test_book_room(self):
        """
        create a Book instance from a room
        """
        # init
        room1 = Room(101,5,2560000)

        # test
        new_book = Book(200, 203, room1)

        # assert
        self.assertEqual(new_book.cost, 2560000*3)

    def test_new_book_user(self):
        """
        create new user and book a room for him/her
        """
        # init
        room1 = Room(101,5,2560000)
        user1 = User("Sattar Khan", "09148519080", 40)
        new_book = Book(200, 203, room1)

        # test
        book_inv = BookInventory()
        book_inv.add_book(new_book, user1)

        # assert
        self.assertEqual(book_inv.get_books_by_user(user1), [new_book])

    def test_show_available_rooms(self):
        """
        show rooms which are not busy
        """
        # init
        hotel_room = Bookee()

        # test
        no_of_available = len(hotel_room.get_available_rooms())
        new_book = Book(200, 203, hotel_room.get_available_rooms()[0])

        # assert
        # print([str(x) for x in hotel_room.get_available_rooms()])
        self.assertEqual(len(hotel_room.get_available_rooms()), no_of_available - 1)

    def test_user_books(self):
        """
        reservation process for a user
        """
        #init
        book_inv = BookInventory()
        user2 = User("Bagher Khan", "09141027080", 46)
        hotel_room = Bookee()

        booked_before = book_inv.get_books_by_user(user2)
        new_book = Book(204, 205, hotel_room.get_available_rooms()[0])
        book_inv.add_book(new_book,user2)
        booked_after = book_inv.get_books_by_user(user2)

        # print([str(x) for x in book_inv.get_books_by_user(user2)])
        # assert
        self.assertTrue(len(booked_after) - len(booked_before) ==  1)


    def test_hotel_which_user_booked_room_from(self):
        """
        a story showing how to find which hotel user booked a room from
        """
        book_inv = BookInventory()
        hotel_room = Bookee()

        user3 = User("AmirKabir", "09101007070", 52)
        room2 = Room(212, 5, 200000)
        hotel2 = Hotel("Sorena", "Sistan", (20,20), "0250989988")
        hotel_room.add_bookee(hotel2, room2)

        book_user3 = Book(150,151, room2)
        book_inv.add_book(book_user3, user3)
        # print(book_inv.get_books_by_user(user3)[0])
        # print(hotel_room.hotel_room)
        self.assertEqual(hotel2,
                             hotel_room.get_hotel_by_room(
                                book_inv.get_books_by_user(user3)[0].bookee
                             )
                         )

