def lis(arr):
    t = [0]*len(arr)
    t[0]=1
    j=1
    while j<len(arr):
        i=0
        while i<j:
            if arr[j]>arr[i] and t[j]<t[i]:
                t[j]+=1
            i+=1
        t[j]+=1
        j+=1
    return max(t)
    # return t
print(lis([5,4,3,2,1]))