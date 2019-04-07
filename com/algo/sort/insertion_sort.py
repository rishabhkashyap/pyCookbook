

def sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i
        element=arr[i]
        while(j>0 and arr[j-1]> element):
            arr[j]=arr[j-1]
            j-=1

        arr[j]=element






if __name__=='__main__':
    arr=[10,5,4,3,9,2,1]
    print('Array before sorting')
    print(*arr)
    print()
    sort(arr)
    print('Array after sorting')
    print(*arr)