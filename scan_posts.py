import os

print("Hello world!")
dir_name = "_posts"

directory = os.fsencode(dir_name)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".md"): 
        print(filename)
        #detect links
        continue
    else:
        continue

