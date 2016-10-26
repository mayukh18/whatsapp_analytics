import sys
import pandas as pd
import pickle
reload(sys)
sys.setdefaultencoding('utf8')

lines = []
numbers = ['0','1','2','3','4','5','6','7','8','9']

def whatsapp_parser():

    if len(sys.argv) < 4:
        print ("Run: python whatsapp_parser.py < Input TextFileName>  <Output csv filename>  <Output pkl filename>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        for line in f:
            lines.append(line.strip('\n'))


    final = []
    id = 0
    for i in range(len(lines)):
        if len(lines[i])==0:
            continue
        if str(lines[i][0]) in numbers and (lines[i][1]=='/' or lines[i][2]=='/'):
            final.append(lines[i])
            id += 1
        else:
            final[id-1] = final[id-1]+' '+lines[i]

    names = []
    texts = []

    print "Total number of messages:", len(final)

    for i in range(len(final)):
        temp = {}
        parts = final[i].split(',')
        parts = parts[1].split('-')[1][1:]
        parts = parts.split(':')

        if len(parts)>1 and parts[1]!=' <Media omitted>':
            text = parts[1]
            name = parts[0]
        else:
            continue

        names.append(name)
        texts.append(text)

    data = pd.DataFrame({'speaker':names, 'text': texts})
    data.to_csv(sys.argv[2], index=False)

    out = {}

    for i in range(len(names)):
        if names[i] not in out:
            temp = {}
            temp['total_count'] = 1
            temp['messages'] = [texts[i]]
            out[names[i]] = temp
        else:
            out[names[i]]['total_count'] += 1
            out[names[i]]['messages'].append(texts[i])

    output = open(sys.argv[3], 'wb')
    pickle.dump(out, output)
    output.close()

if __name__ == "__main__":
    whatsapp_parser()