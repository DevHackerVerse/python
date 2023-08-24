while True :
    print("\n\n                        CALCULATOR")

    print("\n+ = Add \n- = subtract \n* = Multiply \n/ = Divide \np = To the Power \nro = Under Root")
    print("\nq = For find Quotient \nr = For find Remainder")
    a=int(input("\nEnter a number "))
    op=input("Enter operation ")
    b=int(input("\nEnter another number "))
    re =None
    c = 1/b
    if op=="+" :
        re = a+b
    elif op=="-" :
        re = a-b
    elif op=="*" :
        re = a*b
    elif op=="/" :
        re = a/b
    elif op=="p" :
        re = a**b
    elif op=="ro" :
        re = a**c
    elif op=="q" :
        re = a//b
    elif op=="r" :
        re = a%b
    else :
        print("\n\nInvaild Operations")
    if re == None :
        re = ""
    else :
        print("\nThe answer is ",re)
        
        coice = input("For exist press n and for continue y :-  ")
    if coice == 'n' :
        break
    elif coice == 'y' :
        continue









