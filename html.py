
from game_of_life import next_generation, print_world, import_RLE_seed, prune, print_world_HTML,flip_world_horizontal, shift_world_vertical

def life_sequence(world,sleep=1):

    last_body_count = 0
    counter = 0

    print '<!DOCTYPE html><html><head><title></title><link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Dosis"><style>.generations{ display: none } .svgText { font-family: Dosis; font-size: 1em;} </style></head><body>'

    for generation in range(1,50000):

        print '<div id="generation_'+str(generation)+'" class="generations">'
        print '<svg width="1400" height="1000">'

        print_world_HTML(world,generation)

        print '</div></svg>'

        print '<script type="text/javascript">'
        #print 'setTimeout(function(){ document.getElementById("generation_'+str(x)+'").style.display="block"; }, '+str(100*x)+');'
        #print 'setTimeout(function(){ document.getElementById("generation_'+str(x)+'").style.display="none"; }, '+str((100*x)+100)+');'
        print 'setTimeout(function(){ var elem = document.getElementById("generation_'+str(generation)+'"); elem.parentNode.removeChild(elem); },'+str(100 * generation)+');'
        print 'setTimeout(function(){ document.getElementById("generation_'+str(generation+1)+'").style.display="block"; }, '+str(100 * generation)+');'
        print '</script>'

        #old_world = world
        new_world = next_generation(world)

        if len(new_world) == 0 :
            print "All cells dead at generation #",generation
            break

        world = new_world

        # Break once the population has been stabilized
        if len(world) == last_body_count:
            counter += 1
            if counter > 100 :
                #print "Population stable at generation:",x - counter
                break
        else:
            last_body_count = len(world)

    print '</body></html>'
    return


# Die Hard
#world =  [ (0,1),(1,1),(1,2),(6,0),(5,2),(6,2),(7,2) ]

# R-Pentomino
#world = [ (1,0),(2,0),(0,1),(1,1),(1,2) ]

# Rabits http://pentadecathlon.com/lifeNews/methuselahs/
#rle='o3b3o$3o2bo$bo!'

# 202P15H6V0A16.1 P.Tooke http://pentadecathlon.com/objects/class4/typeB/others/others.php
#rle='22b2o10bo$5b2o2bo8b2o2bo2bo8bo4bo$5b3o9b2obo7b3o2bo5bo$b3obo11bo2b3o6bo4b2obobo7bo$obobob3obo11bobo8bobo2bobo7b2o$o3b6o6bo5bo2b2o3b4o5bo7bo$o12b2o3b3obo4bo3bobo2bo2bo5bo$bobo8b3obo5bob2ob4o3b2o9bo$12bo5b2o2bob2o$bobo8b3obo5bob2ob4o3b2o9bo$o12b2o3b3obo4bo3bobo2bo2bo5bo$o3b6o6bo5bo2b2o3b4o5bo7bo$obobob3obo11bobo8bobo2bobo7b2o$b3obo11bo2b3o6bo4b2obobo7bo$5b3o9b2obo7b3o2bo5bo$5b2o2bo8b2o2bo2bo8bo4bo$22b2o10bo!'

# xxxP200H100V0A359
#rle='4o$o3bo$o$bo2bo3$3bo$2bo$2bo$2b2o$4bo$8b2o2b2o$8b2o2b2o2$4o$o3bo$o$bo2bo!'

# xxxP200H100V0A359 duplicated and inverted using flip_world_horizontal(world) + shift_world_vertical(world,20)
world=[(0, 20), (-1, 20), (-2, 20), (-3, 20), (0, 21), (-4, 21), (0, 22), (-1, 23), (-4, 23), (-3, 26), (-2, 27), (-2, 28), (-2, 29), (-3, 29), (-4, 30), (-8, 31), (-9, 31), (-12, 31), (-13, 31), (-8, 32), (-9, 32), (-12, 32), (-13, 32), (0, 34), (-1, 34), (-2, 34), (-3, 34), (0, 35), (-4, 35), (0, 36), (-1, 37), (-4, 37), (0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (4, 1), (0, 2), (1, 3), (4, 3), (3, 6), (2, 7), (2, 8), (2, 9), (3, 9), (4, 10), (8, 11), (9, 11), (12, 11), (13, 11), (8, 12), (9, 12), (12, 12), (13, 12), (0, 14), (1, 14), (2, 14), (3, 14), (0, 15), (4, 15), (0, 16), (1, 17), (4, 17)]

#world = import_RLE_seed(rle)
#print_world(world)

#world = flip_world_horizontal(world)
#print_world(world)

#world = shift_world_vertical(world,20)
#print_world(world)

#world += import_RLE_seed(rle)

#print '<!DOCTYPE html><html><head><title></title><style>.generations{ display: none }</style></head><body>'

#print_world_HTML([], world)

#old_world = world
#world = next_generation(world)

#print_world_HTML(old_world, world)

#print world
life_sequence(world,sleep=0)

