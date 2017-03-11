import re
s = "From stephen.marquard@uct.ac.za Sat Jan 5 $09:14:16 2008"
t = re.findall('^From.* (\$[0-9]+:[0-9]+:[0-9]+)',s)
print(t)

t=re.findall('^New.*: [0-9]+')