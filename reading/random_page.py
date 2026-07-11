import random, webbrowser

with open("reading/wiki.txt", "r") as f:
    pages = [x.rstrip() for x in f.readlines()]

webbrowser.open(random.choice(pages))