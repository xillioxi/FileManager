import os
import shutil
import datetime
import random
from collections import deque
import formatExcluder
import Logger

class FileManager():
    def __init__(self):
        self.__relativepath = os.getcwd() #Gets the current directory
        self.__filenames = os.listdir(self.__relativepath) #Filenames
        self.formatexcluder = formatExcluder()
        self.origin = ""
        self.dest = ""
        self.logger = Logger()

        print("Initialize")

    def getRelativePath(self):
        return self.__relativepath

    def getDirectory(self):
        return self.__filenames

    def rel_join(self,path):
        return os.path.join(self.__relativepath,path)
    

        
    def listdir(self,path):
        return os.listdir(path)

    def basepath(self,path):
        return os.path.basename(path)

    def retrievePath(self,path,name):
        #Given the path of the parent folder retrieves the path of the children folder given a name
        #If the folder dosen't exists it throws an error
        try: 
            dirs = self.listdir(path)
            for der in dirs:
                if(os.path.basename() == name):
                    return der

        except:
            print("The specified folder dosen't exist")

    def filter(self,directories,function,mode="include"):
        #Given a list of directories, filter all of the directories using the excluder
        #returns an array of files
        newarray = []
        if mode=="exclude":
            #All entries with the formats in the formatExcluder is removed from the array
            for i in range(len(directories)):
                if(function(directories[i])):
                    continue
                else:
                    newarray.append(directories[i])

            return newarray

        elif mode=="include":
            for i in range(len(directories)):
                if(function(directories[i])):
                    newarray.append(directories[i])
                else:
                    continue
            return newarray
            
        else:
            assert True, "Error Filter Mode, filter method only has 'include' or 'exclude'"
            return []

    def setOrigin(self,path):
        self.origin = path
        
    def setDest(self,path):
        self.path = path

    def move(self):
        self.logger.operation = "MOVE"
        shutil.move(self.origin,self.dest)
        self.logger.add(self.origin,self.dest)

    @staticmethod
    def join(path,anthrpath):
        return os.path.join(path,anthrpath)

    

def main():
    ft = FileManager()
    paths = []
    dests = []
    suitable_paths = ft.filter(ft.getDirectory(),ft.formatexcluder.contains,"exclude")


    """
    

    for i in range(len(suitable_paths)):
        path = ft.listdir(suitable_paths[i])
        suitable_paths[i]
        for i in range(len(path)):
            paths.append(ft.rel_join(path[i]))

    for i in range(len(paths)):
        dest = ft.basepath(paths[i])
        dest2 = ft.rel_join("path")
        dest = ft.join(dest2,dest)
        dests.append(ft.rel_join(dest))

    for i in range(len(paths)):
        ft.setOrigin(paths[i])
        ft.setDest(dests[i])
        ft.move()

    """

main()