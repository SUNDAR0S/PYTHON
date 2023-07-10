try:
    n=int(input("ENTER RANGE :  "))
    list_=[]
    for i in range(0,n):
        num=int(input())
        list_.append(num)
    a=int(input("ENTER THE INDEX VALUE : "))
    print("THE ELEMENT AT ",a," IS ",list_[a])
except IndexError:
    print("INDEX EXCEEDS LIMIT !  ")
    print("THE LAST INDEX IS : ",len(list_) -1)
