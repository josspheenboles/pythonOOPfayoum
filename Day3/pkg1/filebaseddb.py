import sys
def inserttrainee(filepath,id,name,track):
    try:
        file=open(filepath,'a')
        if(file.writable()):
            file.write(str(id)+','+name+','+track+'\n')
        file.close()
    except:
        print(sys.exc_info()[1])
def gettrainees(filepath,rownumber=None):
    try:
        data=None
        file=open(filepath,'r')
        if(file.readable()):
            if(rownumber is not None):
                data = file.readlines()[rownumber]
            else:
                data=file.readlines()
        file.close()
    except:
        print(sys.exc_info()[1])
    else:
        return data

dbpath='traineedb'
class Trainee:
    pass