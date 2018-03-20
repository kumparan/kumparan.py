import unittest

from kumparan import utils


class TestUtils(unittest.TestCase):
    def test_unixtimestamp(self):
        timestamp = utils.unixtimestamp()
        self.assertTrue(timestamp > 0)


if __name__ == '__main__':
    unittest.main()
