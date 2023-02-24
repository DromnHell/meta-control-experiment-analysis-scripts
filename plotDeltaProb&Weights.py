#!/usr/bin/env python3
#encoding: utf-8

# ---------------------------------------------------------------------------
# IMPORT
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import statistics
import math
from scipy.interpolate import spline
from operator import add
import sys
import os
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# COLOR
# ---------------------------------------------------------------------------
color = ["red","royalblue","darkgreen","gold","purple","lawngreen","peru","c","navy","fuchsia"]
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# EXPE ON REAL WORLD / MF OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MF/real/exp1_alpha0.6_gamma0.9_beta100_optimistic/allDeltaWeights_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MF/real/exp2_alpha0.6_gamma0.9_beta100_optimistic/allDeltaWeights_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MF/real/exp3_alpha0.6_gamma0.9_beta100_optimistic/allDeltaWeights_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MF/real/exp4_alpha0.6_gamma0.9_beta100_optimistic/allDeltaWeights_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MF/real/exp5_alpha0.6_gamma0.9_beta100_optimistic/allDeltaWeights_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MF/real/exp6_alpha0.6_gamma0.9_beta100_optimistic/allDeltaWeights_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MF/real/exp7_alpha0.6_gamma0.9_beta100_optimistic/allDeltaWeights_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MF/real/exp8_alpha0.6_gamma0.9_beta100_optimistic/allDeltaWeights_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MF/real/exp9_alpha0.6_gamma0.9_beta100_optimistic/allDeltaWeights_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MF/real/exp10_alpha0.6_gamma0.9_beta100_optimistic/allDeltaWeights_log.dat"
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
yAll = list()
xAll = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	cumulatedWeights = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		l = 0
		for line in file1:
			x.append(l)
			deltaWeight = 20*(math.fabs(float(line.split(" ")[2].rstrip())))
			cumulatedWeights += deltaWeight
			y.append(deltaWeight)
			l += 1
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c=color[i], label="exp"+str(i+1))
	yAll.append(y)
	xAll.append(x)
	# -----------------------------------------------------------------------
	i += 1
# ---------------------------------------------------------------------------
minLen = 1000000000000
# ---------------------------------------------------------------------------
for l in xAll:
	if len(l) < minLen:
		minLen = len(l)
		xMean = l
# ---------------------------------------------------------------------------
yMean = [0] * minLen
# ---------------------------------------------------------------------------
yMean = [statistics.mean(k) for k in zip(yAll[0],yAll[1],yAll[2],yAll[3],yAll[4],yAll[5],yAll[6],yAll[7],yAll[8],yAll[9])]
ySD = [statistics.pstdev(k) for k in zip(yAll[0],yAll[1],yAll[2],yAll[3],yAll[4],yAll[5],yAll[6],yAll[7],yAll[8],yAll[9])]
#-------------------------------------------------------------------c---------
plt.plot(xMean, yMean, c="blue", label="MF")
plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="blue", alpha=0.2)
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# EXPE ON REAL WORLD / MB OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MB/real/exp1_gamma0.95_beta40_optimistic/allDeltaProb_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MB/real/exp2_gamma0.95_beta40_optimistic/allDeltaProb_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MB/real/exp3_gamma0.95_beta40_optimistic/allDeltaProb_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MB/real/exp4_gamma0.95_beta40_optimistic/allDeltaProb_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MB/real/exp5_gamma0.95_beta40_optimistic/allDeltaProb_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MB/real/exp6_gamma0.95_beta40_optimistic/allDeltaProb_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MB/real/exp7_gamma0.95_beta40_optimistic/allDeltaProb_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MB/real/exp8_gamma0.95_beta40_optimistic/allDeltaProb_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MB/real/exp9_gamma0.95_beta40_optimistic/allDeltaProb_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/MB/real/exp10_gamma0.95_beta40_optimistic/allDeltaProb_log.dat"
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
yAll = list()
xAll = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	cumulatedProb = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		l = 0
		for line in file1:
			x.append(l)
			deltaProb = float(line.split(" ")[3].rstrip())
			cumulatedProb += deltaProb
			y.append(deltaProb)
			l += 1
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c=color[i], label="exp"+str(i+1))
	yAll.append(y)
	xAll.append(x)
	# -----------------------------------------------------------------------
	i += 1
# ---------------------------------------------------------------------------
minLen = 1000000000000
# ---------------------------------------------------------------------------
for l in xAll:
	if len(l) < minLen:
		minLen = len(l)
		xMean = l
# ---------------------------------------------------------------------------
yMean = [0] * minLen
# ---------------------------------------------------------------------------
yMean = [statistics.mean(k) for k in zip(yAll[0],yAll[1],yAll[2],yAll[3],yAll[4],yAll[5],yAll[6],yAll[7],yAll[8],yAll[9])]
ySD = [statistics.pstdev(k) for k in zip(yAll[0],yAll[1],yAll[2],yAll[3],yAll[4],yAll[5],yAll[6],yAll[7],yAll[8],yAll[9])]
#-------------------------------------------------------------------c---------
plt.plot(xMean, yMean, c="red", label="MB")
plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="red", alpha=0.2)

# ---------------------------------------------------------------------------
# SHOW
# ---------------------------------------------------------------------------
plt.grid(linestyle='--')
plt.xlabel("Number of actions")
plt.ylabel("Delta prob & weights")
plt.legend()
plt.show()
# ---------------------------------------------------------------------------














