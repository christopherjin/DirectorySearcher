from pathlib import Path
import shutil #for the duplication function
filelist = []
def projectOne():
    #first step in project function
    #Main function that keeps track of the initial input
    userinput = input("Enter something: ")
    path = Path(userinput)
    if (path.exists()):
        testPath(userinput)
    else:
        print("ERROR")
        projectOne()
def testPath(userinput):
    #2nd step in project function
    #Keeps track of the function that the user requests, has 3 helper functions
    #for whatever the user chooses
    firstPath = Path(userinput)
    inputTestPath = input()
    if (inputTestPath[:2] == "N "):
        testPathN(firstPath,inputTestPath)
        actionLine()
    elif (inputTestPath[:2] == "E "):
        testPathE(firstPath,inputTestPath)
        actionLine()
    elif (inputTestPath[:2] == "S "):
        testPathS(firstPath,inputTestPath)
        actionLine()
    else:
        print("ERROR")
        testPath(userinput)
def testPathN(firstPath,inputTestPath):
    #Function if the user chooses "N"
    #Finds files with the name the user requests
    #helper function for testPath
    typeN = inputTestPath[2:]
    for file in firstPath.iterdir():
        if file.is_dir():
            testPathN(file, inputTestPath)
        elif typeN == file.name:
            filelist.append(str(file))
def testPathE(firstPath,inputTestPath):
    #Function if the user chooses "E"
    #Finds files with certain file types
    #helper function for testPath
    typeE = inputTestPath[2:]
    for file in firstPath.iterdir():
        if file.is_dir():
            testPathE(file, inputTestPath)
        elif file.suffix == typeE:
            filelist.append(str(file))
def testPathS(firstPath,inputTestPath):
    #Function if the user chooses "E"
    #Finds files above certain data sizes
    #helper function for testPath
    typeS = int(inputTestPath[2:])
    for file in firstPath.iterdir():
        if file.is_dir():
            testPathS(file, inputTestPath)
        if file.stat().st_size > typeS:
            filelist.append(str(file))
def actionLine():
    #3rd step in project function
    #Keeps track of the function that the user requests, has 4 helper functions
    #for whatever the user chooses
    inputActionLine = input()
    if (inputActionLine == "P"):
        actionLineP()
    elif (inputActionLine == "F"):
        actionLineF()
    elif (inputActionLine == "D"):
        actionLineD()
    elif (inputActionLine == "T"):
        actionLineT()
    else:
        print("ERROR")
        actionLine()
def actionLineP():
    #Prints list of files from step 2
    #helper function for actionLine
    for item in filelist:
        print (item)
def actionLineF():
    #reads first line in each file from step 2
    #helper function for actionLine
    for file in filelist:
        path = Path(file)
        item = path.open('r')
        print (file)
        print(item.readline())
        item.close
def actionLineD():
    #creates duplicate for all files from step 2
    #helper function for actionLine
    for files in filelist:
        print (files)
        newspot = files + ".dup"
        oldfile = Path(files)
        dupfile = Path(newspot)
    shutil.copy(str(oldfile),str(dupfile))
def actionLineT():
    #updates file modified time for all files from step 2
    #helper function for actionLine
    for files in filelist:
        touched = Path(files)
        print (files)
        touched.touch(exist_ok = True)
projectOne()

