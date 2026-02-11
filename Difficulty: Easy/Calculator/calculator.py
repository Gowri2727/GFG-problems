def utility(a, b, opr):
    #code here
    if opr == 1:
        res = a + b
        print(str(res), end="")
        
    elif opr == 2:
        res = a - b
        print(str(res), end="")
        
    elif opr == 3:
        res = a * b
        print(str(res), end="")
        
    else:
        print("Invalid Input", end="")