def puzzle_solver(pieces, width, height):
    result = []
    # creating the index
    x_limit = width - 1
    y_limit = height - 1

    # drawing an empty puzzle
    for arr in range(height):
        temp = [""] * width
        result.append(temp)

    remaining = []
    # put the corners
    for p in pieces:
        if p[0][0] == None and p[0][1] == None and p[1][0] == None:
            result[0][0] = p
        elif p[0][0] == None and p[0][1] == None and p[1][1] == None:
            result[0][x_limit] = p
        elif p[0][0] == None and p[1][0] == None and p[1][1] == None:
            result[y_limit][0] = p
        elif p[0][1] == None and p[1][1] == None and p[1][0] == None:
            result[y_limit][x_limit] = p
        else:
            remaining.append(p)

    def fill_pieces(result, remaining):

        while len(remaining) > 0:
            for p in remaining:
                north = p[0]
                west = (p[0][0], p[1][0])

                def x_solving(result, index):
                    for i in range(len(result[index]) - 1):
                        if result[index][i] != '':
                            check = (result[index][i][0][1],
                                     result[index][i][1][1])
                            if check == west:
                                result[index][i + 1] = p
                                try:
                                    remaining.remove(p)
                                    return True
                                except ValueError:
                                    break

                def y_solving(result, index):
                    for i in range(1, height - 1):
                        if result[index][i] != '':
                            check = (result[index][i][1])
                            if check == north:
                                result[i][index] = p
                                try:
                                    remaining.remove(p)
                                    return True
                                except ValueError:
                                    break

                for xxx in range(max(height, width)):
                    x_solving(result, xxx)
                    y_solving(result, xxx)


    fill_pieces(result, remaining)

    answer = []
    for res in result:
        list = []
        for r in res:
            list.append(r[2])
        answer.append(tuple(list))

    print(answer)

    return answer
