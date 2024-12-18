# check the plugs available

t1 = str(input()).strip()
lst = t1.split(' ')

total = 0

for i in lst:
    total += int(i) - 1
    

print(total + 1)