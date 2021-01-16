class stackNum:
    def __init__(self,args=[]):
        if type(args) != list:
            raise Exception("args must be a list")
        for i in args:
            if type(i) != int:
                raise Exception("elements in agrs must be integers")

        self._args = args
        self.top = len(self._args) - 1

    def __str__(self):
        return "<stack contains: " + str(self._args)  + ">"

    def push(self, x):
        self._args.append(x)
        self.top = len(self._args) - 1
    
    def pop(self):
        if self.top != -1:
            x = self._args.pop()
            self.top = len(self._args) - 1
            return x
        else:
            raise Exception("stack empty")

    def empty(self):
        return True if self.top == -1 else False

    def reverse(self):
        return stackNum(self._args[::-1])

    def copy(self):
        ls = [x for x in self._args]
        return stackNum(ls)
    
def print_board(ls):
    print(ls)
    for i in ls:
        lsi = [0] * len(ls)
        lsi[i] = 1
        print(*lsi)
    print()

def is_threatened(x1,y1,x2,y2):

    if x1 == x2:
        return True

    if y1 == y2:
        return True

    if abs((x2 - x1)/(y2 - y1)) == 1:
        return True

    return False

def board_is_safe(ls):

    ls_temp = ls.copy()

    counter = 0
    while not ls_temp.empty():
        pos_1 = (ls_temp.pop(), counter)

        ls_temp_temp = ls_temp.copy()

        inner_counter = counter + 1

        while not ls_temp_temp.empty():
            pos_2 = (ls_temp_temp.pop(), inner_counter)

            if is_threatened(*pos_1, *pos_2):
                return False

            inner_counter += 1

        counter += 1

    return True



def main(n):

    safe_ls = []
    ls = stackNum([0,0])
    flag = False
    while True:

        if board_is_safe(ls) and not flag:
            if ls.top == n - 1:
                temp = ls.copy()
                l = temp._args
                safe_ls.append(l)

            ls.push(0)
        else:

            if not ls.empty():
                x = ls.pop()
                x += 1
                if x < n:
                    ls.push(x)
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
