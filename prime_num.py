def prime_chk(n):
    for i in range(1,n):
        if n>1:
            for j in range(2,n):
                if i%j==0:
                    break
                else:
                 print(i)

interval=10
prime_chk(interval)