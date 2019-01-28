import sys, time, types, abc, datetime
import uuid
import enum


class PricingPolicy(enum.Enum):
    DAILY = 1
    ONCE = 2


class AssociationPolicy(enum.Enum):
    INFINITE = 0
    FINITE = 1


class User:
    def __init__(self, name, id=None):
        self.name = name
        if not id:
            self.id = uuid.uuid4().hex

    def __str__(self):
        return "User Instance: " + self.name


class Book:
    def __init__(self, bookee, start_date, end_date=None):
        self.start_date = start_date
        self.end_date = end_date
        self.bookee = bookee  # Bookable
        if bookee.get_bookable_spec().get_property('association_policy') == AssociationPolicy.FINITE:
            amount = bookee.get_bookable_spec().get_property('amount')
            if amount > 0:
                bookee.get_bookable_spec().set_property('amount', amount - 1)
                if amount == 1:
                    bookee.make_unavailable()
            else:
                Exception()

    def calculate_cost(self):
        if self.bookee.get_bookable_spec().get_property('pricing_policy') is PricingPolicy.ONCE:
            return self.bookee.get_bookable_spec().get_property('cost_per_unit')
        else:
            return (self.end_date - self.start_date) * self.bookee.get_bookable_spec().get_property('cost_per_unit')

    def __str__(self):
        return "Book instance for "+ str(self.bookee.get_bookable_spec.get_property('type'))


class BookInventory:
    user_book = dict()

    def get_books_by_user(self, user):
        if user not in self.user_book.keys():
            return []
        return self.user_book[user]

    def get_user_by_book(self, book):
        for _user, _book in self.user_book.items():
            if book in _book:
                return _user
        return None

    # TODO: Test case it
    def add_book(self, user, book):
        if user in self.user_book.keys():
            self.user_book[user].append(book)
        else:
            self.user_book[user] = [book]

    def get_users(self):
        return list(self.user_book.keys())


class BookableSpec:
    __properties = None
    
    def __init__(self):
        self.__properties = dict()

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
        for prop in self.__properties.keys() & otherSpec.get_keys():
            if not self.__properties[prop] == otherSpec.get_property(prop):
                return False
        return True

    def get_keys(self):
        return self.__properties.keys()


class Bookable:
    __bookable_spec = None

    def __init__(self, spec):
        self.__bookable_spec = spec

    def get_bookable_spec(self) -> BookableSpec:
        return self.__bookable_spec

    def get_bookable_type(self):
        self.__bookable_spec.get_property('type')

    def set_bookable_spec(self, bookable_spec):
        self.__bookable_spec = bookable_spec


class BookableInventory:
    __bookable_list = list()

    def search(self, bookspec):
        result = []
        for bookable in self.__bookable_list:
            if bookable.get_bookable_spec().matches(bookspec):
                result.append(bookable)
        return result

    def get_bookable_list(self):
        return self.__bookable_list

    def add_bookable(self, bookable):  # bookable is a Bookable
        self.__bookable_list.append(bookable)
