from sys import argv
script, filepath=argv
#truncating and writing data to files
print("We are going to erase %s" %filepath)
print("CTRL-c to stop or enter to continue")
raw_input("?")

target=open(filepath, 'w')
#print(target.read())-- can't read a file open in write mode
raw_input("you sure about deleting?")
target.truncate()
#truncate is not needed here as opening a file in write mode
#using 'w' will automatically clear the previous content
#print(target.read())

print("writing to file now")
name=raw_input("write you name")
target.write(name)
target.write("\n")
print("file is written")
raw_input("enter to read")
#print(target.read())
target.close()
