from booking import *


class Room(Bookable):
    """
    Room has-the-behaviour of Bookable
    """

    def __init__(self, spec: BookableSpec):
        super().__init__(self)
        self.set_bookable_spec(spec)
        self.get_bookable_spec().set_property('pricing_policy', PricingPolicy.DAILY)
        self.get_bookable_spec().set_property('type', 'room')
        self.get_bookable_spec().set_property('available', True)
        self.get_bookable_spec().set_property('association_policy', AssociationPolicy.FINITE)
        self.get_bookable_spec().set_property('amount', 1)
        self.available = True
        self.roomNo = spec.get_property('room_no')
        self.capacity = spec.get_property('capacity')
        self.cost_per_unit = spec.get_property('cost_per_unit')

    def make_available(self):
        self.available = True
        self.get_bookable_spec().set_property('available', self.available)

    def make_unavailable(self):
        self.available = False
        self.get_bookable_spec().set_property('available', self.available)

    def __str__(self):
        return "It's room number: " + str(self.get_bookable_spec().get_property('room_no'))


class Hotel:
    def __init__(self, name, address, location, id=None):
        if not id:
            self.id = uuid.uuid4().hex
        else:
            self.id = id
        self.address = address
        self.location = location
        self.name = name


class Bookee:
    hotel_room = dict() # Hotel and [Room]

    def add_bookee(self, hotel, room):
        if hotel in self.hotel_room.keys():
            self.hotel_room[hotel].append(room)
        else:
            self.hotel_room[hotel] = [room]

    def get_rooms_by_hotel(self, hotel):
        if hotel not in self.hotel_room.keys():
            return []
        return self.hotel_room[hotel]

    def get_hotel_by_room(self, room):
        for _hotel,_room in self.hotel_room.items():
            if room in _room:
                return _hotel

    def get_available_rooms(self):
        ava = []
        for hotel in self.hotel_room.keys():
            for room in self.hotel_room[hotel]:
                if room.available:
                    ava.append(room)
        return ava

    def get_hotels(self):
        return list(self.hotel_room.keys())


# if __name__ == "__main__":
#     user1 = User("hamze")
#     room1 = Room(303, 3, 320000)
#     book_obj = Book(room1, 100, 103)
#     book_inv = BookInventory()
#     book_inv.add_book(user1, book_obj)
