import shutil
from os import remove

class WebsiteBlock:
    def __init__(self):
        self.hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
        self.pathListWeb = r""
        self.hostOriginal = """
        # Copyright (c) 1993-2009 Microsoft Corp.
        #
        # This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
        #
        # This file contains the mappings of IP addresses to host names. Each
        # entry should be kept on an individual line. The IP address should
        # be placed in the first column followed by the corresponding host name.
        # The IP address and the host name should be separated by at least one
        # space.
        #
        # Additionally, comments (such as these) may be inserted on individual
        # lines or following the machine name denoted by a '#' symbol.
        #
        # For example:
        #
        #      102.54.94.97     rhino.acme.com          # source server
        #       38.25.63.10     x.acme.com              # x client host
        
        # localhost name resolution is handled within DNS itself.
        #	127.0.0.1       localhost
        #	::1             localhost
        """

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
    def __delete_file(self,path):
        try:
            remove(path)
        except:
            pass

    def __backup(self,path1, path2):
        try:
            self.__delete_file(path1)
            shutil.copy(path1, path2)
            print("Backup - Sucess ")
        except:
            print("Backup - there was mistake error ")

    def block(self):

        pass
    def unlock(self):

        pass
    def reset(self):

        pass