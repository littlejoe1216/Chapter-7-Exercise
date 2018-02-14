#Joe Gutierrez Exercise 1

fname = input('Enter the file name: ')

fhand = open('mbox.txt')
count = 0
for line in fhand:
    
    print (line.upper())
