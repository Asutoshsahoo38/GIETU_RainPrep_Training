## How many 5 and 1 rupees u have to give to complete the goal
## incomplete program
n1 = int(input("5 rupee"))
n2 = int(input("1 rupee"))
m = int(input())
if (m%5 ==0):
    result = m//5
    q = 0
    print(q,result)
    exit()
elif(m%5 != 0):
    q= m%5
    result = q*1 + (m-q)//5
    if(result == m):
        
        print(q,(m-q)//5)
    exit()
    
