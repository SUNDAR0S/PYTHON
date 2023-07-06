num = int(input("Enter a number: "))

fact = 1

if num%2==1:
    print("FACTORIAL")
    if num < 0:
       print("Retry ...Factorial doesn't support -ve no's")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
           fact*=i
        
       print("The factorial of",num,"is",fact)
       
else:
    print("\t\tPALINDROME\n")
    temp = num
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    if num == reverse:
      print('Palindrome')
    else:
      print("Not a Palindrome")
