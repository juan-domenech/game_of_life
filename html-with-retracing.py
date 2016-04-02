
from game_of_life import next_generation, print_world_HTML_with_retracing

def life_sequence(world,sleep=1):

    print '<!DOCTYPE html><html><head><title>Game of Life animation generated with Python and HTML5/SVG</title>'
    #print '<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Dosis">'
    print '<link rel="image_src" href="https://www.doc.ic.ac.uk/project/examples/2012/163/g1216326/img/gameoflife.png"/>'
    print '<style>.generations{ display: block } .svgText { font-family: Dosis; font-size: 1em;}'
    print '</style></head><body>'
    print
    print '<!--'
    print 'Game of Life animation generated with Python and HTML5/SVG'
    print 'Seed (based on xxxP200H100V0A359):'
    print '[(0, 20), (-1, 20), (-2, 20), (-3, 20), (0, 21), (-4, 21), (0, 22), (-1, 23), (-4, 23), (-3, 26), (-2, 27), (-2, 28), (-2, 29), (-3, 29), (-4, 30), (-8, 31), (-9, 31), (-12, 31), (-13, 31), (-8, 32), (-9, 32), (-12, 32), (-13, 32), (0, 34), (-1, 34), (-2, 34), (-3, 34), (0, 35), (-4, 35), (0, 36), (-1, 37), (-4, 37), (0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (4, 1), (0, 2), (1, 3), (4, 3), (3, 6), (2, 7), (2, 8), (2, 9), (3, 9), (4, 10), (8, 11), (9, 11), (12, 11), (13, 11), (8, 12), (9, 12), (12, 12), (13, 12), (0, 14), (1, 14), (2, 14), (3, 14), (0, 15), (4, 15), (0, 16), (1, 17), (4, 17)]'
    print
    print 'https://github.com/juan-domenech/game_of_life/html.py'
    print '-->'
    print

    print '<div id="generation-0" class="generations">'
    print '<svg width="1200" height="600" style="background: black">'

    for generation in range(1,1000):

        # print '<div id="generation_'+str(generation)+'" class="generations">'
        # print '<svg width="1400" height="600">'

        print_world_HTML_with_retracing(world, generation)

        world.pop(0)

        world.append(next_generation(world[8]))

        if len(world) == 0 :
            print "All cells dead at generation #",generation
            break

        print '<!-- -->'

    print '</div></svg>'

        # print '<script type="text/javascript">'
        # print 'setTimeout(function(){var elem=document.getElementById("generation_'+str(generation)+'");elem.parentNode.removeChild(elem);},'+str(100 * generation)+');'
        # print 'setTimeout(function(){document.getElementById("generation_'+str(generation+1)+'").style.display="block";},'+str(100 * generation)+');'
        # print '</script>'
        # print


    print '</body></html>'
    return


world = [ [],[],[],[],[],[],[],[],[],[] ]

# Die Hard
#seed =  [ (0,1),(1,1),(1,2),(6,0),(5,2),(6,2),(7,2) ]

# R-Pentomino
#seed = [ (1,0),(2,0),(0,1),(1,1),(1,2) ]

# Rabits http://pentadecathlon.com/lifeNews/methuselahs/
#rle='o3b3o$3o2bo$bo!'
#seed = import_RLE_seed(rle)

# 202P15H6V0A16.1 P.Tooke http://pentadecathlon.com/objects/class4/typeB/others/others.php
#rle='22b2o10bo$5b2o2bo8b2o2bo2bo8bo4bo$5b3o9b2obo7b3o2bo5bo$b3obo11bo2b3o6bo4b2obobo7bo$obobob3obo11bobo8bobo2bobo7b2o$o3b6o6bo5bo2b2o3b4o5bo7bo$o12b2o3b3obo4bo3bobo2bo2bo5bo$bobo8b3obo5bob2ob4o3b2o9bo$12bo5b2o2bob2o$bobo8b3obo5bob2ob4o3b2o9bo$o12b2o3b3obo4bo3bobo2bo2bo5bo$o3b6o6bo5bo2b2o3b4o5bo7bo$obobob3obo11bobo8bobo2bobo7b2o$b3obo11bo2b3o6bo4b2obobo7bo$5b3o9b2obo7b3o2bo5bo$5b2o2bo8b2o2bo2bo8bo4bo$22b2o10bo!'
#seed = import_RLE_seed(rle)

# xxxP200H100V0A359
#rle='4o$o3bo$o$bo2bo3$3bo$2bo$2bo$2b2o$4bo$8b2o2b2o$8b2o2b2o2$4o$o3bo$o$bo2bo!'
#seed = import_RLE_seed(rle)

# xxxP200H100V0A359 duplicated and inverted using flip_world_horizontal(world) + shift_world_vertical(world,20)
seed =[(0, 20), (-1, 20), (-2, 20), (-3, 20), (0, 21), (-4, 21), (0, 22), (-1, 23), (-4, 23), (-3, 26), (-2, 27), (-2, 28), (-2, 29), (-3, 29), (-4, 30), (-8, 31), (-9, 31), (-12, 31), (-13, 31), (-8, 32), (-9, 32), (-12, 32), (-13, 32), (0, 34), (-1, 34), (-2, 34), (-3, 34), (0, 35), (-4, 35), (0, 36), (-1, 37), (-4, 37), (0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (4, 1), (0, 2), (1, 3), (4, 3), (3, 6), (2, 7), (2, 8), (2, 9), (3, 9), (4, 10), (8, 11), (9, 11), (12, 11), (13, 11), (8, 12), (9, 12), (12, 12), (13, 12), (0, 14), (1, 14), (2, 14), (3, 14), (0, 15), (4, 15), (0, 16), (1, 17), (4, 17)]

world.pop(0)
world.append(seed)

life_sequence(world,sleep=0)

