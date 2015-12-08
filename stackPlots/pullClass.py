#!/bin/python
from ROOT import *
from copy import deepcopy
from math import *
from array import array
from pullUtils import *


class myStack:
	myHistograms = []
	tStack = ''
	mySumHists = ''
	myData = ''
	dataLegend = ''
	varName = ''
	dirName = ''
	lumi = ''
	def __init__(self, name, title, varName, dirName, lumi):
		self.myHistograms = []
		self.mySignals = []
		self.tStack = ''
		self.mySumHists = ''
		self.myData = ''
		self.dataLegend = ''
		self.varName = ''
		self.tStack = THStack(str(name), str(title))
		self.varName = varName
		self.dirName = dirName
		self.lumi = lumi
		self.SUM = ''
	def addHist(self, hist, legend, norm):
		self.myHistograms.append([deepcopy(hist), str(legend), norm])
	def addSignal(self, hist, legend, norm):
		self.mySignals.append([deepcopy(hist), str(legend), norm])
	def addData(self, hist, legend):
		self.myData = deepcopy(hist)
		self.dataLegend = legend
	def drawStack(self, fileName):
		if len(self.myHistograms) < 1:
			print 'Your list of histograms is empty!'
			return 0
		if self.myData == '':
			print "You haven't added a data histogram!"
			return 0
		mySumHists = self.myHistograms[0][0].Clone("mySumHists")
		mySumHists.Reset()
#		legend = TLegend(0.11, 0.65, 0.89, 0.9)
#		legend.AddEntry(self.myData, self.dataLegend, "lep")
		for Hist in self.myHistograms:
			hist = Hist[0]
#			hist.Sumw2()
			self.tStack.Add(hist)
			mySumHists.Add(hist,1)
#			legend.AddEntry(hist, Hist[1], 'f')
#		self.tStack.SetMinimum(-0.1)
		generalMaximus = max( self.myData.GetMaximum(), self.tStack.GetMaximum() )
		self.tStack.SetMaximum(generalMaximus*1.5)
		pullHandE = doPull(mySumHists, self.myData, self.tStack)
		pullH = pullHandE[0]
		pullE = pullHandE[1]
		LowEdge = pullHandE[2]
		UpEdge = pullHandE[3]
		self.SUM = self.tStack.GetStack().Last().Clone("SUM")
		self.SUM.SetLineWidth(0)
		self.SUM.SetFillColor(15)
		self.SUM.SetFillStyle(3254)
		legend = MakeLegend(self.myHistograms, self.myData, self.lumi, self.mySignals, self.SUM)
		SavePull(pullH, pullE, LowEdge, UpEdge, self.dirName)
		SaveNoPull(self.myData, self.tStack, fileName)
		SaveWithPull(self.myData, self.tStack, legend, pullH, pullE, fileName, self.varName, self.dirName, self.lumi, self.mySignals, self.SUM)

