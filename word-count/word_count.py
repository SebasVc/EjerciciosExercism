def count_words(sentence):
    res = {}
    for w in sentence.casefold().replace(".", "").replace(":", "").replace(",", " ").replace("_", " ").split():
        if w.startswith("'") or w.endswith("'") or "!&@$%^" in w:
            key = w.replace("'", "").replace("!", "").replace("&", "").replace(
                "@", "").replace("$", "").replace("%", "").replace("^", "")
        else:
            key = w
        if key not in res:
            res[key] = 0
        res[key] += 1
    return res