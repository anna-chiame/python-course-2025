# open and read the created file
with open("myfile.txt", 'r', encoding="utf-8") as f :
    read = f.read()
    print(read)