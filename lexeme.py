from pathlib import Path

import pymorphy2


def make_unique_list(iterable):
    return list(dict.fromkeys(iterable))


morph = pymorphy2.MorphAnalyzer()


with open(Path("data/raw_mat.txt")) as fp:
    raw_words = fp.read().split("\n")


words = make_unique_list(
    parse.word 
    for raw_word in raw_words 
    for parse in morph.parse(raw_word.lower())[0].lexeme
)


with open(Path("data/mat.txt"), "w") as fp:
    words = fp.write("\n".join(words))
