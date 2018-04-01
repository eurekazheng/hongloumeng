s = open('hongloumeng.txt', 'r')
q = s.read()
f = q.split('\n')
num = 0
for p in f:
    b = open('p/' + str(num) + '.txt', 'w')
    b.write(p)
    print('Paragraph ' + str(num) + ' exported.')
    num += 1
s.close()
