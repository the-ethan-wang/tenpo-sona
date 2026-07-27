for n in range(8):
    diff_sum=set()
    for i in range(n):
        for j in range(n):
            diff_sum.add((abs(i-j),i+j))
    print(len(diff_sum))

# hmk.