file = open("C:\\Users\\Vlad\\Documents\\GitHub\\collage\\python\\practice\\task2\\file\\text.txt", "r")
word1 = ""
word2 =""
word3 =""
for i in file:
    arr = list(i)
    for i in arr[0]:
        word1+=i
    for i in arr[1]:
        word2+=i
    for i in range(0, 5):
        word3+=arr[i]
print(word1)
print(word2)
print(word3)
file.close()