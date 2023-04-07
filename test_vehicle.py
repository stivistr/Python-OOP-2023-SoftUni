from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(10.5, 100.5)

    def test_correct_initialization(self):
        self.assertEqual(10.5, self.vehicle.fuel)
        self.assertEqual(100.5, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_can_not_drive_without_fuel(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_distance_with_enough_fuel(self):

        self.vehicle.fuel = 50
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_refuel_with_more_fuel_than_capacity_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(15)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_needed_fuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(10)

        self.assertEqual(10, self.vehicle.fuel)

    def test_right_string_representation(self):
        result = self.vehicle.__str__()

        self.assertEqual("The vehicle has 100.5 horse power "
                         "with 10.5 fuel left and 1.25 fuel consumption", self.vehicle.__str__())


if __name__ == '__main__':
    main()
