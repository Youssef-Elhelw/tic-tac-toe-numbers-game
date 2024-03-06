# File: CS112_A1_T6_20230499.py

# Purpose: a simple numbers game with Tic-Tac-Toe board (3x3) player 1 will choose if they want to play with odd numbers or even numbers.
# each player will use a number just once and 
# fist player to reach an horizontal,vertical or diagonal line which numbers equal to 15 will win

# Author: Youssef Saleh Ahmed Mohammed Elhelw

# ID: 20230499

# Version: 1.0

# Date: 3/1/2024
start_again_exit=1
while start_again_exit:# if players want to play again or exit the game
    # prepaing the main 3 rows and then mix them together in one array
    row1=["X","X","X"]
    row2=["X","X","X"]
    row3=["X","X","X"]
    allrows=[row1,row2,row3]
    def draw_board():# drawing the board
        print("-------")
        print("|"+allrows[0][0]+"|"+allrows[0][1]+"|"+allrows[0][2]+"|")
        print("-------")
        print("|"+allrows[1][0]+"|"+allrows[1][1]+"|"+allrows[1][2]+"|")
        print("-------")
        print("|"+allrows[2][0]+"|"+allrows[2][1]+"|"+allrows[2][2]+"|")
        print("-------")
    # a function to check if any player win or not
    def check_win():
        if allrows[0][0]!='X'and allrows[0][1]!='X'and allrows[0][2]!='X':
            if int(allrows[0][0])+int(allrows[0][1])+int(allrows[0][2])==15:
                return True
        if allrows[1][0]!='X'and allrows[1][1]=='X'and allrows[1][2]!='X':
            if int(allrows[1][0])+int(allrows[1][1])+int(allrows[1][2])==15:
                return True
        if allrows[2][0]!='X'and allrows[2][1]!='X'and allrows[2][2]!='X':
            if int(allrows[2][0])+int(allrows[2][1])+int(allrows[2][2])==15:
                return True
        if allrows[0][0]!='X'and allrows[1][0]!='X'and allrows[2][0]!='X':
            if int(allrows[0][0])+int(allrows[1][0])+int(allrows[2][0])==15:
                return True 
        if allrows[0][1]!='X'and allrows[1][1]!='X'and allrows[2][1]!='X':
            if int(allrows[0][1])+int(allrows[1][1])+int(allrows[2][1])==15:
                return True
        if allrows[0][2]!='X'and allrows[1][2]!='X'and allrows[2][2]!='X':
            if int(allrows[0][2])+int(allrows[1][2])+int(allrows[2][2])==15:
                return True
        if allrows[0][0]!='X' and allrows[1][1]!='X'and allrows[2][2]!='X':
            if int(allrows[0][0])+int(allrows[1][1])+int(allrows[2][2])==15:
                return True
        if allrows[0][2]!='X'and allrows[1][1]!='X'and allrows[2][0]!='X':
            if int(allrows[0][2])+int(allrows[1][1])+int(allrows[2][0])==15:
                return True
            else:
                return False
    odd_list=[1,3,5,7,9]
    even_list=[0,2,4,6,8]
    p1_type=input("\nPlayer 1 choose your list\nA)Even List\nB)Odd List\n").lower()
    while p1_type!='a' and p1_type!='b': 
        p1_type=input("Please choose a valid choice\nA)Even List\nB)Odd List\n").lower()
    if p1_type =='a':
        print("\nPlayer 1 this ur list---> "+str(even_list))
        print("\nPlayer 2 this ur list---> "+str(odd_list))
        p1_type=even_list
        p2_type=odd_list
    else:
        print("\nPlayer 1 this ur list---> "+str(odd_list))
        print("\nPlayer 2 this ur list---> "+str(even_list))
        p1_type=odd_list
        p2_type=even_list
    row_list=["1",'2',"3"]
    coulmn_list=["1","2","3"]
    draw_board() #show the board to players so they can choose the row and column
    while (not check_win()):
        p1_row=input("Player 1 choose a row: ")
        while p1_row not in row_list:# check if player 1 chose an invalid row
            p1_row=input("Player 1 choose a valid row: "+"--->"+str(row_list)+"\n")
        p1_clmn=input("Player 1 choose a column: ")
        while p1_clmn not in coulmn_list:# check if player 1 chose an invalid column
            p1_clmn=input("Player 1 choose a valid column: "+"--->"+str(coulmn_list)+"\n")
        while allrows[int(p1_row)-1][int(p1_clmn)-1]!="X":
            print("\n***wrong position***\n")
            p1_row=input("Player 1 choose a row: ")
            while p1_row not in row_list:# check if player 1 chose an invalid row
                p1_row=input("Player 1 choose a valid row: "+"--->"+str(row_list)+"\n")
            p1_clmn=input("Player 1 choose a column: ")
            while p1_clmn not in coulmn_list:# check if player 1 chose an invalid column
                p1_clmn=input("Player 1 choose a valid column: "+"--->"+str(coulmn_list)+"\n")
        p1_choice=input("Now player 1 choose a number from your list-->"+str(p1_type)+"\n")
        while int(p1_choice) not in p1_type:# check if player 1 chose a number from their list
            p1_choice=input("Please choose a number from your list-->"+str(p1_type)+"\n")
        p1_type.remove(int(p1_choice))# remove the chosen number so player 1 can't insert it again
        allrows[int(p1_row)-1][int(p1_clmn)-1]=p1_choice
        draw_board()
        if(check_win()):# if "check_win" = true then player 1 won 
            print("\nplayer 1 won")
            break
        if ('X' not in row1)  and ('X' not in row2) and ('X' not in row3) :# is there is nomore boxes to play in then its a draw
            print("***Draw***")
            break
        # repeat the same thing with player 2
        p2_row=input("Player 2 choose a row: ")
        while p2_row not in row_list:# check if player 2 chose an invalid row
            p2_row=input("Player 2 choose a valid row: "+"--->"+str(row_list)+"\n")
        p2_clmn=input("Player 2 choose a column: ")
        while p2_clmn not in coulmn_list:# check if player 2 chose an invalid column
            p2_clmn=input("Player 2 choose a valid column: "+"--->"+str(coulmn_list)+"\n")
        while allrows[int(p2_row)-1][int(p2_clmn)-1]!="X":
            print("\n***wrong position***\n")
            p2_row=input("Player 2 choose a row: ")
            while p2_row not in row_list:# check if player 2 chose an invalid row
                p2_row=input("Player 2 choose a valid row: "+"--->"+str(row_list)+"\n")
            p2_clmn=input("Player 2 choose a column: ")
            while p2_clmn not in coulmn_list:# check if player 2 chose an invalid column
                p2_clmn=input("Player 2 choose a valid column: "+"--->"+str(coulmn_list)+"\n")
        p2_choice=input("Now player 2 choose a number from your list-->"+str(p2_type)+"\n")
        while int(p2_choice) not in p2_type:
            p2_choice=input("Please choose a number from your list-->"+str(p2_type)+"\n")
        p2_type.remove(int(p2_choice))
        allrows[int(p2_row)-1][int(p2_clmn)-1]=p2_choice
        draw_board()
        if(check_win()):
            print("\nplayer 2 won")
            break
    # ask user if they want to rematch or exit  
    c=input("\nthank you for playing my game\nA)Again \nB)Exit\n").lower()
    while c!='a' and c!='b':
        c=input("\nPlease choose a valid Choice\nA)Again \nB)Exit\n").lower()
    if c=='b':
        start_again_exit=0
        print("Bye :)")