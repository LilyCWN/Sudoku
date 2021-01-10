import numpy as np
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


    def VerifyNineNumbers(self, vnTemp):
        vbTemp = np.full(9, False, dtype = bool)
        for i in range(0, 9):
            if ((vnTemp[i] < 1) or (vnTemp[i] > 9)):
                return False
            vbTemp[vnTemp[i - 1]] = True
        return (np.sum(vbTemp) == 9)


    def VerifyRow(self, i, j):
        return self.VerifyNineNumbers(self.vnArr[i, :])


    def VerifyColumn(self, i, j):
        return self.VerifyNineNumbers(self.vnArr[: j], (9, 1))


    def VerifyBlock(self, i, j):
        q = floor(i / 3);
        w = floor(j / 3);
        vbTemp = np.resize(self.vnArr[q: q + 3, w: w + 3], (9, 1))
        return self.VerifyNineNumbers(vbTemp)


    def VerifyCell(self, i, j):
        return self.VerifyRow(i, j) and \
            self.VerifyColumn(i, j) and \
            self.VerifyBlock(i, j)


    def VerifySudoku(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if (not self.VerifyCell(i, j)):
                    return False
        return True
