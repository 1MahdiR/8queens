def copy_ls(ls):

    ls_temp = []
    for i in ls:
        ls_temp.append(i)

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

    safe_ls = []
    ls = [0,0]
    flag = False
    while True:

        if board_is_safe(ls) and not flag:
            if (len(ls) == n):
                safe_ls.append(copy_ls(ls))

            ls.append(0)
        else:

            if len(ls) != 0:
                x = ls.pop()
                x += 1
                if x < n:
                    ls.append(x)
                else:
                    flag = True
                    continue

                flag = False
            else:
                return safe_ls


if __name__ == "__main__":

    ls = main(8)
    for i in range(len(ls)):
        print(i+1)
        print_board(ls[i])
