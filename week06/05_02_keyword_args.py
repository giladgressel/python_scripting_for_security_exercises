## Write a function with keyword arguments
## your function can be a mix of positional and keyword arguments
## it must use a default value for the keyword argument.


def rectangle(length,width=10):
    """
    Input:
        length: int
        width: int, defaults to 10
        
    Returns:
        the area of the rectangle
    """
    return f"The area of the rectangle is {length*width} m2"

area1=rectangle(5)
print(area1)

