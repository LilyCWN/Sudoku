class Sudoku:
    vArr = [ [0] * 9 for i in range(9)] # a 2d array representing the sudoku


    def PrintSudoku(self):
        print("-------------")
        for i in range(0, 9):
            strTemp = "|"
            for j in range(0, 9):
                strTemp = strTemp + str(self.vArr[i][j])
                if (((j + 1) % 3) == 0):
                    strTemp = strTemp + "|"
            print(strTemp)
            if (((i + 1) % 3) == 0):
                print("-------------")
