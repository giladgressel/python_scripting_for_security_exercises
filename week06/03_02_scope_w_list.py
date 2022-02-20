# run the function below

list_of_vowels = ["a", "e", "i", "o", "u"]


def check_for_vowels(string_to_count):
    """
    Function will count if all vowels occur within the string
    """
    for char in string_to_count:
        if char.lower() in list_of_vowels:
            list_of_vowels.remove(char)

    if len(list_of_vowels) == 0:  # all vowels were found, so all vowels removed
        return True
    else:
        return False  # not all vowels found something is still in the list


# run the above function.

print(check_for_vowels("sequoia"))  # should be true

## can you re-use the function?

print(check_for_vowels("The"))  # this should be False!

# what is wrong?

## try printing list_of_vowels
# print(list_of_vowels)
# why is it empty?

## Fix the function so this does not happen!
