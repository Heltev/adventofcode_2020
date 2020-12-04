import sys

def readfile():
  with open('input.txt') as f:
    lines =" ".join(line.strip() for line in f)
  return lines

def part_one():
  passport_dict = {}
  valid_passwords = {}
  substrings=['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
  passports = readfile()
  counter=0
  result=[]
  current_pass_result=[]
  current_passport = []
  lines=passports.split(" ")
  #Ordering data in dictionaries
  for line in lines:
    if len(line.strip()) == 0:
      passport_dict[counter]=current_passport
      counter+=1
      current_passport=[]
    if len(line) != 0: 
      current_passport.append(line)
  #Finding valid passwds by looping through dict and fields
  num_valid_passwords = 0
  num_correct_fields = 0
  for key,value in passport_dict.items():
    required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    num_correct_fields=0
    for substring in substrings:
      for element in value:
        if substring in element and substring in required_fields:
          required_fields.remove(substring)
          num_correct_fields +=1
        elif substring not in element and substring == 'cid':
          num_correct_fields +=1
    if len(required_fields) == 0:
      num_valid_passwords+=1
  return num_valid_passwords

def validate_birth_year(data):
  return 1920 <= int(data) <= 2002

def validate_issue_year(data):
  return 2010 <= int(data) <= 2020

def validate_expiration_year(data):
  return 2020 <= int(data) <= 2030

def validate_height(data):
  unit = data[-2:]
  if unit == 'cm':
    if len(data) != 5:
      return False
    height = int(data[0:3])
    return 150 <= height <= 193
  elif unit == 'in':
    if len(data) != 4:
      return False
    height = int(data[0:2])
    return 59 <= height <= 76

def validate_hair_color(data):
  allowed_chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
  if data[0] != '#':
    return False
  for character in data.split('#')[1]:
    if character not in allowed_chars:
      return False
  return True
  
def validate_eye_color(data):
  valid_eyecolors = {'amb', 'blu', 'brn', 'gry','grn','hzl','oth'}
  return data in valid_eyecolors

def validate_passport_id(data):
  if len(data) != 9:
    return False
  for element in data:
    if not element.isdigit():
      return False
  return True

def part_two():
  passport_dict = {}
  valid_passwords = {}
  substrings=['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
  passports = readfile()
  counter=0
  result=[]
  current_pass_result=[]
  current_passport = []
  lines=passports.split(" ")
  #Ordering data in dictionaries
  for line in lines:
    if len(line.strip()) == 0:
      passport_dict[counter]=current_passport
      counter+=1
      current_passport=[]
    if len(line) != 0: 
      current_passport.append(line)
  num_valid_passwords = 0
  num_correct_fields = 0
  for key,value in passport_dict.items():
    required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    num_correct_fields=0
    for substring in substrings:
      for element in value:
        if substring in element and substring in required_fields:
          if substring == 'byr':
            if(validate_birth_year(element.rpartition(':')[2])):
              required_fields.remove(substring)
          if substring == 'iyr':
            if(validate_issue_year(element.rpartition(':')[2])):
              required_fields.remove(substring)
          if substring == 'eyr':
            if(validate_expiration_year(element.rpartition(':')[2])):
              required_fields.remove(substring)
          if substring == 'hgt':
            if(validate_height(element.rpartition(':')[2])):
              required_fields.remove(substring)
          if substring == 'hcl':
            if(validate_hair_color(element.rpartition(':')[2])):
              required_fields.remove(substring)
          if substring == 'ecl':
            if(validate_eye_color(element.rpartition(':')[2])):
              required_fields.remove(substring)
          if substring == 'pid':
            if(validate_passport_id(element.rpartition(':')[2])):
              required_fields.remove(substring)
    if len(required_fields) == 0:
      num_valid_passwords+=1
  return num_valid_passwords

def main():
  if int(sys.argv[1]) == 1:
    print(part_one())
  elif int(sys.argv[1]) == 2:
    print(part_two())
main()