def array(length,start):
    newarr=[]
    i=0
    while(i<length):
        newarr.append(start)
        start=start+1
        i=i+1
    return newarr
print(array(4,5))