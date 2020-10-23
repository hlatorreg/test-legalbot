import re
import os

def _clean(text:str):
    return re.sub(r"(\;\ )|(\:\ )|(\ Rut)", "", text)

def _get_owners(text):
    ruts = []
    text = text.split("\n")[4] # tercer parrafo
    regex_first = r"(?=\:\ ).+?(\s)?(?=\,\sdomiciliad)"
    regex_nexts = r"(?=\;\ ).+?(\s)?(?=\,\sdomiciliad)"
    first_match = re.search(regex_first, text, re.MULTILINE)
    if not first_match:
        return
    first = _clean(first_match.group(0)).split(",")
    if len(first[1].split(" ")) > 2:
        first[1] = f" {first[1].split(' ')[1]}"
    print(f"{first[0]},{first[1]}")
    ruts.append(first[1])
    text = text[first_match.span(0)[1]:]
    while True:
        next_matchs = re.search(regex_nexts, text, re.MULTILINE)
        if not next_matchs:
            break
        _next = _clean(next_matchs.group(0)).split(",")
        if len(_next[1].split(" ")) > 2:
            _next[1] = f" {_next[1].split(' ')[1]}"
        if _next[1] in ruts:
            break
        print(f"{_next[0]},{_next[1]}")
        text = text[next_matchs.span(0)[1]:]
        ruts.append(_next[1])


def print_owners():
    dire = './sociedades-texto'
    for filename in os.listdir(dire):
        print(f"-- {filename} --")
        with open(f"{dire}/{filename}", 'r') as file:
            _get_owners(file.read())
        print()

print_owners()