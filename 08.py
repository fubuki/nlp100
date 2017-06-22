
string = 'An Apple a Day Keeps The Doctor Away.'


def cipher(query):
    result = ''

    for char in query:
        result += str(219 - ord(char)) if char.islower() else char
    return result


print cipher(string)