def readfile():
  with open('input.txt') as f:
    lines = f.read().splitlines()
  return lines


def binary_sort_FB(row_chars):
  row_binary =[]
  for element in row_chars:
    if element == 'F':
      row_binary.append(0)
    elif element =='B':
      row_binary.append(1)
  return row_binary

def binary_sort_LR(col_chars):
  col_binary =[]
  for element in col_chars:
    if element == 'L':
      col_binary.append(0)
    elif element =='R':
      col_binary.append(1)
  return col_binary

def find_seat_col(col):
  col_binary = binary_sort_LR(col)
  seat_col = 0
  for x in range (0,len(col_binary)):
    if col_binary[len(col_binary)-1 -x]:
      seat_col += 2**x
  return seat_col

def find_seat_row(row):
  row_binary = binary_sort_FB(row)
  seat_row = 0
  for x in range (0,len(row_binary)):
    if row_binary[len(row_binary)-1 -x]:
      seat_row += 2**x
  return seat_row

def find_missing_id(seat_ids):
  lowest_id = min(seat_ids)
  highest_id = max(seat_ids)
  num_ids = len(seat_ids)
  for x in range(0,num_ids-1):
    if x+80 not in seat_ids:
      return ("The missing ID is ", x+80)

def find_highest_id():
  seat_rows = []
  seat_cols = []
  seat_ids = []
  lines = readfile()
  highest_id = 0
  for row in lines:
    seat_rows.append(find_seat_row(row[0:7]))
    seat_cols.append(find_seat_col(row[-3:]))
  for x in range(0,len(seat_rows)):
    seat_ids.append((seat_rows[x]*8) + seat_cols[x])
    if ((seat_rows[x]*8) + seat_cols[x]) > highest_id:
      highest_id = (seat_rows[x]*8) + seat_cols[x]
  print("Highest id: ",highest_id)

  print(find_missing_id(seat_ids))

find_highest_id()