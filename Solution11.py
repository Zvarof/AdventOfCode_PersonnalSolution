import functools
import re

Input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split('\n')

print("This is Input : ", Input)



def Expension(data):
    l = len(Input[0])
    h = len(Input)
    i, j = 0, 0

    # Adding columns
    while i<l:
        if all([data[idx1][i] == '.' for idx1 in range(h)]):
            for _1 in range(h):
                data[_1] = data[_1][:i] + '.' + data[_1][i:]           # data[_1].insert(i, '.')
            l += 1
            i += 1
        i+=1

    # Adding rows
    while j<h:
        if all([data[j][idx2] == '.' for idx2 in range(l)]):
            to_add = '.'*l
            data.insert(j, to_add)
            h += 1
            j += 1
        j+=1
    return data

NewUnivers = Expension(Input)

coordonate_galaxie = []
for idx, line in enumerate(NewUnivers):
    for galaxie in re.finditer(r'#', line):
        coordonate_galaxie.append((idx, galaxie.start()))

Total_Distance1 = 0
T = 1
for galaxie in coordonate_galaxie:
    for i in range(T, len(coordonate_galaxie)):
        Total_Distance1 += (abs(galaxie[0] - coordonate_galaxie[i][0]) + abs(galaxie[1] - coordonate_galaxie[i][1]))
    T += 1
# print(Total_Distance1)

"""
print("This is coordonate_galaxie : ", coordonate_galaxie)
for line in NewUnivers:
    print(line)
"""

## Partie 2 : 

"""
# Storing the position of line or column when the univers expend.
# Testing if the 2 compared point are in each side (> à droite et < à gauche) of the expension:
    # YES : Calculate the normal distance + Add 999999*nb d'expension qui répondent à cette condition
    # NO : Calculate the normal distance
    # Si insertion à pos 4, élément
"""

Input2 = """.........................#...........................................................................................................#......
..................#................................................#........................#................#..............................
...........................................................................#........................#...........................#...........
........#...................#........#......#.............#.....................#...........................................................
..........................................................................................................#........#........................
.....................#..........................#..........................................................................#................
.#...........#................................................................................................#....................#......#.
...............................#..........................................#..........#......................................................
....................................#............................#...................................#......................................
.................#.......................................................................................................#..................
.........................#.....................#.......................#........#.....................................................#.....
.....#...............................................#......................................#...............................................
..............................#..................................................................#.............#............................
#....................................#..................................................................#...................................
..........................................................#.................................................................................
......................................................................#...........................................#.........................
............#...............................................................#............................................#.............#....
....#.........................................................................................................................#.............
...................................#.....#.................................................................................................#
................................................#........................#.........#..........................#.............................
..........................#....................................#................................#...........................................
......#..............#...........................................................................................................#..........
.................................#.......................#............................#................#....................................
..................................................#..................#.....#................................................................
............#..............................#.................................................#............................#.................
..................#...............................................................#........................#.....#....................#.....
.....#......................................................................................................................................
..............................................#............#.........................................#...............#......................
..................................................................#.........................................................................
............................#..............................................................................................#.............#..
......................#..........................................................................................................#..........
.......................................................................................#....................................................
.............................................#...............................#.............................#..........................#.....
.#................#.........................................................................................................................
................................#...................................................#..........................#............................
..........#..............#........................................#................................#.....................................#..
...............................................#.......#..................................#.................................................
............................................................#...................................................................#...........
....................#.....................#................................................................................#................
............................#.....................#............................................#............................................
.............#................................................................................................#.............................
.................................................................#......................#...............#...................................
.......................................................................#.........#..................................#.......................
......#.......................#........................#....................................................................................
...................#..................................................................................................................#.....
......................................#..............................................................#...................#..................
.#............................................#................#.............#.................#................#.............#.............
............................................................................................................................................
..................................................................................#..................................#......................
.......#..............#............................................#......#...............................#.............................#...
..................................#..............#..........................................................................................
..............#..........................................#..................................................................................
...............................................................#................................................#.................#.........
.........................#...................................................#.........................................#....................
............................................................................................................................................
...#..............#................................................................................#.......................#................
.....................................................#.................................#......#.............................................
.................................#.......................................#......#..................................#........................
............................................................................................................................................
............................................................................................................................................
....................................#............#...........................#.........................#....................#...............
......#................#.........................................................................#.........................................#
........................................#..................#................................................................................
.................#......................................................................#....................#.....#.................#......
.....................................................................................................#......................................
.#.......................................................................................................................#...............#..
..............................#.................#...........................................................................................
.......#...............#...................#.........................................#.....................#.....#..........................
...................................#...........................................................#............................................
..................#................................................#............#...........................................#......#........
............................................................................................................................................
.......................................................................................................................#....................
.............................#.....................#...........................................................#...........................#
...............#....................#.............................................................#.........................................
.....#..............#..................................................................................#....................................
#..............................................#...........................#................................................#...........#...
..................................................................#.............#..........#.......................................#........
............................................................................................................................................
.........#......#..........#........................#............................................................#..........................
........................................................................................#..........#........................................
........................................#...................#........#....................................#............#....................
..............................#..................................................#..........................................................
............................................#.........................................................#.....................................
.....#........#...........#..........................................................#......................................#...............
................................................#........................#.................................................................#
.....................................#.....................#..................................................#.................#.....#.....
.#.......#.........................................................#................................#.......................................
............................................................................................................................................
...............................#...........#................................................................................................
.................................................................................................#..........#.....#.........................
......#...........#........#.......................#..............................#.................................................#.......
.........................................................................#..................................................................
...........#..................................#........................................................................#.....#..............
.......................................#......................................................................#.............................
#.....................#.........................................................................#........................................#..
.................................................................................#...................#......................................
.................................................#..............#...........#......................................................#........
................#............#.....#........................................................................................................
.....#......................................#...............................................................................................
.......................................................#.....#.........................#.........#...................#......................
................................#....................................................................................................#......
.....................#.........................................................................................#............................
............#.......................................#...............#..........#....................#.......................................
.........................................................................................#..................................................
................................................#..............................................#.......................................#....
...#......................#...............................................................................................#......#..........
...........................................................#.................#.......#......................................................
..........................................................................................................#...........#.....................
......................................#........................#.....#.......................#................................#......#......
...................#..............................................................................#.........................................
.#..........................................................................................................................................
.......................#......#...........................................#.........#...........................#..........#................
.............#...................................#....................................................#...................................#.
...................................#........#...............................................................................................
................................................................................................#...................#.......................
.................................................................................................................................#..........
.....................#......................................#................#.......#......................................................
#......#..................#..............................................................................#..............#...................
...........................................#.....................................................................#..........................
.............#......................#...........#......................................................................................#....
...................#.....................................#............#.....................................................................
.......................................................................................#.........#.....#.............#......................
...........................................................................#....................................................#...........
..................................#.............................#..............................................#............................
...............#..........#......................#..................................#.......................................#...............
........................................#...................................................................................................
...........................................................................................#............#...................................
.............................#...............................................#........................................................#.....
.............#................................#......#.........#......#............................#............#...........................
...#.....................................................................................................................#..................
.........................................................#...........................#.....................................................#
........#........................................#..................................................................#..............#........
#..........................#......#.....#................................................#..................................................
............................................................................................................................................
....................................................#........#.................................#.......................#....................
.................#..........................................................................................................................
.......................#....................#........................#.....................#...........#..........#.........................
.....#..............................#.......................................................................#................#............#.
..........................................................#...............#.................................................................
...........#.......#.....................#...........#.........#.................#.................#........................................""".split('\n')

def GetRowColExpension(data, ColList, RowList):
    l = len(Input2[0])
    h = len(Input2)
    i, j = 0, 0

    # Getting Columns that will be expended
    while i<l:
        if all([data[idx1][i] == '.' for idx1 in range(h)]):
            ColList.append(i)
        i+=1

    # Getting Rows that will be expended
    while j<h:
        if all([data[j][idx2] == '.' for idx2 in range(l)]):
            RowList.append(j)
        j+=1
    return RowList, ColList

coordonate_galaxie2 = []
for idx, line in enumerate(Input2):
    for galaxie in re.finditer(r'#', line):
        coordonate_galaxie2.append((idx, galaxie.start()))

Expension_Row = []
Expension_Col = []
Expension_Row, Expension_Col = GetRowColExpension(Input2, Expension_Col, Expension_Row)

Total_Distance2 = 0
T2 = 1
for galaxie in coordonate_galaxie2:
    for i in range(T2, len(coordonate_galaxie2)):
        Total_Distance2 += (abs(galaxie[0] - coordonate_galaxie2[i][0]) + abs(galaxie[1] - coordonate_galaxie2[i][1])) + sum([(galaxie[0]>Row and coordonate_galaxie2[i][0]<Row) or (galaxie[0]<Row and coordonate_galaxie2[i][0]>Row) for Row in Expension_Row])*999999 + sum([(galaxie[1]>Col and coordonate_galaxie2[i][1]<Col) or (galaxie[1]<Col and coordonate_galaxie2[i][1]>Col) for Col in Expension_Col])*999999
    T2 += 1

print("This is the supposed Total Distance 2 : ", Total_Distance2)