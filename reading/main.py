from tqdm import tqdm
from urllib.parse import unquote
from pathlib import Path
import os
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(user_agent='Wikistats (ethan_and_such@gmail.com)', language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
wiki_html = wikipediaapi.Wikipedia(user_agent='Wikistats (ethan_and_such@gmail.com)', language='en', extract_format=wikipediaapi.ExtractFormat.HTML)

def get_data(page: wikipediaapi.WikipediaPage):
    assert page.exists()
    return {
        #"title": page.title,
        #"sections": page.sections,
        #"summary": page.summary,
        "fullurl": page.fullurl,
        #"canonicalurl": page.canonicalurl,
        #"categories": page.categories,
        "length": page.length,
    }

def get_page(title):
    page = wiki_wiki.page(title)
    if not page.exists():
        print(f"[!] Page {title} not found.")
        return
    return page

if __name__ == "__main__":
    base = Path(__file__).resolve().parent
    wiki_fp = os.path.join(base, "wiki.txt")

    with open(wiki_fp, "r", encoding="utf-8") as f:
        urls = [unquote(x.rstrip()) for x in f.readlines()]

    titles = [x.removeprefix("https://en.wikipedia.org/wiki/") for x in urls]

    print("Getting pages...")

    pages = [get_page(title) for title in tqdm(titles, desc="Getting pages")]

    datas = [get_data(page) if page else {} for page in tqdm(pages, desc="Extracting data")]

    print("Sorting by length...")

    datas.sort(key=lambda data: data["length"])

    url_string = "\n".join([data["fullurl"] for data in datas])

    with open(wiki_fp, "w", encoding="utf-8") as f:
        f.write(url_string)