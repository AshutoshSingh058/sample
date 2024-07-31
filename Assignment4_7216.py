def inputpoly():
    x=int(input("Enter degree of polynomial :"))
    y=int(input("Enter number of terms in polynomial :"))
    p=[0]*(x+1)
    for i in range (0, y):
        a,b=0,0
        b=int(input("Enter the exponent of term: "))
        a=int(input("Enter the coefficient of term: "))
        p[b]=a

    return p

def printpoly(p):
    a=len(p)
    for i in range (-1, -a-1, -1):
        if(i!=-a and p[i]!=0):
            print(p[i],"x^%d"%(a-i*(-1)),end=" + ")
        
        elif(i==-a and p[i]!=0 ):
            print(p[i])

def addpoly(p1, p2):
    a=len(p1)
    b=len(p2)
    # p3=[]
    if(a>b):
        p3=p1.copy()
        for i in range (0,b):
            p3[i]+= p2[i]

    else:
        p3=p2.copy()
        for i in range (0,a):
            p3[i]+= p1[i]
    
    # print("Addition of two polynomials is :")
    return p3

def multipoly(p1,p2):
    a=len(p1)
    b=len(p2)
    p3=[0]*(a+b-1)
    for i in range(0,a):
        for j in range (0,b):
            p3[i+j]+=p1[i]*p2[j]

    return p3
   

def evaluatepoly(p, x):
    a=len(p)
    s=0
    for i in range(0, a):
        s+=p[i]*(x**i)
    
    return s


# 2nd representation methods

def inputpoly2():
    # x=int(input("Enter degree of polynomial :"))
    y=int(input("Enter number of terms in polynomial :"))
    p=[]
    for i in range (0, y):
        a,b=0,0
        b=int(input("Enter the exponent of term: "))
        a=int(input("Enter the coefficient of term: "))
        p.append([b,a])
    p.sort(reverse=True)
    return p

def printpoly2(p):
    a=len(p) 
    for i in range (0, a+1):
        if(i!=a-1 ):
            print(p[i][1],"x^%d"%p[i][0],end=" + ")
        else:
            print(p[i])

def addpoly2(p1, p2):
    a=len(p1)
    b=len(p2)
    p3=[]
    c,d=0,0
    while(c<a and d<b):
        if(p1[c][0]==p2[d][0]):
            p3.append([p1[c][0], p1[c][1]+p2[c][1]])
            c+=1
            d+=1
        elif(p1[c][0]>p2[d][0]):
            p3.append(p2[d])
            d+=1
        elif(p1[c][0]<p2[d][0]):
            p3.append(p1[c])
            c+=1
    
    while(c<a ):
        p3.append(p1[c])
        c+=1
    
    while(d<b ):
        p3.append(p2[d])
        d+=1
    
    return p3

def multipoly2(p1,p2):
    a=p1[0][0]
    b=p2[0][0]
    x=len(p1)
    y=len(p2)
    print(p1)
    print(p2)
    p3=[0]*(a+b+1)
    for i in range(0,x):
        for j in range (0,y):
            p3[i+j]+=p1[i][1]*p2[j][1]

    return p3

def evaluatepoly2(p, x):
    a=len(p)
    s=0
    for i in range(0, a):
        s+=p[i][1]*(x**p[i][0])
    
    return s

# p1=inputpoly()
# p2=inputpoly()

# print("Polynomial 1 is: ")
# printpoly(p1)
# print("Polynomial 2 is: ")
# printpoly(p2)


# print("Addition of polynomials: ")
# printpoly(addpoly(p1, p2))

# print("Multiplication of polynomials: ",end=" ")
# printpoly(multipoly(p1, p2))


# x=int(input("Enter the number to be evaluated: "))
# # p=inputpoly()
# print("Evaluation of polynomial for %d is "% x, evaluatepoly(p1,x))






p1=inputpoly2()
p2=inputpoly2()

# print("Polynomial 1 is: ")
# printpoly2(p1)
# print("Polynomial 2 is: ")
# printpoly2(p2)


# print("Addition of polynomials: ")
# printpoly(addpoly2(p1, p2))

print("Multiplication of polynomials: ",end=" ")
printpoly(multipoly2(p1, p2))


# x=int(input("Enter the number to be evaluated: "))
# # p=inputpoly()
# print("Evaluation of polynomial for %d is "% x, evaluatepoly2(p1,x))
