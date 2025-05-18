# Exercise

# Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there
# if you don't know an algorithm to check for primes
# ask Dr. Kurunandan Sir
# google it

#Check if a given number is prime (return True or False)

number=9
# number=int(input("Give me a number: "))

numbers_to_check=range(2,number)
# print(list(numbers_to_check)) -> [2, 3, 4, 5, 6, 7, 8, 9]

for each_number in numbers_to_check:

    k=number%each_number
    if k==0:
        print(f"{number} is not a prime number")
        break
        
    else:
        print(f"{number} is a prime number")

        

        

    

#Run the program in a range from 0 to 101 (so includes up to 100)

#Put on a list the prime numbers