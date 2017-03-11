import urllib
import re
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    x = re.search('B.*\S', line)
    y = re.findall('B.*\S',line)
    print(x)
    print(y)
    print(line.strip())
