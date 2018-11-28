from unittest import TestCase
from desserts import Dessert, DessertList


class DessertListTests(TestCase):
    def setUp(self):
        self.sample_list = DessertList()

    def test_init(self):
        """Test the __init__ method for DessertList"""
        self.assertEqual(self.sample_list.desserts, [])
        self.assertEqual(self.sample_list.next_id, 1)

    def test_repr(self):
        """Test the __repr__ method for DessertList"""
        self.sample_list.add("Apple Pie", "As American as...", 6000)

        repr_test = "<Dessert, id=1, name=\"Apple Pie\", calories=6000>\n"
        self.assertEqual(repr(self.sample_list), repr_test)

    def test_add(self):
        """Test the add method for DessertList"""
        self.sample_list.add("Apple Pie", "As American as...", 6000)
        self.sample_list.add("Ice Cream", "Lieutenant Dan!!", 1)

        self.assertEqual(self.sample_list.desserts[0].name, "Apple Pie")
        self.assertEqual(self.sample_list.desserts[0].calories, 6000)
        self.assertEqual(self.sample_list.desserts[1].description,
                         "Lieutenant Dan!!")
        self.assertEqual(self.sample_list.next_id, 3)

    def test_serialize(self):
        """Test the serialize method for DessertList"""
        self.sample_list.add("Apple Pie", "As American as...", 6000)
        self.sample_list.add("Ice Cream", "Lieutenant Dan!!", 1)

        serialize_dict = [{
            "id": 1,
            "name": "Apple Pie",
            "description": "As American as...",
            "calories": 6000
        },
                          {
                              "id": 2,
                              "name": "Ice Cream",
                              "description": "Lieutenant Dan!!",
                              "calories": 1
                          }]
        self.assertEqual(self.sample_list.serialize(), serialize_dict)
