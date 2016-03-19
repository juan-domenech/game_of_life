import time
import os

from game_of_life import next_generation, print_world

def life_sequence(world,sleep=1):

    os.system('clear')

    for x in range(1,55555):

        os.system('clear')
        print "Generation #",x
        print
        #print world
        print_world(world)
        time.sleep(sleep)

        new_world = next_generation(world)

        if len(new_world) == 0:
            print "All cells dead at generation #",x
            break
        world = new_world

    return


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

life_sequence(world,sleep=0)
