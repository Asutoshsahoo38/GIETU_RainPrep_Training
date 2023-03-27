#Input of a list in which patient id and Medicine type in present we have to find the maximum 
# medicine type
d = {'P':'Pediatrics','O':"Orthopedics",'E':"ENT"}
l = list(map(str,input().split(',')))
max = 0

for i in d.keys():
    x = l.count(i)
    if (x>max):
        max = x
        c = i
print(d[c])

#---------------------------------------------------------------------------

l = list(map(str,input().split(',')))
P = 0
O = 0
E = 0
for i in range(1,len(l),2):
    if(l[i] == 'P'):
        P +=1
    elif(l[i] == 'O'):
        O +=1
    elif(l[i] == 'E'):
        E += 1
if(P>O and P>E):
    print('Pediatrics')
elif(O>E and O>P):
    print("Orthopedics")
elif(E>O and E>P):
    print("ENT")
    
