#################################
# Auxiliary file that contains the functions check_outputs() and process_patterns()
# used in assignment 1.
#   process_patterns(): reads in the input patterns from a file called *pattern.in* 
#   and passes them to the *processingElement* object. The pattern file consists of 
#   per line. It generates a list of outputs, one per pattern and returns it.

#   check_outputs(): reads in the outputs that are supposed to be generated from a file 
#   called *check.out* and checks them with what your class computed. It will print 
#   "success" if your program worked, and "incorrect" if something went wrong. Because 
#   different systems have different degrees of precision, it will compare the values 
#   truncated to 4 decimal points using the helper_truncate() function defined at the top.
import math

def process_patterns(PE):
    '''This function opens a file called "patterns.in" and reads in one line at a time, 
    creating the pattern list that is then fed to the processing element that was passed in.'''
    patternFile = open("patterns.in","r")
    numPatterns = int(patternFile.readline())
    
    outputs = []
    for line in range(numPatterns):
        readPattern = patternFile.readline().split(",")
        patternValues = [float(value) for value in readPattern]
    
        outputs.append(PE.generate_output(patternValues))
    patternFile.close()
    
    return outputs

def helper_truncate( number, decimal_places=0 ):
    '''Custom made function to truncate a floating point (decimal) number to a certain number \
    of places.'''
    multiplier = 10 **decimal_places
    return math.trunc(number*multiplier) / multiplier

def check_outputs( outputs ):
    '''Thsis function takes the list of values and compares them to the values in the "check.out" file. 
    If they all match, it will print "SUCCESS" and "INCORRECT" and the output that failed otherwise.'''
    
    # First, read the check values from the file.
    checkFile = open("checks.out","r")
    numChecks = int(checkFile.readline()) # how many are there?
    if numChecks != len(outputs):
        print("MISMATCH: File has "+str(numChecks)+" values, but program has "+str(len(outputs)))
        return
    readChecks = checkFile.readline().split()
    checks = [float(item) for item in readChecks]
    checkFile.close()

    # right here, we use the helper_truncate function to truncate both output and check
    # values to 4 decimal places before comparing them. If there is a mismatch, set
    # match to False.
    precision = 4
    for index in range(numChecks):
        truncOutput = helper_truncate( outputs[index], precision)
        truncCheck = helper_truncate( checks[index], precision)
        if truncOutput != truncCheck:
            print("INCORRECT: Pattern["+str(index)+"] Expected - "+str(truncCheck)+" generated - "+str(truncOutput))
            return
    
    # if we got to this point, everything matches. Hooray!
    print("SUCCESS")

def values_differ( produced, expected ):
    return helper_truncate(produced, 4) != helper_truncate(expected, 4)

def check_input_layer_outputs(ann, patternIndex):
    
    checksFile = open("checkInputLayerOutputs.out", "r")
    # We want to skip over whichPattern number of lines.
    for i in range(patternIndex):
        temp = checksFile.readline()
    success = True
    checkValues = [float(item) for item in checksFile.readline().split()]
    
    index=0
    for checkValue in checkValues:
        if values_differ(ann.inputLayerOutput[index], checkValue):
            success = False
            print("ERROR at pattern[{}]: check[{}] is {}".format(patternIndex,index,checkValue)+\
                  ", but inputPE[{}] is {}.".format(index, ann.inputLayerOutput[index]))
        index = index + 1
    if success:
        print("INPUT LAYER NORMALIZING for PATTERN {} SUCCESSFULLY COMPLETED!".format(patternIndex))
    checksFile.close()

def check_hidden_layer_outputs(ann, patternIndex):
    
    checksFile = open("checkHiddenLayerOutputs.out", "r")
    # We want to skip over whichPattern number of lines.
    for i in range(patternIndex):
        temp = checksFile.readline()
    success = True
    checkValues = [float(item) for item in checksFile.readline().split()]
    
    index=0
    for checkValue in checkValues:
        if values_differ( ann.hiddenLayerOutput[index], checkValue) :
            success = False
            print("ERROR at pattern[{}]: check[{}] is {}".format(patternIndex,index,checkValue)+\
                  ", but inputPE[{}] is {}.".format(index, ann.hiddenLayerOutput[index]))
        index = index + 1
    if success:
        print("HIDDEN LAYER OUTPUT FOR PATTERN {} SUCCESSFULLY COMPLETED!".format(patternIndex))
    checksFile.close()

def check_outputs(ann, patternIndex):
    
    checksFile = open("checkOutputs.out", "r")
    # We want to skip over whichPattern number of lines.
    for i in range(patternIndex):
        temp = checksFile.readline()
    success = True
    checkValues = [float(item) for item in checksFile.readline().split()]
    
    index=0
    for checkValue in checkValues:
        if values_differ( ann.output[index], checkValue) :
            success = False
            print("ERROR at pattern[{}]: check[{}] is {}".format(patternIndex,index,checkValue)+\
                  ", but inputPE[{}] is {}.".format(index, ann.output[index]))
        index = index + 1
    if success:
        print("OUTPUT LAYER OUTPUT FOR PATTERN {} SUCCESSFULLY COMPLETED!".format(patternIndex))
    checksFile.close()
