# def chk_palindrome(num):
#     while num > 0:
#         temp = 0
#         remainder = num % 10
#         temp = temp * 10 + remainder
#         num = num / 10
#     return temp
#
#
# n = 121
# reverse = chk_palindrome(n)
# print(reverse)
# if n == reverse:
#     print("ITs a palindrome")
# else:
#     print("Not a palindrome")
#
#
# def che_pali_str(st):
#     if st == (st[::-1]):
#         print("Yes its a palindrome")
#     else:
#         print("Not palindrome")
#
#
# phrase = "Nitin"
# che_pali_str(phrase)


def check_for_palindrome(st):
    n = len(st)
    for i in range(n // 2):
        if st[i] != st[n - i - 1]:
            return False
        return True

st = "abc"
res=check_for_palindrome(st)
if res:
    print("yes")
else:
    print("No")
