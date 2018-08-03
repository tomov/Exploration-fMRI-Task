import os
import sys
import csv
from numpy.random import shuffle, seed, normal, uniform
import numpy as np
import math

nSubjects = 60
nRuns = 8
nBlocks = 4
nTrials = 10
prefix = 'uep'
conds = [[0,0], [1,1], [1,0], [0,1]]
L = ['S', 'R']
sd0 = math.sqrt(100)
sd = [0, math.sqrt(16)]
choiceDuration = 2
feedbackDuration = 1
ibi = 6 #interblock interval *BEFORE* each block starts IMPORTANT: This should match psychopy
fixCrossAtRunStart = 10 #interrun interval *BEFORE* each run starts IMPORTANT: This should match psychopy
isiRange = [1,3]
itiRange = [5,7]
avgIsi = (isiRange[0] + isiRange[1]) / 2
avgIti = (itiRange[0] + itiRange[1]) / 2
fixCrossAtRunEnd = 10


def nrand(m,sd):
    if sd == 0:
        return m;
    else:
        return round(normal(m, sd))

def gen(pilot):
    expectedRunLen = fixCrossAtRunStart + nBlocks*(ibi + nTrials * (choiceDuration + feedbackDuration + avgIsi + avgIti)) + fixCrossAtRunEnd
    print 'expectedRunLen = ', expectedRunLen
    for s in range(nSubjects + 1): #subject zero is the practice subject
        if pilot:
            subjId = '%sP%03d' % (prefix,s)
        else:
            subjId = '%s%03d' % (prefix,s)
        subjFname = os.path.join('csv', '%s.csv' % subjId)
        subjFname_1 = os.path.join('csv', '%s_1.csv' % subjId)
        subjFname_2 = os.path.join('csv', '%s_2.csv' % subjId)

        with open(subjFname, 'w') as subjF:
            subjF.write('runFilename\n')

            subjF_1 = open(subjFname_1, 'w')
            subjF_1.write('runFilename\n')

            subjF_2 = open(subjFname_2, 'w')
            subjF_2.write('runFilename\n')

            for r in range(1, nRuns + 1): 
                runFname = os.path.join('csv', '%s_run%d.csv' % (subjId, r))
                subjF.write(runFname +'\n')
                if r <= 4: 
                    subjF_1.write(runFname + '\n')
                else:
                    subjF_2.write(runFname + '\n')


                with open(runFname, 'w') as runF:
                    runF.write('blockFilename\n')
                    c = [0,1,2,3]  # c is order of conditions
                    shuffle(c)
                    assert len(c) == nBlocks #just to make sure length of these = 4
                    assert len(conds) == nBlocks
                    if pilot:
#                        assert False
                        isiDuration = uniform(1, 3, (nBlocks, nTrials))
                        itiDuration = uniform(2, 4, (nBlocks, nTrials))
                    else:
                        isiDuration = uniform(isiRange[0], isiRange[1], (nBlocks, nTrials))
                        itiDuration = uniform(itiRange[0], itiRange[1], (nBlocks, nTrials))


                    fixedTimes = fixCrossAtRunStart + nBlocks*(ibi + nTrials * (choiceDuration + feedbackDuration)) + fixCrossAtRunEnd

                    actualRunLen = sum(sum(isiDuration)) + sum(sum(itiDuration)) + fixedTimes

                    print 'actualRunLen = ', actualRunLen
                    ratio = (expectedRunLen - fixedTimes) / (actualRunLen - fixedTimes)
                    print 'ratio = ', ratio

                    isiDuration = isiDuration * ratio

                    itiDuration = itiDuration * ratio

                    newActualRunLen = sum(sum(isiDuration)) + sum(sum(itiDuration)) + fixedTimes

                    print 'newActualRunLen = ', newActualRunLen



                    stimOnset = fixCrossAtRunStart

                    colors = [0,1,2,3,4,5,6,7] #shuffles color palette so that each option in each block has a different color
                    shuffle(colors)
                    assert len(colors) == nBlocks*2


                    for b in range(1, nBlocks + 1):
                        blockFname = os.path.join('csv', '%s_run%d_block%d.csv' % (subjId, r, b))
                        runF.write(blockFname + '\n')
                        with open(blockFname, 'w') as blockF:
                            cols = ['subjectId', 'runId', 'blockId', 'trialId', 'condition', 'leftAnswer',
                                'rightAnswer', 'choiceDuration', 'isiDuration', 'feedbackDuration',
                                'itiDuration', 'stimOnset', 'itiOffset', 'leftColor', 'rightColor', 
                                'mu1', 'mu2', 'sd1', 'sd2']
                            blockF.write(','.join(cols) + '\n')
                            k1 = conds[c[b-1]][0]
                            k2 = conds[c[b-1]][1]
                            mu = [nrand(0,sd0), nrand(0, sd0)]

                            leftColor = colors[b*2-2]
                            rightColor = colors[b*2-1]


                            
                            print mu
                            condition = L[k1] + L[k2]
                            stimOnset = stimOnset + ibi

                            for t in range(1, nTrials+1):
                                leftAnswer = nrand(mu[0], sd[k1])
                                rightAnswer = nrand(mu[1], sd[k2])
                                itiOffset = stimOnset + choiceDuration + isiDuration[b-1, t-1] + feedbackDuration + itiDuration[b-1, t-1]

                                row = [subjId, r, b, t, condition, leftAnswer, 
                                    rightAnswer, choiceDuration, isiDuration[b-1, t-1], feedbackDuration, 
                                    itiDuration[b-1, t-1], stimOnset, itiOffset, 
                                    leftColor, rightColor, mu[0], mu[1], sd[k1], sd[k2]]
                                blockF.write(','.join(str(x) for x in row) + '\n')
                                stimOnset = itiOffset




if __name__ == "__main__":

    seed(129523)

    gen(False)
    gen(True)
    
