import unittest


class TestViews(unittest.TestCase):
    def setUp(self):
        pass

    def test_truthy(self):
        self.assertEqual(1, 0+1)


if __name__ == '__main__':
    unittest.main()
