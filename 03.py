
string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

print(sorted(string.split(' '), key=lambda s: len(s)))

print([len(i) for i in string.split(' ')])