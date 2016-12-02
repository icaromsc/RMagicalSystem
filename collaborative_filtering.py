import numpy
import math

#similarity score
highSimilarity=1
highSimilarity=0.5
nothing=0

pc = numpy.corrcoef([1,2,3], [1,5,7])
print numpy.corrcoef([1,2,3], [1,5,7])

#testando algoritmo do calculo do coeficiente de Pearson
def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)


def similarity(pUsers):
    '''find the most user similarity based on Pearson of pUser analysed '''
    min(pUsers, key=lambda x: abs(x - highSimilarity))


def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)


print pearson_def([1,2,3], [1,5,7])
