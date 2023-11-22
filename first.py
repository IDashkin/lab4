fhand = open('mbox.txt')
for line in fhand:
    shout = line.rstrip().upper()
    print(shout)
fhand.close()