#The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
# for i in range(1 , 5):
#     print(i)
# else:
#     print("no break ")
# '''
# Such type of else is useful only if there is an if condition present inside the loop
#  which somehow depends on the loop variable.
# '''
#
#
def check_even(l):
    for i in l:
        if i % 2 == 0:
            print("list contains an even number:", i)

    else:
        print("Even Number finished...")
check_even([12,23,43,22])

#
# import monk
# def monkey_func(self):
#     print("monkey_function is called")
#
# monk.A.myfunc=monkey_func
# obj=monk.A()
# obj.myfunc()
