# Sorting 2
# Radix Sort:Bucket Sort and Counting Sort
#  and Quick Sort


def bucketsort(L):
    # myArray = [34, 7, 23, 1, 89, 56, 78, 45, 12, 90, 67, 23, 45, 91, 53, 22, 77, 30, 89, 4, 100]
    lst=L
    print("Original array:", lst)
    buck = [[], [], [], [], [], [], [], [], [], []]
    maxVal = max(lst)
    exp = 1

    while (maxVal // exp > 0):

        while (len(lst) > 0):
            val = lst.pop()
            bucki= (val // exp) % 10
            buck[bucki].append(val)

        for bucket in buck:
            while len(bucket) > 0:
                val = bucket.pop()
                lst.append(val)

        exp *= 10
        print(lst)
    print("Sorted array:", lst)
    return




#COUNTING SORT

def countingsort(arr):
    n=len(arr)
    maxi=max(arr)
    d=0
    while maxi>0:
        maxi//=10
        d+=1
    mult=1
    for _ in range(d):
        ct_arr=[0]*10
        for i in range(n):
            x=int(arr[i]//mult)%10
            ct_arr[x]+=1
        for i in range(1,10):
            ct_arr[i]+=ct_arr[i-1]
        arr1=[0]*n
        for i in range(n-1,-1,-1):
            x=int(arr[i]//mult)%10
            arr1[ct_arr[x]-1]=arr[i]
            ct_arr[x]-=1
        arr=arr1
        mult*=10
    return arr




#QUICK SORT

def partition ( v, low, high) :
    pivot =v[low]
    print("Pivot Element is: ", pivot)
    i=low
    j = high
    while(i<j):
        while (v[i]<=pivot and i<=high):
            i+=1
        while (v[j]>pivot):
            j-=1
        if(i<j):
            v[i], v[j]=v[j], v[i]
            i+=1
            j-=1
    v[low], v[j]=v[j], v[low]

    return j


def quickSort(v, low, high) :
    if (low < high) :

        pi = partition(v, low, high)
        print("Partition Index is: ", pi)
        # print(v)
        print("[", end=" ")
        for i in range (low, high):
            print(v[i], end=", ")
        print("] \n")
        quickSort(v, low, pi -1)

        quickSort(v, pi + 1, high) 
    

    return v
    




# n= int(input("Enter the length of array:"))
# print("Please input the array:")
# L=[]
# for i in range (0,n):
#     a=int(input())
#     L.append(a)

L=[34, 7, 23, 1, 89, 56, 78, 45, 12, 90, 67, 23, 45, 91, 53, 22, 77, 30, 89, 4, 100]
L=[17, 42, 89, 5, 66, 28, 91, 13, 54, 72, 35, 47, 8, 29, 80, 57, 23, 94, 11, 65]


while(True):
    print("\n Please select operation to be done:")
    print("1. For performing Radix (Bucket) Sort:")
    print("2. For performing Radix (Counting) Sort:")
    print("3. For performing Quick Sort:")
    # print("4. For performing Shell Sort:")
    # print("5. For performing Insertion Sort:")
    
    print("6. to Exit")
    
    
    ch=input("Enter the choice of number: ")
    if(ch=='1'): 
        bucketsort(L)
    elif(ch=='2') :
        rad2_arr=L.copy()
        rad2_arr=countingsort(rad2_arr)
        print("Radix Sort using Counting Sort: \n",rad2_arr)
        # countingsort(L)
    elif (ch=='3'):
        v=list(L)
        n=len(v)
        low=0
        high=n -1
        print(v)

        print(quickSort(v, low, high))
        # print(v)


    elif(ch=='6'): 
        print("Exiting the program")
        break