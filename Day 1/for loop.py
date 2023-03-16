#for loop
n = 100
for i in range(n+1):
    if(i%2 ==0):
        print("even no :",i,end=" ")
    else:
        print("odd no :",i,end = " ")
print()        
#Using step values
#forward way
print("orward wise")
for i in range(1,n,2):
    print(i,end=" ")
print()

#reverse order
print("Reverse order")
for i in range(n,1,-1):
    print(i,end=" ")
print()
#99 , 98 --- 0
    
for i in range(99,0,-1):
    print(i,end=" ") 
