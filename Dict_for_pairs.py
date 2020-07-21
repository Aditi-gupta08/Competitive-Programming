# Python Dictionary for pairs

m = {}

m[(1,2)] = 3
m[(6,2)] = 7

if (6,2) in m:
    print("yes")
else:
    print("no")
    
for i, j in m:
    print(m[(i,j)])
print(m)
    
m[(6, 2)] = min(m[(6,2)], 4)
print(m)