
string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. \
Arthur King Can."


index_string = (1, 5, 6, 7, 8, 9, 15, 16, 19)
words = string.split(" ")

result ={}

for (num, word) in enumerate(words, 1):
    if num in index_string:
        result[word[0:1]] = num
    else:
        result[word[0:2]] = num

print(result)