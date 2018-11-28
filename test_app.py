from unittest import TestCase
from app import app
from desserts import dessert_list, Dessert


class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        """reset the dessert_list after each test.
        Only an issue because we don't know about databases yet."""

        cookie = Dessert(1, "Chocolate chip cookie",
                         "C is for cookie, that's good enough for me", 200)
        sundae = Dessert(2, "Banana split",
                         "I'm going to eat all of my feelings", 600)
        donut = Dessert(3, "Glazed Donut", "Perfect with a cup of coffee", 300)
        dessert_list.desserts = [cookie, sundae, donut]
        dessert_list.next_id = 4

    def test_homepage(self):
        """Make sure homepage has correct routing information"""

        with self.client:
            response = self.client.get('/')
            # test that the status code is a 200
            self.assertEqual(response.status_code, 200)
            # test that there's a table in the response data
            self.assertIn(b'<table>', response.data)
            # test that the description for each endpoint is in the response data
            assertList = [
                b'JSON data of all desserts',
                b'Adds a new dessert to our list (returns data on the new dessert)',
                b'JSON data on a single dessert',
                b'Update an existing dessert (returns data on the updated dessert)',
                b'Removes a dessert from our list (returns data on the deleted dessert)'
            ]
            for string in assertList:
                self.assertIn(string, response.data)
            # e.g. 'JSON data of all desserts' should be in the response data,
            # 'Adds a new dessert to our list' should be in the response data,
            # etc.

    def test_display_desserts(self):
        """Make sure /desserts returns json with all desserts"""

        with self.client:
            response = self.client.get('/desserts')
            self.assertEqual(response.status_code, 200)

            json_response = [{
                'id':
                1,
                'name':
                'Chocolate chip cookie',
                'description':
                "C is for cookie, that's good enough for me",
                'calories':
                200
            },
                             {
                                 'id':
                                 2,
                                 'name':
                                 'Banana split',
                                 'description':
                                 "I'm going to eat all of my feelings",
                                 'calories':
                                 600
                             },
                             {
                                 'id': 3,
                                 'name': 'Glazed Donut',
                                 'description': 'Perfect with a cup of coffee',
                                 'calories': 300
                             }]

            self.assertEqual(response.json, json_response)

    def test_add_dessert(self):
        """Test that add dessert method appends dessert to dessert list"""

        with self.client:
            response = self.client.post(
                "/desserts",
                json={
                    "name": "Junior Mint",
                    "description": "Let's all go to the movies",
                    "calories": 798174124
                })

            self.assertEqual(response.status_code, 200)

            json_response = {
                "name": "Junior Mint",
                "description": "Let's all go to the movies",
                "calories": 798174124,
                "id": 4
            }
            # response.json is the same as input
            self.assertEqual(response.json, json_response)
