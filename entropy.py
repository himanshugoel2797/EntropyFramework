import entropyCalculators
import os

def analyzeFile(filename):
    srcFile = open(filename, 'rb')
    srcFile.seek(0, os.SEEK_END)
    size = srcFile.tell()
    srcFile.seek(0, os.SEEK_SET)
    data = srcFile.read()
    return {entropyCalculators.shannonEntropy(data, len(data)), entropyCalculators.monteCarloEstimation(data, len(data)), entropyCalculators.probabilityRatio(data, len(data))} 