def factorial(num =12):
    if (num < 0):
        return None
    elif (num == 0 or num ==1):
        return 1
    else:
        fact =1
        for i in  range(2,num+1):
            fact = fact *i
        return fact
