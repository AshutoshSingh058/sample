#  Sparse Matrix Algorithm

def sparseinput():
    n=int(input("Enter the number of Rows: "))
    m=int(input("Enter the number of Columns: "))
    sp=[]
    sp.append([n,m,0])
    cnt=0
    for i in range(0,n):
        
        for j in range (0,m):
            # x=[]
            val=int(input("Enter the  Value Number :"))
            if(val!=0):
                sp.append([i, j, val])
                cnt+=1
            # if(len(x)>0):
            #     sp.extend(x)
    sp[0][2]=cnt
    return sp

def print_sparse_matrix(sp):
    for i in range (0, len(sp)):
        print(sp[i])
    return







def sparse_simple_transpose(sp):
    n=sp[0][2]              # Number of values in sparse matrix
    col=sp[0][1]            # Number of Columns
    sp2=[]
    sp2.append([sp[0][1], sp[0][0], n])

    for i in range (0, col):
        for j in range (1, n):
            if(sp[j][1]==i):
                sp2.append([sp[j][1], sp[j][0], sp[j][2]])
            
    return sp2


def sparse_fast_transpose(sp):
    n=sp[0][2]              # Number of values in sparse matrix
    col=sp[0][1]            # Number of Columns
    sp2=[[0,0,0]]*(n+1)
    sp2[0]=[sp[0][1], sp[0][0], n]

    arr=[0]*(col)

    for i in range (1, n):
        arr[sp[i][1]]+=1
    
    # arr[0]+=1
    # print(arr)
    # x=0
    
    arr2=[0]*col
    arr2[0]=1
    for i in range (1,col):
       arr2[i]+=arr2[i-1]+ arr[i-1]
    #    x=arr[i] 
    # print(arr2)
    


    for i in range (1,n+1):
        
        sp2[arr2[sp[i][1]]]=[sp[i][1], sp[i][0], sp[i][2]]
        arr2[sp[i][1]]+=1
        
            
    return sp2

def addition_sparse_matrix(sp1, sp2):
    p1=0
    p2=0
    sp3=[]
    sp3.append([sp1[0][0], sp1[0][1],0])

    while(p1<=sp1[0][2] and p2<=sp2[0][2]):
        if(sp1[p1][0]==sp2[p2][0] and sp1[p1][1]==sp2[p2][1]):
            sp3.append([sp1[p1][0], sp1[p1][1], (sp1[p1][2]+sp2[p2][2])])
            p1+=1
            p2+=1
            sp3[0][2]+=1
        
        elif(sp1[p1][0]==sp2[p2][0]):
            if(sp1[p1][1]>sp2[p2][1]):
                sp3.append(sp2[p2])
                p2+=1
            else:
                sp3.append(sp1[p1])
                p1+=1
            sp3[0][2]+=1
        
        elif(sp1[p1][0]>sp2[p2][0]) :
            sp3.append(sp2[p2])
            p2+=1
            sp3[0][2]+=1

        else:
            sp3.append(sp1[p1])
            p1+=1
            sp3[0][2]+=1
        
    while(p1<= sp1[0][2]):
        sp3.append(sp1[p1])
        p1+=1
        sp3[0][2]+=1

    while(p2<= sp2[0][2]):
        sp3.append(sp2[p2])
        p2+=1
        sp3[0][2]+=1
    
    del sp3[1]
    sp3[0][2]-=1
    # sp3[0][2]=len(sp3)-2

    return sp3


            
# def multiplication_sparse_matrix(sp1, sp2):


        



# Function Call

def menu():
    while True:
        print("\nSparse Matrix Algorithm Menu")
        print("1. Input Sparse Matrix")
        print("2. Print Sparse Matrix")
        print("3. Simple Transpose of Sparse Matrix")
        print("4. Fast Transpose of Sparse Matrix")
        print("5. Addition of Two Sparse Matrices")
        print("6. Multiplication of Two Sparse Matrices")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        sp=[[0,0,0]]
        if choice == '1':
            sp = sparseinput()
            print("Sparse Matrix Input Complete.")

        elif choice == '2': 
            print_sparse_matrix(sp)
            
        elif choice == '3':
            sp_transposed = sparse_simple_transpose(sp)
            print("\nSimple Transposed Sparse Matrix:")
            print_sparse_matrix(sp_transposed)
            
        elif choice == '4':
            sp_transposed = sparse_fast_transpose(sp)
            print("\nFast Transposed Sparse Matrix:")
            print_sparse_matrix(sp_transposed)
        
        elif choice == '5':
            print("Input Sparse Matrix 1:")
            sp1 = sparseinput()
            print("Input Sparse Matrix 2:")
            sp2 = sparseinput()
            sp_sum = addition_sparse_matrix(sp1, sp2)
            print("\nSum of Sparse Matrices:")
            print_sparse_matrix(sp_sum)
        
        # elif choice == '6':
        #     print("Input Sparse Matrix 1:")
        #     sp1 = sparseinput()
        #     print("Input Sparse Matrix 2:")
        #     sp2 = sparseinput()
        #     mp_sum = multiplication_sparse_matrix(sp1, sp2)
        #     print("\nSum of Sparse Matrices:")
        #     print_sparse_matrix(mp_sum)

        elif choice == '7':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Run the menu function
menu()
