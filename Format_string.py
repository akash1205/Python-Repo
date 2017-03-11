camel = 42.2
#prints the integer value saved in camel as string
print("acd %r " %camel)

#multiple format specifier in the string. When there are multiple format
#specifier in the string, use parenthesis
cow = 28
print("abcd %d,%d" %(camel, cow))

#ex 7
print("mary has a little lamb")
print("its fleece was white as %s" %"snow")
print("and everywhere that mary went.")
print("." * 10)
end1="c"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="b"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"

print(end1+end2+end3+end4+end5+end6,)
print(end7+end8+end9+end10+end11+end12)
formatter = "%r,%r,%r"
#this will print in the value of end1-3 in raw format i.e.
#will be printed as strings, with single quotes. %r is basically used for formatting
print(formatter %(end1,end2,end3))


#to print the paragraph as written, use 3 double quotes:
print("""
	a
	b
	c
	""")
