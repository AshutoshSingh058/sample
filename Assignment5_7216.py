# To implement Searching Algorithms

def inputarray(n,a):
    global L
    L=[] 
    if (a==1):
        print("Enter the numbers:")
        for i in range (0,n):
            x=int(input())
            L.append(x)
    else:
        for i in range(n):
            L.append(i)
    return L


# Linear Search
def linearsearch(search_element, L):

    counter=0
    ans=-1
    n=len(L)
    for i in range(0,n):
        counter+=1
        if(L[i]==search_element):
            ans=i
            break

    if(ans!=-1):
        print("Element found at index ",ans)
        print(counter)
        
    else:
        print("Element not found !!!")
        print("Number of operations performed: ",counter)
    return



# Binary Search
def binarysearch(key, L):
    counter=0
    ans=-1
    L.sort()
    start=0
    end=len(L)
    while(start<=end):
        counter+=1
        mid=(start+end)//2
        # print(mid)
        if(key==L[mid]):
            ans=mid
            break
        
        elif(key>L[mid]):
            start=mid+1
        else :
            end=mid-1
    
    if(ans>=0):
        # print(L)
        print("Element found at index: ", ans)
        
    else:
        print("Element not found !!!")
    print("Number of operations performed: ",counter)
    return

#Sentinel Search
def sentinelsearch(key, L):
    cnt=0
    n=len(L)
    L.append(key)
    i=0
    while(L[i]!=key):
        cnt+=1
        i+=1

    if(i<n):
        L.pop()
        print("Element found at index: ", i)
   
    else:
        L.pop()
        print("Element not found !!!")
    print("Number of operations performed: ",cnt)
        
    return 
    

#Fibonacci Search
def fibonaccisearch(key,L):
    n=len(L)
    f=[0,0,1]
    while(f[-1]<n):
        x=f[-1]+f[-2]
        f.append(x)

    ans=-1
    offset=0
    cnt=0
    fn=f[-1]
    fn1=f[-2]
    fn2=f[-3]
    z=-4

    while(L[fn2]>0 and offset+fn2<n):
        cnt+=1
        if(L[offset+fn2]==key):
            offset+=fn2
            ans= offset
            break
        elif(key>L[offset+fn2]):
            offset+=fn2
            fn=fn1
            fn1=fn2
            fn2=f[z]
            z-=1
        elif(key<L[offset+fn2]):
            fn=fn2
            fn1=f[z]
            z-=1
            fn2=f[z]
            z-=1
    
    if(ans>=0):
        # print(L)
        print("Element found at index: ", ans)
        
    else:
        print("Element not found !!!")
    print("Number of operations performed: ",cnt)
    return



def menu():
    while True:
        print("\n Searching Algorithm Menu")
        print("1. Input Array by values")
        print("2. Input Array by Size")
        print("3. To perform Linear Search")
        print("4. To perform Sentinal Search")
        print("5. To perform Binary Search ")
        print("6. To perform Fibonacci Search")
        print("7. Exit")

        ch=input("Please Enter operation to be performed:")

        if ch=='1':
            print("Input the Array")
            n=int(input("Enter the size of array : "))
            inputarray(n,1)
        
        elif ch=='2':
            n=int(input("Enter the size of array : "))
            inputarray(n,2)

        elif ch=='3':
            key=int(input("Enter  the element to search: "))
            linearsearch(key, L)

        elif ch=='4':
            key=int(input("Enter  the element to search: "))
            sentinelsearch(key, L)
            
            
        elif ch=='5':
            key=int(input("Enter  the element to search: "))
            binarysearch(key, L)
            
        
        elif ch=='6':
            key=int(input("Enter  the element to search: "))
            fibonaccisearch(key,L)

        elif ch == '7':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")


#Calling Menu function
menu()



