def readfile():
  with open('input.txt') as f:
    lines = f.readlines()
  return lines

max_bit_length = 36

def binary_to_decimal(bin):
  dec_value = 0
  for x in range(0,len(bin)):
    if bin[len(bin)-1-x] == '1':
      dec_value += 2**x
  return dec_value

def decimal_to_binary(dec):
  bin_value = []
  while dec:
    rest = dec %2
    bin_value.append(rest)
    dec = dec//2
  bin_value.reverse()
  bin_str =''
  for element in bin_value:
    bin_str+=str(element)
  print(type(bin_str))
  return bin_str

#Legger på riktig antall nuller for å lage en 36-bits streng
def add_leading_zeros(binary):
  bit_string = '0'*(max_bit_length-len(binary))
  for bit in binary:
    bit_string += bit
  return bit_string

# gir ut en 36-bits streng etter at masken er lagt på
def apply_mask(mask, value):
  result =''
  for x in range(0,len(mask)-1):
    if mask[x] == 'X':
      result += value[x]
    else:
      result+= mask[x]
  return result

def init_program():
  lines = readfile()
  init_dict = {}
  for line in lines:
    if 'mask' in line:
      mask = line.rsplit('= ')[1]
    else:
      memory_addr = line.split('[')[-1].split(']')[0]
      value = line.split('[')[-1].split(']')[1].rsplit('= ')[1]
      init_dict[memory_addr] = apply_mask(mask,add_leading_zeros(decimal_to_binary(int(value))))
  return get_sum_in_memory(init_dict)

def get_sum_in_memory(memory_dict):
  sum = 0
  for key,value in memory_dict.items():
    sum += binary_to_decimal(value)
  return sum

print(init_program())