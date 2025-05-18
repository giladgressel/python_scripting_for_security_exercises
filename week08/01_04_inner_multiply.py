# write a function accepts as input an infinite amount of tuples
# it returns a list, where each element is the inner multiplication

# example input: (1,2), (2,2), (3,2), (4,5)
# output: [2,4,6,20]

def inner_multiplication(*inputs):
    result=[]
    for i,j in inputs:
        result.append(i*j)
    return(result)
    
a=inner_multiplication((1,2), (2,2), (3,2), (4,5))
print(a)

b=inner_multiplication((1,2), (2,2), (3,2), (4,5),[5,3.0],{4,2})
print(b)
