lines = ["This is first line","This is Second Line","This is third line"]

with open ("file1.text","w") as fp:
    for line in lines:
        fp.write(line+"\n")

