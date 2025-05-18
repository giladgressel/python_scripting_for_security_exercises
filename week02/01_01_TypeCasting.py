# Type Casting Exercise

a = 7

# 1. print the type of the variable
#   Convert integer variable to float and confirm the type cast worked (print it out)

print(type(a))

f=float(a)
print(type(f))


# 2. Now, Convert your float variable to string and print out the type

s=str(f)
print(type(s))


# 3. Finally, Convert your string variable back to integer and print it out (the type)
a=float(s)
print(type(a))
a=int(a)
print(type(a))
 
a='10.5'
print(type(a))

a=8*"ha "
print(a)
