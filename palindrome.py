 '''A string is said to be palindrome if reverse of
 the string is same as string. 
 For example, “radar”  is palindrome'''
 
 
x=input("Enter the value: ")
w = "" 
for i in x: 
    w = i + w 
    if (x == w):
        print('True')