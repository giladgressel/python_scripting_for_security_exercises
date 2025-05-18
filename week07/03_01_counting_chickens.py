"""
create a chicken class that has the following

# class attributes
time_of_day
number_of_eggs_laid

# instance attributes (uses the self variable)
breed
gender
weight
lays_eggs (boolean)

# methods
lay_egg --> this function should depend on time of day (chickens only lay eggs at night!),
it should also use random numbers to deterimine if laying the egg worked or not


## Create 100 instances of your chickens using a for loop

Use a for loop to update the time of day (go through each hour of the day)
within the loop have your chickens all try to lay eggs
Afterwards, print out how many total eggs were hatched -- for all chickens and individually.
What was the average number of eggs per chicken?
"""
import random
class Chicken:
    """This is a class that makes chickens"""
    
    times=["morning","afternoon","night"]
    
    time_of_day=random.choice(times)# Chooses randomly which time of the day it is
    number_of_eggs_laid=0
    
    def __init__(self,breed,gender,weight:float,lays_eggs:bool):
        self.breed=breed
        self.gender=gender
        self.weight=weight
        self.lays_eggs=lays_eggs
        
    def lay_egg(self):
        if self.lays_eggs==True and Chicken.time_of_day=="night":
            print(f"Egg layed")
            Chicken.number_of_eggs_laid+=1
        else:
            print(f"Egg can't be layed")
            
a1=Chicken(breed="farmer",gender="female",weight="2.5",lays_eggs=True)
a1.lay_egg()
print(Chicken.number_of_eggs_laid,Chicken.time_of_day)

        
        
    