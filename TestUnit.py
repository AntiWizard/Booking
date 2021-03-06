import unittest
from booking import *


class TestBookable(unittest.TestCase):

    def test_match(self):
        spec1 = BookableSpec()
        spec2 = BookableSpec()
        spec1.set_property('type', 'room')
        spec1.set_property('cost_per_unit', 25000000)
        spec1.set_property('floor', 2)
        spec1.set_property('pricing_policy', PricingPolicy.DAILY)

        spec2.set_property('type', 'room')
        spec2.set_property('cost_per_unit', 25000000)
        spec2.set_property('pricing_policy', PricingPolicy.DAILY)

        self.assertTrue(spec1.matches(spec2))

    def test_search(self):
        class SessionBookable(Bookable):
            def get_cost_per_unit(self):
                super().get_cost_per_unit()

            def get_bookable_type(self):
                super().get_bookable_type()

            def search(self):
                super().search()

            def get_bookable_spec(self):
                return super().get_bookable_spec()

        spec1 = BookableSpec()
        spec1.set_property('cost_per_unit', 250000)
        spec1.set_property('pricing_policy', PricingPolicy.ONCE)

        spec2 = BookableSpec()
        spec2.set_property('cost_per_unit', 25000000)
        spec2.set_property('pricing_policy', PricingPolicy.DAILY)


        session_book1 = SessionBookable(spec1)
        session_book2 = SessionBookable(spec2)

        room_inv = BookableInventory()
        room_inv.add_bookable(session_book1)
        room_inv.add_bookable(session_book2)

        target_spec = BookableSpec()
        target_spec.set_property('pricing_policy', PricingPolicy.DAILY)
        result_spec = room_inv.search(target_spec)

        self.assertEqual(result_spec, [session_book2])

    def test_calculate_cost(self):
        class RoomBookable(Bookable):
            def get_cost_per_unit(self):
                super().get_cost_per_unit()

            def get_bookable_type(self):
                super().get_bookable_type()

            def search(self):
                super().search()

            def get_bookable_spec(self):
                return super().get_bookable_spec()

        spec1 = BookableSpec()
        spec1.set_property('type', 'room')
        spec1.set_property('cost_per_unit', 250000)
        spec1.set_property('floor', 2)
        spec1.set_property('pricing_policy', PricingPolicy.DAILY)

        room_bookable = RoomBookable(spec1)

        room_book = Book(room_bookable, 200,205)

        self.assertEqual(room_book.calculate_cost(), 5*250000)

