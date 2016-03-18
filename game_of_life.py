
#
# Die -> <2 neighbours
# Die -> >3 neighbours
# Born -> =3 neighbours
# Survive -> =2 neighbours
# Survive -> =3 neighbours
#

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
        if len(neighbours) < 2 or len(neighbours) > 3:
            pass
        else:
            new_world.append(item)

        # Survive -> =2 neighbours
        # Survive -> =3 neighbours
        if len(neighbours) == 2 or len(neighbours) == 3:
            new_world.append(item)

        # Born -> =3 neighbours
        top_left,bottom_right = find_corners(world)

        for y in range( top_left[1]-1, bottom_right[1] +2 ):

            for x in range( top_left[0]-1, bottom_right[0] +2 ):

                if len( get_neighbours(world, (x,y) ) ) == 3:
                    new_world.append((x,y))
                    if DEBUG:
                        print "New cell: (",x,y,")"
                #if (x,y) in world:
                #    print "["+str(x)+","+str(y)+"]\t",
                #else:
                #    print "("+str(x)+","+str(y)+")\t",

    new_world = sorted ( list(set( new_world )) )

    #print
    #print_world(new_world)

    if len(new_world) == 0:
        print "No cells survived!"

    if DEBUG:
        print new_world

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
    top_left =  (0,0)
    bottom_right = (0,0)

    for item in world:
        if item[0] < top_left[0]:
            top_left = item[0],top_left[1]
        if item[1] < bottom_right[1]:
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

    ex = ''

    print 'World: Population:',len(world),"  X-Axis Size:', abs(top_left[0]) + abs(bottom_right[0]+1),'  Y-Axis Size:', abs(top_left[1]) + abs(bottom_right[1]+1)

    for y in range( top_left[1], bottom_right[1] +1 ):

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
        ex = ''

        print
    print

    return

