# Conway's Game of Life

https://www.youtube.com/watch?v=R9Plq-D1gEk

## Code

### Requirements
Python 2.7.x

### game_of_life.py
Main module.

#### next_generation(world)
Calculate next generation.

#### print_world(world)
Print generation on console.

#### print_world_HTML(world,generation)
Print generation in HTML/SVG.

#### import_RLE_seed(rle)
Import seed in RLE format (http://www.conwaylife.com/wiki/Run_Length_Encoded)
Note: Only valid for jumps up to 99 cells.

### animation.py
Render animation on concole.

### html.py
Render animation in HTML/SVG format.
Redirection of the output to a file is required to capture the result.

### test_game_of_life.py
Test suite.


## Animations

#### Two puffers in opposite direction (1150 Generations)

Generation #1 seed:
![Seed](http://juan-domenech.github.io/sandbox/python/game-of-life/seed-two-puffers-opposite-direction.png)

https://juan-domenech.github.io/sandbox/python/game-of-life/two-puffers-opposite-direction-1150generations.html


#### Seed 'Rabbits' (3000 Generations)

![Rabbits](http://juan-domenech.github.io/sandbox/python/game-of-life/seed-rabbits-3000-generations.png)

https://juan-domenech.github.io/sandbox/python/game-of-life/rabbits-3000-generations.html

