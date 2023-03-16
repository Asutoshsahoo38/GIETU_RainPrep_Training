## LIST
l = []
print(l,type(l))
list1 = [10,20,30,40]
print('Inserting an element')
list1.append(501)
print(list1)
list1.extend([60,70,80,90,100])
print(list1)
list1.insert(4,200)
print(list1)
print('remove the element')
list1.remove(80)
print(list1)
list1.pop()
print(list1)
del list1[2]
print(list1)
