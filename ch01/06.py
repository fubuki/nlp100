
string1 = 'paraparaparadise'
string2 = 'paragraph'

def ngram(query, n):
    last = len(query) - n + 1
    result = []
    for i in range(0, last):
        result.append(query[i:i+n])
    return result

x = set(ngram(string1, 2))
y = set(ngram(string2, 2))

print(x.union(y))
print(x.difference(y))
print(x.intersection(y))

print("se" in x)
print("se" in y)