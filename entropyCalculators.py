import math

def buildHistogram(data, len):
    histogram = {}
    for i in range(0, len):
        if data[i] in histogram:
            histogram[data[i]]+=1
        else:
            histogram[data[i]] = 1
    return histogram

def shannonEntropy(data, length):
    entropy = 0
    histogram = buildHistogram(data, length)
    for b in histogram.keys():
        frequency = histogram[b] / length
        entropy += frequency * math.log2(frequency)
    return -entropy

def probabilityRatio(data, length):
    entropy = 0
    histogram = buildHistogram(data, length)
    for b in histogram.keys():
        entropy += histogram[b] / length
    entropy /= len(histogram.keys())
    return (1 / 255) / entropy

def monteCarloEstimation(data, length):
    expectedValue = (254 * math.exp(255))
    entropy = 0
    for b in range(0, length):
        entropy += data[b] * math.exp(data[b])
    entropy /= length
    entropy /= expectedValue
    if entropy > 1:
        entropy -= 1
    return entropy
