filenames = ['a.txt', 'b.txt', 'c.txt']

for file in filenames:
    x = open(file, 'r')
    text = x.read()
    print(text)
