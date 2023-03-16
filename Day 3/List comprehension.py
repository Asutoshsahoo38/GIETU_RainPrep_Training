#List Comprehension

l1 = [1,2,3,4,4,5,6,7,3,99,5,5,4]
result = []

#for loop version
for i in (l1):
    result.append(i)
print(result)

## List Comprehension version
print([i for i in (l1)])

##For loop finding odd number
for i in l1:
    if(i%2 != 0):
        print(i,end = " ")
print()        

## List Comprehension --> odd numbers 
print([i for i in l1 if(i%2 != 0)])


## If it's odd square it and if it's even the cube it

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
res = []
# for loop
for i in mat:
    for j in i:
        if(j%2 != 0):
            res.append(j**2)
        else:
            res.append(j**3)
print(res)            

## List Comprehension
r = []

r.append([j**2 if j%2 != 0  else j**3 for i in mat for j in i ] )
print(r)
            
## 2D array in for loop
for i in mat:
    r1 = []
    for j in i:
        if(j%2 != 0):
            r1.append(j**2)
        else:
            r1.append(j**3)
    res.append(r1)    
print(res)    
    
## 2D array in list Comprehension

print([[j**2 if j%2 != 0  else j**3  for j in i ] for i in mat])   
