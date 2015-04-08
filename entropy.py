import entropyCalculators
import os

def analyzeFile(filename):
    srcFile = open(filename, 'rb')
    srcFile.seek(0, os.SEEK_END)
    size = srcFile.tell()
    srcFile.seek(0, os.SEEK_SET)
    data = srcFile.read()
    return {entropyCalculators.shannonEntropy(data, len(data)), entropyCalculators.monteCarloEstimation(data, len(data)), entropyCalculators.probabilityRatio(data, len(data))}

def analyzeByteMap(data, length):
    probabilityHistogram = {}
    occuranceCount = {}
    for i in range(0, 256):
        probabilityHistogram[i] = {}
        occuranceCount[i] = 0
        for j in range(0, 256):
            probabilityHistogram[i][j] = 0
 #Just finished setting up the probability histogram for all bytes so that we
 #can sample individual probabilities depending on hte byte ordering
    for i in range(0, length - 1):
        probabilityHistogram[data[i]][data[i + 1]] += 1
        occuranceCount[data[i]] += 1
    for i in range(0, 256):
        for j in range(0, 256):
            if probabilityHistogram[i][j] != 0:
               probabilityHistogram[i][j] /= occuranceCount[i]
    return probabilityHistogram

def analyzeByteMapFile(filename):
    srcFile = open(filename, 'rb')
    srcFile.seek(0, os.SEEK_END)
    size = srcFile.tell()
    srcFile.seek(0, os.SEEK_SET)
    data = srcFile.read()
    return analyzeByteMap(data, len(data))

def analyzeByteMapFileToFile(filename, outFile):
    probabilityHist = analyzeByteMapFile(filename)
    oFile = open(outFile, 'w')
    for i in range(0, 256):
        oFile.write(str(i) + ":" + "\n")
        for j in range(0, 256):
            if probabilityHist[i][j] != 0:
               oFile.write("\t" + str(j) + ":\t" + str(probabilityHist[i][j]) + "\n")