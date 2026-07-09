def siv(n):
    if(n<2):return[]
    isp=[True]*(n+1)
    isp[0]=isp[1]=False
    p=2
    while(p**2<=n):
        if(isp[p]):
            for m in range(p*p,n+1,p):
                isp[m]=False
        p+=1
    return [i for i,ps in enumerate(isp) if ps]

# Truly a line of all tim
print((lambda x:"\n".join(x)+"\n\n"+str(len(x))+" prims")([*map(str,siv(100))]))
