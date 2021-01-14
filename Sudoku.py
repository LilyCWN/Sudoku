import numpy as np
import math
import random

class Sudoku:
    vnArr = np.zeros((9, 9), dtype = int) # a 2d array representing the sudoku
    nRandomSeed = 1


    def PrintSudoku(self):
        print("-------------")
        for i in range(0, 9):
            strTemp = "|"
            for j in range(0, 9):
                strTemp = strTemp + str(self.vnArr[i][j])
                if (((j + 1) % 3) == 0):
                    strTemp = strTemp + "|"
            print(strTemp)
            if (((i + 1) % 3) == 0):
                print("-------------")


    def VerifyNineNumbers(self, vnTemp, bCanHaveBlanks = False):
        print(vnTemp)
        vbTemp = np.full(9, False, dtype = bool)
        if (not bCanHaveBlanks):
            for i in range(0, 9):
                if ((vnTemp[i] < 1) or (vnTemp[i] > 9)):
                    return False
                vbTemp[vnTemp[i] - 1] = True
            return (np.sum(vbTemp) == 9)
        else: # verify all element is unique except for blanks
            for i in range(0, 9):
                if ((vnTemp[i] >= 1) and (vnTemp[i] <= 9)):
                    if (vbTemp[vnTemp[i] - 1]):
                        return False
                    vbTemp[vnTemp[i] - 1] = True
            return True


    def VerifyRow(self, i, bCanHaveBlanks = False):
        print("VerifyRow: " + str(i))
        return self.VerifyNineNumbers(self.vnArr[i, :], bCanHaveBlanks)


    def VerifyColumn(self, j, bCanHaveBlanks = False):
        print("VerifyColumn: " + str(j))
        return self.VerifyNineNumbers(np.resize(self.vnArr[:, j], (9)), bCanHaveBlanks)


    def VerifyBlock(self, i, j, bCanHaveBlanks = False):
        q = math.floor(i / 3) * 3;
        w = math.floor(j / 3) * 3;
        vbTemp = np.resize(self.vnArr[q: q + 3, w: w + 3], (9))
        print("VerifyBlock: " + str(i) + ", " + str(j))
        return self.VerifyNineNumbers(vbTemp, bCanHaveBlanks)


    def VerifyCell(self, i, j, bCanHaveBlanks = False):
        return self.VerifyRow(i, bCanHaveBlanks) and \
            self.VerifyColumn(j, bCanHaveBlanks) and \
            self.VerifyBlock(i, j, bCanHaveBlanks)


    def VerifySudoku(self, bCanHaveBlanks = False):
        for i in range(0, 9):
            if (not self.VerifyRow(i, bCanHaveBlanks)):
                return False
        for j in range(0, 9):
            if (not self.VerifyColumn(j, bCanHaveBlanks)):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if (not self.VerifyBlock(i, j, bCanHaveBlanks)):
                    return False
        return True


    def RandomizeSudoku(self, nSeed = 1):
        np.random.seed(nSeed) # apply the seed
        random.seed(nSeed)

        vnStaticList = np.arange(1, 10) # array with element 1 - 9
        np.random.shuffle(vnStaticList)
        self.vnArr[0, :] = vnStaticList # generate 1st row
