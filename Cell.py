import numpy as np
import math
import random


class Cell:
	bIsFilled = False
	vbPossible = [True] * 9
	nVal = 0


	def Fill(self, nNumber):
		self.nVal = nNumber
		self.bIsFilled = True


	def SetNotPossible(self, nNumber):
		self.vbPossible[nNumber - 1] = False


	def GetNumOfPossible(self):
		if self.bIsFilled:
			return 0
		else:
			return sum(self.vbPossible)
