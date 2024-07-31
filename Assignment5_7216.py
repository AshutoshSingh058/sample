# To implement Linear Search and Binary Search
import time
start_time = time.time()


L=[]
def inputarray(n):
    global L
    L=[] 
    # a=int(input("Enter the choice(1/2)"))
    a=2
    if(a==1):
        for i in range(n):
            x=int(input("Enter the number:"))
            L.append(x)
    else:
        for i in range(n):
            # x=int(input("Enter the number:"))
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


# search_element=int(input("Enter  the element to search: "))
# linearsearch(search_element, L)



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
    
    n=len(L)
    L.append(key)
    i=0
    while(L[i]!=key):
        i+=1
    if(i<n):
        L.pop()
        return i
    else:
        L.pop()
        return -1
    












# n=int(input("Enter the number of elements: : "))
n=100000
inputarray(n) 
# n=len(L) 

# key=int(input("Enter  the element to search: "))
key=565
linearsearch(key, L)
# print(sentinelsearch(key, L))

# binarysearch(key, L)


# n=int(input("Enter the number of elements: : "))
# inputarray(n)
# print(L)















































print("Process finished --- %s seconds ---" % (time.time() - start_time))