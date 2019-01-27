import unittest
from booking import *


class TestBookHotel(unittest.TestCase):

    # def test_new_book_user(self):
    #     """
    #     create new user and book a room for him/her
    #     """
    #     # init
    #     room1 = Room(101,5,2560000)
    #     user1 = User("Sattar Khan", "09148519080", 40)
    #     new_book = Book(200, 203, room1)
    #
    #     # test
    #     book_inv = BookInventory()
    #     book_inv.add_book(new_book, user1)
    #
    #     # assert
    #     self.assertEqual(book_inv.get_books_by_user(user1), [new_book])
    #
    # def test_user_books(self):
    #     """
    #     reservation process for a user
    #     """
    #     #init
    #     book_inv = BookInventory()
    #     user2 = User("Bagher Khan", "09141027080", 46)
    #     hotel_room = BookableRoom()
    #
    #     booked_before = book_inv.get_books_by_user(user2)
    #     new_book = Book(204, 205, hotel_room.get_available_rooms()[0])
    #     book_inv.add_book(new_book,user2)
    #     booked_after = book_inv.get_books_by_user(user2)
    #
    #     # print([str(x) for x in book_inv.get_books_by_user(user2)])
    #     # assert
    #     self.assertTrue(len(booked_after) - len(booked_before) ==  1)

    def test_match(self):
        spec1 = BookableSpec()
        spec2 = BookableSpec()
        spec1.set_property('type', 'roo2222m')
        spec1.set_property('cost_per_unit', '25000')
        spec1.set_property('floor', 2)
        spec1.set_property('pricing_policy',PricingPolicy.daily)
        spec2.set_property('type', 'room')
        spec2.set_property('cost_per_unit', '25000000')
        spec2.set_property('pricing_policy', PricingPolicy.once)

        print
        self.assertTrue(spec1.matches(spec2))
