#kongapi gateway

s = 'SIEMENS INDIA'
l = []
for i,v in enumerate(s):
    if i%2==0:
        print(v)
    else:
        print(v.lower())


s = ['abc', 'gqa', 'jqz', 'mjq', 'xyz', 'lmx']
# sort the nmbers
s = [5,3,4,15,0]
o = []
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i] < s[j]:
            o.append(s[j])
            o.append((s[i]))
print(o)

# how to flatten the list
L = [[1,2,[3,4]], [5,[6,[7,8]]]]
#L = [1,2,3,4,5,6,7,8]
o = []
import re
for i in range(len(L)):
    # if type(i) != 'int' and type(i) == 'list':
    #     for j in range(len(i)):
    #         o.append((i[j]))
    # o.append(L[i])
#
# print(o)
    o.append(str(L[i]).replace('[','').replace(']',''))
print(o)

# recrsive functions in python

# git qestion how to delete a commit which we had pshed and it in middle of few commits
