loop = True
count = 1
list_name = []
while loop:
    name = input("Moi nhap vao ten sinh vien thu {0}:  ".format(count)).title()
    count +=1
    if name == "#":
        # loop = False
        break
    list_name.append(name)
list_name.sort()
print(list_name)