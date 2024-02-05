
def find_combinations(total):
    combinations_amounts = []  #This is a variable that stores the current combination of coin counts.
                               # It's a list with six elements representing the counts of 100s, 50s, 25s, 10s, 5s, and 1s coins.
                               #[]是集合的意思
    for count_5 in range(total // 5 + 1):
        for count_10 in range(total // 10 + 1):
            for count_25 in range(total // 25 + 1):
                for count_50 in range(total // 50 + 1):
                    for count_100 in range(total // 100 + 1):
                        total_so_far = count_5 * 5 + count_10 * 10 + count_25 * 25 + count_50 * 50 + count_100 * 100
                        if total_so_far == total:
                            combinations_amounts.append([count_5,count_10,count_25,count_50,count_100])
                            print(combinations_amounts)
                            #.append(): This is a method (function) that belongs to lists in Python.
                            # It allows you to add an element to the end of a list.

    print("Total combination is")
    print(len(combinations_amounts))
    return combinations_amounts
find_combinations(200)
