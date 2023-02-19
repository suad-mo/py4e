fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
    
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    # print(line)
    count = count + 1
print('Line Count:', count)
