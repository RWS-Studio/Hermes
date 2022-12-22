# sort.py is a script which sort your list that you found

liste = []

with open("./lists/2/list_to_sort.txt", "r") as f:
    for i in f:
        i = i[0:i.find(":")] # change this to stick with our list
        liste.append(i)
    f.close()
        
with open("./lists/2/sortedd_list.txt", "w") as f:
    for i in liste:
        f.write(f"{i} \n")
    f.close()