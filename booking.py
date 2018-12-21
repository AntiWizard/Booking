import sys , time , types , abc, datetime
import uuid

class Room:
    def __init__(self, room_no, capacity, costPerUnit):
        self.room_no = room_no
        self.capacity = capacity
        self.busy = False
        self.costPerUnit = costPerUnit


class Hotel:
    rooms = []
    def __init__(self, name, address, location, phone, id=None):
        self.name = name
        self.address = address
        self.location = location
        self.phone = phone
        if not id:
            self.id = uuid.uuid4().hex

    def addRoom(self, room):
        if(type(room) == Room):
            self.rooms.append(room)
        else:
            print("Error : miss match type")

class Bookee:
    inventory = []
    def __init__(self,type):
        self.type = type
    def addBookee(self, item):
        self.inventory.append(item)

class User:
    def __init__(self, name, phone, id=None):
        self.name = name
        self.phone = phone
        if not id:
            self.id = uuid.uuid4().hex
    def __str__(self):
        return "User Instance: " + self.name

class Book:
    def __init__(self, start_date, end_date, bookee, booker):
        self.start_date = start_date
        self.end_date = end_date
        self.bookee = bookee
        self.booker = booker

    def calculateCost(self):
        self.cost = (self.end_date - self.start_date) * self.bookee.costPerUnit
        return self.cost

    def __str__(self):
        return "Book instance for user " + self.booker.name

class BookInventory:
    booking_map = dict()

    # @staticmethod
    def addMapping(self, user, book):
        self.booking_map[user] =  book

    def findByBook(self, book):
        for _user,_book in self.booking_map.items():
            if _book == book:
                return _user
    def findByUser(self, user):
        return self.booking_map[user]
