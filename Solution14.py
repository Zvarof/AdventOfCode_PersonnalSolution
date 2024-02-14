import re

InputBrut = """.OO..##.###..#O.O..O#.OOO.....#..O##O#.OO...O..##.O.O.......##O...O...O#O.O.#..O..O.#O..OO...#......
....OO..#.#...O#.O..#O..#OO...OO..O......O#........O...#..OO..#.#.O#..OO...O####.O...O.O.#.O..O.O..O
.O#.......O.OO#OO##O#O..O.O....#.OO..O...O.OO........O..#...O.O......##....O.....##.O.#.#.O..O......
..##.#.....#..#.O#O...O..O...OOO.##O.O##...O#.OO.#....OOO.OO.#O.O.O#...OO.OO.....O#..#...O...OO#...O
OO..#..OO#..#..O..#O..O.O##O#OOO.#...OO.#....#..#....O.####O.##..O......#O..OOO#O.#...#.O...OO...OO#
#.O.#O.#.#..O.#.............#.#.OO......#.O.O##O###........#.....#.....#.....O.O.OO.O....O.......O.#
O#...#...........#..OO...O..#.....#...O.#.......O#.....##O#.OO##.......#..O......#..O..O.#O.#.#..O.#
OO...O##..O.#.......O#.........OO#..O..#O..#OO.O........#.O.O.O....OO#...#.#.#O...##O.#OO.#.....#..O
#OO...O...O...O....O...............O.#O..OO##O##O.....#.##...OO.O.#.##.##.O..#..#.O..#.#..O.........
.O..O.#...##..#.#OO....#.O#...OO#.......O..OO.#...OO##..O..O...O.O...O.#.O#.....O..OO.O.#.OO..#.##..
...OO.O.O.O#....#...O...#....OO.#O.#O..O.OO..OOO.O....#O.#...#.O#.O............#......O.O....#OO##.#
...#O......#O#..O....#.##..O.O.O#..#O.#O...O...#..#O..##.O#..O#....O##.O.#OOO.#........O##.OO.O..OO#
#OOO....#O...O.O....O.......O...O..#....##.#..#.O#O#.O#....#.#.#O#....#.#.....##.#O..OOO....#.O.....
#OO.O...#O.O....O..#..O.#....#....O#..O...##..#..OO#.....#O.O#O..O....#OO....##OO....#...OOOO.OO###.
O..#..O#.O.#..OO.#.OO...O..O......#........#O......O.OO.#....#..O#O.......OO##O..##OOOO.#.#OOO.....O
...#OO.#OO.O.##.O#.OO#...#..#.O##O#...#.#O...#.....#..O..O....O.OO.O.#..O.#.O...#.O#..O....O.#...O#.
#....O.....O.O...#..O....#..O..O.OO...#....O..O...#.....#...#....O.#.OO...OO#...O....#O.O..O.OO.O..O
..O#.....#O#....#.....OOO.#.......OO.O..#.#....#O......O.#.O.#..O...#.O...O..O.##O.O#O..#.O......#.#
....#O#.#..O#.OO.#.#.O.#......#OO...O#OO.........OOO..##...#..##O#..OOO...O..O..O##O...#..#.O.O..#..
..O#.O.......OOO..##..#...#....#.#..#O.OO..O..##..OO#.O...O..#OO...##O.#O..OO.....#O..#.....#O.....#
...OO.O.#.O.O..##O#...OO...##.O..OOO##.O.O.#..#.OO..O...O.#....O.O.....O##.#O.O.O#.#.......OO#......
O...#.O...O...#..OO...O..#..#........O...#...#......O#.#.....O.#.........#.#......O#O.O.........#...
.......O#...#...........O.#O#.O#.#.O.O..O..OO.#......##.OO..#......OO#....#O#OO.O.#..O#..O.OO..O..##
.O.....O.#.........O...O...O...O...OOOO..O....OO....#.#....O#.#..#.OO.OO....#.......#...#OO.....O.OO
O....OO....O..O.OO.###..O##.OO.#......O.O...##...#O...O..O...##.O.O...O....O.#OO.....O.....O.O.OO.OO
#O......OO....##..O..###.O....#.#.#.OO.............O.O.OOOO#.O.O..#O...O#..O......O.O.O.#.#.......O.
O#O.....#...#..O#.#....#..###..O..O...#....O....##.....#...O#.#.O.O......O..OOOOO....OO..#...#.OO#..
..O........OO....##...#O.....#.O.....O#.O..#.O.#.O......O#...OOO....O...#..OO....O..#...O.O..##.....
O...O..O.O....O.OO.O.OO..OO...#O...O.#.O..#O...#...#...O..##...#...OO#.....##..O#O.O....#.....OO#..O
...O#O..O..##.OO.......#.#O...O..#.#...#.O.#O##OOO.OOO...#.....O....##.....OOO.....O..O.O#.O....O...
O#..#O.O....#.........O#.OO#...OO......#......O.#...............O##OO.....O.....O.O..##..O#....#.OO.
#O..O.OO....##O......O.O...O#O..#.O..........O....#........O#.#..O..O............#..#...OO#.###..#.#
...#...#.#O....O.O.....OO.O.O...O.#.#.O...OO..O#....O#O......O.O..##.#.O.....#..O.O.#.#O...O.#......
.O...O#.O.......O.#....O.#...#.#..#O.....#..#..#.#O#..#.......O..#.#..O.OO.#OO.OOO..O....#.....OO#.O
O#.#..#.O..O..#O.......O.#..#....#.O..#...#......O...O##....O..#...O....#O..#.....OO.O.O#..O.#..#O..
#.#.....O...#O.#..O...#O..##..#O..#O...O.#OO...#....OO#..O.#O#O........OOO...O##..#..OO.O.O.O.O.....
..OO...#..OOO.O#..#...O..O.......O.#.#.O#.##OO....#..O....#..#.O.#O...O.O#O........O#OOOO#.#..O#.#..
.O....#.O#OOO.....O.#O............O...O#...O...O..O.#..O.O.....O#.O....O......O...O.O..OOO..O.##.O..
#...#........#..........###.O....OO.#.....#OOOO.OO#.OO...##...OO...O#.......O...#.#..#O..#.....#O#O.
O.O.#...O.#.....OO...O.O#......#........#..O...O..O.#..OO#.....#...O.##O#....O#..O#...##.O.O.#.#....
............OO.....O........##O.O...#..#.O.#...OO..#.O.#O.............O..#O.....#...O.#....O..O#..#.
.#..#.O.#......O..O##O.O.#..O..#O.O..O.O........O.......#.#.#O.#..O...O...O....O.O#...#..OO..O....OO
#..#..O....OO#.#.O.#......O...O.O#O...O#...O...#...#O.#....#..#O...O...........#.#.#..O##..#........
..O......O.#.OO.#O...O..#O...OO.#.....##...#.#....O....OO.#O.O.#....OO..#....#.#...#.O.....OO#..O...
#..........#...O.O....##....OO..O..O..#...#..###....##..O#..#.........#.....O#...#.#.......#.##.##O.
###.O.#..#.O.O.O..O..O...O...#O...O##.#..#O..O...#....O.....#..##......OO.#O...O#..O.O.O......#...OO
....O#........O.O#.O#O#...O.......#..O.#..#........O.....O#..O..O.OOO....OO.....#....O#.#..O.....##.
#.#O...#.O#O..#.#OOOO#.......#....O...O#.##.O....#..O.......O.##.#.OO...O...#O..O..#O.#......O.O.##.
.#O...OO#......O...#..##............O...##...O.#O....#..OO......O.O##OO..OO....##O.##..O............
O.O..OO.O.#.#....#..O.O.O.OOO...OO..#....O....O.#.#....#.O#.#.....O#O...O.OO..O.#O.#..OO#.O#........
#..#.O.##.##...#OO..O...OOOO#O##..#...#.##....#O.#O#.O.O#.#.O#...#.OO.......O........O..#.#.OOO#....
##....O...O#....O...O.#OO.O..O.....O#O#.#...OO.........#.......O.#.#..O..#O...#..O.#...#.##...O..O.O
.........O...O.O...#..O.O..OO.#...O.#.O........O.O.O....O...O..O..........O....O......O..#O.O..#O...
.......#.#....O#OOO.O.O..O.##...O..###.......O#.##...O.O....#.OOO..O...#.#.......#O.OO...O...OO.O...
.O...O...O....#.O.#...#..##O....#..O....O#..O.#.O..#...........#..O..##OO.......##..#.....O#...O#..#
...O....O....#....O..####.#O#.....#O.O..#..#O.OO...#...O.##.#.#....#...O...O..#.....OO.O....#..O..O.
.OO#.#...#....O.#O#.##....OO............O.....#.OO#O.#O.#..#...#.O....O.O..#..##.......O..O.#..##O.O
O...#.........#.O....O..O.....#.......#.OO...OO.#O#.#...OOO.O.O#.O.#...#O......#....O.......#.O.#.O.
.....O.............O.#..#.#..#.#...#..OOO....#.OO.O...O..#.##O.#O...O.O.OO......#....OO..O..........
O....#....#.#....#.........#...O.O#....OO.#..#O..#....OO...#....O...O#...O.......OOO...#......#...#O
..O..##O.#O.OOO..#..O.#....#.OOOO..O.O.....##O.....O.#.O.###..##....O..OOOO..#.#OO.O.OO.#O#..#...#.O
O#...O......#..#.....#..##.#OO#O#.....O...##....OO...O##...O....O.#...#O..#.O#..#O.O..#...#...OOO..O
O...##.O..O..O#....#..O........O....O#...O..O......O...OO...OO.#OO.O..#....O#O....O..#..#..OO.OO....
O..#.#O....O..O.O..O#...O.O...O..#.#.#..##.#O......#...OOO.#O...#..O.....O###O.....#.......O#.O.O...
OOO#..#.#...O...O..O.O..O#O.....#O.#..O....O...O.#..O.#...O#.......#.....#O.#.#..O...##..#.....O...O
O#...O#....O.#.#......O.....O.##.......#.O.......#.#.#...#..#O....##O......O..O.#.#..O..#..O.O#O.O..
O.O...O##.O#.....O......#...O.#...O.O..#........O..O..O#.O..OO#O.OO.........O...O..#.O......O...O#.O
..#......OO.#....O...O..O..##...#O#O#O..O..O......O..O.#O#..O......O..........OO..OOO#..#.OO....O...
.......##......#.O..#....#.O#O..O#...O#....O.OOOO..#.O.O..O..O..O.........O...O#...O..#O..#.#..O...O
.O#..OOOO.O......#O......OOO#.#.O.#O...##...O.O...##.O#.O.#.......#.......##...#O.O...#.#..O..##O..O
....OO......#.#.....O.#.OOO.O#.#...O.##.O..OO....#OO..O..O.O.O#..OO....O.O..#.O.##..O...OO..OO..OO#.
........#O.....#....O#.#OOO.O...........OO....#.#.....OO#..#OO..#..#.....O#O..OO..OO..O......#..O.O.
O#O....#.#......O#...#.##O..OO.O.....#O..#..O..O......O##..#OO...OOOO.....O#....O..O.....OOO...#O..O
...O..#..O......OO.#.....#.O...O.O.#.O..OO..#....#...#....O.#O.O...O.O......O......O..#...#O###.OO..
#O###.....#....#.#O..#...#O..OO....#.O...#.##OO.#.#.#.....#....O.###...#....#.#...O.......O...O..#.O
..#..O.O..#.........O#..OOOO###..O##.#........O...#.#O#..#...O...O#....O..#.#...O.O..OO.....O.......
#...O..#.......O........O....#.O......#...##.##......O.....O.##.O..O.....##...#OOO..O...O##.O.O.....
......#.OO....###.......#.###..OO#.OOO#O#.OOO#..O....OO........#...O...O#.OO.#....O#.......#..#..#..
#..#OOO....#.#.O.O..........#O....O#...O..O..#...O....O#..##.O..O.#O...#.#.#..O..O.O.#O..O..O...#.#.
.#...O.O##.....#..O.....OOO.#.....#OOO#.#..O.....O.#.O.O.#.#.O.O#.........O....#...#O.O##.##..O.O#.O
OOO...#O.OO....#.OOO..O....O.OO.O.#.O.#.#...#....OO........O..#..OO....#O....#.#O##.OO#O#.##OO.O.O.#
...O#..OO.....O#...#O........O....O#O....OO...#....O###..##.O..#..#.#..O..#O.OO..O........##O#.#..OO
.O...#..#....O.##...#.........##.#..O.O.....#.##..O.#O.#..O#...#....#.#.........##.O...O...OO#..O..#
O....##.O...O........O#..#...OO#O..OO..#.........##......O.......OO..O...O.O..#..........#.O..#...O.
###.#.........#OO....##...O#...O....O........#...#.O.#O.#.....##..O..#O.##......#.#.O.......O...O...
..#.OOOO..O......O#O.O.#.O.#..#.O...O..O.O..##O.O.......#...O#..#..O.#.#.O#.##...O......#.#...#.....
O.#.OOO.#......O....O..O...O#........#....#.......#O..O.OO..#.O#.OO..#.OOO..#O.....#OOOO..#.........
##.O...####OO#...O#.OO...O...O.......O...OO..####...OOOO..O##O....OOO....#..O.O........O....#.#.#O..
O.O....O...O#...O.#....O.....OO#O#OO..O##.O..O...O.#.....#O...O..#O...O#.....O##...O.OO...#.........
....#OO..OO..#O#......O#.O..#O..#..OO..#....#.....#.....O.O..O#....O.O..O.#..O#O###O....O...OO...#.#
#..OO.##O..OO.O..O...#....O.....##O..#............##.O.#...O.#O..#O..#...#...O.O....#O.....O.....O..
..O#..#...##.#.#.O#.OOO.O#.#....OO.#....#...#...#.....#O.....O..O...O.....#.O.O.O#...#O.#...##.O..O#
#....#.O...O#...##O.#....O........O...O#.#.#...#O#..O..O.#O.....O..O....#....O.O#O#....#O#..#......#
.O.O#.........O.....##.O.#..............O...#.#OOO.O.OO..O..O..O##....#.......OO....O....#OO#..OO...
##.O#...OO...O.O...........O..O.##O..#.#...#..O..#.##....#..###O..##........OOO.#.O.#......#......#.
#......O#..O#.#.#..#O##..OO#O...##O.#...#.OO...#.O..O##O.O...........O.##...###O..#.#.O.O..OO.O..O..
#.....#.##.O.O.#....O..#O......O.O#...#..O.#O#OO...#.OO...O.O##.O...O.......#...##....#O.....O.##O#.
...O.OO.O...O#..OO.O....#.#.O....O...#..#O.O..OO.#....O.O#.O#..O..O...O..O........#..#..#..#..OO.O#.
.#O.O....#....#.OO.#.O...O......O....O#.....##...#O...##...#.#OO..O#O..O##.#.#..O...O.....#..O##.O..
OOO....OOOO...#.#...#.....###...O......O.#.O.....O...#.O##...##O.#.#...O....O.O...#.O...#O....O....."""

Input=InputBrut.split('\n')

'''
print(f'This is Input : {Input}')

Empty_space = [[height for height in range(len(Input)) if Input[height][length] == '.'] for length in range(len(Input[0]))]
Inamovible_rock = [[height for height in range(len(Input)) if Input[height][length] == '#'] for length in range(len(Input[0]))]
Movible_rock = [[height for height in range(len(Input)) if Input[height][length] == 'O'] for length in range(len(Input[0]))]

print(f'Empty_space : {Empty_space} \n')
print(f'Inamovible_rock : {Inamovible_rock} \n')
print(f'Movible_rock : {Movible_rock} \n')


Final_Block_Position = [[Bloc-min(min([Bloc-Rock-1 for Rock in Rocks if Rock<Bloc] + [99999]), sum([Empty<Bloc for Empty in Emptys])) for Bloc in Blocs] for Emptys, Rocks, Blocs in zip(Empty_space, Inamovible_rock, Movible_rock)]
print(f'Final_Rock_Position : {Final_Block_Position}')

# Need to take into account that Movible_Rock can act as Inamovible Rock is preceded by a #
for line in Final_Block_Position:
    for idx in range(1, len(line)):
        if line[idx] <= line[idx-1]:
            line[idx] = line[idx-1]+1

print(f'Final_Rock_Position2 : {Final_Block_Position}')

result = sum([sum([len(Final_Block_Position)-rock for rock in line]) for line in Final_Block_Position])
print(f'The final result for Part 1 is supposed to be : {result}')
'''

## Part 2 - Hoping that there is a cycle pattern to reduce the number of iteration to a modulo + x 

# Getting the coordonate of all # and O

len_line = len(Input[0])
len_vertical = len(Input)

print(f' This is len_line : {len_line}')

Moving = [(idx, idx_elem) for idx, line in enumerate(Input) for idx_elem, elem in enumerate(line) if elem == 'O']
Stoping = [(idx, idx_elem) for idx, line in enumerate(Input) for idx_elem, elem in enumerate(line) if elem == '#']

print(f' This is Moving : {Moving} \n')
print(f' This is Stop : {Stoping} \n') 

def tilt_north(Moving, Stop):
    Transition_Move = [[] for _ in range(len_line)]
    Transition_Stop = [[] for _ in range(len_line)]

    # Sorting by column
    for move in Moving:
        Transition_Move[move[1]].append(move)
    for bloc in Stop:
        Transition_Stop[bloc[1]].append(bloc)
    
    # Iterating
    Moving = [(max([bloc[0]+1 for bloc in bloc_part if move[0]>bloc[0]] + [0]), move[1]) for move_part, bloc_part in zip(Transition_Move, Transition_Stop) for move in move_part]

    # Dealing with move being at the same place (iterating over the array, and if == ref : -> previous + counter)
    ref = (999, 999)
    counter = 0
    for idx, coordonate in enumerate(Moving):
        if coordonate == ref:
            counter += 1
            Moving[idx] = (ref[0] + counter, ref[1])
        else:
            ref = Moving[idx]
            counter = 0

    return Moving

def tilt_south(Moving, Stop):
    Transition_Move = [[] for _ in range(len_line)]
    Transition_Stop = [[] for _ in range(len_line)]

    # Sorting by column
    for move in Moving:
        Transition_Move[move[1]].append(move)
    for bloc in Stop:
        Transition_Stop[bloc[1]].append(bloc)
    
    # Iterating
    Moving = [(min([bloc[0]-1 for bloc in bloc_part if move[0]<bloc[0]] + [len_vertical-1]), move[1]) for move_part, bloc_part in zip(Transition_Move, Transition_Stop) for move in move_part]

    # Dealing with move being at the same place (iterating over the array, and if == ref : -> previous + counter)
    ref = (999, 999)
    counter = 0
    for idx, coordonate in enumerate(Moving):
        if coordonate == ref:
            counter += 1
            Moving[idx] = (ref[0] - counter, ref[1])
        else:
            ref = Moving[idx]
            counter = 0
    
    return Moving

def tilt_west(Moving, Stop):
    Transition_Move = [[] for _ in range(len_vertical)]
    Transition_Stop = [[] for _ in range(len_vertical)]

    # Sorting by rows
    for move in Moving:
        Transition_Move[move[0]].append(move)
    for bloc in Stop:
        Transition_Stop[bloc[0]].append(bloc)
    
    # Iterating
    Moving = [(move[0], max([bloc[1]+1 for bloc in bloc_part if move[1]>bloc[1]] + [0])) for move_part, bloc_part in zip(Transition_Move, Transition_Stop) for move in move_part]

    # Dealing with move being at the same place (iterating over the array, and if == ref : -> previous + counter)
    ref = (999, 999)
    counter = 0
    for idx, coordonate in enumerate(Moving):
        if coordonate == ref:
            counter += 1
            Moving[idx] = (ref[0], ref[1] + counter)
        else:
            ref = Moving[idx]
            counter = 0
    
    return Moving

def tilt_east(Moving, Stop):
    Transition_Move = [[] for _ in range(len_vertical)]
    Transition_Stop = [[] for _ in range(len_vertical)]

    # Sorting by rows
    for move in Moving:
        Transition_Move[move[0]].append(move)
    for bloc in Stop:
        Transition_Stop[bloc[0]].append(bloc)
    
    # Iterating
    Moving = [(move[0], min([bloc[1]-1 for bloc in bloc_part if move[1]<bloc[1]] + [len_vertical-1])) for move_part, bloc_part in zip(Transition_Move, Transition_Stop) for move in move_part]

    # Dealing with move being at the same place (iterating over the array, and if == ref : -> previous + counter)
    ref = (999, 999)
    counter = 0
    for idx, coordonate in enumerate(Moving):
        if coordonate == ref:
            counter += 1
            Moving[idx] = (ref[0], ref[1] - counter)
        else:
            ref = Moving[idx]
            counter = 0
    
    return Moving

def Cycle(Moving, Stoping):
    Moving = tilt_north(Moving, Stoping)
    # print(f'This is Moving Blocs Position after North : {Moving} \n \n')
    Moving = tilt_west(Moving, Stoping)
    # print(f'This is Moving Blocs Position after West : {Moving} \n \n')
    Moving = tilt_south(Moving, Stoping)
    # print(f'This is Moving Blocs Position after South : {Moving} \n \n')
    Moving = tilt_east(Moving, Stoping)
    # print(f'This is Moving Blocs Position after East : {Moving} \n \n')
    return Moving

Dict_Pos = {tuple(Moving) : 0}
counter = 1

while False :                                                   # Set to true to make it run
    Moving = Cycle(Moving, Stoping)
    New = tuple(Moving)

    if New in Dict_Pos:
        print(f'This is the number of time before reaching a cycle : {counter}')
        print(f'This is the first time this specification position occured : {Dict_Pos[New]}')
        break

    Dict_Pos[New] = counter
    counter += 1
    # Give first time counter == 103, reaching again with counter = 117 | (1000000000 - 103) % 14 == 1 -> Test avec range(104)

for _ in range(104):
    Moving = Cycle(Moving, Stoping)

result2 = sum([len_vertical-move[0] for move in Moving])
print(f'The final result for Part 2 is supposed to be : {result2}')

# [104] : 94255 - OK