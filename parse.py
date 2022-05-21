from pathlib import Path

import requests
from bs4 import BeautifulSoup


html = requests.get("http://www.russki-mat.net/e/mat_slovar.htm")
html.encoding = "utf-8"


soup = BeautifulSoup(html.text)
raw_words = soup.find_all("span", class_="lem")[10:113]


words = sorted(raw_word.text.lower() for raw_word in raw_words)

with open(Path("data/raw_mat.txt"), "w") as fp:
    fp.write("\n".join(words))
