def check_even(num):
    if num % 2 == 0:
        print(num,"is Even Number")
    else:
        print(num,"It is not even")

def evenrange(start, end):
    result=[]
    for num in range(start, end+1):
        if(num%2==0):
            result.append(num)
    return result