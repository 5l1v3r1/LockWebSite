import os
# Path of the file

class WebsiteBlock:
    def __init__(self):
        self.hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
        self.WeblistBlock = r""

    def __read_file(self, path):
        content = ""
        file = open(path, "r")
        for l in file.readlines():
            content += l
        return content
    def __write_file(self,path, text):
        file = open(path, "a")
        for l in text:
            file.write("\n"+ l)

    def block(self):

        pass
    def unlock(self):

        pass
    def reset(self):

        pass



"""

path = r"Websites List.txt"
hostPath = r"test.txt"

file = open(path, "r")
for l in file.readlines():
    print(l)

# Modifica Host



"""