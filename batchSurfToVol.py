
# ------------------------------------------------------
# main program
# ------------------------------------------------------

import os
from curvature_analysis import calc_stvr_batch

studyDir = '/absolute/path/to/parstubuilder/parametric/study/directory'

# get list of simulation directories from parStudyInfo.txt file (generated by parstubuilder)
simList = []
with open(studyDir+'/parStudyInfo.txt') as fin:
    for line in fin:
        if 'Unique parameter set' in line:
            break
    for line in fin:
        simList.append(line.rstrip())
fin.close()

# run paraview stvr post processor on each simulation 
downSampleRate = 1
arrayName = 'c2'
outFileName = 'c2_surfToVolRatio'
for pth in sorted(simList):
    simPath = studyDir+'/'+pth
    dataDir = simPath+'/vtkoutput'
    saveDir = simPath+'/postoutput'
    # check/creat postoutput directory
    if not os.path.exists(saveDir):
        try:
            os.mkdir(saveDir)
        except OSError as er:
            print(type(er))
            print('OSError exception thrown while trying to create:\n')
            print(saveDir+'\n')
    print("processing " + simPath)
    calc_stvr_batch(dataDir,saveDir,outFileName,arrayName,downSampleRate)
