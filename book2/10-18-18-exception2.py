import io

filename = "file.txt"
mode = "r"

try:
    with open (filename,mode) as fp:
        content = fp.read()
        print(content)

except FileNotFoundError:
    print(filename,"not Found please check if the file's name is correct")

except io.UnsupportedOperation:
    print("Are you sure",filename,"is readable")
