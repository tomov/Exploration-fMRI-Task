#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Wed Jul 25 20:09:00 2018
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'uncertaintyExperiment'  # from the Builder filename that created this script
expInfo = {u'mriMode': u'scan', u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/gershmanlab/Documents/SVM Experiment V4/uncertaintyExperiment.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text='Press "1" for left box or "2" for right box\n             to make your choice.',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
win.setColor('black')

leftPressInstr = "with your index finger"
rightPressInstr = "with your middle finger"



instruction ='''In this task, you have a choice between two slot machines, represented by colored buttons. ''' \
+ ''' When you click one of the buttons, you will win or lose points. ''' \
+ ''' Choosing the same slot machine will not always give you the same points, but one slot machine is always better than the other. ''' \
+ ''' Your goal is to choose the slot machine that will give you the most points.''' \
+ ''' After making your choice, you will receive feedback about the outcome.

Sometimes the machines are "safe" (always delivering the same feedback), and sometimes the machines are "risky" (delivering variable feedback). '''\
+ ''' Before you make a choice, you will get information about each machine: "S" indicates SAFE, "R" indicates RISKY. '''\
+ ''' **Note that safe/risky is independent of how rewarding a machine is: a risky machine may deliver more points on average than a safe machine, and vice versa. '''\
+ ''' You cannot predict how good a machine is based on whether it is safe or risky. 

You will play 30 games, each with a different pair of slot machines.''' \
+ ''' Each game will consist of 10 trials. 

Press %s to choose the left machine.
Press %s to choose the right machine.

Now press space to begin the first game.''' % (leftPressInstr, rightPressInstr)

# Initialize components for Routine "newRun"
newRunClock = core.Clock()
runInstr = visual.TextStim(win=win, ori=0, name='runInstr',
    text='We are about to begin a new round.\n\n        Are you ready to begin?',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
import os

subjectFilename = os.path.join('csv', expInfo['participant'] + '.csv')
print 'Loading from ', subjectFilename

# Initialize components for Routine "waitForTrigger"
waitForTriggerClock = core.Clock()
fmriClock = core.Clock() # clock for syncing with fMRI scanner
# definitely log it!

#trigger = 'parallel'
trigger = 'usb'
if trigger == 'parallel':
    from psychopy import parallel 
elif trigger == 'usb':
    from psychopy.hardware.emulator import launchScan    

    # settings for launchScan:
    MR_settings = { 
        'TR': 2.5, # duration (sec) per volume
        'volumes': 141, # number of whole-brain 3D volumes / frames
        'sync': 'equal', # character to use as the sync timing event; assumed to come at start of a volume
        'skip': 0, # number of volumes lacking a sync pulse at start of scan (for T1 stabilization)
        }


# Initialize components for Routine "fixationCross"
fixationCrossClock = core.Clock()
fixationCross1 = visual.TextStim(win=win, ori=0, name='fixationCross1',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "newBlock"
newBlockClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='New block is starting',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ibiFixationCross"
ibiFixationCrossClock = core.Clock()
ibifixationCross = visual.TextStim(win=win, ori=0, name='ibifixationCross',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
#from psychopy import logging
#logging.console.setLevel(logging.DEBUG)

import time
import numpy as np
import seaborn as sns

# constants
#
leftButton = '1' # index finger
rightButton = '2' # middle finger

# log wall time
#
expInfo['expStartWallTime'] = time.ctime()




# color palette
palette = sns.color_palette("hls", 8)


rewards = []
# psychopy only writes the data at the very end
# we want data with intermediate results
# so we have this thing that dumps to a .wtf-file
# as the experiment is going on
#
streamingFilename = thisExp.dataFileName + '.wtf'
streamingFile = open(streamingFilename, 'a')
streamingDelim = ','

# get names of data columns
#
def getExpDataNames():
    names = thisExp._getAllParamNames()
    names.extend(thisExp.dataNames)
    # names from the extraInfo dictionary
    names.extend(thisExp._getExtraInfo()[0])
    return names

# write a header lines
#
def writeHeadersToStreamingFile():
    for heading in getExpDataNames():
        streamingFile.write(u'%s%s' % (heading, streamingDelim))
    streamingFile.write('\n')
    streamingFile.flush()

def flushEntryToStreamingFile(entry):
    for name in getExpDataNames():
        entry.keys()
        if name in entry.keys():
            ename = unicode(entry[name])
            if ',' in ename or '\n' in ename:
                fmt = u'"%s"%s'
            else:
                fmt = u'%s%s'
            streamingFile.write(fmt % (entry[name], streamingDelim))
        else:
            streamingFile.write(streamingDelim)
    streamingFile.write('\n')
    streamingFile.flush()

nextEntryToFlush = 0

# write entries that we haven't flushed yet
# this writes both to the .wtf file and to the mysql db
#
def flushEntries():
    global nextEntryToFlush

    # don't write anything during the initial run
    # that's b/c the number of columns can change
    #
    if runs.thisN == 0:
        return

    # if we're after the initial run, flush everything
    # that we haven't flushed yet
    #
    while nextEntryToFlush < len(thisExp.entries):
        flushEntryToStreamingFile(thisExp.entries[nextEntryToFlush])
        nextEntryToFlush += 1


rightBox = visual.Rect(win=win, name='rightBox',
    width=[0.3, 0.5][0], height=[0.3, 0.5][1],
    ori=0, pos=[0.25, 0],
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,1,0], fillColorSpace='rgb',
    opacity=1,depth=-2.0, 
interpolate=True)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
leftBox = visual.Rect(win=win, name='leftBox',
    width=[0.3, 0.5][0], height=[0.3, 0.5][1],
    ori=0, pos=[-0.25, 0],
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,1], fillColorSpace='rgb',
    opacity=1,depth=-4.0, 
interpolate=True)
leftHighlight = visual.Rect(win=win, name='leftHighlight',
    width=[0.3, 0.5][0], height=[0.3, 0.5][1],
    ori=0, pos=[-0.25, 0],
    lineWidth=10, lineColor=[0,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-5.0, 
interpolate=True)
rightHighlight = visual.Rect(win=win, name='rightHighlight',
    width=[0.3, 0.5][0], height=[0.3, 0.5][1],
    ori=0, pos=[0.25, 0],
    lineWidth=10, lineColor=[0,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-6.0, 
interpolate=True)
leftAnswerText = visual.TextStim(win=win, ori=0, name='leftAnswerText',
    text='X',    font='Arial Bold',
    pos=[-0.25, 0], height=0.15, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-7.0)
rightAnswerText = visual.TextStim(win=win, ori=0, name='rightAnswerText',
    text='Y',    font='Arial Bold',
    pos=[0.25, 0], height=0.15, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-8.0)
L_condition = visual.TextStim(win=win, ori=0, name='L_condition',
    text='default text',    font='Arial',
    pos=[-0.25, 0.32], height=.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0)
R_condition = visual.TextStim(win=win, ori=0, name='R_condition',
    text='default text',    font='Arial',
    pos=[0.25, 0.32], height=.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-11.0)
fixationITIcross = visual.TextStim(win=win, ori=0, name='fixationITIcross',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0)
ITI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ITI')

# Initialize components for Routine "fixationCross"
fixationCrossClock = core.Clock()
fixationCross1 = visual.TextStim(win=win, ori=0, name='fixationCross1',
    text='+',    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED

# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(instrText)
instructionsComponents.append(key_resp_2)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t  # underestimates by a little under one frame
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()

# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(subjectFilename),
    seed=None, name='runs')
thisExp.addLoop(runs)  # add the loop to the experiment
thisRun = runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisRun.rgb)
if thisRun != None:
    for paramName in thisRun.keys():
        exec(paramName + '= thisRun.' + paramName)

for thisRun in runs:
    currentLoop = runs
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun.keys():
            exec(paramName + '= thisRun.' + paramName)
    
    #------Prepare to start Routine "newRun"-------
    t = 0
    newRunClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    #runInstr.setText("Beginning round #" + str(runs.thisN + 1))
    # keep track of which components have finished
    newRunComponents = []
    newRunComponents.append(runInstr)
    newRunComponents.append(key_resp_3)
    for thisComponent in newRunComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "newRun"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = newRunClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *runInstr* updates
        if t >= 0.0 and runInstr.status == NOT_STARTED:
            # keep track of start time/frame for later
            runInstr.tStart = t  # underestimates by a little under one frame
            runInstr.frameNStart = frameN  # exact frame index
            runInstr.setAutoDraw(True)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in newRunComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "newRun"-------
    for thisComponent in newRunComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
       key_resp_3.keys=None
    # store data for runs (TrialHandler)
    runs.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        runs.addData('key_resp_3.rt', key_resp_3.rt)
    
    # the Routine "newRun" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "waitForTrigger"-------
    t = 0
    waitForTriggerClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    #expInfo['mriMode'] = 'scan' #hack we're always in fMRI mode
    
    if expInfo['mriMode'] != 'off': # or 'scan' !
        assert expInfo['mriMode'] == 'scan'
    
        if trigger == 'usb':
            vol = launchScan(win, MR_settings, 
                  globalClock=fmriClock, # <-- how you know the time! 
                  mode=expInfo['mriMode']) # <-- mode passed in
        elif trigger == 'parallel':
            parallel.setPortAddress(0x378)
            pin = 10; wait_msg = "Waiting for scanner..."
            pinStatus = parallel.readPin(pin)
            waitMsgStim = visual.TextStim(win, color='DarkGray', text=wait_msg)
            waitMsgStim.draw()
            win.flip()
            while True:
                if pinStatus != parallel.readPin(pin) or len(event.getKeys('esc')):
                   break
                   # start exp when pin values change
            globalClock.reset()
            logging.defaultClock.reset()
            logging.exp('parallel trigger: start of scan')
            win.flip()  # blank the screen on first sync pulse received
    else:
        fmriClock.reset()
    
    expInfo['triggerWallTime'] = time.ctime()
    core.wait(1)
    # keep track of which components have finished
    waitForTriggerComponents = []
    for thisComponent in waitForTriggerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "waitForTrigger"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = waitForTriggerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitForTriggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "waitForTrigger"-------
    for thisComponent in waitForTriggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    routineTimer.reset()
    # the Routine "waitForTrigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "fixationCross"-------
    t = 0
    fixationCrossClock.reset()  # clock 
    frameN = -1
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationCrossComponents = []
    fixationCrossComponents.append(fixationCross1)
    for thisComponent in fixationCrossComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixationCross"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationCrossClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixationCross1* updates
        if t >= 0.0 and fixationCross1.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationCross1.tStart = t  # underestimates by a little under one frame
            fixationCross1.frameNStart = frameN  # exact frame index
            fixationCross1.setAutoDraw(True)
        if fixationCross1.status == STARTED and t >= (0.0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixationCross1.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fixationCross"-------
    for thisComponent in fixationCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(runFilename),
        seed=None, name='blocks')
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    
    for thisBlock in blocks:
        currentLoop = blocks
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock.keys():
                exec(paramName + '= thisBlock.' + paramName)
        
        #------Prepare to start Routine "newBlock"-------
        t = 0
        newBlockClock.reset()  # clock 
        frameN = -1
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        newBlockComponents = []
        newBlockComponents.append(text)
        for thisComponent in newBlockComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "newBlock"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = newBlockClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t  # underestimates by a little under one frame
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            if text.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                text.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in newBlockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "newBlock"-------
        for thisComponent in newBlockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        #------Prepare to start Routine "ibiFixationCross"-------
        t = 0
        ibiFixationCrossClock.reset()  # clock 
        frameN = -1
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ibiFixationCrossComponents = []
        ibiFixationCrossComponents.append(ibifixationCross)
        for thisComponent in ibiFixationCrossComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "ibiFixationCross"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ibiFixationCrossClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ibifixationCross* updates
            if t >= 0.0 and ibifixationCross.status == NOT_STARTED:
                # keep track of start time/frame for later
                ibifixationCross.tStart = t  # underestimates by a little under one frame
                ibifixationCross.frameNStart = frameN  # exact frame index
                ibifixationCross.setAutoDraw(True)
            if ibifixationCross.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                ibifixationCross.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ibiFixationCrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "ibiFixationCross"-------
        for thisComponent in ibiFixationCrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(blockFilename),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        for thisTrial in trials:
            currentLoop = trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial.keys():
                    exec(paramName + '= thisTrial.' + paramName)
            
            #------Prepare to start Routine "trial"-------
            t = 0
            trialClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            # log some times
            #
            trials.addData('trialStartWallTime', time.ctime())
            trials.addData('actualChoiceOnset', fmriClock.getTime())
            
            #trials.addData('mu1', mu1)
            #trials.addData('mu2', mu2)
            #trials.addData('sd1', sd1)
            #trials.addData('sd2', sd2)
            
            # ------------------ Feedback code -------------------
            #
            
            # clear the feedback
            #
            isFeedbackShown = False
            
            # ------------ Choice Highlight Code ----------------
            #
            
            # don't highlight the choices initially
            #
            leftHighlight.setOpacity(0)
            rightHighlight.setOpacity(0)
            
            # don't show the answers initially
            leftAnswerText.setOpacity(0)
            rightAnswerText.setOpacity(0)
            
            # hack to re-render the answer text with new opacity
            leftAnswerText.setText(str(int(round(leftAnswer))))
            rightAnswerText.setText(str(int(round(rightAnswer))))
            
            # track whether subject has responded so we can record response time
            # also initialize the response time by 3 (== timeout)
            # respTime is also used to terminate the relevant elements in the GUI
            # also used for feedback timing
            #
            respTime = choiceDuration # by default it's timeout
            
            # calculate the ITI, assuming trial will timeout.
            # we later change it to the actual ITI when the subject responds
            # note that we need to adjust for psychopy drift
            #
            timeLeftUntilItiOffset = itiOffset - fmriClock.getTime()
            actualItiDuration = timeLeftUntilItiOffset - (choiceDuration + isiDuration + feedbackDuration)
            print '   now = ', fmriClock.getTime()
            print '   itiOffset = ', itiOffset
            print '   expected iti duration = ', itiDuration
            print '   initial actual ITI duration = ', actualItiDuration
            itiDriftAdjustment = actualItiDuration - itiDuration
            print '           adjustment = ', itiDriftAdjustment 
            if actualItiDuration < 0:
                actualItiDuration = 0 # worst case scenario... if we've drifted too far
            
            hasResponded = False
            lastReponseKey = None
            
            fixationITIcross.setColor('white')
            
            
            leftBox.fillColor = palette[leftColor]
            rightBox.fillColor = palette[rightColor]
            leftBox.draw()
            rightBox.draw()
            
            print blocks.nTotal
            assert blocks.nTotal == 4 # if number of blocks changes, initialize more colors in the palette in Begin Experiment
            
            reward = 0
            
            
            responseKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
            responseKey.status = NOT_STARTED
            L_condition.setText(condition[0])
            R_condition.setText(condition[1])
            # keep track of which components have finished
            trialComponents = []
            trialComponents.append(rightBox)
            trialComponents.append(ISI)
            trialComponents.append(leftBox)
            trialComponents.append(leftHighlight)
            trialComponents.append(rightHighlight)
            trialComponents.append(leftAnswerText)
            trialComponents.append(rightAnswerText)
            trialComponents.append(responseKey)
            trialComponents.append(L_condition)
            trialComponents.append(R_condition)
            trialComponents.append(fixationITIcross)
            trialComponents.append(ITI)
            for thisComponent in trialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "trial"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = trialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # highlight subject's response
                #
                if responseKey.keys and not hasResponded:
                    hasResponded = True
                
                    respTime = responseKey.rt
                
                    # see how much time we have left for the ITI
                
                    timeLeftUntilItiOffset = itiOffset - fmriClock.getTime()
                    actualItiDuration = timeLeftUntilItiOffset - (isiDuration + feedbackDuration)
                    print '      final ITI = ', actualItiDuration
                    itiDriftAdjustment = actualItiDuration - (choiceDuration - respTime) - itiDuration
                    print '           adjustment = ', itiDriftAdjustment 
                    if actualItiDuration < 0:
                        actualItiDuration = 0 # worst case scenario... if we've drifted too far
                
                    # log some stuffs
                    #
                    trials.addData('actualChoiceOffset', fmriClock.getTime())
                    trials.addData('actualIsiOnset', fmriClock.getTime())
                    trials.addData('responseTime', respTime)
                    trials.addData('actualItiDuration', actualItiDuration)
                    trials.addData('itiDriftAdjustment', itiDriftAdjustment)
                
                
                
                
                    # highlight choice
                    #
                    if responseKey.keys == '1': # left choice
                        leftHighlight.opacity = 1
                        reward = leftAnswer
                #        leftAnswerText.opacity = 1
                    elif responseKey.keys == '2': # right choice
                        rightHighlight.opacity = 1
                        reward = rightAnswer
                #        rightAnswerText.opacity= 1
                    else:
                        assert False, 'Can only have one response, left or right choice'
                    
                    # save last response so we don't re-render
                    # deprecated -- we only remember the last choice
                    #
                    lastReponseKey = responseKey.keys
                
                
                    # hack to re-render the text with new opacity
                    #
                    leftHighlight.draw()
                    rightHighlight.draw()
                    leftAnswerText.setText(leftAnswerText.text)
                    rightAnswerText.setText(rightAnswerText.text)
                
                
                # show user some feedback, and log the ISI / feedback times
                #
                # print 'wtf', t, (respTime + isiDuration), (t >= respTime + isiDuration), isiDuration, feedbackDuration
                
                if t >= respTime + isiDuration and not isFeedbackShown:
                    isFeedbackShown = True
                    print '      Feedback time: ', t
                
                    # log some times
                    #
                    trials.addData('actualIsiOffset', fmriClock.getTime())
                    trials.addData('actualFeedbackOnset', fmriClock.getTime())
                    trials.addData('actualFeedbackOffset', fmriClock.getTime() + feedbackDuration)
                    trials.addData('actualItiOnset', fmriClock.getTime() + feedbackDuration)
                
                
                    if not responseKey.keys:
                        # no response was made => timeout
                        #
                        fixationITIcross.setColor('red')
                    else: 
                        if responseKey.keys == '1': # left choice
                            leftAnswerText.opacity = 1
                        elif responseKey.keys == '2': # right choice
                
                            rightAnswerText.opacity= 1
                        else:
                            assert False, 'Can only have one response, left or right choice'
                
                        # hack to re-render the text with new opacity
                        #
                        leftHighlight.draw()
                        rightHighlight.draw()
                        leftAnswerText.setText(leftAnswerText.text)
                        rightAnswerText.setText(rightAnswerText.text)
                
                
                
                # *rightBox* updates
                if t >= 0.0 and rightBox.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    rightBox.tStart = t  # underestimates by a little under one frame
                    rightBox.frameNStart = frameN  # exact frame index
                    rightBox.setAutoDraw(True)
                if rightBox.status == STARTED and t >= (0.0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                    rightBox.setAutoDraw(False)
                
                # *leftBox* updates
                if t >= 0.0 and leftBox.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    leftBox.tStart = t  # underestimates by a little under one frame
                    leftBox.frameNStart = frameN  # exact frame index
                    leftBox.setAutoDraw(True)
                if leftBox.status == STARTED and t >= (0.0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                    leftBox.setAutoDraw(False)
                
                # *leftHighlight* updates
                if t >= 0 and leftHighlight.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    leftHighlight.tStart = t  # underestimates by a little under one frame
                    leftHighlight.frameNStart = frameN  # exact frame index
                    leftHighlight.setAutoDraw(True)
                if leftHighlight.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                    leftHighlight.setAutoDraw(False)
                
                # *rightHighlight* updates
                if t >= 0 and rightHighlight.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    rightHighlight.tStart = t  # underestimates by a little under one frame
                    rightHighlight.frameNStart = frameN  # exact frame index
                    rightHighlight.setAutoDraw(True)
                if rightHighlight.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                    rightHighlight.setAutoDraw(False)
                
                # *leftAnswerText* updates
                if t >= respTime + isiDuration and leftAnswerText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    leftAnswerText.tStart = t  # underestimates by a little under one frame
                    leftAnswerText.frameNStart = frameN  # exact frame index
                    leftAnswerText.setAutoDraw(True)
                if leftAnswerText.status == STARTED and t >= (respTime + isiDuration + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    leftAnswerText.setAutoDraw(False)
                
                # *rightAnswerText* updates
                if t >= respTime + isiDuration and rightAnswerText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    rightAnswerText.tStart = t  # underestimates by a little under one frame
                    rightAnswerText.frameNStart = frameN  # exact frame index
                    rightAnswerText.setAutoDraw(True)
                if rightAnswerText.status == STARTED and t >= (respTime + isiDuration + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    rightAnswerText.setAutoDraw(False)
                
                # *responseKey* updates
                if t >= 0.0 and responseKey.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    responseKey.tStart = t  # underestimates by a little under one frame
                    responseKey.frameNStart = frameN  # exact frame index
                    responseKey.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(responseKey.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if responseKey.status == STARTED and t >= (0.0 + (respTime-win.monitorFramePeriod*0.75)): #most of one frame period left
                    responseKey.status = STOPPED
                if responseKey.status == STARTED:
                    theseKeys = event.getKeys(keyList=['1', '2'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if responseKey.keys == []:  # then this was the first keypress
                            responseKey.keys = theseKeys[0]  # just the first key pressed
                            responseKey.rt = responseKey.clock.getTime()
                            # was this 'correct'?
                            if (responseKey.keys == str('')) or (responseKey.keys == ''):
                                responseKey.corr = 1
                            else:
                                responseKey.corr = 0
                
                # *L_condition* updates
                if t >= 0 and L_condition.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    L_condition.tStart = t  # underestimates by a little under one frame
                    L_condition.frameNStart = frameN  # exact frame index
                    L_condition.setAutoDraw(True)
                if L_condition.status == STARTED and t >= (0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                    L_condition.setAutoDraw(False)
                
                # *R_condition* updates
                if t >= 0.0 and R_condition.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    R_condition.tStart = t  # underestimates by a little under one frame
                    R_condition.frameNStart = frameN  # exact frame index
                    R_condition.setAutoDraw(True)
                if R_condition.status == STARTED and t >= (0.0 + (respTime + isiDuration + feedbackDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                    R_condition.setAutoDraw(False)
                
                # *fixationITIcross* updates
                if t >= respTime + isiDuration + feedbackDuration and fixationITIcross.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    fixationITIcross.tStart = t  # underestimates by a little under one frame
                    fixationITIcross.frameNStart = frameN  # exact frame index
                    fixationITIcross.setAutoDraw(True)
                if fixationITIcross.status == STARTED and t >= (respTime + isiDuration + feedbackDuration + (actualItiDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                    fixationITIcross.setAutoDraw(False)
                # *ISI* period
                if t >= respTime and ISI.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ISI.tStart = t  # underestimates by a little under one frame
                    ISI.frameNStart = frameN  # exact frame index
                    ISI.start(isiDuration)
                elif ISI.status == STARTED: #one frame should pass before updating params and completing
                    ISI.complete() #finish the static period
                # *ITI* period
                if t >= respTime + isiDuration + feedbackDuration and ITI.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ITI.tStart = t  # underestimates by a little under one frame
                    ITI.frameNStart = frameN  # exact frame index
                    ITI.start(actualItiDuration)
                elif ITI.status == STARTED: #one frame should pass before updating params and completing
                    ITI.complete() #finish the static period
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "trial"-------
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # log some times
            #
            trials.addData('trialEndWallTime', time.ctime())
            trials.addData('actualItiOffset', fmriClock.getTime())
            
            trials.addData('reward', reward)
            rewards.append(reward)
            
            
            print 'Total number of rewards:', len(rewards)
            
            r = np.random.choice(rewards)
            print 'subject reward:', r
            flushEntries()
            # check responses
            if responseKey.keys in ['', [], None]:  # No response was made
               responseKey.keys=None
               # was no response the correct answer?!
               if str('').lower() == 'none': responseKey.corr = 1  # correct non-response
               else: responseKey.corr = 0  # failed to respond (incorrectly)
            # store data for trials (TrialHandler)
            trials.addData('responseKey.keys',responseKey.keys)
            trials.addData('responseKey.corr', responseKey.corr)
            if responseKey.keys != None:  # we had a response
                trials.addData('responseKey.rt', responseKey.rt)
            # the Routine "trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'blocks'
    
    
    #------Prepare to start Routine "fixationCross"-------
    t = 0
    fixationCrossClock.reset()  # clock 
    frameN = -1
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationCrossComponents = []
    fixationCrossComponents.append(fixationCross1)
    for thisComponent in fixationCrossComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixationCross"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationCrossClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixationCross1* updates
        if t >= 0.0 and fixationCross1.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationCross1.tStart = t  # underestimates by a little under one frame
            fixationCross1.frameNStart = frameN  # exact frame index
            fixationCross1.setAutoDraw(True)
        if fixationCross1.status == STARTED and t >= (0.0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixationCross1.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fixationCross"-------
    for thisComponent in fixationCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'runs'






# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
