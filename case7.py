with open('input.txt', 'r', encoding='utf-8') as f_in:
    import random as r
    def all_text(f_in):
        text1 = ''
        for line in f_in:
            text1 += line
        text1.replace('/n', ' ')
        text1 = text1.split()
        text = []
        for i in text1:
            if i[-1] in ':;"':
                i = i[:-1]
            text.append(i)
        return text
    text = all_text(f_in)

    def start_words(text):
        key1 = []
        for i in text:
            if i.istitle() == True:
                key1.append(i)
        key = []
        for i in key1:
            if i not in key:
                key.append(i)
        return key
    start = start_words(text)


    def end_words(text):
        words = []
        for i in text:
            if i[-1] in '.!?':
                words.append(i)
        return words

    end = end_words(text)


    def pairs(text):
        p = []
        for i in range(len(text) - 1):
            chain = (text[i], text[i+1])
            p.append(chain)
        return p
    list_pair = pairs(text)


    dic_text = {}
    for pair in list_pair:
        if pair[0] not in dic_text.keys():
            dic_text[pair[0]] = [pair[1]]
        else:
            dic_text[pair[0]].append(pair[1])


    def first_word(start):
        import random as r
        n = r.randint(0, len(start)-1)
        return start[n]


    n = int(input('Количество генерируемых предложений: '))

    def sentence(dic_text, start, end):
        first_w = first_word(start)
        n_text = [first_w]
        iterator = 0
        while len(n_text) < 5:
            word = r.choice(dic_text[n_text[-1]])
            if word not in end:
                n_text.append(word)
            elif (iterator > 5) and (iterator < 50):
                n_text.pop()
                iterator -=5
            else:
                break
            iterator += 1
        while (n_text[-1] not in end) and (len(n_text) < 20):
            word = r.choice(dic_text[n_text[-1]])
            n_text.append(word)
        if n_text[-1] not in end:
            for i in ':;"!,.?':
                n_text[-1].replace(i, '')
            n_text[-1] = n_text[-1] + r.choice(list('.!?'))
        return n_text
with open('output.txt', 'w', encoding='utf-8') as f_out:
    for i in range(n):
        f_out.write(' '.join(sentence(dic_text, start, end)) + '')







