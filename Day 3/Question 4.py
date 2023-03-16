## Input of a comma separated values
# Num1 = sum of all elements excluding between 5 and 8
# Num2 = string of elements btween 5 and 8
# Output num1 = num2
array = list(map(int,input().split(',')))# 3,2,6,5,1,4,8,9
number1 = sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l = array[array.index(5):array.index(8)+1]
number2 = ''
for i in l:
    number2 += str(i)
print(number1)  
print(number2)
print(int(number2)+number1)   
