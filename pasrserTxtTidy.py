import pandas as pd
import re
import time
import os

def loadPass(file):
    with open(file) as f:
        content = f.readlines()
    return content

def tidy(content):
    '''
    Tidy the data
    Split 
    '''
    raw = [re.split('[\s|]', i) for i in content]
    return raw


def getFrame(content):
    data = pd.DataFrame(content)
    try:
        data.drop(7, axis = 1, inplace = True)
    except:
        pass
    data.columns = [
        'Account', 'Password', 'Server', 
        'Role', 'Occupation', 'Level', 'Balance',
        ]
    data['OperatingDate'] = ''
    data['Notes'] = ''
    return data

def generateFolder(directory):
    log_location = directory + '/log'
    folder = os.path.exists(log_location)
    print(folder)
    if not folder:
        os.makedirs(log_location)
    

def generateLog(inFilePath, mainFileName, outDirectory):

    # load file file
    c = loadPass(inFilePath)
    # Clean the data and split it
    tidyC = tidy(c)
    res = ['\t'.join(i) + '\n' for i in tidyC]
    # Insert seperator into the log file:
    res.insert(0, '='*20 + '\n' + time.asctime(time.localtime()) + '\n')

    # Gnerate Folder:
    # Record history
    generateFolder(outDirectory)
    with open(outDirectory + '/log/history.txt', 'a') as f:
        f.writelines(res)

    # export file
    df = getFrame(tidyC)
    print(df)
    df.to_csv(outDirectory +'/' + mainFileName.split('.')[0] + '.csv', index = False, sep = '\t')


def run(infilePath, mainFileName, outDirectory):
    generateLog(infilePath, mainFileName, outDirectory)


