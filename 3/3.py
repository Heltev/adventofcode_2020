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
    if line[x] == '#':
      trees+=1
    x+=3
    y+=1
    if x>30:
      x-=31
  print(trees)

def part_two(x_slope, y_slope):
  grid = readfile()
  trees=0
  x,y=0,0
  for line in grid:
    if line[x] == '#' and y%y_slope == 0:
      trees+=1
    if y%y_slope == 0:
      x+=x_slope
    y+=1
    if x>30:
      x-=31
  return trees


def main():
  if int(sys.argv[1]) == 1:
    part_one()
  elif int(sys.argv[1]) == 2:
    trees=[]
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    for element in slopes:
      trees.append((part_two(element[0], element[1])))
    print(trees)  
main()