max = str(0)

for i in range(999,100,-1):
    for x in range(999,100,-1):
        f = str(x * i)
        if len(f) == 5:
            if f[0] == f[-1] and f[1] == f[-2] and int(f) > int(max):
                max = f
                break
        elif len(f) == 6:
            if f[0] == f[-1] and f[1] == f[-2] and f[2] == f[-3] and int(f) > int(max):
                max = f
                break

print(max)
