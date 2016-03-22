import time
import os

from game_of_life import next_generation, print_world, import_RLE_seed, prune, flip_world_horizontal, shift_world_vertical

def life_sequence(world,sleep=1):

    os.system('clear')

    last_body_count = 0
    counter = 0

    for x in range(1,55555):

        os.system('clear')
        print "Generation #",x
        print
        print_world(world)
        # Optionally: Remove distant cells
        #world = prune(world,50)
        time.sleep(sleep)

        new_world = next_generation(world)

        if len(new_world) == 0 :
            print "All cells dead at generation #",x
            break
        world = new_world

        # Break once the population has been stabilized
        if len(world) == last_body_count:
            counter += 1
            if counter > 100 :
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
#rle='o3b3o$3o2bo$bo!'

# Diagonal Spacehip by N.Beluchenko http://pentadecathlon.com/objects/spaceships/small/smallest.php
#rle='2b2o$b3ob3o$3bo3b2o$2ob2o2bo2bobo$o6bob4o$6b2obo2bo$o4b2o3bob2o$2o8bobo2bo$o2b5ob3o4bo$bo9bo4bo$b2obo2bo3bo3bo$2bo9b2o$9b2o2b2o4bo$2bo3b2obo4b3o2bo$3b2obob5o5bob2o$7b2ob2ob2ob2o2b3o$17bobo4bo$8b2o4bobo3b6o$13bo7b2o$13bo3bo$13bo4bo3b3o6bo$14b5o3b2ob2o2b2ob2o$17b2obo2bob2o2bo$16b2o5bo4bo2b3o$15b3obobobobo$22bo2bo$18bobo$19bo2$21b3o$21b3o2$20b2o$20b2o$21bo!'

# (P4) orthogonal spaceship 9P4H2V0 by J.H.Conway
#rle='4o$o3bo$o$bo2bo!'

# 64P2H1V0.1 (P2) orthogonal spaceship by D.Hickerson
#rle='5bobo$4bo2bo$3b2o$2bo$b4o$o4bo$o2bo$o2bo$bo$2b4obo$3bo3bo$4bo$4bobo$$3b3o$3b2o$3b3o$$4bobo$4bo$3bo3bo$2b4obo$bo$o2bo$o2bo$o4bo$b4o$2bo$3b2o$4bo2bo$5bobo!'

# 83P7H1V1.1 Diagonal Spaceship by M.Merzenich
#rle='12b3o$12bo$13bo2b2o$16b2o$12b2o$13b2o$12bo2bo2$14bo2bo$14bo3bo$15b3obo$20bo$2o2bobo13bo$obob2o13bo$o4bo2b2o13b2o$6bo3bo6b2o2b2o2bo$2b2o6bo6bo2bo$2b2o4bobo4b2o$9bo5bo3bo3bo$10bo2bo4b2o$11b2o3bo5bobo$15bo8b2o$15bo4bo$14bo3bo$14bo5b2o$15bo5bo!'

# 1571P200H100V0A195.1 [B Type 5]
#rle='bo$o$o3bo$4o2$8b2ob2o$8b2ob2o$4bo$2b2o$2bo$2bo$3bo3$bo$o$o3bo$4o!'

# xxxP200H100V0A359 http://pentadecathlon.com/objects/class4/typeB/Bheptomino/bHeptomino.php
rle='4o$o3bo$o$bo2bo3$3bo$2bo$2bo$2b2o$4bo$8b2o2b2o$8b2o2b2o2$4o$o3bo$o$bo2bo!'

# 202P15H6V0A16.1 P.Tooke http://pentadecathlon.com/objects/class4/typeB/others/others.php
#rle='22b2o10bo$5b2o2bo8b2o2bo2bo8bo4bo$5b3o9b2obo7b3o2bo5bo$b3obo11bo2b3o6bo4b2obobo7bo$obobob3obo11bobo8bobo2bobo7b2o$o3b6o6bo5bo2b2o3b4o5bo7bo$o12b2o3b3obo4bo3bobo2bo2bo5bo$bobo8b3obo5bob2ob4o3b2o9bo$12bo5b2o2bob2o$bobo8b3obo5bob2ob4o3b2o9bo$o12b2o3b3obo4bo3bobo2bo2bo5bo$o3b6o6bo5bo2b2o3b4o5bo7bo$obobob3obo11bobo8bobo2bobo7b2o$b3obo11bo2b3o6bo4b2obobo7bo$5b3o9b2obo7b3o2bo5bo$5b2o2bo8b2o2bo2bo8bo4bo$22b2o10bo!'

world = import_RLE_seed(rle)
print_world(world)

world = flip_world_horizontal(world)
print_world(world)

world = shift_world_vertical(world,20)
print_world(world)

world += import_RLE_seed(rle)

life_sequence(world,sleep=0)