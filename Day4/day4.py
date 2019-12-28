numbers = [];

def checkDouble(num):
    number = list(num);
    for i, digit in enumerate(number):
        if(i+1==len(number)):
            break
        if(digit==number[i+1]):
            return True
    return False

def checkNoDecrease(num):
    number = list(num)
    for i, digit in enumerate(number):
        if(i+1==len(number)):
            break
        if(digit>number[i+1]):
            return False
    return True

def checkDouble_2(num):
    number = list(num)
    i=0
    while i < len(number):
        n = number[i]
        j = 1;
        while True:
            if(i+j < len(number) and n == number[i+j]):
                j += 1 
            else:
                break;
        if(j==2):
            return True
        i += j
    return False
        

count = 0
for n in range(245183, 790572):
    n = str(n)
    if(checkDouble_2(n) and checkNoDecrease(n)):
        count = count + 1

print(count)



