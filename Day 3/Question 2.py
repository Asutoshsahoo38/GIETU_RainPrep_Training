## find the index of the element of list_b from my_list using dict(key value pair
my_list = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]
r = {}
## List comprehension

print({i:my_list.index(i) for i in list_b})    
    
## Using update loops
for i in list_b:
    r.update({i:my_list.index(i)})
print(r) 
