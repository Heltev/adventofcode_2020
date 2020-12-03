import sys

def readfile():
  with open('input.txt') as f:
    lines = f.read().splitlines()
  return lines

def part_one():
  grid = readfile()
  trees=0
  x,y=0,0
  for line in grid:
    print(y)
    if line[x] == '#':
      print("tree")
      trees+=1
      #line[x] = 'X'
    else:
      print("Not tree")
      #line[x] = 'O'
    x+=3
    y+=1
    if x>30:
      x-=31
  for line in grid:
    print(line)
  print(trees)

def part_two(x_slope, y_slope):
  grid = readfile()
  trees=0
  x,y=0,0
  for line in grid:
    #print(y)
    if line[x] == '#':
      #print("tree")
      trees+=1
      #line[x] = 'X'
    else:
      print("Not tree")
      #line[x] = 'O'
    x+=x_slope
    y+=1
    if x>30:
      x-=31
  #for line in grid:
    #print(line)
  print(trees)

def part_two_trick(x_slope, y_slope):
  grid = readfile()
  trees=0
  x,y=0,0
  for line in grid:
    if y % 2 != 0:
      fake = True
    elif y % 2 == 0:
      fake=False
    #print(y)
    if line[x] == '#' and not fake:
      #print("tree")
      trees+=1
      #line[x] = 'X'
    else:
      print("Not tree")
      #line[x] = 'O'
    x+=x_slope
    if fake:
      x-=x_slope
    y+=1
    if x>30:
      x-=31
  #for line in grid:
    #print(line)
  print(trees)

#def part_two(x_slope, y_slope):
#  grid = readfile()
#  trees=0
#  x,y=0,0
#  for line in grid:
#    #print(y)
#    if line[x] == '#':
#      #print("tree")
#      trees+=1
#      #line[x] = 'X'
#    else:
#      continue
#      print("Not tree")
#      #line[x] = 'O'
#    x+=x_slope
#    y+=1
#    if x>30:
#      x-=31
#  #for line in grid:
#    #print(line)
#  
#  print("X slope = ", x_slope, " gives: ", trees, "trees")
#
def main():
  if int(sys.argv[1]) == 1:
    part_one()
  elif int(sys.argv[1]) == 2:
    #part_two(1,1)
    #part_two(3,1)
    #part_two(5,1)
    #part_two(7,1)
    part_two_trick(1,2)
main()