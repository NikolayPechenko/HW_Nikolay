calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, *list_to_search):
    a = 0
    for words in list_to_search:
        if string.upper() == words.upper():
            a += 1
    count_calls()
    if a > 0:
        return True
    else:
        return False


print(is_contains('Russia', 'ussr', 'Russia', 'Russian'))
print(is_contains('Serbia', 'German', 'France', 'China'))
print(string_info('Georgia'))
print(calls)



