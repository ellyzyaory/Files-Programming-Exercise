import re

def hapax(book):
    file = open(book, 'r', encoding="utf8")
    text = re.findall("\w+", file.read().lower())
    words_used = {}
    list = []

    for word in text:
        words_used.setdefault(word, 0)
        if word in words_used:
            words_used[word] += 1

    for key in words_used.keys():
        if words_used[key]:
            list.append(key)

    return list

if __name__ == "__main__":
    print(hapax("C:\\Users\\Johanes\\Desktop\\wuthering_heights.txt"))
