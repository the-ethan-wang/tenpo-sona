t=int(input())

for _ in range(t):
    n=int(input())
    a=[*map(int,input().split())]
    loss=True
    curr=0
    for item in a:
        if item==1:
            curr+=1
        else:
            if curr==1 or curr>=3:
                loss=False
            curr=0
    if curr==1 or curr>=3:
        loss=False

    if(not loss):
        print("Alice")
    else:
        print("Bob")