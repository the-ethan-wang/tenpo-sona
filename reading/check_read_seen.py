with open("reading/wiki.txt", "r") as f:
    unseen = [x.rstrip() for x in f.readlines()]

with open("reading/seen_wiki.txt", "r") as f:
    seen = [x.rstrip() for x in f.readlines()]

seen_set = set(seen)
unseen_set = set(unseen)



print("Seen AND unseen:")

for item in seen_set.intersection(unseen_set):
    print(item)

print("\n\n---\n")
print("seen spacing or # or repeats")

for item in seen_set:
    if item.strip() != item or "#" in item or seen.count(item)>1:
        print(item)

print("\n\n---\n")
print("unseen spacing or # or repeats")

for item in unseen_set:
    if item.strip() != item or "#" in item or unseen.count(item)>1:
        print(item)