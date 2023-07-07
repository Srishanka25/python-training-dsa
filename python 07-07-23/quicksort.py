def quick(l):
    if len(l) <=1 :
        return l
    pivot=l[0]
    l1=[i for i in l if i<pivot]
    l2=[i for i in l if i>pivot]
    return quick(l1)+[pivot]+quick(l2)

l=[3,2,4,1,5,6]
ans=quick(l)
print(ans)