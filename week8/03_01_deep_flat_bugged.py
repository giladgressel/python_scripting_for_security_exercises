# debug this code
# I broke all kinds of things. NOTHING is safe !!!


# Make your list flatten code do a DEEP flatten and account for other datatypes

hard_nested_list = [
    [1, 2, [1, [1, 2], 2], 3, 4],
    [5, 6],
    [7, 8, 9],
    "shiva",
    10,
    [1, 2, [8, 9,], "Devi"],
    10.0,
    (1, 2),
]

# should get back
# [1, 2, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 'shiva', 10, 1,2,8,9, "Devi", 10.0, 1, 2]

many_nests = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", "h"]
# should get back
# ['a', 'bb', 'ccc', 'ddd', 'ee', 'ff', 'g', 'h']

final_list = []
while True:
    for element in hard_nested_list:
        if isinstance(element, (list, tuple, str)):
            final_list.append(element)
        elif isinstance(element, (int, float, str)):
            final_list.append(element)  # string,

    for elem in final_list:
        if isinstance(element, (tuple, list)):
            hard_nested_list = []
            final_list = hard_nested_list
            break  # the else below will not execute, we repeat the while loop
    else:  # no break!!! only executes if for loop finishes
        break

