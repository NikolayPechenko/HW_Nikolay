def all_variants(text):
    for i in range(len(text)):
        for j in range(i, len(text)+1):
            if text[i:j] != '':
                yield text[i:j]


a = all_variants("abc")
for k in a:
    print(k)
