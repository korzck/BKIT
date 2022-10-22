from math import sqrt
print("Input coefficients A, B, C (ex. '3 4 5' equals to 3x\u2074+ 4x\u00b2 + 5 = 0)")

while True:
    try:
        args = [float(i) for i in input().split()]
        break
    except:
        print("Invalid args! Try again")

while(len(args)!=3):
    if (len(args)<3):
        print("Too few args! Try again")
    if (len(args)>3):
        print("Too much args! Try again")
    args = [float(i) for i in input().split()]

solution = []
for i in range(0,2):
    for j in range(0,2):
        try:
            x = (-1)**j*sqrt((-args[1]+(-1)**i*sqrt(args[1]**2-4*args[0]*args[2]))/(2*args[0]))
            if x not in solution:
                solution.append(x)
        except:
            pass
if len(solution)==0:
    print("no roots")
else:
    print("roots:")
    for i in range(len(solution)):
        print("{0:1}){1:>2}{2:.5f}".format(i, str(solution[i])[0] if solution[i]<0 else '',  abs(solution[i])))
