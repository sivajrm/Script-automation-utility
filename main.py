import sys
import time
import concurrent.futures
import subprocess
testInfodict={}

def executeFunc(procName):   							#To start the execution of the file processing i.e, opening a notepad      
    proc=subprocess.Popen([sys.executable, "func.py"])  #Here, if the developer has the actualFile, then the actualFile will be taken in the Popen() argument for file name
    print("Executing File Name:",procName," having File ID:",proc.pid)
    start= time.time()
    new_process = {'started':start,'name':procName}
    testInfodict[proc.pid]=new_process
    
def getInputFromUser(): 						         #to get the input and pass it to the main function
    print("Enter the files in a single line single spaced to execute in parallel or in new line to execute after the previous tasks...")
    print("Enter # in new line to begin processing")
    inp = ""
    while True:
        inputFiles = input()
        if inputFiles.find('#') == -1:			         #to terminate the input
            inp += inputFiles+'\n'
        else:
            break
    singleLineFiles = inp.split('\n')                    #parse file names by new line
    print (singleLineFiles)
    return singleLineFiles

def addKilledEntryToDict(pid,end):						 #updating the ended_time of the file in the dictionary
    try:
        testInfodict[pid]["ended"] = end				
    except KeyError:
        testInfodict[pid] = {"ended": end}

                
def calculateStats():								    #for outputting the test statistics
    print("\n\n-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    print("OVERALL STATS FOR THE EXECUTION")
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    print("\nFILE NAME     START             TO       END                      TIME TAKEN")
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    for eachProcess in testInfodict:
        print(testInfodict[eachProcess]["name"],"\t-> ",testInfodict[eachProcess]["started"],"\tto ",testInfodict[eachProcess]["ended"],"\ttaking:",testInfodict[eachProcess]["ended"]-testInfodict[eachProcess]["started"])
        
def startExecting(inputFromMain):                      #Driver to do the execution of the input Files
    getFuncInParallel=[]
    for eachLine in inputFromMain:
        getFuncInParallel=eachLine.split(' ')          #parse the file for concurrent execution provided on the single line single spaced
        for eachFile in getFuncInParallel: 
            if eachFile == '':                         #if file name contains only space remove that file
                getFuncInParallel.remove(eachFile)
        if len(getFuncInParallel) > 0:
            print("\n\nExecuting concurrently:",getFuncInParallel)    
            NUM_WORKERS = len(getFuncInParallel) 
            start_time = time.time()
            with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:    #Concurrent execution block
                future={executor.submit(executeFunc,fileName) for fileName in getFuncInParallel}
                concurrent.futures.wait(future)
            n=0
            while n < len(getFuncInParallel):         #to wait for all files provided in the single line to finish processing
                kill=input("\n\nEnter 'end <space> file_ID' to end the file execution: ")
                kill = kill.lower()
                cmd=[]
                cmd=kill.split(' ')
                if cmd[0] == 'end':
                    pid=int(cmd[1])
                    if pid in testInfodict:
                        subprocess.Popen("taskkill /F /T /PID %i"%int(pid), shell=True) #ending the required file execution
                        end=time.time()
                        addKilledEntryToDict(int(pid),end)
                        print("Ended executing file with ID:",pid)
                        n+=1
                    else:
                        print("Entered File ID",pid,"does not exist")
                else:
                    print("Err! Please re-enter correct command")
            end_time = time.time()        
            print("Time for the current step test execution: %ssecs" % (end_time - start_time))
        
def isEmpty(s):                     #check if string is Empty
    return not bool(s and s.strip())

if __name__ == "__main__": 
    singleLineFiles=getInputFromUser() 
    if not isEmpty(singleLineFiles[0]):
        startExecting(singleLineFiles)
    else:
        print("No input files to execute")    
    calculateStats()
