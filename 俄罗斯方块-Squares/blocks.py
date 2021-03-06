import random
from collections import namedtuple

Point = namedtuple('Point', 'X Y')
Shape = namedtuple('Shape', 'X Y Width Height')
Block = namedtuple('Block', 'template start_pos end_pos name next color')

red = (243, 60, 54)
green = (0, 128, 128)
blue = (63, 133, 255)
lime = (0, 156, 200)
purple = (138, 99, 194)
yellow = (230, 230, 80)
orange = (255, 167, 13)

# S形方块
S_BLOCK = [Block(['.OO',
                  'OO.',
                  '...'], Point(0, 0), Point(2, 1), 'S', 1, red),
           Block(['O..',
                  'OO.',
                  '.O.'], Point(0, 0), Point(1, 2), 'S', 0, red)]

# Z形方块
Z_BLOCK = [Block(['OO.',
                  '.OO',
                  '...'], Point(0, 0), Point(2, 1), 'Z', 1, lime),
           Block(['.O.',
                  'OO.',
                  'O..'], Point(0, 0), Point(1, 2), 'Z', 0, lime)]

# I型方块
I_BLOCK = [Block(['.O..',
                  '.O..',
                  '.O..',
                  '.O..'], Point(1, 0), Point(1, 3), 'I', 1, blue),
           Block(['....',
                  '....',
                  'OOOO',
                  '....'], Point(0, 2), Point(3, 2), 'I', 0, blue)]

# O型方块
O_BLOCK = [Block(['OO',
                  'OO'], Point(0, 0), Point(1, 1), 'O', 0, green)]

# J型方块
J_BLOCK = [Block(['O..',
                  'OOO',
                  '...'], Point(0, 0), Point(2, 1), 'J', 1, purple),
           Block(['.OO',
                  '.O.',
                  '.O.'], Point(1, 0), Point(2, 2), 'J', 2, purple),
           Block(['...',
                  'OOO',
                  '..O'], Point(0, 1), Point(2, 2), 'J', 3, purple),
           Block(['.O.',
                  '.O.',
                  'OO.'], Point(0, 0), Point(1, 2), 'J', 0, purple)]

# L型方块
L_BLOCK = [Block(['..O',
                  'OOO',
                  '...'], Point(0, 0), Point(2, 1), 'L', 1, yellow),
           Block(['.O.',
                  '.O.',
                  '.OO'], Point(1, 0), Point(2, 2), 'L', 2, yellow),
           Block(['...',
                  'OOO',
                  'O..'], Point(0, 1), Point(2, 2), 'L', 3, yellow),
           Block(['OO.',
                  '.O.',
                  '.O.'], Point(0, 0), Point(1, 2), 'L', 0, yellow)]

# T型方块
T_BLOCK = [Block(['.O.',
                  'OOO',
                  '...'], Point(0, 0), Point(2, 1), 'T', 1, orange),
           Block(['.O.',
                  '.OO',
                  '.O.'], Point(1, 0), Point(2, 2), 'T', 2, orange),
           Block(['...',
                  'OOO',
                  '.O.'], Point(0, 1), Point(2, 2), 'T', 3, orange),
           Block(['.O.',
                  'OO.',
                  '.O.'], Point(0, 0), Point(1, 2), 'T', 0, orange)]

BLOCKS = {'O': O_BLOCK,
          'I': I_BLOCK,
          'Z': Z_BLOCK,
          'T': T_BLOCK,
          'L': L_BLOCK,
          'S': S_BLOCK,
          'J': J_BLOCK}


def get_block():
    block_name = random.choice('O I Z T L S J'.split())
    block = BLOCKS[block_name]
    index = random.randint(0, len(block) - 1)
    return block[index]


def get_next_block(block):
    b = BLOCKS[block.name]
    return b[block.next]
