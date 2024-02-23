def checkprime(n):
    if (n >= 1):
        for i in range(2,n):
            if(n % i)==0:
                return False
            else:
                if(n-1 == i):
                    return True    
    else:
        print("this is Invalid input")

def range_prime(start,end):
    result = []
    for num in range(start, end+1):
        if(checkprime(num)):
            result.append(num)
    return result    