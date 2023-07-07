l=[3,4,2,6,1]
for i in range(len(l)):
    mini=i
    for j in range(i+1,len(l)):
        if l[mini] > l[j]:
            mini = j
    
    l[i],l[mini]=l[mini],l[i]

print(l)