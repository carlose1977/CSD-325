'''
---

# CSD325-T301 - Week 6.2 Assignment: Forest Fire Simulation

---

**Professor**: John Woods<br>
**@Copyright**: BELLEVUE.edu<br>
**Modified By**: Carlos E. Escamilla<br>
**Email**: CEEscamilla@my365.BELLEVUE.edu<br>
**OS**: Windows 11 x64<br>
**Processor**: i9-13900<br>
**GPU**: NVIDIA GeForce RTX 3060<br>
**IDE**: DataSpell 2025.2<br>
**Interpreter**: Python 3.12<br>
**Libraries Managed by**: Miniforge3 (Prefer Anaconda, but it is not permitted at work)

---

**Version**:
- 1.0.0 - 2025.09.08 Week1: Programming Logic
- 1.0.1 - 2025.09.15 Week2: Documenting Debugging
- 1.0.2 - 2025.09.22 Week3: Brownfield Development
- 1.0.3 - 2025.09.29 Week4: CSV Read and Matplotlib
- 1.0.4 - 2025.10.06 Week5: Forest Fire Simulation 1
- 1.0.5 - 2025.10.13 Week6: Forest Fire Simulation 2

**Description**:
Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation

**Modifications**:
- Add a lake roughly in the center of the display.
- The water feature should use a different character (not A or @) and be blue.
- The water feature cannot be modified once it is in place, the water feature acts as a firebreak that flames cannot cross.

'''

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~' # Week 6 Modification: Add Water

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5
LAKE_WIDTH = 10 # Week 6 Modification: Width of lake
LAKE_HEIGHT = 6 # Week 6 Modification: Height of lake


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                # Week 6 Modification: Water cannot be modified
                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Week 6 Modification: Fire spreads to neighboring trees,
                            # but NOT to water (water acts as firebreak)
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)

def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    # Week 6 Modification: Calculate lake center position
    lake_center_x = WIDTH // 2
    lake_center_y = HEIGHT // 2
    lake_start_x = lake_center_x - (LAKE_WIDTH // 2)
    lake_start_y = lake_center_y - (LAKE_HEIGHT // 2)
    lake_end_x = lake_start_x + LAKE_WIDTH
    lake_end_y = lake_start_y + LAKE_HEIGHT

    for x in range(WIDTH):
        for y in range(HEIGHT):

            # Week 6 Modification: Place water in the lake area
            if (lake_start_x <= x < lake_end_x and
                    lake_start_y <= y < lake_end_y):
                forest[(x, y)] = WATER
            elif (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest

def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')

            # Week 6 Modification: Display water in blue
            elif forest[(x, y)] == WATER:
                bext.fg('blue')
                print(WATER, end='')

            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.


