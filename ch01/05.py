
string = 'I am an NLPer'


def ngram(query, n):
    last = len(query) - n + 1
    result = []
    for i in range(0, last):
        result.append(query[i:i+n])
    return result

print(ngram(string, 2))

print(ngram(string.split(), 2))
