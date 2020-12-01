def readfile():
  with open('input.txt') as f:
    lines = f.read().splitlines()
  #file = open('input.txt', 'r') 
  #lines = file.readlines() 
  numbers = [int(line) for line in lines]
  return numbers


def part_one():
  numbers = readfile()
  for first_num in numbers:
    for second_num in numbers:
      if first_num + second_num == 2020:
        print (first_num, " + ", second_num, " = 2020")
        print ("The answer is: ", first_num*second_num)
        break

def part_two():
  numbers = readfile()
  for first_num in numbers:
    for second_num in numbers:
      for third_num in numbers:
        if first_num + second_num + third_num == 2020:
          print (first_num, " + ", second_num, " + ", third_num, " = 2020")
          print ("The answer is: ", first_num*second_num*third_num)
          break

def main():
  part_one()
  part_two()
main()