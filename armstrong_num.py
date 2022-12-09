
def check_armstrong(n):
    new_num=0
    while(n>0):
        digit=n%10
        new_num=new_num+digit*digit*digit
        n=n//10
    return new_num


num=153
result=check_armstrong(num)
if num==result:
    print('Its a Armstrong number')
else:
    print("Not a armstrong numer")