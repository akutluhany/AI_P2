#CloseAI, Team 1191
 
# nxn dimension 
n = 4
# m parts
m = 3
# Board
board = [["-"] * n for i in range(n)]
# If game is still going on
game_still_going = True
# Who won? Or tie?
winner = None
# Whose turn it is
currentPlayer = "X"

def display_board():
   for i in range(len(board)):
      for j in range(len(board[i])):
         print(board[i][j], end=' ')
      print()
    
def play_game():
   display_board()
   while game_still_going:
      # Handle a single turn of an arbitrary player
      handle_turn(currentPlayer)
      # Is game over?
      check_if_gameOver()
      # Switch to the other player
      flipPlayer()
   # Game over
   if winner == "X" or winner == "O":
      print(winner + " won.")
   elif winner == None:
      print("Tie.")
      
# Handle a single turn of an arbitrary player         
def handle_turn(player):
   positionX = input("Choose position: row= ")
   positionY = input("Choose position: cloumn= ")
   positionX = int(positionX)
   positionY = int(positionY)
   board[positionX][positionY] = player
   display_board()
   
# Is game over?
def check_if_gameOver():
   check_for_winner()
   check_if_tie()
   
# See if X or O won, or Tie    
def check_for_winner():

   global winner
   
   # Check rows
   row_winner = check_rows()
   # Check columns
   column_winner = check_columns()
   # Check diagonals
   diagonal_winner = check_diagonals()    
   if row_winner:
      winner = row_winner
   elif column_winner:
      winner = column_winner
   elif diagonal_winner:
      winner = diagonal_winner
   else:
      # No win
      winner = None
   return
   
#check rows   
def check_rows():

   global game_still_going
   #print("checking rows for X")
   count=0
   for i in range(len(board)):
      for j in range(len(board[i])):
         if board[i][j] == "X":
            count = count+1
            #print("i="+ str(i)+" j="+str(j)+ " count="+ str(count)+" m="+str(m))
            if count == m:
               game_still_going = False
               # return the winner: X
               return "X"
         else:
            count = 0
            #print("reset count for X to 0")
         #reset count for the new row   
         count = 0   
            
   #print("checking rows for 0")         
   count=0
   for i in range(len(board)):
      for j in range(len(board[i])):
         if board[i][j] == "O":
            count = count+1
            #print("i="+ str(i)+" j="+str(j)+ " count="+ str(count)+" m="+str(m))
            if count == m:
               game_still_going = False
               # return the winner: O
               return "O"
         else:
            count = 0
            #print("reset count for O to 0")
         #reset count for the new row   
         count = 0         
   return
   
# check columns for win: 
# either m consecuive Xs or m consecutive Os
def check_columns():

   global game_still_going
   
   count=0
   for j in range(len(board)):
      for i in range(len(board[j])):
         if board[i][j] == "X":
            count = count+1
            if count == m:
               game_still_going = False
               # return the winner: X
               return "X"
         else:
            count = 0
         #reset count for the new column   
         count = 0   
            
   count=0
   for j in range(len(board)):
      for i in range(len(board[j])):
         if board[i][j] == "O":
            count = count+1
            if count == m:
               game_still_going = False
               # return the winner: O
               return "O"
         else:
            count = 0
         #reset count for the new column   
         count = 0            
   return  
 
#check diagonals
def check_diagonals():
   #TODO
   # Primary diagonals
   # Check for "X"
   
   # Check for "O"  
      
   # Secondary diagonals
   # Check for "X"
   
   # Check for "O"  
        
   return
     
def check_if_tie():

   global game_still_going
   full = True
   
   for i in range(len(board)):
      for j in range(len(board[i])):
          if board[i][j] == "-":
             full = False
            
   if full == True:
      game_still_going = False
   return
   
#  If current player is X make it O or vice versa
def flipPlayer():

   global currentPlayer
   
   if currentPlayer == "X":
      currentPlayer = "O"
   elif currentPlayer == "O":
      currentPlayer = "X"
   return
   
play_game()   
