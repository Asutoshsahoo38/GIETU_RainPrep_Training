#catagories of functions
#based of argument
# 1. positional arguments
def function(n1,n2,n3,n4):
    print(n1,n2,n3,n4)
function(10,20,30,40)
#2. Keyword arguments
def function2(n1,n2,n3,n4):
    print("n1",n1,"n2",n2,"n3",n3,"n4",n4)
function2(n4=40,n3=30,n2=20,n1=10)  

#default argument
def function3(name,roll,branch,unversity="GIET"):
    print(name,roll,branch,unversity)
function3("Ashu",281,"cse")
function3("utu ",289,"cse")    
function3("don",2831,"cse")    

## single args multiple value
def func4(*var):
    sum = 0
    for i in var:
        sum+=i
    return sum
print(func4(1,2,3,4,5))
