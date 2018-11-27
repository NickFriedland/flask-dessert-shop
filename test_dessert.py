from unittest import TestCase
from desserts import Dessert


class DessertTests(TestCase):
    def setUp(self):
        self.dessert = Dessert(1, "Snickerdoodle cookies", "Best name ever",
                               200)

    def test_init(self):
        """Test the __init__ method for Dessert"""
        self.assertEqual(self.dessert.id, 1)
        self.assertEqual(self.dessert.name, 'Snickerdoodle cookies')
        self.assertEqual(self.dessert.description, 'Best name ever')
        self.assertEqual(self.dessert.calories, 200)

    def test_repr(self):
        """Test the __repr__ method for Dessert"""

        self.assertEqual(
            repr(self.dessert),
            '<Dessert, id=1, name="Snickerdoodle cookies", calories=200>')

    def test_serialize(self):
        """Test the serialize method for Dessert"""

        result = {
            'id': 1,
            'name': 'Snickerdoodle cookies',
            'description': 'Best name ever',
            'calories': 200
        }
        self.assertEqual(self.dessert.serialize(), result)
