import jieba
import pandas as pd
import csv

numP = 4211

# Create results dictionary
# Format: a dictionary from character to character synonyms arrays
char = {}
result = {}
csvfile = open('char.csv', mode='rt', encoding="utf-8")
reader = csv.reader(csvfile)
for row in reader:
    char[row[0]] = row
numChar = len(char)
for n in char:
    result[n] = {}
    for m in char:
        result[n][m] = 0

for i in range(numP):
    f = open('p/' + str(i) + '.txt', 'r').read()
    words = list(jieba.cut(f))
    for n in char:
        for m in char:
            if n in words and m in words:
                result[n][m] = result[n][m] + 1;
                print(n + ' and ' + m + ' coexists in paragraph ' + str(i))

print(result)
o = pd.DataFrame(result)
o.to_csv('result.csv', mode='w', encoding='UTF-8')
