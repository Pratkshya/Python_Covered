import os

filename = os.path.join("myFile/","secondFile.txt")

f = open(filename, "w")
f.write("Hello")
f.close()