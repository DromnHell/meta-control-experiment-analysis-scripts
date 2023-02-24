#!/usr/bin/env python3
#encoding: utf-8

# ---------------------------------------------------------------------------
# IMPORT
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import math
import statistics
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
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MF/real/exp1_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MF/real/exp2_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MF/real/exp3_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MF/real/exp4_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MF/real/exp5_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MF/real/exp6_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MF/real/exp7_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MF/real/exp8_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MF/real/exp9_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MF/real/exp10_alpha0.6_gamma0.9_beta100/allReward_log.dat"
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
yAll = list()
xAll = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	cumulatedReward = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		a = 0
		for line in file1:
			a += 1
			cumulatedReward += int(line.split(" ")[2].rstrip())
			if int(line.split(" ")[2].rstrip()) == 1:
				y.append(a)
				a = 0
		x = list(range(1,cumulatedReward+1))
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c = color[i], label = "exp"+str(i+1), alpha = 0.4, zorder = 2)
	yAll.append(y)
	xAll.append(x)
	i += 1
# ---------------------------------------------------------------------------
maxLen = 0
# ---------------------------------------------------------------------------
for expe in xAll:
	if len(expe) > maxLen:
		maxLen = len(expe)
xMean = list(range(1, maxLen+1))
yMean = [0 for i in range(maxLen)]
ySD = [0 for i in range(maxLen)]
#-----------------------------------------------------------------------------
for it in xMean:
	d = 0
	for expe in yAll:
		if it <= len(expe):
			yMean[it-1] += expe[it-1]
			d += 1
	yMean[it-1] = yMean[it-1] / d
#-----------------------------------------------------------------------------
for it in xMean:
	d = 0
	accu = 0
	for expe in yAll:
		if it <= len(expe):
			accu += (expe[it-1] - yMean[it-1])**2
			d += 1
	ySD[it-1] += math.sqrt(accu / d)
#-----------------------------------------------------------------------------
#plt.plot(xMean, yMean, c = "black", label = "Mean", zorder = 1, linewidth = 3, alpha = 0.8)
#plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color = "grey", zorder = 1, alpha = 0.5)
plt.plot(xMean, yMean, c = "red", label = "Hab", zorder = 1, linewidth = 3, alpha = 0.8)
plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color = "red", zorder = 1, alpha = 0.5)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# EXPE ON REAL WORLD / MB OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MB/real/exp1_gamma0.9_beta100/allReward_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MB/real/exp2_gamma0.9_beta100/allReward_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MB/real/exp3_gamma0.9_beta100/allReward_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MB/real/exp4_gamma0.9_beta100/allReward_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MB/real/exp5_gamma0.9_beta100/allReward_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MB/real/exp6_gamma0.9_beta100/allReward_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MB/real/exp7_gamma0.9_beta100/allReward_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MB/real/exp8_gamma0.9_beta100/allReward_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MB/real/exp9_gamma0.9_beta100/allReward_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/MB/real/exp10_gamma0.9_beta100/allReward_log.dat"
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
yAll = list() 
xAll = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	cumulatedReward = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		a = 0
		for line in file1:
			a += 1
			cumulatedReward += int(line.split(" ")[2].rstrip())
			if int(line.split(" ")[2].rstrip()) == 1:
				y.append(a)
				a = 0
		x = list(range(1,cumulatedReward+1))
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c = color[i], label = "exp"+str(i+1), alpha = 0.4, zorder = 2)
	yAll.append(y)
	xAll.append(x)
	i += 1
# ---------------------------------------------------------------------------
maxLen = 0
# ---------------------------------------------------------------------------
for expe in xAll:
	if len(expe) > maxLen:
		maxLen = len(expe)
xMean = list(range(1, maxLen+1))
yMean = [0 for i in range(maxLen)]
ySD = [0 for i in range(maxLen)]
#-----------------------------------------------------------------------------
for it in xMean:
	d = 0
	for expe in yAll:
		if it <= len(expe):
			yMean[it-1] += expe[it-1]
			d += 1
	yMean[it-1] = yMean[it-1] / d
#-----------------------------------------------------------------------------
for it in xMean:
	d = 0
	accu = 0
	for expe in yAll:
		if it <= len(expe):
			accu += (expe[it-1] - yMean[it-1])**2
			d += 1
	ySD[it-1] += math.sqrt(accu / d)
#-----------------------------------------------------------------------------
#plt.plot(xMean, yMean, c = "black", label = "Mean", zorder = 1, linewidth = 3, alpha = 0.8)
#plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color = "grey", zorder = 1, alpha = 0.5)
plt.plot(xMean, yMean, c = "blue", label = "GD", zorder = 1, linewidth = 3, alpha = 0.8)
plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color = "blue", zorder = 1, alpha = 0.5)
# ---------------------------------------------------------------------------



# ---------------------------------------------------------------------------
# SHOW
# ---------------------------------------------------------------------------
plt.grid(linestyle='--')
plt.xlabel("Reward")
#plt.ylabel("Number of actions from the reward")
plt.ylabel("Mean number of actions from the reward")
plt.legend()
plt.show()
# ---------------------------------------------------------------------------

