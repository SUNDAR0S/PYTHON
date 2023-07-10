class NegativeValue(Exception):
    pass
try:
    name=input("ENTER YOUR NAME : ")
    age=int(input("ENTER YOUR AGE : "))
    if age<0:
        raise NegativeValue
    marks=[]
    for i in range(0,6):
        mark=float(input("ENTER MARKS : "))
        marks.append(mark)
    dict_={"NAME":name,"AGE":age,"MARKS":marks}
    print("DETAILS : \n",dict_)
except NegativeValue:
    print("AGE IS NEGATIVE")

 
