import sys

def readfile():
  with open('input.txt') as f:
    lines = f.read().splitlines()
  return lines

def part_one():
  valid_passwd = 0
  lines = readfile()
  for line in lines:
    split_line = line.split(' ')
    lower_limit,upper_limit = split_line[0].split('-')
    lower_limit_int = int(lower_limit)
    upper_limit_int = int(upper_limit)
    occur = split_line[2].count(split_line[1].strip(':'))
    if occur < lower_limit_int:
      print ("number of occurences too low")
    elif occur > upper_limit_int:
      print ("number of occurences too high")
    else:
      valid_passwd += 1
  print (valid_passwd)

def part_two():
  valid_passwd = 0
  lines = readfile()
  for line in lines:
    split_line = line.split(' ')
    first_pos,last_pos = split_line[0].split('-')
    first_pos_int = int(first_pos) - 1
    last_pos_int = int(last_pos) - 1
    target_char = split_line[1].strip(':')
    target_string = split_line[2]
    if target_string[first_pos_int] == target_char and target_string[last_pos_int] != target_char:
      print("target char ", target_char, " found")
      valid_passwd += 1
    elif target_string[last_pos_int] == target_char and target_string[first_pos_int] != target_char:
      print("target char ", target_char, " found")
      valid_passwd += 1
    print(valid_passwd)

def main():
  if int(sys.argv[1]) == 1:
    part_one()
  elif int(sys.argv[1]) == 2:
    part_two()
main()