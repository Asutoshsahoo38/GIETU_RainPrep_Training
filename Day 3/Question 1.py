## find the index of the element of list_b from my_list
my_list = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]
r = []
for i in list_b:
    r.append((i,my_list.index(i)))
print(r)        
    
    
