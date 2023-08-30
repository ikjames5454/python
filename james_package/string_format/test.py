import unittest
from math import pi

from james_package.string_format.area import areas


class TestAreaFunction(unittest.TestCase):
    def test_area_function(self):
        self.assertAlmostEqual(areas(1), pi)
        self.assertAlmostEqual(areas(0), 0 * 2)
        self.assertAlmostEqual(areas(2), pi * 2 ** 2)

    def test_values(self):
        self.assertRaises(ValueError, areas, -1)
        self.assertRaises(ValueError, areas, -5)

    def test_radius_type(self):
        self.assertRaises(TypeError, areas, True)
        self.assertRaises(TypeError, areas, 2 + 5j)
