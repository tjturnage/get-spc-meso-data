import re
master = []
with open('desc_text.txt', 'r') as fin:
    for line in fin:
        l2 = line.replace('"','')
        if 'image' in l2:
            sliced = l2[32:-7]
            pair = sliced.split('>')
            master.append(pair)

print(master)