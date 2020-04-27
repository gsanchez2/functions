'''
Created on Apr 4, 2020

@author: ITAUser
'''

def sum_two_numbers(num1, num2, num3):
    sumOfNums = num1 + num2 + num3
    return sumOfNums

x = sum_two_numbers (4, 5, 3142)

print (x)

x = sum_two_numbers(456879867564, 1234567, 789876543)

print(x)

def taxCalc(subTotal, tax):
    taxAmount = subTotal * tax 
    total = subTotal + taxAmount
    shipping = 0
    
    if(total > 100):
        shipping = 0
    elif(total > 50):
        shipping = 10
    else:
        shipping = 5
    
    total = total + shipping
    return total

y = taxCalc (152, .05)

print(y)

y = taxCalc (80, .05)

print(y)

y = taxCalc (10, .05)

print(y)

def capFirstName(name):
    name = name[0].upper() + name[1:]
    return name

z = capFirstName("gisel")
print(z)
                 


