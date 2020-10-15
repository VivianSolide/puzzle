def puzzle_solver(pieces, width, height):
    result = []

    # creating the index
    x_limit = width - 1
    y_limit = height - 1

    # drawing an empty puzzle
    for arr in range(height):
        temp = [None] * width
        result.append(temp)

    remaining = []
    # put the corners
    for p in pieces:
        if p[0][0] == None and p[0][1] == None and p[1][0] == None:
            # TOP LEFT
            result[0][0] = p
        elif p[0][0] == None and p[0][1] == None and p[1][1] == None:
            # TOP RIGHT
            result[0][x_limit] = p
        elif p[0][0] == None and p[1][0] == None and p[1][1] == None:
            # BOTTOM LEFT
            result[y_limit][0] = p
        elif p[0][1] == None and p[1][1] == None and p[1][0] == None:
            # BOTTOM RIGHT
            result[y_limit][x_limit] = p
        else:
            remaining.append(p)

    def fill_pieces(result, remaining):
        x = 0
        y = 0

        for i in range(width):
            if result[i][x] != None:
                for p in remaining:
                    if result[i][0][0][1] == p[0][0] and result[i][0][1][1] == p[1][0]:
                        result[i][1] = p
                        remaining.remove(p)

    fill_pieces(result,remaining)

    print(remaining)

    # def convert(list):
    #     # for el in list:
    #     return tuple(list)

    # result = list(map(convert, result))

    return result
