# Exercise

# stage 1
# Write a program to count the number of strings where the string length is 2 or more
# sample list: ['aaaa', 'a', 'ab', 'abc', ]
# result : 3

target=['aaaa', 'a', 'ab', 'abc','India']
result=0

for x in target:
    
    len_x=len(x)
    if len_x>1:
        result+=1
        
print(result)



## Stage 2
# Now count the number of strings that have length 2 or more
# AND the first and last character are same from a given list of strings.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
