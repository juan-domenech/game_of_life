import unittest
import time
import os

from game_of_life import next_generation, print_world

# Blinker (period 2)
#world = [(1,0), (1,1), (1,2)]
# R-Pentomino
#world = [ (1,0),(2,0),(0,1),(1,1),(1,2) ]
# Die Hard
world =  [ (0,1),(1,1),(1,2),(6,0),(5,2),(6,2),(7,2) ]
print "Generation # 0"
print_world(world)
time.sleep(1)

for x in range(1,55555):

    new_world = next_generation(world)
    os.system('clear')
    print "Generation #",x
    print_world(new_world)

    if len(new_world) == 0:
        print "All dead at generation #",x
        break
    #time.sleep(5)
    world = new_world





class test_game_of_life(unittest.TestCase):

    # Empty
    def test(self):
        self.assertEquals( next_generation( [] ) , [] )

    # Solitarie cell that dies
    #def test(self):
    #    self.assertEquals( next_generation( [(0,0)] ) , [] )

    # Block (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns)
    #def test(self):
    #    self.assertEquals( next_generation( sorted ( [(0,0), (0,1), (1,1), (1,0)] ) ) , sorted( [(0,0), (0,1), (1,1), (1,0)] ) )

    # Beehive (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns)
    #def test(self):
    #    self.assertEquals( next_generation( sorted ( [(1,0), (2,0), (0,1), (3,1), (1,2), (2,2)] ) ) , sorted( [(1,0), (2,0), (0,1), (3,1), (1,2), (2,2)] ) )

    # Blinker (Period 2) (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns)
    #def test(self):
    #    self.assertEquals( next_generation( sorted ( [(1,0), (1,1), (1,2)] ) ) , sorted( [(0,1), (1,1), (2,1)] ) )
