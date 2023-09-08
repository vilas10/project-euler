def euler48(n: int, m: int):
    # n = 1000, m = 10000000000
    # Using modulo principles:
    # 1. (a+b) mod m = a mod m + b mod m
    # 2. (ab) mod m = (a * b mod m) mod m
    # Applying these:

    # Step 1
    summation = 0

    def power_with_modulo(k, m):
        prod = 1
        for i in range(1, k + 1):
            prod *= k
            prod %= m

        return prod

    for i in range(1, n + 1):
        summation += power_with_modulo(i, m)
        summation %= m

    print(summation)
    return summation


def euler28(spiral_side_length: int):
    # Mathematical approach: diagonals starting from 1 following AP of differences
    # Sum of corners = 16n^2 + 4n + 4
    # Total Sum = 1 + Sigma(16n^2 + 4n + 4) = 1+(2/3)n(8n^2+15n+13)
    n = (spiral_side_length - 1) // 2

    diagonal_sum = int(1 + 2 * n * (8 * n * n + 15 * n + 13) / 3)
    # diagonal_sum = 1
    #
    # for n in range(1, loops):
    #     diagonal_sum += 16*n*n + 4*n + 4
    #
    print(diagonal_sum)
    return diagonal_sum


def euler24(permute_count: int, s: str):
    count = [0]  # (No of permutations performed, output string)
    result = []
    chars = list(s)  # Characters to be permuted
    n = len(s)  # No of characters in permutation
    included = [False for _ in range(len(s))]
    curr_state = []

    def permute(chars, n, depth, curr_state, included, count, result):
        if depth == n:
            count[0] += 1
            if count[0] == permute_count:
                result.append("".join(curr_state))
        else:
            for i in range(n):
                if not included[i]:
                    curr_state.append(chars[i])
                    included[i] = True
                    permute(chars, n, depth + 1, curr_state, included, count, result)
                    if len(result) > 0:
                        return
                    curr_state.pop()
                    included[i] = False

    permute(chars, n, 0, curr_state, included, count, result)

    print(result[0])
    return result[0]


def euler49(n: int):
    primes = primes_below(n)
    four_digit_primes = [p for p in primes if 1000 < p < 10000]
    print("count: ", len(four_digit_primes))
    print("primes: ", four_digit_primes)
    ap_primes = []
    for i in range(len(four_digit_primes) - 2):
        for j in range(i + 2, len(four_digit_primes)):
            sum_of_primes = four_digit_primes[i] + four_digit_primes[j]
            if sum_of_primes & 1 == 0:
                mean = sum_of_primes // 2

                if mean in four_digit_primes:
                    if sorted(str(four_digit_primes[i])) == sorted(str(four_digit_primes[j])) == sorted(str(mean)):
                        ap_primes.append(str(four_digit_primes[i]) + str(mean) + str(four_digit_primes[j]))

    print(ap_primes)

    return ap_primes[1]


def euler50(n: int):
    primes = primes_below(n)
    print(len(primes))

    # print(primes)

    primes_set = set(primes)
    longest = 2
    length = 1
    for i in range(len(primes) - 1):
        sum_of_cons_primes = primes[i]

        for j in range(i + 1, len(primes)):
            sum_of_cons_primes += primes[j]

            if sum_of_cons_primes > primes[-1]:
                break

            if sum_of_cons_primes in primes_set:
                if length <= j - i + 1:
                    length = j - i + 1
                    longest = sum_of_cons_primes

    print(length, longest)

    return longest


def divisors_of_all_numbers(n):
    primes = []
    divisors = [{}, {1}]
    for num in range(2, n + 1):
        divs = {1, num}
        prime = True
        for p in primes:
            if p * p > num:
                break

            if num % p == 0:
                prime = False
                # get divisors of both p and num // p
                div = divisors[num // p]
                # multiply div1 divisors with p
                newdiv = [d * p for d in div]
                divs.update(div)
                divs.update(newdiv)
                break

        divisors.append(divs)

        if prime:
            primes.append(num)

    return divisors


def primes_below(n):
    primes = []

    for num in range(2, n + 1):
        prime = True
        for p in primes:
            if p * p > num:
                break

            if num % p == 0:
                prime = False
                break

        if prime:
            primes.append(num)

    return primes


def euler23(n: int):
    primes = []
    divisors = [{}, {1}]
    abundant_sums = set()

    for num in range(2, n + 1):
        divs = {1, num}
        prime = True
        for p in primes:
            if p * p > num:
                break

            if num % p == 0:
                prime = False
                # get divisors of both p and num // p
                div = divisors[num // p]
                # multiply div1 divisors with p
                newdiv = [d * p for d in div]
                divs.update(div)
                divs.update(newdiv)
                break

        divisors.append(divs)

        if prime:
            primes.append(num)
        # as per requirements divisor sum should exclude the number itself
        div_sum = sum(divs) - num
        if div_sum > num:
            abundant_sums.add(num)

    # print(len(abundant_sums))

    # finding numbers cannot be written as sum of abundant numbers below n
    def check_sum_of_two_abundant_numbers(num: int):
        for a in abundant_sums:
            if num - a in abundant_sums:
                return True

        return False

    non_abundant_sum = 0
    for num in range(1, n + 1):
        non_abundant_sum += num if not check_sum_of_two_abundant_numbers(num) else 0

    print(non_abundant_sum)

    return non_abundant_sum


def euler17(n: int):
    letter_map = {
        1: 3,
        2: 3,
        3: 5,
        4: 4,
        5: 4,
        6: 3,
        7: 5,
        8: 5,
        9: 4,
        10: 3,
        11: 6,
        12: 6,
        13: 8,
        14: 8,
        15: 7,
        16: 7,
        17: 9,
        18: 8,
        19: 8,
        20: 6,
        30: 6,
        40: 5,
        50: 5,
        60: 5,
        70: 7,
        80: 6,
        90: 6,
        100: 7,
        1000: 8
    }

    i, count = 1, 0
    first9 = 0
    first99 = 0
    while i <= n:
        if i < 20:
            if i == 10:
                first9 = count

            count += letter_map.get(i)
            i += 1
        elif i < 100:
            tenths = i // 10
            count += (letter_map.get(tenths * 10) * 10 + first9)
            i += 10
        elif i < 1000:
            if i == 100:
                first99 = count

            hundredths = i // 100
            count += ((letter_map.get(hundredths) + letter_map.get(100) + 3) * 100 + first99 - 3)
            i += 100
        elif i == 1000:
            thousands = i // 100
            count += (letter_map.get(thousands) + letter_map.get(1000))
            i += 1

        print(i - 1, count)

    print(count)
    return count


def euler11(n: int):
    f = open("p011_grid.txt", "r")
    grid = []

    for line in f:
        grid.append([int(num) for num in line.split(" ")])

    if len(grid) < n or len(grid[0]) < n:
        return 0

    prod = [[[1 for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]

    max_product = -1
    for i in range(len(prod)):
        for j in range(len(prod[i])):
            for k in range(n):

                # 0 for horizontal product
                if j - k >= 0:
                    prod[i][j][0] *= grid[i][j - k]

                # 1 for vertical product
                if i - k >= 0:
                    prod[i][j][1] *= grid[i - k][j]

                # 2 for diagonal product
                if i - k >= 0 and j - k >= 0:
                    prod[i][j][2] *= grid[i - k][j - k]

            max_product = max(max_product, prod[i][j][0], prod[i][j][1], prod[i][j][2])

    for i in range(len(prod)):
        for j in range(len(prod[i]) - 1, -1, -1):
            for k in range(n):
                # 3 for reverse diagonal product
                if i - k >= 0 and j + k <= len(prod[i]) - 1:
                    prod[i][j][3] *= grid[i - k][j + k]

            max_product = max(max_product, prod[i][j][3])

    # print(prod)
    print(max_product)

    return max_product


def euler22():
    f = open("p022_names.txt", "r")
    names = [name[1:-1] for name in f.read().split(",")]
    names.sort()

    name_score = 0
    for i, name in enumerate(names):
        score = sum([ord(c) - ord('A') + 1 for c in name])
        name_score += score * (i + 1)

    print(name_score)
    return name_score


def euler25(digits: int):
    f1 = [1]
    f2 = [1]
    f3 = []
    term = 2

    def add_lists(l1, l2):
        result = []
        i, c = 0, 0
        while i < len(l1) or i < len(l2):
            s = l2[i] + c

            if i < len(l1):
                s += l1[i]

            c = s // 10
            result.append(s % 10)
            i += 1

        if c > 0:
            result.append(c)

        return result

    while len(f3) < digits:
        f3 = add_lists(f1, f2)
        f1 = f2
        f2 = f3

        # print(f3)
        term += 1

    print("Term: ", term)
    return term


def euler19():
    day = 1
    year = 1900
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sun = 0

    def leapyear(y: int):
        return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

    for y in range(1900, 2001):
        for m in range(len(months)):
            if y > 1900 and day == 0:
                sun += 1

            day = (day + months[m]) % 7

            if m == 1 and leapyear(y):
                day = (day + 1) % 7

    print(sun)


def euler20(num):
    fact = [1]

    for n in range(1, num+1):
        f = []
        c = 0
        for m in reversed(fact):
            prod = m * n + c
            c = prod // 10
            f.insert(0, prod % 10)

        fact = ([int(d) for d in str(c)] if c > 0 else []) + f

    print("".join([str(d) for d in fact]), "sum", sum(fact))


def euler21(n: int):
    primes = []
    divisor_sum_pairs = set()
    divisors = [{}, {1}]
    amicables = []
    # print(divisors)

    for num in range(2, n + 1):
        divs = {1, num}
        prime = True
        for p in primes:
            if num % p == 0:
                prime = False
                # get divisors of both p and num // p
                div = divisors[num // p]
                # multiply div1 divisors with p
                newdiv = [d * p for d in div]
                divs.update(div)
                divs.update(newdiv)
                break

        divisors.append(divs)

        if len(divs) == 2:
            primes.append(num)
        # as per requirements divisor sum should exclude the number itself
        div_sum = sum(divs) - num
        pair = str(num) + "-" + str(div_sum)
        if pair in divisor_sum_pairs:
            amicables.extend([num, div_sum])

        divisor_sum_pairs.add(str(div_sum) + "-" + str(num))

    amicable_sum = sum(amicables)

    print("amicable numbers: ", amicables)
    print("amicable numbers sum: ", sum(amicables))

    return amicable_sum


def euler30(power):
    powers = [n ** power for n in range(10)]
    result = 0
    for n in range(2, 1000000):
        total = sum(powers[int(c)] for c in str(n))
        if total == n:
            print('digit fifth power sum', n)
            result += n

    return result
