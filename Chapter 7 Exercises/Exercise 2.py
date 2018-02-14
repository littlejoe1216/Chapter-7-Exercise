#Joe Gutierrez Exercise 2
fname = input('Enter the file name: ')

fhand = open('mbox.txt')
count = 0
avg = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:')
		count = count + 1
		hobo = line
		random = float(hobo[20:])
		avg = avg + random
print(avg/3)
		