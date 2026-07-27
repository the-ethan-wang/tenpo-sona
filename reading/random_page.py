import random, webbrowser

with open("reading/wiki.txt", "r") as f:
    pages = [x.rstrip() for x in f.readlines()]

for i in range(10):
    webbrowser.open(random.choice(pages))