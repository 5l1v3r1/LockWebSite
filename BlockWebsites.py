import os
# Path of the file
path = r"Websites List.txt"
hostPath = r"test.txt"

file = open(path, "r")
for l in file.readlines():
    print(l)

# Modifica Host

lista = ["web1", "web2", "Web3"]
file = open(hostPath, "a")
for d in lista:
    file.write("\n"+ d)

