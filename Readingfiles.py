from sys import argv

script, filepath=argv
fileopen=open(filepath)
print("here is your file %s" %filepath)
print(fileopen.read())
#to read one line of the fileopen
#but the below command will not read anythin as
#the filehandler is the end of the file.
#to read the first line, we will have to close the file
#and open it again.
print("\n")
fileopen.close()
fileopen=open(filepath)
print(fileopen.readline())
fileopen.close()
