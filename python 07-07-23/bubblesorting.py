l=[3,4,2,6,1]
n=len(l)
for i in range(n-1):
    swap=False
    for j in range(n-i-1):
        if l[j] > l[j+1]:
            swap=True
            l[j], l[j+1]= l[j+1],l[j]
    if swap==False:
        break
print(l) 