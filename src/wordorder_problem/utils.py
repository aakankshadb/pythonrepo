def total_words(n, words):
    d = {}
    for word in words:
        key = word
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1

    print(len(d))
    for key, val in d.items():
        print(val, end=' ')