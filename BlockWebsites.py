import shutil
from os import remove

class WebsiteBlock:
    def __init__(self):
        #self.hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
        self.pathListWeb = r"list websites.txt"
        self.hostsTextOriginal = ""\
        "# Copyright (c) 1993-2009 Microsoft Corp.\n"\
        "#\n"\
        "# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.\n"\
        "#\n"\
        "# This file contains the mappings of IP addresses to host names. Each\n"\
        "# entry should be kept on an individual line. The IP address should\n"\
        "# be placed in the first column followed by the corresponding host name.\n"\
        "# The IP address and the host name should be separated by at least one\n"\
        "# space.\n"\
        "#\n"\
        "# Additionally, comments (such as these) may be inserted on individual\n"\
        "# lines or following the machine name denoted by a '#' symbol.\n"\
        "#\n"\
        "# For example:\n"\
        "#\n"\
        "#      102.54.94.97     rhino.acme.com          # source server\n"\
        "#       38.25.63.10     x.acme.com              # x client host\n"\
        "\n"\
        "# localhost name resolution is handled within DNS itself.\n"\
        "#	127.0.0.1       localhost\n"\
        "#	::1             localhost"
        self.hostsPath = r"test.txt"

    def __read_file(self, path):
        content = ""
        file = open(path, "r")
        for l in file.readlines():
            content += l
        file.close()
        return content
    def __write_file(self,path, text, type = "a"):
        file = open(path, type)
        file.write(text)
        file.close()
    def __rewrite_file(self,path, text):
        self.__write_file(path, text, "w")
    def __delete_file(self,path):
        try:
            remove(path)
        except:
            pass
    """
    def __backup(self,path1, path2):
        try:
            self.__delete_file(path1)
            shutil.copy(path1, path2)
            print("Backup - Sucess ")
        except:
            print("Backup - there was mistake error ")
    """
    def block(self):
        webs = self.__read_file(self.pathListWeb)
        self.__write_file(self.hostsPath, webs)
    def unlock(self):
        self.__rewrite_file(self.hostsPath, self.hostsTextOriginal)
    def reset(self):
        self.unlock()



if __name__ == '__main__':
    pass