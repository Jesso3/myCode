def main():

  with open("tic_tac_toe_input.txt", "r") as file:
    input_data = file.readlines()
  xWins = 0
  oWins = 0
  ties = 0
  xMoves = []
  oMoves = []
  for row in input_data:
    row = row.split()
    for i in range(9):
      if i % 2 == 0:
        xMoves.append(int(row[i]))
        if check_combs(xMoves) == True:
           xWins += 1
           break
      else:
        oMoves.append(int(row[i]))
        if check_combs(oMoves) == True:
           oWins += 1
           break
    if check_combs(oMoves) == False and check_combs(xMoves) == False:
       ties += 1
    xMoves = []
    oMoves = []
  print(xWins,oWins,ties)
  print(xWins*oWins*ties)

def check_combs(moves):
  if (1 in moves and 4 in moves and 7 in moves) or (2 in moves and 5 in moves and 8 in moves) or (3 in moves and 6 in moves and 9 in moves) or (1 in moves and 2 in moves and 3 in moves) or (4 in moves and 5 in moves and 6 in moves) or (7 in moves and 8 in moves and 9 in moves) or (1 in moves and 5 in moves and 9 in moves) or (3 in moves and 5 in moves and 7 in moves):
    return True
  return False

main()