from collections import defaultdict


def euler932(n: int):
    # 2025 = (20 + 25) ^ 2
    # concatenation of a and b => ab = (a + b) ^ 2
    # T(n) = sum of all 2025 numbers with n digits or less
    # T(4) = 5131
    # T(16) = ?
    # valid
    def is2025num(ab, a, b):
        # print('is2025num', a, b)
        return ab == (a + b) ** 2

    # last_digit = {0, 1, 5, 6}

    valid_splits = {
        0: {0},
        1: {0, 8},
        4: {4, 8},
        5: {0},
        6: {0, 8},
        9: {4, 8}
    }

    def find2025(num):
        snum = str(num)
        # if int(snum[-1]) not in last_digit:
        #     return False
        valid = valid_splits[int(snum[-1])]
        l = len(snum)
        start = max(1, l//2-1)
        end = min(l//2+2, len(snum))
        # for i in range(1, len(snum)):
        for i in range(start, end):
            if snum[i] != '0' and int(snum[i-1]) in valid:
                a = snum[:i]
                b = snum[i:]
                if is2025num(num, int(a), int(b)):
                    print(f'{a},{b},{num}')
                    return num
        return 0

    limit = 10 ** n
    i = 1
    total = 0  # 9^2

    while (sq := (i * i)) < limit:
    # # q = [0, 1, 5, 6]
    # # flag = True
    # # while flag:
    # #     q = [num + 10 for num in q]
    # #     for i in q:
    # #         sq = i * i
    #         if sq >= limit:
    #             flag = False
    #             break
            # print(sq)
        if find2025(sq):
            # print(sq)
            total += sq
        i += 1

    return total


print('result:', euler932(16))


