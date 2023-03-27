#Find the common elements from both str
s1 = 'I like Python'
s2 = 'Java is a very  popular language'
s3 = ''
for i in s2:
    if(i == " "):
        pass
    else:
        if i in s1:
            if i not in s3:
                s3 += i
print(s3)        
