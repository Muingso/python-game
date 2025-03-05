BMW = [1,7,9,18,32,34,45,54,77,81,88,95,97,100]
 
BT =[]
AT = []
AS = []

for i in BMW:
    if 1<=i<=30:
        BT.append(i) 
    elif i>=31 and i<=69:
        AT.append(i)
    elif i>=70 and i<=100:
        AS.append(i)

print(BT)
print(AT)
print(AS)
print(BMW)
