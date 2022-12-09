def sortdecor(func):
    def inner(l):
        new_dict={l[i]:l[i+1] for i in range(0,len(l),2)}
        sorted_dict=sorted(new_dict.items(),key=lambda x:x[1])
        print(sorted_dict)
    return inner
@sortdecor
def li_to_dict(l):
    pass
li=[12,6,3,53,9,16]
li_to_dict(li)