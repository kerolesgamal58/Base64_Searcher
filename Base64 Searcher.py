import base64
import sys

strToBeEncoded = sys.argv[1]
noOfLevels = sys.argv[2]


def getBase64(strToBeEncoded):
    return base64.b64encode(strToBeEncoded.encode("ascii")).decode("ascii")

def getWorstCaseBothSides(strToBeEncoded, index):
    beginAt = 0
    # if index == 0:
    if index == 1:
        beginAt = 2             # the third char
        strToBeEncoded = "x" + strToBeEncoded
    elif index == 2:
        beginAt = 3
        strToBeEncoded = "xx" + strToBeEncoded
    strLength = len(strToBeEncoded)
    endAt = strLength * 4 // 3
    return getBase64( strToBeEncoded )[beginAt:endAt + 1]

def joinArrToString(arrToBeJoined):
    return "|".join(arrToBeJoined)

def getWorstCaseAtLevel(arrOfStrToBeEncoded):
    posibilities = []
    for strToBeEncoded in arrOfStrToBeEncoded:
        for i in range(3):
            posibilities.append(getWorstCaseBothSides(strToBeEncoded, i))
    return posibilities

def getWorstCases(strToBeEncoded, noOfLevels):
    arrOfEncodedLevels = []
    arrOfStrToBeEncoded = [strToBeEncoded]
    x = []
    for s in range(noOfLevels):
        x = getWorstCaseAtLevel( arrOfStrToBeEncoded )
        arrOfEncodedLevels.append( joinArrToString(x) )
        arrOfStrToBeEncoded = x
    return arrOfEncodedLevels

a = getWorstCases(strToBeEncoded, int(noOfLevels))
print(a)

