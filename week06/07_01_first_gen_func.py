## Write a generator that will produce a list of even numbers

# use a function


def list_of_even_nums(start, stop):
    """
    input:
        start: int
        stop: int
    returns:
        generator object

    Your function should create a generator object that will
    be the sequence of even numbers from start to stop
    Make sure to use the yield keyword!
    """


# use your generator
for i in list_of_even_nums(2, 11):
    print(i)
## should print out 2,4,6,8,10
