## return a list counting the character and numeric
def count_letter_digits(n):
    c = 0
    d = 0
    for i in n:
        if i.isdigit():
            d +=1
        elif i.isalpha():
            c += 1
    return [c,d]



print(count_letter_digits(input()))

## find the sum of pair from the list that is equal to n
def find_pairsof_number(l,n):
    c = 0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if(l[i]+l[j] == n):
                c += 1
    return c
    
l1 = [1,2,7,4,5,6,0,3]
n = int(input())
print(find_pairsof_number(l1,n))

##last element of list

def strreturn(s):
    if(len(s)<2):
        return -1
    elif(len(s)==2):
        return s+s
    else:
        return s[0:2]+s[-3:]
s = input()
print(strreturn(s))

##check for double of a number is equal to the give number or not

n = int(input())
double = n*2
l1 = list(str(n))
l2 = list(str(double))
l1.sort()
l2.sort()
if(l1 == l2):
    print("yes")
else:
    print('no')
    
## 1. find % of student more than avg
## 2. find the frequency
## 3. sort the mark
    
def cal_avg(l):
    c = 0
    avg = 18
    for i in l:
        if(i>=avg):
            c += 1
    per = c/10*100
    return per
def frequency(l):
    l1 = []
    for i in range(26):
        l1.append(l.count(i))
    return l1        
def sort_mark(l):
    l.sort()
    return l
l =[12,18,25,24,2,5,18,20,20,21]

print(cal_avg(l))
print(frequency(l))
print(sort_mark(l))

## Translating the english to other language using dictionary
def translate(book,s):
    l1 = []
    for i in s:
        l1.append(book[i])
    return str(l1)    
    

book = {
    'merry':'god',
    'christmas':'jul',
    'and':'och',
    'year':'ar',
    'new':'nytt',
    'happy':'gott'
}

s = list(map(str,input().split()))    
print(translate(book,s))


##find subArray

n1 = int(input())
n2 = int(input())
l1 = []
l2 = []

for i in range(n1,n2+1):
    l1.append(i)
    
    

for i in range(len(l1)+1):
    for j in range(i,len(l1)):
        l2.append(l1[i:j+1])
print(l2)
