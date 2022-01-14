i = open("input.txt", "r")
o = open("words.txt", "w")

lines = i.readlines()

in_word = ''
in_location = {'a': 0, 'b': 1, 'e': 3}
not_in_word = 'diuftrldmocks'
not_in_location = {}

def is_in_word(a, b):
    for x in a:
        if x not in b:
            return False
    return True

def is_in_location(a, b):
    for x in a:
        if b[a[x]] != x:
            return False
    return True

def is_not_in_word(a, b):
    for x in a:
        if x in b:
            return False
    return True

def is_not_in_location(a, b):
    for x in a:
        if b[a[x]] == x:
            return False
    return True

words = []
for x in lines:
    # if len(x) == 6:

    if is_in_word(in_word, x) and is_in_location(in_location, x) and is_not_in_word(not_in_word, x) and is_not_in_location(not_in_location, x):
        words.append(x.lower())


o.writelines(words)

# o.write("test")
