i = 0
for i in range(5):
    print(" ",end="")
    print(" " *2*(4-i),end=' ')
    print("*"*4*(i+1),end=' ')
    print(" " *4*(5-i),end=' ')
    print("*"*4*(i+1))

for j in range(12):
    print(" "*2*j,end=' ')
    print("*"*4*(12-j))
    
