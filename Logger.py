import FileManager

########## IN PROGRESS ############
class Logger():
    def __init__(self):
        self.Log = []
        self.operation = ""
        self.datetime = str(datetime.datetime.now())
        self.path = "Log"
        self.filename = self.datetime
        rel_path = FileManager.join(self.path,self.filename)

    def generateLog():
        if self.operation != "":
            file = open(rel_path,"w")
            print("********************************** DATE : ",self.datetime, "*************", "OPERATION:", self.operation, "**********************************" )
            print("\n\n\n\n")
            for i in range(len(self.Log)):
                file.write(self.Log[i][0] +  "    ==>    " + self.Log[i][1] + "\n")
            file.close()
        else:
            print("Logging Operation has not been taken yet")
    
    def addEntry(origin,dest):
        self.Log.append([origin,dest])
        #Generates an Edit Log Based Upon the Relocations
        #The Log format contains the Ruleset which is used to transfer the files
        #
#fileTranslator = FileTranslator()
#print(fileTranslator.getSubDirectories())
