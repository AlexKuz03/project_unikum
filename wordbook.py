def create_wordbook(word, length_wb):
    wordbook = [[], []]
    for i in range(0, length_wb):
        wordbook[0].append(max(l, key=word.count))
        wordbook[1].append(word.count(wordbook[0][i]))
        word = list(filter(lambda x: x != wordbook[0][i], l))
    return wordbook

l = ['s', 'd', 'asas', 'a', 'a', 'asas']
length_wb = int(input('input length of the wordbook:'))
print(create_wordbook(l, length_wb))

