
def f(string: str):
    list = string.split(" ")

    for i in range(len(list)):
        list[i] = list[i][::-1]

    return " ".join(list)


print(f("junyiacademy") == "ymedacaiynuj")
print(f("flipped class room is import") == "deppilf ssalc moor si tropmi")
