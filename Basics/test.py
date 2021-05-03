print(__file__)
with open('../test.txt', 'w') as fp:
    fp.write('relative path test')

with open('../test.txt', 'r') as fp:
    print(fp.read())