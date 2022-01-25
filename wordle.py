i = open("input.txt", "r")
o = open("words.txt", "w")

lines = i.readlines()

in_word = 'no'
in_location = {'o': 2, 'k': 0, 'n': 1}
not_in_word = 'saiebrwc'
not_in_location = {3: 'n', 4: 'n'}

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
        if b[x] == a[x]:
            return False
    return True

words = []
for x in lines:
    # if len(x) == 6:
    # if '-' not in x and '.' not in x and '\'' not in x:
    if is_in_word(in_word, x) and is_in_location(in_location, x) and is_not_in_word(not_in_word, x) and is_not_in_location(not_in_location, x):
        words.append(x.lower())

o.writelines(words)

# o.write("test")
