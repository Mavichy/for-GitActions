import random
def calculator(a,b,s):
    if s =='+':
        return a + b
    if s =='-':
        return a - b
    if s =='*':
        return a * b
    if s =='//':
        return a // b
    if s =='/':
        return a / b
    if s =='%':
        return a % b
    if s == '?':
        return random.randint(a,b)

if __name__ == '__main__':
    a = int(input())
    s = input()
    b = int(input())
    calculator(a,b,s)

