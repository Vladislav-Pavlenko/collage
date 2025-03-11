
def readFile ():
    file = open("C:\\Users\\Vlad\\Documents\\GitHub\\collage\\python\\practice\\file\\students.txt", "r")
    print(file)
    file.close()

def writeFile (content):
    file = open("C:\\Users\\Vlad\\Documents\\GitHub\\collage\\python\\practice\\file\\students.txt", "w")
    file.write(str(content))
    file.close()

def updateFile (content):
    file = open("C:\\Users\\Vlad\\Documents\\GitHub\\collage\\python\\practice\\file\\students.txt", "a")
    file.write(str(content))
    file.close()


def sortFile():
    obj = {}
    with open("C:\\Users\\Vlad\\Documents\\GitHub\\collage\\python\\practice\\file\\students.txt", "r+") as file:
        for i in file:
            arr = i.split(' ', 1)
            obj[arr[0]] = int(arr[1])
        sortedObj = dict(sorted(obj.items(), key=lambda item: item[1]))
        file.seek(0)
        file.truncate()
        for name, score in sortedObj.items():
            file.write(f"{name} {score}\n")

sortFile()
