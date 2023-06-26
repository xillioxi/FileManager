
######## FINIHSED ##########
class formatExcluder():
    def __init__(self):
        #TODO: Change to set later
        self.formats = []
        self.filename = "excludedFormats.txt"
        self.loadFormat()
    
    def loadFormat(self):
        #Checks if file exists, if not create a file
        if not (os.path.exists(self.filename)):
            print(f"The file {self.filename} dosen't exist.")
            self.writeFormat()
        else:
        #Takes a text file and loads everything into the format array
            file = open(self.filename,"r")
            for line in file:
                line = line.strip()
                self.formats.append(line)
            file.close()

    def writeFormat(self):
        #Writes list of formats to an existing text file
        self.healthCheck()
        file = open(self.filename,"w")
        for fileFormat in self.formats:
            file.write(fileFormat + "\n")
        file.close()
        print(f"The file {self.filename} has been successfully written" )

    def contains(self,path):
        # filename: string: repersenting a path or a filename
        # Checks if the path or filename contains one of the formats
        for fileFormat in self.formats:
            formatStrLen = len(fileFormat)
            #If format is longer than the path, then it is not possible they meet
            if(len(fileFormat) > len(path) ):
                continue
            if(path[-(formatStrLen):] == fileFormat):
                return True
        return False

    def add(format):
        #Adds an entry to the table
        self.formats.append(format)
    
    def remove(form):
        for i in range(len(self.formats)):
            if(self.formats[i] == form):
                self.formats[i] == ""
                return True
        return False

    def healthCheck(self):
        #Checks if the format in the format array is of the right type
        for fileFormat in self.formats:
            assert fileFormat[0:1] == ".","Exclusion Fileformat Error '" + fileFormat  + "' is not a valid file format"