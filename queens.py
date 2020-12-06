def copy_ls(ls):

    ls_temp = []
    for i in ls:
        ls_temp.append(i)

    return ls_temp

def reverse_ls(ls):
    ls_temp = []
    while len(ls) != 0:
        ls_temp.append(ls.pop())

    return ls_temp

def is_threatened(x1,y1,x2,y2):
    
    if x1 == x2:
        return True

    if y1 == y2:
        return True

    if abs((x2 - x1)/(y2 - y1)) == 1:
        return True

    return False


def print_board(ls):
    print(ls)
    for i in ls:
        lsi = [0] * len(ls)
        
        lsi[i] = 1

        print(*lsi)
    print()


def board_is_safe(ls):
    
    ls_temp = copy_ls(ls)

    counter = 0
    while len(ls_temp) != 0:
        pos_1 = (ls_temp.pop(), counter)

        ls_temp_temp = copy_ls(ls_temp)
        
        inner_counter = counter + 1

        while len(ls_temp_temp) != 0:
            pos_2 = (ls_temp_temp.pop(), inner_counter)
            
            if is_threatened(*pos_1, *pos_2):
                return False

            inner_counter += 1

        counter += 1

    return True



def main(n):
    
    board = [0] * n

    print_board(board)

    row_counter = 0
    while True:
        print_board(board)
        if board_is_safe(board):
            print_board(board)
            break

        ls_temp = []
        for i in range(row_counter):
            ls_temp.append(board.pop())
    
        ls_temp = reverse_ls(ls_temp)

        x = board.pop()
        if x == n-1:
            board.append(0)
            row_counter += 1
        else:
            board.append(x + 1)

        while len(ls_temp) != 0:
            board.append(ls_temp.pop())


if __name__ == "__main__":
    main(4)

