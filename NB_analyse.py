import pandas as pd

data = pd.read_csv('NBdata.csv')

chat = {}

for index,row in data.iterrows():
    if row.speaker not in chat:
        chat[row.speaker] = [row.text]
    else:
        chat[row.speaker].append(row.text)


import nltk

def str_stemmer(s):
    ss= ''.join([i if ord(i) < 128 else ' ' for i in s])
    punc=".,/?;:[{]}\|><-_\"*+^#%&();0123456789@!`~="
    exclude = set(punc)
    ss.replace('\n', ' ')
    temp = []
    for ch in ss:
        if ch in exclude:
            temp.append(' ')
        else:
            temp.append(ch)
    #s=''.join(ch for ch in ss if ch not in exclude)
    s = ''.join(temp)
    s=s.split()
    s = [w.lower() for w in s]
    out=" ".join(s)
    return out

all_words =

words = nltk.word_tokenize(str_stemmer(" ".join(chat['Sanchayan'])))


result = nltk.FreqDist(words)

print result.most_common(50)