import nltk
import pandas
import pickle

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


pkl_file = open('nb.pkl', 'rb')
mydict = pickle.load(pkl_file)
pkl_file.close()

newdict = {}

for key in mydict:
    temp = {}
    temp['text'] = str_stemmer(" ".join(mydict[key]['messages']))
    temp['word_count'] = len(temp['text'].split())
    temp['text_count'] = mydict[key]['total_count']
    key.replace('+91 89272 99929', 'Patra')
    key.replace('\xe2\x80\xaa+91 89002 45775\xe2\x80\xac', 'unknown')
    key.replace('\xe2\x80\xaa+91 97481 84976\xe2\x80\xac', 'Kaushal')
    if temp['text_count']>20:
        newdict[key] = temp

word_text_ratio = []

for key in newdict:
    word_text_ratio.append((float(newdict[key]['word_count'])/newdict[key]['text_count'], key))

sorted = word_text_ratio.sort()
print word_text_ratio

import matplotlib.pyplot as plt
import numpy as np

width = 0.35       # the width of the bars

fig, ax = plt.subplots()

x = np.arange(5)
myticks = [t[1] for t in word_text_ratio[len(word_text_ratio)-5:]]
plt.xticks(x, myticks)
y = [t[0] for t in word_text_ratio[len(word_text_ratio)-5:]]

rects1 = ax.bar(x, y, width, color='r')


#plt.plot(x,y)
plt.show()