def odd_check(num):
    if(num%2 != 0):
        print("This is odd Number")
    else:
        print("This is not Even Number")

def oddrange(start , end):
    result=[]
    for num in range(start, end+1):
        if(num % 2 != 0):   
            
            result.append(num)
    return result

