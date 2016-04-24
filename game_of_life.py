# Game of Life
# https://www.youtube.com/watch?v=R9Plq-D1gEk

# Rules
#
# Die -> <2 neighbours
# Survive -> =2 neighbours
# Survive -> =3 neighbours
# Die -> >3 neighbours
# Born -> =3 neighbours
#

# Coordinates system: (0,0) = center of the world
"""
(-1,-1) (0,-1) (1,-1)

(-1,0)  (0,0)  (1,0)

(-1,1)  (0,1)  (1,1)

"""

DEBUG = False

def next_generation(world):

    new_world = []

    if not world:
        return new_world

    if DEBUG:
        print "Current Generation"
        print_world(world)

    for item in world:

        # Get Neighbours
        neighbours = get_neighbours(world,item)

        # Die -> <2 neighbours
        # Die -> >3 neighbours
        if not (len(neighbours) < 2 or len(neighbours) > 3 ) :
            new_world.append(item)

        # Survive -> =2 neighbours
        # Survive -> =3 neighbours
        if len(neighbours) == 2 or len(neighbours) == 3 :
            new_world.append(item)


    # Born -> =3 neighbours
    potentials = []

    # Get all the potentials cells where life could arise around every existing cell
    for item in world:
        potentials.append( [ item for item in get_all_neighbours( item ) ] )

    # Remove duplicates converting to set() and then back to list()
    potentials = list ( set ( [ item2 for item in potentials for item2 in item ] ) )

    # Add those cells with a total of 3 living cells as neighbours
    for item in potentials:
        if len( get_neighbours(world, item) ) == 3:
            new_world.append( item )
            if DEBUG:
                print "New cell:",item

    if DEBUG and len(new_world) == 0:
        print "No cells survived!"

    # Remove duplicates and sort the list to help the unitest
    new_world = sorted ( list(set( new_world )) )

    if DEBUG:
        print "Output:"
        print new_world
        print print_world(new_world)

    return new_world


def get_neighbours(world,cell):

    neighbours = []
    # (0,-1)
    if (cell[0],cell[1]-1) in world:
        neighbours.append( (cell[0],cell[1]-1) )
    # (1,-1)
    if (cell[0]+1,cell[1]-1) in world:
        neighbours.append( (cell[0]+1,cell[1]-1) )
    # (1,0)
    if (cell[0]+1,cell[1]) in world:
        neighbours.append( (cell[0]+1,cell[1]) )
    # (1,1)
    if (cell[0]+1,cell[1]+1) in world:
        neighbours.append( (cell[0]+1,cell[1]+1) )
    # (0,1)
    if (cell[0],cell[1]+1) in world:
        neighbours.append( (cell[0],cell[1]+1) )
    # (-1,1)
    if (cell[0]-1,cell[1]+1) in world:
        neighbours.append( (cell[0]-1,cell[1]+1) )
    # (-1,0)
    if (cell[0]-1,cell[1]) in world:
        neighbours.append( (cell[0]-1,cell[1]) )
    # (-1,-1)
    if (cell[0]-1,cell[1]-1) in world:
        neighbours.append( (cell[0]-1,cell[1]-1) )

    if DEBUG:
            print "Neighbours of ",cell," : ",neighbours

    return neighbours


# Including empty cells
def get_all_neighbours( cell ):

    neighbours = []

    # (0,-1)
    neighbours.append( (cell[0],cell[1]-1) )
    # (1,-1)
    neighbours.append( (cell[0]+1,cell[1]-1) )
    # (1,0)
    neighbours.append( (cell[0]+1,cell[1]) )
    # (1,1)
    neighbours.append( (cell[0]+1,cell[1]+1) )
    # (0,1)
    neighbours.append( (cell[0],cell[1]+1) )
    # (-1,1)
    neighbours.append( (cell[0]-1,cell[1]+1) )
    # (-1,0)
    neighbours.append( (cell[0]-1,cell[1]) )
    # (-1,-1)
    neighbours.append( (cell[0]-1,cell[1]-1) )

    if DEBUG:
            print "Neighbours of ",cell," : ",neighbours

    return neighbours


def find_corners(world):
    top_left =  world[0]
    bottom_right = world[0]

    for item in world:
        if item[0] < top_left[0]:
            top_left = item[0],top_left[1]
        if item[1] < top_left[1]:
            top_left = top_left[0],item[1]
    if DEBUG:
        print "Top Left",top_left

    for item in world:
        if item[0] > bottom_right[0]:
            bottom_right = item[0],bottom_right[1]
        if item[1] > bottom_right[1]:
            bottom_right = bottom_right[0],item[1]
    if DEBUG:
        print "Bottom Right",bottom_right

    return top_left,bottom_right


def print_world(world):

    # Find corners to know how big our world is
    top_left,bottom_right = find_corners(world)

    print 'World: Population:',len(world),'  X-Axis Size:', abs(top_left[0]) + abs(bottom_right[0]+1),'  Y-Axis Size:', abs(top_left[1]) + abs(bottom_right[1]+1),' Corner Top-Left:',top_left,'Corner Bottom-Right:',bottom_right
    print

    for y in range( top_left[1], bottom_right[1] +1 ):

        ex = ''

        for x in range( top_left[0], bottom_right[0] +1 ):

            if DEBUG:
                if (x,y) in world:
                    print "["+str(x)+","+str(y)+"]\t",
                else:
                    print "("+str(x)+","+str(y)+")\t",
            else:
                if (x,y) in world:
                    # Print square character
                    ex += unichr(0x2588)+" "
                else:
                    ex += ". "
        print ex

    print
    return


def print_world_HTML(world, generation):

    # Center of our SVG canvas: '<svg width="1400" height="600">'
    x_center = 600
    y_center = 300
    # Square total side length
    pixels = 5
    # Square visual side length
    square = 4

    # Find corners to know how big our world is (just needed for the information bar)
    top_left,bottom_right = find_corners(world)

    # Print information bar
    print '<text x="2" y="20" class="svgText">Generation #'+str(generation)+'  Population:'+str(len(world))+' cells   X-Axis-Size:'+str(abs(top_left[0]))+'   Y-Axis-Size:'+str(abs(top_left[1]) + abs(bottom_right[1]+1))+'  Corner Top-Left '+str(top_left)+'  Corner Bottom-Right '+str(bottom_right)+'  Rate:100ms</text>'

    # Loop over all the current alive cells and convert them into SVG squares
    for item in world:
        print '<rect x="'+str((item[0]*pixels)+x_center)+'" y="'+str((item[1]*pixels)+y_center)+'" width="'+str(square)+'" height="'+str(square)+'" fill="black"/>'

    return


def print_world_HTML_with_retracing(world, generation, palette):

    # Center of our SVG canvas: '<svg width="1400" height="600">'
    x_center = 600
    y_center = 200
    # Square total side length
    pixels = 5
    # Square visual side length
    square = 4

    # Find corners to know how big our world is (just needed for the information bar)
    top_left,bottom_right = find_corners(world[9])

    # Print information bar
    print '<rect x="2" y="5" width="900" height="20" fill="black"/>'
    print '<text x="2" y="20" class="svgText" fill="white">Generation #'+str(generation)+'  Population:'+str(len(world[9]))+' cells   X-Axis-Size:'+str(abs(top_left[0])+abs(bottom_right[0]))+'   Y-Axis-Size:'+str(abs(top_left[1]) + abs(bottom_right[1]+1))+'  Corner Top-Left '+str(top_left)+'  Corner Bottom-Right '+str(bottom_right)+'  Rate:100ms</text>'

    # Loop over all the current alive cells and convert them into SVG squares
    for item in world[9]:
        x = (item[0]*pixels)+x_center
        y = (item[1]*pixels)+y_center
        if x > 0 and x < 1200 and y > 0 and y < 600 :
            print '<rect x="'+str((item[0]*pixels)+x_center)+'" y="'+str((item[1]*pixels)+y_center)+'" width="'+str(square)+'" height="'+str(square)+'" fill="'+palette[0]+'"/>'

    for item in world[8]:
        if item not in world[9]:
            x = (item[0]*pixels)+x_center
            y = (item[1]*pixels)+y_center
            if x > 0 and x < 1200 and y > 0 and y < 600 :
                print '<rect x="'+str((item[0]*pixels)+x_center)+'" y="'+str((item[1]*pixels)+y_center)+'" width="'+str(square)+'" height="'+str(square)+'" fill="'+palette[1]+'"/>'

    for item in world[7]:
        if item not in world[9] and item not in world[8] :
            x = (item[0]*pixels)+x_center
            y = (item[1]*pixels)+y_center
            if x > 0 and x < 1200 and y > 0 and y < 600 :
                print '<rect x="'+str((item[0]*pixels)+x_center)+'" y="'+str((item[1]*pixels)+y_center)+'" width="'+str(square)+'" height="'+str(square)+'" fill="'+palette[2]+'"/>'

    for item in world[6]:
        if item not in world[9] and item not in world[8] and item not in world[7] :
            x = (item[0]*pixels)+x_center
            y = (item[1]*pixels)+y_center
            if x > 0 and x < 1200 and y > 0 and y < 600 :
                print '<rect x="'+str((item[0]*pixels)+x_center)+'" y="'+str((item[1]*pixels)+y_center)+'" width="'+str(square)+'" height="'+str(square)+'" fill="'+palette[3]+'"/>'

    for item in world[5]:
        if item not in world[9] and item not in world[8] and item not in world[7] and item not in world[6] :
            x = (item[0]*pixels)+x_center
            y = (item[1]*pixels)+y_center
            if x > 0 and x < 1200 and y > 0 and y < 600 :
                print '<rect x="'+str((item[0]*pixels)+x_center)+'" y="'+str((item[1]*pixels)+y_center)+'" width="'+str(square)+'" height="'+str(square)+'" fill="'+palette[4]+'"/>'

    for item in world[4]:
        if item not in world[9] and item not in world[8] and item not in world[7] and item not in world[6] and item not in world[5] :
            x = (item[0]*pixels)+x_center
            y = (item[1]*pixels)+y_center
            if x > 0 and x < 1200 and y > 0 and y < 600 :
                print '<rect x="'+str((item[0]*pixels)+x_center)+'" y="'+str((item[1]*pixels)+y_center)+'" width="'+str(square)+'" height="'+str(square)+'" fill="'+palette[5]+'"/>'

    for item in world[3]:
        if item not in world[9] and item not in world[8] and item not in world[7] and item not in world[6] and item not in world[5] and item not in world[4] :
            x = (item[0]*pixels)+x_center
            y = (item[1]*pixels)+y_center
            if x > 0 and x < 1200 and y > 0 and y < 600 :
                print '<rect x="'+str((item[0]*pixels)+x_center)+'" y="'+str((item[1]*pixels)+y_center)+'" width="'+str(square)+'" height="'+str(square)+'" fill="'+palette[6]+'"/>'

    for item in world[2]:
        if item not in world[9] and item not in world[8] and item not in world[7] and item not in world[6] and item not in world[5] and item not in world[4] and item not in world[3] :
            x = (item[0]*pixels)+x_center
            y = (item[1]*pixels)+y_center
            if x > 0 and x < 1200 and y > 0 and y < 600 :
                print '<rect x="'+str((item[0]*pixels)+x_center)+'" y="'+str((item[1]*pixels)+y_center)+'" width="'+str(square)+'" height="'+str(square)+'" fill="'+palette[7]+'"/>'

    for item in world[1]:
        if item not in world[9] and item not in world[8] and item not in world[7] and item not in world[6] and item not in world[5] and item not in world[4] and item not in world[3] and item not in world[2] :
            x = (item[0]*pixels)+x_center
            y = (item[1]*pixels)+y_center
            if x > 0 and x < 1200 and y > 0 and y < 600 :
                print '<rect x="'+str((item[0]*pixels)+x_center)+'" y="'+str((item[1]*pixels)+y_center)+'" width="'+str(square)+'" height="'+str(square)+'" fill="'+palette[8]+'"/>'

    for item in world[0]:
        if item not in world[9] and item not in world[8] and item not in world[7] and item not in world[6] and item not in world[5] and item not in world[4] and item not in world[3] and item not in world[2] and item not in world[1] :
            x = (item[0]*pixels)+x_center
            y = (item[1]*pixels)+y_center
            if x > 0 and x < 1200 and y > 0 and y < 600 :
                print '<rect x="'+str((item[0]*pixels)+x_center)+'" y="'+str((item[1]*pixels)+y_center)+'" width="'+str(square)+'" height="'+str(square)+'" fill="'+palette[9]+'"/>'

    return


# Optionally remove distant cells to avoid gliders proliferation
def prune(world, limit = 50):
    return [cell for cell in world if abs(cell[0]) < limit and abs(cell[1]) < limit ]


def flip_world_horizontal(world):
    new_world = []
    for item in world:
        new_world.append( (item[0]* -1, item[1] ) )
    return new_world


def shift_world_vertical(world, shift):
    new_world = []
    for item in world:
        new_world.append( (item[0], item[1]+shift ) )
    return new_world


#http://www.conwaylife.com/wiki/Run_Length_Encoded
def import_RLE_seed(rle):

    ### Warning! Horrible code ahead

    x = y = num = 0
    world = []
    doubleJump = False
    tripleJump = False

    for item in range(0, len(rle) ) :

        if doubleJump:
            doubleJump = False
            #print "doubleJump False"
            continue

        if tripleJump:
            tripleJump = False
            #print "doubleJump False"
            continue

        if rle[item] == 'o' :
            # Alive cell
            world.append( (x,y) )
            x += 1
        elif rle[item] == 'b' :
            # Dead cell
            x += 1
        # Multiple line break
        elif rle[item] in '0123456789' and rle[item+1] == '$':
            y += int(rle[item])-1
        # Jump
        elif rle[item] in '0123456789' :
            # Double digit
            if rle[item+1] in '0123456789' :
                for jump in range(0, int( rle[item]+rle[item+1] ) ) :
                    if rle[item+2] == 'o':
                        world.append( (x,y) )
                    x += 1
                doubleJump = True
                tripleJump = True
            # Single digit
            else:
                for jump in range(0, int(rle[item]) ) :
                    if rle[item+1] == 'o':
                        world.append( (x,y) )
                    x += 1
                doubleJump = True

        elif rle[item] == '$' :
            # End of line
            x = 0
            y += 1
        elif rle[item] == '!' :
            # End of seed
            pass
        else:
            print "ERROR: Unrecognized symbol",item

    return world
