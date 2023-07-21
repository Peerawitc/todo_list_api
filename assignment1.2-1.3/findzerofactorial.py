x =  10
def findzero(x):
    factorial = 1
    count = 0
    for i in range(x,1,-1):
        factorial = factorial * i
    factorial = str(factorial)
    print("facetorial ="+factorial)
    for i in factorial[::-1]:
        if i == "0":
            count+=1
        else:
            break
    return count

print("zero count = "+str(findzero(x)))