# run the function below

my_list = [1, 2, 3]


def times_nums():
    for i in range(3):
        my_list.append(i * my_list[i])
    final_list = my_list
    return final_list


# run the above function.
f = remove_ints()
print(f)  # what prints out?

print(f"my list is:\n{my_list}")  # is this what you expected? What is happening?

### fix the above function so that it does not modify my_list!
