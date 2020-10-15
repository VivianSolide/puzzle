def puzzle_solver(pieces, width, height):
    result = []
    index = width - 1

    def convert(list):
        return tuple(list)

    def find_place(p):
        if result[0][0] != None and result[0][0][0] == p[0] and result[index][0][0][1] == p[0][0]:
            result[0][1] = p
        elif result[index][0] != None and result[index][0][0] == p[0] and result[0][0][1][1] == p[0][0]:
            result[index][1] = p
        if p[0][0] == None and p[1][0] == None:
            result[1][0] = p
            print(result)
        else:
            # print("pddd", p)
            find_place(p)
            pass

    for arr in range(height):
        temp = [None] * width
        result.append(temp)

    for p in pieces:
        if p[0][0] == None and p[0][1] == None and p[1][0] == None:
            # TOP LEFT
            result[0][0] = p
        elif p[0][0] == None and p[0][1] == None and p[1][1] == None:
            # TOP RIGHT
            result[0][index] = p
        elif p[0][0] == None and p[1][0] == None and p[1][1] == None:
            # BOTTOM LEFT
            result[index][0] = p
        elif p[0][1] == None and p[1][1] == None and p[1][0] == None:
            # BOTTOM RIGHT
            result[index][index] = p
        else:
            find_place(p)

    result = list(map(convert, result))

    return result
