import random

query = 'I couldn`t believe that I could actually understand what I was reading : the \
phenomenal power of the human mind .'


term_list = query.split(" ")

result = []
for term in term_list:
    if len(term) < 4:
        result.append(term)
    else:
        mid_list = list(term[1:-1])
        random.shuffle(mid_list)
        result.append(term[0] + "".join(mid_list) + term[-1])

print " ".join(result)
