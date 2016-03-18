import unittest

from game_of_life import test

class test_game_of_life(unittest.TestCase):

    def test(self):
        self.assertEquals(test(1),1)
        