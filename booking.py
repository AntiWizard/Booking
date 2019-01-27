import sys, time, types, abc, datetime
import uuid


class Room:
    def __init__(self, room_no, capacity, costPerUnit):
        self.room_no = room_no
        self.capacity = capacity
        self.busy = False
        self.costPerUnit = costPerUnit

    def make_available(self):
        self.busy = False

    def __str__(self):
        return str(self.room_no)


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
        self.bookee = bookee  # Bookable
        self.bookee.busy = True

    def calculate_cost(self):
        self.cost = (self.end_date - self.start_date) * self.bookee.costPerUnit
        return self.cost

        self.booke

    def __str__(self):
        return "Book instance for room no " + str(self.bookee.room_no)










class BookInventory:
    user_book = dict()

    def add_book(self, book, user):
        if user in self.user_book.keys():
            self.user_book[user].append(book)
        else:
            self.user_book[user] = [book]

    def get_books_by_user(self, user):
        if not user in self.user_book.keys():
            return []
        return self.user_book[user]

    def get_user_by_book(self, book):
        for _user, _book in self.user_book.items():
            if book in _book:
                return _user
        return None

    def get_users(self):
        return list(self.user_book.keys())

    def search(self):
        # TODO: do search
        pass



class BookableSpec:
    __properties = dict()

    def get_property(self, prop):
        if prop in self.__properties.keys():
            return self.__properties[prop]
        else:
            return None

    def set_property(self, prop, value):
        try:
            self.__properties.update({prop:value})
        except Exception :
            return False
        return True


    def matches(self, otherSpec):
        for prop in self.__properties.keys() & otherSpec.keys():
            if not self.__properties[prop] == otherSpec[prop]:
                return False
        return True


class AbstractBookable(metaclass=abc.ABCMeta):
    __bookable_spec = BookableSpec()

    def get_bookable_type(self):
        self.__bookable_spec.get_property('type')

    @abc.abstractmethod
    def get_cost_per_unit(self):
        pass

    @abc.abstractmethod
    def search(self):
        pass


class BookableRoom(AbstractBookable):
    def getBookableType(self):
        super().getBookableType()

    def search(self):
        super().search()

    def get_cost_per_unit(self):
        pass

    hotel_room = dict()  # Hotel and [Room]

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
        for _hotel, _room in self.hotel_room.items():
            if room in _room:
                return _hotel

    def get_available_rooms(self):
        ava = []
        for hotel in self.hotel_room.keys():
            for room in self.hotel_room[hotel]:
                if not room.busy:
                    ava.append(room)
        return ava

    def get_hotels(self):
        return list(self.hotel_room.keys())

