## YOU DO NOT NEED TO DO ANYTHING TO THIS CELL, EXCEPT TO RUN IT.
import math

def sigmoid(input):
    '''Custom made function to calculate the sigmoid function given an input'''
    return 1/(1+math.exp(-input))

class processingElement:
    def __init__(self, weightFile, nWeights=0):
        self.numWeights = nWeights
        inWeights = weightFile.readline().split()
        self.weights = [ float(item) for item in inWeights]
        if self.numWeights != len(self.weights):
            print("weights do not match! "+self.numWeights+" versus "+len(self.weights))
            self.numWeights = len(self.weights)

    def generate_output(self, pattern):
        '''This function takes as input a set of input patterns and generates the sigmoid operation 
        of the sum of projects with the pattern and the associated weights. It returns that value.'''
        
        # check to make sure that the number of pattern values match 
        if len(pattern) != self.numWeights:
            print("pattern {} and weight {} number mismatch!".format(len(pattern), self.numWeights) )
            return 1

        sumProduct = 0
        patternIndex = 0
        for weight in self.weights:
            sumProduct = sumProduct + (weight * pattern[patternIndex])
            patternIndex = patternIndex + 1

        sigmoidValue = sigmoid(sumProduct)
        return sigmoidValue
