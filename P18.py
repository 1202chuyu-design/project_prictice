dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

s = input()
list = []
for i in s:
    list.append(dict[i])

total = list[-1]
for i in range(len(list)-1):
    if list[i] < list[i+1]:
        list[i] *= -1
    total += list[i]
    
print(total)