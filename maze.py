__author__ = 'agervail'
import time
import sys

count = 0


def print_maze():
    for line in maze:
        for c in line:
            print c,# + '\t',
        print ''


def isEmpty(car):
    return car not in ['E', '#', 'S', '*']


def explore_voisins(y, x, dist):
    global count
    count += 1
    r = [sys.maxint] * 4

    if x > 0 and isEmpty(maze[y][x - 1]):
        old = maze[y][x - 1]
        maze[y][x - 1] = str(dist) if old == ' ' else str(min(int(old), dist))
        if old == ' ' or int(old) > dist:
            r[0] = explore_voisins(y, x - 1, dist + 1)

    if y > 0 and isEmpty(maze[y - 1][x]):
        old = maze[y - 1][x]
        maze[y - 1][x] = str(dist) if old == ' ' else str(min(int(old), dist))
        if old == ' ' or int(old) > dist:
            r[1] = explore_voisins(y - 1, x, dist + 1)

    if x < X - 1 and isEmpty(maze[y][x + 1]):
        old = maze[y][x + 1]
        maze[y][x + 1] = str(dist) if old == ' ' else str(min(int(old), dist))
        if old == ' ' or int(old) > dist:
            r[2] = explore_voisins(y, x + 1, dist + 1)

    if y < Y - 1 and isEmpty(maze[y + 1][x]):
        old = maze[y + 1][x]
        maze[y + 1][x] = str(dist) if old == ' ' else str(min(int(old), dist))
        if old == ' ' or int(old) > dist:
            r[3] = explore_voisins(y + 1, x, dist + 1)

    if E in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        print 'found'
        return min(min(r), dist)
    else:
        return min(r)


with open('input_maze.txt', 'r') as f:
    X, Y = [int(i) for i in f.readline().split()]
    maze = []
    for line in f.readlines():
        s_in = line.find('S')
        if s_in != -1:
            S = (s_in, len(maze))
        e_in = line.find('E')
        if e_in != -1:
            E = (e_in, len(maze))
        maze.append([c for c in line.strip()])

print_maze()

x, y = S
dist = 1

before = time.time()
found = False
best = explore_voisins(y, x, dist)
after = time.time()
print_maze()

x, y = E
ar = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
while S not in ar:
    mini = sys.maxint
    for di in ar:
        v = maze[di[1]][di[0]]
        if isEmpty(v):
            if int(v) < mini:
                mini = int(v)
                x, y = di
    maze[y][x] = '*'
    ar = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

print 'nb_iteration : ', count
print 'time : ', after - before
print 'best_distance : ', best
for y, line in enumerate(maze):
    for x, c in enumerate(line):
        if isEmpty(c):
            maze[y][x] = ' '
print_maze()