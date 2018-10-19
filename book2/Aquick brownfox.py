#str = "a quick brown fox jump over the lazy dog"
#for c in "abcdefghijklmnopqrstuvwxyz":
 #   print (c, str.count(c))


with open("country.txt", "r") as fp:
    lines = fp.read()
    for line in lines:
        for c in "abcdefghijklmnopqrstuvwxyz":
            with open(c+".txt","w") as f:        
                for line in lines:
                    f.write(line)
        
