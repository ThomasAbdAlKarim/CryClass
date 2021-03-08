import os


Pain_Path = []
Hungry_Path = []
Uncomfortable_Path = []




def LOAD():
    Paths = [os.walk('Recordings/Pain'),os.walk('Recordings/Hungry'),os.walk('Recordings/Uncomfortable')]

    for Dirpath,DirName,File in Paths[0]:
        Pain_Path = File

    
    for i in range(len(Pain_Path)):
        Pain_Path[i] = os.path.join('Recordings/Pain',Pain_Path[i])


    for Dirpath,DirName,File in Paths[1]:
        Hungry_Path = File

    for i in range(len(Hungry_Path)):
        Hungry_Path[i] = os.path.join('Recordings/Hungry',Hungry_Path[i])

    for Dirpath,DirName,File in Paths[2]:
        Uncomfortable_Path = File
    for i in range(len(Uncomfortable_Path)):
        Uncomfortable_Path[i] = os.path.join('Recordings/Uncomfortable',Uncomfortable_Path[i])

    return Pain_Path,Hungry_Path,Uncomfortable_Path
