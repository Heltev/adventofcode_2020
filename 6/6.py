def readfile():
  with open('input.txt') as f:
    lines = f.read().splitlines()
  return lines

def gather_individual_answers_per_group():
  answers=[]
  temp_answer = []
  group_answers = ''
  lines = readfile()
  for line in lines:
    if line != '':
      temp_answer.append(line)
    elif line == '':
      answers.append(temp_answer)
      group_answers = ''
      temp_answer = []
  #One more add to catch last group
  answers.append(temp_answer)
  return answers

def gather_group_answers():
  answers=[]
  temp_answer = []
  group_answers = ''
  lines = readfile()
  for line in lines:
    if line != '':
      group_answers += line
    elif line == '':
      answers.append(group_answers)
      group_answers = ''
      temp_answer = []
  #One more add to catch last group
  answers.append(group_answers)
  return answers

def find_num_unique_yes(group_answers):
  answer_set = set()
  answer_set.update(group_answers)
  return len(answer_set)
  print("The set for string ", group_answers)
  print(answer_set)

def find_num_group_yes(group_answers):
  splitted_list = []
  temp_list = []
  for element in group_answers:
    splitted_list.append(list(element))
  return number_of_yes(splitted_list)

def number_of_yes(splitted_list):
  answer_dict = {}
  num_people_in_group = len(splitted_list)
  num_yes = 0
  for element in splitted_list:
    for character in element:
      if character in answer_dict:
        answer_dict[character] += 1
      elif character not in answer_dict:
        answer_dict[character] = 1

  for key,value in answer_dict.items():
    if value == num_people_in_group:
      num_yes += 1
  return num_yes

def find_sum_of_unique_yes():
  group_answers = gather_group_answers()
  num_unique_yes_per_group = []
  for line in group_answers:
    num_unique_yes_per_group.append(find_num_unique_yes(line))
  return sum(num_unique_yes_per_group)

def find_sum_of_group_yes():
  group_answers=gather_individual_answers_per_group()
  num_group_yes_per_group = []
  for element in group_answers:
    if len(element) > 0:
      num_group_yes_per_group.append(find_num_group_yes(element))
  return sum(num_group_yes_per_group)

print(find_sum_of_unique_yes())
print(find_sum_of_group_yes())