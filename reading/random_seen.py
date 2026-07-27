import random, webbrowser

with open("reading/seen_wiki.txt", "r") as f:
    pages = [x.rstrip() for x in f.readlines()]

webbrowser.open(random.choice(pages))