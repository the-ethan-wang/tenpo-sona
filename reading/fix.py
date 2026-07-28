with open("reading/wiki.txt", "r") as f:
    unseen = [x.rstrip() for x in f.readlines()]

unseen = list(set(unseen))

better=[]
for item in unseen:
    better.append(item.split("#")[0])

better = list(set(better))

with open("reading/wiki.txt", "w") as f:
    f.write("\n".join(better))