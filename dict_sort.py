# d={
#     "g":[43,12,9,21],
#     "d":[9,91,23,54],
#     "p":[11,43,23,2]
# }
# res={}
# for key,value in sorted(d.items()):
#     res[key]=sorted(d[key])
# print(res)
#
# print({key:sorted(d[key]) for key,value in sorted(d.items())})


markdict={"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
marklist=list(markdict.items())
print(marklist)
l=len(marklist)
for i in range(l-1):
    for j in range(i+1,l):
        if marklist[i][1]>marklist[j][1]:
            t=marklist[i]
            marklist[i]=marklist[j]
            marklist[j]=t
sortdict=dict(marklist)
print(sortdict)