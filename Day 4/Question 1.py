## Print the nearest palindrome greater than given number
import sys
def nxt_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
s = int(input())
print(nxt_palindrome(s))
    
