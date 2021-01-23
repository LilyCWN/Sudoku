import numpy as np
import math
import random
from tkinter import *
from Cell import Cell

class Sudoku:
	vCell = [[Cell()] * 9] * 9
	vnArr = np.zeros((9, 9), dtype = int) # a 2d array representing the sudoku
	nRandomSeed = 1
	table = Tk()
	vEntry = [[0] * 9] * 9
	vnEntryVal = []


	def HandleClickEvent(self, event):
		print("clicked!")
		self.PrintSudoku(True)


	def test(self, i, j):
		self.FillCell(i, j, self.vnEntryVal[i * 9 + j].get())
		self.PrintSudokuConsole()


	def PrintSudokuGUI(self):
		# table.bind("<1>", self.HandleClickEvent)
		for i in range(0, 9):
			for j in range(0, 9):
				self.vnEntryVal.append(StringVar())
				bg = '#EEEEEE' if (((i % 3) != 2) and ((j % 3) != 2)) else '#BEBEBE'
				self.vEntry[i][j] = Entry(self.table, width = 2, fg = 'blue', font = ('Consolas', 16, 'bold'),\
					justify = CENTER, textvariable = self.vnEntryVal[i * 9 + j], bg = bg)
				self.vEntry[i][j].bind ("<FocusOut>", \
					lambda event, a = i, b = j: self.test(a, b))
				self.vEntry[i][j].grid(row = i, column = j)
				self.vEntry[i][j].insert(END, self.vnArr[i][j])
				# create root window
				#!/usr/bin/env python
		self.table.mainloop()


	def PrintSudoku(self, bConsole = False):
		if (not bConsole):
			return self.PrintSudokuGUI()
		else:
			return self.PrintSudokuConsole()


	def PrintSudokuConsole(self):
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


	def FillCell(self, i, j, nVal):
		self.vnArr[i, j] = nVal
		(self.vCell[i][j]).Fill(nVal)


	def RandomizeSudoku(self, nSeed = 1):
		np.random.seed(nSeed) # apply the seed
		random.seed(nSeed)

		vnStaticList = np.arange(1, 10) # array with element 1 - 9
		np.random.shuffle(vnStaticList)
		for i in range(0, 9):
			self.FillCell(0, i, vnStaticList[i]) # generate 1st row
