"""
experiment with the function below
1. run the script as is. What prints out? Are you surprised?
2. is it possible to modify the function so that print(x) gets different results?
3. why is this happening?
"""
x = 100


def add_to_me(num):
    y = num + x
    x = 100
    return y


z = add_to_me(10)
print(z)

print(x)  # what do you think will print out?
