def readfile():
  with open('input.txt') as f:
    lines = f.read().splitlines()
  return lines

def is_empty(seat_state):
  if seat_state == 'L':
    return True
  elif seat_state == '#':
    return False

def get_seat_state(row,seat):
  return seats[row][seat]

seats = readfile()
#tolerance = 5
num_rows = len(seats)
num_cols = len(seats[0])

def find_occupied_seats(rules):
  global seats
  if rules == 'adjacency':
    tolerance = 4
  elif rules == 'vision':
    tolerance = 5
  seats_changed = 0
  occupied_seats = 0
  still_state = False
  seat_empty = False
  seat_should_change = False
  while not still_state:
    new_seating = [ [ 0 for i in range(num_cols) ] for j in range(num_rows) ]
    for row in range(0,num_rows):
      for seat in range(0,num_cols):
        if is_seat(row,seat):
          seat_empty = is_empty(seats[row][seat])
          if rules == 'adjacency':
            neighbour_seat_state = get_adjacent_seat_state(row,seat,is_corner(row,seat), is_edge(row,seat))
          elif rules == 'vision':
            neighbour_seat_state = get_visible_seat_state(row,seat)
          seat_should_change = should_change(seat_empty, neighbour_seat_state,tolerance)
          if seat_should_change:
            seats_changed +=1
            new_seating[row][seat] = change_occupied_state(row,seat)
          else:
            new_seating[row][seat] = get_seat_state(row,seat)
        elif not is_seat(row,seat):
          new_seating[row][seat]= '.'
    seats = new_seating
    #print(seats_changed)
    if seats_changed == 0:
      still_state = True
    seats_changed=0
  
  for row in seats:
    for seat in row:
      if seat == '#':
        occupied_seats +=1
  return occupied_seats
  

def should_change(is_empty, adj_seat_state, tolerance):
  #print(tolerance)
  occupied_seats = 0
  if is_empty:
    return sum(adj_seat_state) == len(adj_seat_state)
  elif not is_empty:
    for element in adj_seat_state:
      if not element:
        occupied_seats +=1
    return occupied_seats >= tolerance

def change_occupied_state(seat_row, seat_col):
  if seats[seat_row][seat_col] == 'L':
    return '#'
  elif seats[seat_row][seat_col] == '#':
    return 'L'
  return new_seating


def is_seat(seat_row,seat_col):
  if seats[seat_row][seat_col] == '.':
    return False
  else:
    return True

def is_corner(seat_row,seat_col):
  if (seat_row == 0 or seat_row == num_rows-1) and (seat_col == 0 or seat_col == num_cols-1):
    return True
  else:
    return False

def is_edge(seat_row,seat_col):
  if seat_row == 0 or seat_row == num_rows-1 or seat_col == 0 or seat_col == num_cols-1:
    return True
  else: 
    return False


def get_adjacent_seat_state(seat_row, seat_col, is_corner, is_edge):
  seat_states = []
  for adj_seat in get_adjacent_seat_pos(seat_row,seat_col, is_corner, is_edge):
    if is_seat(adj_seat[0],adj_seat[1]):
      empty = is_empty(seats[adj_seat[0]][adj_seat[1]])
      seat_states.append(empty)
  return seat_states

def get_visible_seat_state(seat_row, seat_col):
  seat_states = []
  for visbl_seat in get_visible_seat_pos(seat_row,seat_col):
    if visbl_seat:
      if is_seat(visbl_seat[0],visbl_seat[1]):
        empty = is_empty(seats[visbl_seat[0]][visbl_seat[1]])
        seat_states.append(empty)
  return seat_states

def get_visible_seat_pos(seat_row,seat_col):
  return get_visible_diagonal_north_west(seat_row,seat_col) +get_visible_diagonal_north_east(seat_row,seat_col) +get_visible_diagonal_south_east(seat_row,seat_col) +get_visible_diagonal_south_west(seat_row,seat_col) +get_visible_left_seat(seat_row,seat_col) +get_visible_right_seat(seat_row,seat_col) +get_visible_above_seat(seat_row,seat_col) +get_visible_below_seat(seat_row,seat_col) 

def get_visible_above_seat(seat_row,seat_col):
  above_seat = []
  check_row = seat_row-1
  check_col = seat_col
  while check_row >= 0:
    if is_seat(check_row,check_col):
      above_seat.append((check_row,check_col))
      return above_seat
    check_row -= 1
  return above_seat
  
def get_visible_below_seat(seat_row,seat_col):
  below_seat = []
  check_row = seat_row+1
  check_col = seat_col
  while check_row < num_rows:
    if is_seat(check_row,check_col):
      below_seat.append((check_row,check_col))
      return below_seat
    check_row += 1
  return below_seat

def get_visible_left_seat(seat_row,seat_col):
  left_seat = []
  check_row = seat_row
  check_col = seat_col-1
  while check_col >= 0:
    if is_seat(check_row,check_col):
      left_seat.append((check_row,check_col))
      return left_seat
    check_col -= 1
  return left_seat

def get_visible_right_seat(seat_row,seat_col):
  right_seat = []
  check_row = seat_row
  check_col = seat_col+1
  while check_col < num_cols:
    if is_seat(check_row,check_col):
      right_seat.append((check_row,check_col))
      return right_seat
    check_col += 1
  return right_seat

def get_visible_diagonal_north_west(seat_row,seat_col):
  diag_seat = []
  check_row = seat_row-1
  check_col = seat_col-1
  while check_row >= 0 and check_col >= 0:
    if is_seat(check_row,check_col):
      diag_seat.append((check_row,check_col))
      return diag_seat
    check_row -= 1
    check_col -= 1
  return diag_seat
  
def get_visible_diagonal_north_east(seat_row,seat_col):
  diag_seat = []
  check_row = seat_row-1
  check_col = seat_col+1
  while check_row >= 0 and check_col < num_cols:
    if is_seat(check_row,check_col):
      diag_seat.append((check_row,check_col))
      return diag_seat
    check_row -= 1
    check_col +=1
  return diag_seat

def get_visible_diagonal_south_east(seat_row,seat_col):
  diag_seat = []
  check_row = seat_row+1
  check_col = seat_col+1
  while check_row < num_rows and check_col < num_cols:
    if is_seat(check_row,check_col):
      diag_seat.append((check_row,check_col))
      return diag_seat
    check_row += 1
    check_col +=1
  return diag_seat

def get_visible_diagonal_south_west(seat_row,seat_col):
  diag_seat = []
  check_row = seat_row+1
  check_col = seat_col-1
  while check_row < num_rows and check_col >= 0:
    if is_seat(check_row,check_col):
      diag_seat.append((check_row,check_col))
      return diag_seat
    check_row += 1
    check_col -=1
  return diag_seat
  

    


def get_adjacent_seat_pos(seat_row,seat_col, is_corner, is_edge):
  seats_over = []
  seats_side = []
  seats_under = []
  if not is_edge and not is_corner:
    seats_over.append((seat_row-1,seat_col-1))
    seats_over.append((seat_row-1,seat_col))
    seats_over.append((seat_row-1,seat_col+1))
    seats_side.append((seat_row,seat_col-1))
    seats_side.append((seat_row,seat_col+1))
    seats_under.append((seat_row+1,seat_col-1))
    seats_under.append((seat_row+1,seat_col))
    seats_under.append((seat_row+1,seat_col+1))
  elif is_edge and not is_corner:
    if seat_row == 0:
      seats_side.append((seat_row,seat_col-1))
      seats_side.append((seat_row,seat_col+1))
      seats_under.append((seat_row+1,seat_col-1))
      seats_under.append((seat_row+1,seat_col))
      seats_under.append((seat_row+1,seat_col+1))
    elif seat_row == num_rows-1:
      seats_over.append((seat_row-1,seat_col-1))
      seats_over.append((seat_row-1,seat_col))
      seats_over.append((seat_row-1,seat_col+1))
      seats_side.append((seat_row,seat_col-1))
      seats_side.append((seat_row,seat_col+1))
    elif seat_col == 0:
      seats_over.append((seat_row-1,seat_col))
      seats_over.append((seat_row-1,seat_col+1))
      seats_side.append((seat_row,seat_col+1))
      seats_under.append((seat_row+1,seat_col))
      seats_under.append((seat_row+1,seat_col+1))
    elif seat_col == num_cols-1:
      seats_over.append((seat_row-1,seat_col-1))
      seats_over.append((seat_row-1,seat_col))
      seats_side.append((seat_row,seat_col-1))
      seats_under.append((seat_row+1,seat_col-1))
      seats_under.append((seat_row+1,seat_col))
  elif is_corner:
    if seat_row == 0 and seat_col == 0:
      seats_side.append((seat_row,seat_col+1))
      seats_under.append((seat_row+1,seat_col))
      seats_under.append((seat_row+1,seat_col+1))
    elif seat_row == 0 and seat_col == num_cols-1:
      seats_side.append((seat_row,seat_col-1))
      seats_under.append((seat_row+1,seat_col-1))
      seats_under.append((seat_row+1,seat_col))
    elif seat_row == num_rows-1 and seat_col == 0:
      seats_over.append((seat_row-1,seat_col))
      seats_over.append((seat_row-1,seat_col+1))
      seats_side.append((seat_row,seat_col+1))
    elif seat_row == num_rows-1 and seat_col == num_cols-1:
      seats_over.append((seat_row-1,seat_col-1))
      seats_over.append((seat_row-1,seat_col))
      seats_side.append((seat_row,seat_col-1))

  return seats_over +seats_side + seats_under

print("Total number of occupied seats, adjacency: ",find_occupied_seats('adjacency'))
seats = readfile()
print("Total number of occupied seats, vision: ",find_occupied_seats('vision'))

