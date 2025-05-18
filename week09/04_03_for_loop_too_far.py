"""
Wrap the code below in a try - except
What is the correct exception to use?

Fix the error by "padding" the word with blank spaces (or - dashes) when the exception is hit.
"""

word = "abcde"
    
for i in range(12):
    try:
        # print(i+1,word[i],"\n")
        print(i+1,word[i:i+1])
 

    except Exception as e:
        print(e)
        print(i+1,"-")
        
    else: # If there is no exceptions, this block executes
        print(f"As per now, you have {i} letters")
    finally:
        print(f"Your final word is '{i},{word[0:i+1]}'")