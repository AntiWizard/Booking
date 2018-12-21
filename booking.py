import sys , time , types , abc, datetime
import uuid

class Room:
    def __init__(self, room_no, capacity, costPerUnit):
        self.room_no = room_no
        self.capacity = capacity
        self.busy = False
        self.costPerUnit = costPerUnit


class Hotel:
    def __init__(self, name, address, location, telNum, id=None):
        if not id:
            self.id = uuid.uuid4().hex
        else:
            self.id = id
        self.address = address
        self.location = location
        self.telNum = telNum
        self.name = name


class Bookee:
    hotel_room = dict() # Hotel and [Room]

    def add_bookee(self, hotel, room):
        if hotel in self.hotel_room.keys():
            self.hotel_room[hotel].append(room)
        else:
            self.hotel_room[hotel] = [room]

    def get_rooms_by_hotel(self, hotel):
        if not hotel in self.hotel_room.keys():
            return []
        return self.hotel_room[hotel]

    def get_hotel_by_room(self, room):
        for _hotel,_room in self.hotel_room.items():
            if room in _room :
                return _hotel

    def get_available_rooms(self):
        ava = []
        for hotel in self.hotel_room.keys():
            for room in self.hotel_room[hotel]:
                if not room.busy:
                    ava.append(room)
        return ava


class User:
    def __init__(self, name, phone, age, id=None):
        self.name = name
        self.phone = phone
        self.age = age
        if not id:
            self.id = uuid.uuid4().hex
    def __str__(self):
        return "User Instance: " + self.name

class Book:
    def __init__(self, start_date, end_date, bookee):
        self.start_date = start_date
        self.end_date = end_date
        self.bookee = bookee # Room
        self.cost = self.calculate_cost()

    def calculate_cost(self):
        self.cost = (self.end_date - self.start_date) * self.bookee.costPerUnit
        return self.cost

    def __str__(self):
        return "Book instance for user " + self.booker.name


class BookInventory:
    book_user = dict()

    def add_book(self, book, user):
        if user in self.book_user.keys():
            self.book_user[user].append(book)
        else:
            self.book_user[user] = [book]

    def get_books_by_user(self, user):
        if not user in self.book_user.keys():
            return []
        return self.book_user[user]

    def get_user_by_book(self, book):
        for _user,_book in self.book_user.items():
            if book in _book:
                return _user
        return None
