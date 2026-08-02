import random, webbrowser

with open("reading/wiki.txt", "r") as f:
    pages = [x.rstrip() for x in f.readlines()]

for i in range(20):
    webbrowser.open(pages[i])