with open("reading/wiki.txt", "r") as f:
    unseen = [x.rstrip() for x in f.readlines()]

with open("reading/seen_wiki.txt", "r") as f:
    seen = [x.rstrip() for x in f.readlines()]

print(f"{(len(unseen))/len(seen):.2f}")

print(len(unseen))