a = int(input())
i = 0
for x in range(1, a + 1):
    if(a % x == 0): 
        i += 1
print(str(i))