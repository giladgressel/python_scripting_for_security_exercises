# write a recursive function to calculate the factorial

def factorial(n):
    """
    input: 
        n: int
    returns: 
        factorial of n
    
    reminder: factorial 8! is
    8*7*6*5*4*3*2*1
    """
    if n<=1: # This is a base case
        return 1
    
    return factorial(n-1)*n
    
for number in range (0,10):
    print(f"Factorial of {number} is {factorial(number)}")


    