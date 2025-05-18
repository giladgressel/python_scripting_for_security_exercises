#Exercise

# Write a Python program to flatten a shallow list

#Sample Input: [[2,4,3],[1,5,6], [9], [7,9,0]]
#Output: [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

def flaten_list(list1):
    final_list=[]
    for i in list1:
        # final_list.extend(i) # We are appending each element of the iterable "i"
        final_list+=i
    return final_list
        
    
    
list1=[[2,4,3],[1,5,6], [9], [7,9,0]]
    
print(flaten_list(list1))