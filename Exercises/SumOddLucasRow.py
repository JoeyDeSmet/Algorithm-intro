

def luc(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return luc(n-1) + luc(n-2)

def sumOfEvenLucasNumbers(n):
    current = 1
    sum = 2
    while current < n:
        nextNumber = luc(current)

        if nextNumber % 2 == 0:
            sum += nextNumber
        
        current += 1
    return sum


print(sumOfEvenLucasNumbers(4))