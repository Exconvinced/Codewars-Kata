intList = [-6, -3, -2, -1, 0, 1, 3, 4, 5,
           7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]


def solution(intList):
    newList, group = [], []

    for i in range(intList[0], intList[-1] + 2):
        if i in intList:
            group.append(str(i))
        else:
            if len(group) < 3:
                for k in group:
                    newList.append(str(k))
                del group[:]
            else:
                newList.append(f'{str(group[0])}-{str(group[-1])}')
                del group[:]

    return ','.join(newList)


solution(intList)
