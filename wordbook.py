def create_wordbook(word, length_wb):
    wordbook = [[], []]
    for i in range(0, length_wb):
        wordbook[0].append(max(l, key=word.count))
        wordbook[1].append(word.count(wordbook[0][i]))
        word = list(filter(lambda x: x != wordbook[0][i], l))
    return wordbook

w = ['s', 'd', 'bb', 'a', 'a', 'bb']
length_wb = int(input('input the length of the wordbook:'))
print(create_wordbook(w, length_wb))

