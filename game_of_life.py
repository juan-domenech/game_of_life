
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
    top_left,bottom_right = find_corners(world)

    for y in range( top_left[1]-1, bottom_right[1] +2 ):

        for x in range( top_left[0]-1, bottom_right[0] +2 ):

            if (x,y) not in world:
                if len( get_neighbours(world, (x,y) ) ) == 3:
                    new_world.append( (x,y) )
                    if DEBUG:
                        print "New cell: (",x,",",y,")"


    if DEBUG and len(new_world) == 0:
        print "No cells survived!"

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
                    ex += "* "
                else:
                    ex += ". "
        print ex
        print

    print

    return


#http://www.conwaylife.com/wiki/Run_Length_Encoded
def import_RLE_seed(rle):

    x = y = num = 0
    world = []
    doubleJump = False

    for item in range(0, len(rle) ) :

        if doubleJump:
            doubleJump = False
            print "doubleJump False"
            continue

        if rle[item] == 'o' :
            # Alive cell
            world.append( (x,y) )
            x += 1
        elif rle[item] == 'b' :
            # Dead cell
            x += 1
        elif rle[item] in '0123456789' :
            # Jump
            for jump in range(0, int(rle[item]) ) :
                if rle[item+1] == 'o':
                    world.append( (x,y) )
                x += 1
            print "doubleJump True"
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
