import time
import os

from game_of_life import next_generation, print_world, import_RLE_seed, prune

def life_sequence(world,sleep=1):

    os.system('clear')

    last_body_count = 0
    counter = 0

    for x in range(1,55555):

        os.system('clear')
        print "Generation #",x
        print
        #print world
        print_world(world)
        #
        world = prune(world,40)
        time.sleep(sleep)

        new_world = next_generation(world)

        if len(new_world) == 0:
            print "All cells dead at generation #",x
            break
        world = new_world

        if len(world) == last_body_count:
            counter +=  1
            if counter > 100:
                print "Population stable at generation:",x - counter
                break
        else:
            last_body_count = len(world)

    return


# Blinker (period 2)
#world = [(1,0), (1,1), (1,2)]

# R-Pentomino
#world = [ (1,0),(2,0),(0,1),(1,1),(1,2) ]

# Die Hard Step 128
#world = [(0,0),(1,1),(2,1)]

# Bacon Stage1
#world= [(0,0),(0,1),(1,1),(1,0),(2,2),(2,3),(3,2),(3,3)]

# Die Hard
#world =  [ (0,1),(1,1),(1,2),(6,0),(5,2),(6,2),(7,2) ]

# Acorn http://pentadecathlon.com/lifeNews/2005/02/new_methuselah_records.html
#rle='bo$3bo$2o2b3o!'

# Rabits http://pentadecathlon.com/lifeNews/methuselahs/
rle='o3b3o$3o2bo$bo!'

world = import_RLE_seed(rle)
print_world(world)

life_sequence(world,sleep=0)