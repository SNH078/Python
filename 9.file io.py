
# open file , read it 
f=open("file1.txt")
data=f.read()
print(data)
f.close()

#  write
str="hey i am good vibe"
ff=open("file2.txt","w")
ff.write(str)
ff.close()

# read lines separately
fff=open("file3.txt")
lines=fff.readlines() # list is returned
print(lines,type(lines))
fff.close()

# read line om command
fff=open("file3.txt")
line1=fff.readline() # list is returned
print(line1,type(line1))

line2=fff.readline() # list is returned
print(line2,type(line2))
fff.close()

#  modes of opening a file ---
"""
r- open for reading 
w- open for writiing 
a- open for appending
+ : open for updating 
"rb" : will open for read in binary mode
"rt" : will open for read in text mode
"""


# with --TO AVOID using close()
word="bhai"
with open("file1.txt","r") as f:
    content=f.read()  
contentnew =content.replace(word,"bro")

with open("file1.txt","w") as f:
    f.write(contentnew)