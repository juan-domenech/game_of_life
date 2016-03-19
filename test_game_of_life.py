import unittest

from game_of_life import next_generation, life_sequence


class test_game_of_life(unittest.TestCase):

    # Empty
    def test(self):
        self.assertEquals( next_generation( [] ) , [] )

    # Solitarie cell that dies
    def test(self):
        self.assertEquals( next_generation( [(0,0)] ) , [] )

    # Block (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns)
    def test(self):
        self.assertEquals( next_generation( sorted ( [(0,0), (0,1), (1,1), (1,0)] ) ) , sorted( [(0,0), (0,1), (1,1), (1,0)] ) )

    # Beehive (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns)
    def test(self):
        self.assertEquals( next_generation( sorted ( [(1,0), (2,0), (0,1), (3,1), (1,2), (2,2)] ) ) , sorted( [(1,0), (2,0), (0,1), (3,1), (1,2), (2,2)] ) )

    # Blinker Vertical (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns)
    def test(self):
        self.assertEquals( next_generation( sorted ( [(1,0), (1,1), (1,2)] ) ) , sorted( [(0,1), (1,1), (2,1)] ) )

    # Blinker Horizontal (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns)
    def test(self):
        self.assertEquals( next_generation( sorted ( [(0, 1), (1, 1), (2, 1)] ) ) , sorted( [(1,0), (1,1), (1,2)] ) )

    # Beacon Stage #1
    def test(self):
        self.assertEquals( next_generation( sorted ( [(0,0),(0,1),(1,1),(1,0),(2,2),(2,3),(3,2),(3,3)] ) ) , sorted( [(0,0),(0,1),(1,0),(2,3),(3,2),(3,3)] ) )

    # Beacon Stage #2
    def test(self):
        self.assertEquals( next_generation( sorted ( [(0,0),(0,1),(1,0),(2,3),(3,2),(3,3)] ) ) , sorted( [(0,0),(0,1),(1,1),(1,0),(2,2),(2,3),(3,2),(3,3)] ) )

    # Die Hard (Stage 12)
    def test(self):
        self.assertEquals( next_generation( sorted ( [(0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (3, 3), (5, -1), (5, 5), (6, -1), (6, 5), (7, -1), (7, 5), (9, 1), (9, 2), (9, 3)] ) ) , sorted( [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (3, 1), (3, 3), (4, 2), (6, -2), (6, -1), (6, 0), (6, 4), (6, 5), (6, 6), (8, 2), (9, 2), (10, 2)] ) )

    # Die Hard (Step 128)
    def test(self):
        self.assertEquals( next_generation( [(0,0),(1,1),(2,1)] ) , [] )

    # Die Hard (Step 129) Two vertical cells together that dies
    def test(self):
        self.assertEquals( next_generation( [(0,0),(0,1)] ) , [] )


# Blinker (period 2)
#world = [(1,0), (1,1), (1,2)]

# R-Pentomino
world = [ (1,0),(2,0),(0,1),(1,1),(1,2) ]

# Die Hard Step 128
#world = [(0,0),(1,1),(2,1)]

# Bacon Stage1
#world= [(0,0),(0,1),(1,1),(1,0),(2,2),(2,3),(3,2),(3,3)]

# Die Hard
#world =  [ (0,1),(1,1),(1,2),(6,0),(5,2),(6,2),(7,2) ]

#life_sequence(world,sleep=0)

