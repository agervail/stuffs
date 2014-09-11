__author__ = 'agervail'
import random
import bisect
import time
from Tkinter import *

evaporation_coef = 0.1
pheromon_quantity = 50
map_size = (10, 10)
begin = (5, 0)
end = (5, 9)
nb_ants = 50
nb_iteration = 1000


class Ant:
  def __init__(self, begin):
    self.pos = begin
    self.path = []
    self.path.append(begin)
    self.reached_goal = False
    self.rect = None
    self.pheromon = 0


class Map:
  def __init__(self, size, b, e):
    self.size = size
    self.begin = b
    self.end = e
    self.squares = []
    for i in range(size[0]):
      self.squares.append([])
      for j in range(size[1]):
        self.squares[i].append(1)

  def get_near_pos(self, pos):
    res = []
    for p in [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]:
      if 0 <= p[0] < self.size[0] and 0 <= p[1] < self.size[1]:
        res.append((p, self.squares[p[0]][p[1]]))
    return res

  def evaporate(self):
    for i in range(self.size[0]):
      for j in range(self.size[1]):
        if self.squares[i][j] - evaporation_coef >= 1:
          self.squares[i][j] -= evaporation_coef


class Window:
  def __init__(self, my_map, ants):
    self.master = Tk()
    width = my_map.size[0] * 20
    height = my_map.size[1] * 20
    self.w = Canvas(self.master, width=width, height=height)
    self.w.pack()
    # draw rects
    self.rects = []
    for i in range(my_map.size[0]):
      self.rects.append([])
      for j in range(my_map.size[1]):
        self.rects[i].append(self.w.create_rectangle(20 * i, 20 * j,
                                                     20 * (i + 1), 20 * (j + 1),
                                                     fill="#FFFFFF", outline='black'))
    #draw ants
    for la in ants:
      la.rect = self.w.create_rectangle(20 * la.pos[0] + 5, 20 * la.pos[1] + 5,
                                        20 * (la.pos[0] + 1) - 5, 20 * (la.pos[1] + 1) - 5,
                                        fill="#000", outline='black')
    self.w.pack()

  def update_rects(self, pos, pheromon):
    # pheromon /= 10
    #pheromon *= 10
    if pheromon > 255.0:
      color = '00'
    else:
      color = str(hex(255 - int(pheromon)))[2:]
    if len(color) < 2:
      color = '0' + color
    self.w.itemconfig(self.rects[pos[0]][pos[1]], fill="#FF" + color + "FF")


def choose_next(path, choices):
  fresh_choices = []
  for c, w in choices:
    if c not in path:
      fresh_choices.append((c, w))
  if not fresh_choices:
    fresh_choices = choices
  cumdist = []
  cur = 0
  for c, w in fresh_choices:
    cumdist.append(w + cur)
    cur += w
  x = random.random() * cumdist[-1]
  return fresh_choices[bisect.bisect(cumdist, x)][0]


my_map = Map(map_size, begin, end)

ants = []
for i in range(nb_ants):
  ants.append(Ant(my_map.begin))

my_win = Window(my_map, ants)


def compute():
  for i in range(nb_iteration):

    for ant in ants:
      # time.sleep(0.005)
      if ant.reached_goal:
        if len(ant.path) > 0:
          #Ant coming back home
          n = ant.path.pop()
          ant.pos = n
          #w.coords(ant.rect, n[0] * 20 + 5, n[1] * 20 + 5, (n[0]+1) * 20 - 5, (n[1]+1) * 20 - 5)
          my_map.squares[n[0]][n[1]] += ant.pheromon
        else:
          #Ant came back to home
          ant.reached_goal = False
      else:
        n = choose_next(ant.path, my_map.get_near_pos(ant.pos))
        #print n, ant.pos
        ant.pos = n
        ant.path.append(n)
        #print n
        #w.coords(ant.rect, n[0] * 20 + 5, n[1] * 20 + 5, (n[0]+1) * 20 - 5, (n[1]+1) * 20 - 5)
        #map.squares[n[0]][n[1]] += 0.6
        if n == my_map.end:
          ant.reached_goal = True
          ant.pheromon = pheromon_quantity / len(ant.path)
          my_win.w.itemconfig(ant.rect, fill='#f00')
      #w.coords(ant.rect, n[0] * 20 + 5, n[1] * 20 + 5, (n[0]+1) * 20 - 5, (n[1]+1) * 20 - 5)
      my_win.update_rects(n, my_map.squares[n[0]][n[1]])
    my_win.w.update()
    my_map.evaporate()
  for i in range(my_map.size[0]):
    for j in range(my_map.size[1]):
      n = (i, j)
      my_win.update_rects(n, my_map.squares[n[0]][n[1]])
  my_win.w.update()
  my_win.master.destroy()
  print ('OVER')


# my_win.w.pack()
my_win.master.after(0, compute)
my_win.master.mainloop()

current = begin
path = []
for _ in range(100):
  ne = my_map.get_near_pos(current)
  maxi = 0
  for n, w in ne:
    if w > maxi and n not in path:
      current = n
      maxi = w
  path.append(current)
  if current == end:
    break
print path
print len(path)