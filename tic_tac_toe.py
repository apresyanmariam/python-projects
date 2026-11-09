import time
def x_o_game():
    board_list = [
        [" ", " ", " "], 
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    combinations = [
        [0, 0, 0, 1, 0, 2],
        [1, 0, 1, 1, 1, 2],
        [2, 0, 2, 1, 2, 2],
        [0, 0, 1, 0, 2, 0],
        [0, 1, 1, 1, 2, 1],
        [0, 2, 1, 2, 2, 2],
        [0, 0, 1, 1, 2, 2],
        [2, 0, 1, 1, 0, 2]
    ]
    comp_win = False
    count = 0

    def print_board(board):
        time.sleep(1)
        print(" | ".join(board[0]),"\n---------")
        print(" | ".join(board[1]),"\n---------")
        print(" | ".join(board[2]))

    print("Welcome to the Tic Tac Toe game!")
    print_board(board_list)
    
    
    while True:
        print("X's turn")
        row_id = int(input("enter the index of the row: "))
        col_id = int(input("enter the index of the column: "))

        while board_list[row_id][col_id] != " ":
            print("Invalid move, try again")
            print_board(board_list)
            row_id = int(input("enter the index of the row: "))
            col_id = int(input("enter the index of the column: ")) 
        board_list[row_id][col_id] = "X"   
        count += 1    
        print_board(board_list)


        if count > 2:
            if all(item == "X" for item in board_list[0]) or \
            all(item == "X" for item in board_list[1]) or \
            all(item == "X" for item in board_list[2]) or \
            all(item == "X" for item in [board_list[0][0], board_list[1][0], board_list[2][0]]) or \
            all(item == "X" for item in [board_list[0][1], board_list[1][1], board_list[2][1]]) or \
            all(item == "X" for item in [board_list[0][2], board_list[1][2], board_list[2][2]]) or \
            all(item == "X" for item in [board_list[0][2], board_list[1][1], board_list[2][0]]) or \
            all(item == "X" for item in [board_list[0][0], board_list[1][1], board_list[2][2]]): 
                print("X wins")
                break
        if count == 5:
            print("it's a tie")
            break

        print("computer's turn")
        if count >= 2:
            for cmb in combinations:
                if board_list[cmb[0]][cmb[1]] == "O" and \
                board_list[cmb[2]][cmb[3]] == "O" and \
                board_list[cmb[4]][cmb[5]] == " ":
                    board_list[cmb[4]][cmb[5]] = "O"
                    comp_win = True
                    break
                elif board_list[cmb[0]][cmb[1]] == "O" and \
                board_list[cmb[2]][cmb[3]] == " " and \
                board_list[cmb[4]][cmb[5]] == "O":
                    board_list[cmb[2]][cmb[3]] = "O"
                    comp_win = True                   
                    break
                elif board_list[cmb[0]][cmb[1]] == " " and \
                board_list[cmb[2]][cmb[3]] == "O" and \
                board_list[cmb[4]][cmb[5]] == "O":
                    board_list[cmb[0]][cmb[1]] = "O"
                    comp_win = True
                    break
            else:
                for cmb in combinations:
                    if board_list[cmb[0]][cmb[1]] == " " and \
                    board_list[cmb[2]][cmb[3]] == "X" and \
                    board_list[cmb[4]][cmb[5]] == "X":
                        board_list[cmb[0]][cmb[1]] = "O"
                        combinations.remove(cmb)
                        break
                    elif board_list[cmb[0]][cmb[1]] == "X" and \
                    board_list[cmb[2]][cmb[3]] == " " and \
                    board_list[cmb[4]][cmb[5]] == "X":
                        board_list[cmb[2]][cmb[3]] = "O"
                        combinations.remove(cmb)
                        break
                    elif board_list[cmb[0]][cmb[1]] == "X" and \
                    board_list[cmb[2]][cmb[3]] == "X" and \
                    board_list[cmb[4]][cmb[5]] == " ":
                        board_list[cmb[4]][cmb[5]] = "O"
                        combinations.remove(cmb)
                        break
                else:
                    for cmb in combinations:
                        if board_list[cmb[0]][cmb[1]] == "O" and \
                        board_list[cmb[2]][cmb[3]] == " " and \
                        board_list[cmb[4]][cmb[5]] == " ":
                            board_list[cmb[4]][cmb[5]] = "O"
                            break
                        elif board_list[cmb[0]][cmb[1]] == " " and \
                        board_list[cmb[2]][cmb[3]] == " " and \
                        board_list[cmb[4]][cmb[5]] == "O":
                            board_list[cmb[0]][cmb[1]] = "O"
                            break
                        elif board_list[cmb[0]][cmb[1]] == " " and \
                        board_list[cmb[2]][cmb[3]] == "O" and \
                        board_list[cmb[4]][cmb[5]] == " ":
                            board_list[cmb[4]][cmb[5]] = "O"
                            break
                    else:
                        filled = False
                        for row in range(3):
                            if filled:
                                break
                            for col in range(3):
                                if board_list[row][col] == " " and not filled:
                                    board_list[row][col] = "O"
                                    filled = True
                                    break
                                
        elif board_list[1][1] == "X":
            board_list[0][0] = "O"
        else:
            board_list[1][1] = "O"
        
        print_board(board_list)

        if comp_win:
            print("computer wins")
            break

x_o_game()