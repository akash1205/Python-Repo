from sys import argv
from os.path import exists
script, from_file, to_file = argv
infile=open(from_file)
indata=infile.read()
print(len(indata))
#to check if the file exists or not
print(exists(to_file))
out_file=open(to_file,'w')
out_file.write(indata)
out_file.close()
infile.close()


#alteration
open(to_file,'w').write(open(from_file).read())
