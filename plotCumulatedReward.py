#!/usr/bin/env python3
#encoding: utf-8

# ---------------------------------------------------------------------------
# IMPORT
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import statistics
from scipy import stats
from scipy.interpolate import spline
from operator import add
import sys
import os
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# COLOR
# ---------------------------------------------------------------------------
color = ["lightpink","royalblue","darkgreen","gold","purple","lawngreen","peru","coral","navy","fuchsia","springgreen"]
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# SIMULATION ON SQUARES WORLD / MF OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onSquaresWorld/optimisticQ1/exp1_alpha0.6_gamma0.9_beta100/v1_TBMF_exp1_reward_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onSquaresWorld/optimisticQ1/exp2_alpha0.6_gamma0.9_beta100/v1_TBMF_exp2_reward_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onSquaresWorld/optimisticQ1/exp3_alpha0.6_gamma0.9_beta100/v1_TBMF_exp3_reward_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onSquaresWorld/optimisticQ1/exp4_alpha0.6_gamma0.9_beta100/v1_TBMF_exp4_reward_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onSquaresWorld/optimisticQ1/exp5_alpha0.6_gamma0.9_beta100/v1_TBMF_exp5_reward_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onSquaresWorld/optimisticQ1/exp6_alpha0.6_gamma0.9_beta100/v1_TBMF_exp6_reward_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onSquaresWorld/optimisticQ1/exp7_alpha0.6_gamma0.9_beta100/v1_TBMF_exp7_reward_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onSquaresWorld/optimisticQ1/exp8_alpha0.6_gamma0.9_beta100/v1_TBMF_exp8_reward_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onSquaresWorld/optimisticQ1/exp9_alpha0.6_gamma0.9_beta100/v1_TBMF_exp9_reward_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onSquaresWorld/optimisticQ1/exp10_alpha0.6_gamma0.9_beta100/v1_TBMF_exp10_reward_log.dat"
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
y_all = list()
x_all = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	cumulatedReward = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		l = 0
		for line in file1:
			x.append(l)
			cumulatedReward += int(line.split(" ")[2].rstrip())
			y.append(cumulatedReward)
			l += 1
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c=color[i])
	y_all.append(y)
	x_all.append(x)
	# -----------------------------------------------------------------------
	i += 1
# ---------------------------------------------------------------------------
minLen = 1000000000000
# ---------------------------------------------------------------------------
for l in x_all:
	if len(l) < minLen:
		minLen = len(l)
		xMean = l
# ---------------------------------------------------------------------------
yMean = [statistics.mean(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
ySD = [stats.sem(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])] 
# ---------------------------------------------------------------------------
#plt.plot(xMean, yMean, c="#996600", label="Hab - Squares world")
#plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="#996600", alpha=0.1)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# SIMULATION ON MODEL / MF NON OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/Hab_only/simu/onModel/nonOptimisticQ0/exp1_alpha0.8_gamma0.8_beta70/v2_TBMF_exp1_reward_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/Hab_only/simu/onModel/nonOptimisticQ0/exp2_alpha0.8_gamma0.8_beta70/v2_TBMF_exp2_reward_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/Hab_only/simu/onModel/nonOptimisticQ0/exp3_alpha0.8_gamma0.8_beta70/v2_TBMF_exp3_reward_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/Hab_only/simu/onModel/nonOptimisticQ0/exp4_alpha0.8_gamma0.8_beta70/v2_TBMF_exp4_reward_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/Hab_only/simu/onModel/nonOptimisticQ0/exp5_alpha0.8_gamma0.8_beta70/v2_TBMF_exp5_reward_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/Hab_only/simu/onModel/nonOptimisticQ0/exp6_alpha0.8_gamma0.8_beta70/v2_TBMF_exp6_reward_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/Hab_only/simu/onModel/nonOptimisticQ0/exp7_alpha0.8_gamma0.8_beta70/v2_TBMF_exp7_reward_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/Hab_only/simu/onModel/nonOptimisticQ0/exp8_alpha0.8_gamma0.8_beta70/v2_TBMF_exp8_reward_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/Hab_only/simu/onModel/nonOptimisticQ0/exp9_alpha0.8_gamma0.8_beta70/v2_TBMF_exp9_reward_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/Hab_only/simu/onModel/nonOptimisticQ0/exp10_alpha0.8_gamma0.8_beta70/v2_TBMF_exp10_reward_log.dat"
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
y_all = list()
x_all = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	cumulatedReward = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		l = 0
		for line in file1:
			x.append(l)
			cumulatedReward += int(line.split(" ")[2].rstrip())
			y.append(cumulatedReward)
			l += 1
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c=color[i])
	y_all.append(y)
	x_all.append(x)
	# -----------------------------------------------------------------------
	i += 1
# ---------------------------------------------------------------------------
minLen = 1000000000000
# ---------------------------------------------------------------------------
for l in x_all:
	if len(l) < minLen:
		minLen = len(l)
		xMean = l
# ---------------------------------------------------------------------------
yMean = [statistics.mean(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
ySD = [stats.sem(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
# ---------------------------------------------------------------------------
#plt.plot(xMean, yMean, c="red", label="Model of real world - non optimistic behavior")
#plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="red", alpha=0.1)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# SIMULATION ON MODEL / MF OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp1_beta100/v1_TBMC_exp1_expert_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp2_beta100/v1_TBMC_exp2_expert_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp3_beta100/v1_TBMC_exp3_expert_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp4_beta100/v1_TBMC_exp4_expert_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp5_beta100/v1_TBMC_exp5_expert_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp6_beta100/v1_TBMC_exp6_expert_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp7_beta100/v1_TBMC_exp7_expert_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp8_beta100/v1_TBMC_exp8_expert_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp9_beta100/v1_TBMC_exp9_expert_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp10_beta100/v1_TBMC_exp10_expert_log.dat"
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
y_all = list()
x_all = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	cumulatedReward = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		l = 0
		for line in file1:
			x.append(l)
			cumulatedReward += int(line.split(" ")[2].rstrip())
			y.append(cumulatedReward)
			l += 1
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c=color[i])
	y_all.append(y)
	x_all.append(x)
	# -----------------------------------------------------------------------
	i += 1
# ---------------------------------------------------------------------------
minLen = 1000000000000
# ---------------------------------------------------------------------------
for l in x_all:
	if len(l) < minLen:
		minLen = len(l)
		xMean = l
# ---------------------------------------------------------------------------
yMean = [statistics.mean(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
ySD = [stats.sem(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
# ---------------------------------------------------------------------------
#plt.plot(xMean, yMean, c="#ff9900", label="Hab - Model of real world")
#plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="#ff9900", alpha=0.1)
plt.plot(xMean, yMean, c="red", label="Hab only")
plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="red", alpha=0.1)
# ---------------------------------------------------------------------------









# ---------------------------------------------------------------------------
# SIMULATION ON SQUARES WORLD / MB OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onSquaresWorld/exp1_gamma0.9_beta100/v1_TBMB_exp1_reward_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onSquaresWorld/exp2_gamma0.9_beta100/v1_TBMB_exp2_reward_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onSquaresWorld/exp3_gamma0.9_beta100/v1_TBMB_exp3_reward_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onSquaresWorld/exp4_gamma0.9_beta100/v1_TBMB_exp4_reward_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onSquaresWorld/exp5_gamma0.9_beta100/v1_TBMB_exp5_reward_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onSquaresWorld/exp6_gamma0.9_beta100/v1_TBMB_exp6_reward_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onSquaresWorld/exp7_gamma0.9_beta100/v1_TBMB_exp7_reward_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onSquaresWorld/exp8_gamma0.9_beta100/v1_TBMB_exp8_reward_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onSquaresWorld/exp9_gamma0.9_beta100/v1_TBMB_exp9_reward_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onSquaresWorld/exp10_gamma0.9_beta100/v1_TBMB_exp10_reward_log.dat"
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
y_all = list()
x_all = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	cumulatedReward = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		l = 0
		for line in file1:
			x.append(l)
			cumulatedReward += int(line.split(" ")[2].rstrip())
			y.append(cumulatedReward)
			l += 1
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c=color[i])
	y_all.append(y)
	x_all.append(x)
	# -----------------------------------------------------------------------
	i += 1
# ---------------------------------------------------------------------------
minLen = 1000000000000
# ---------------------------------------------------------------------------
for l in x_all:
	if len(l) < minLen:
		minLen = len(l)
		xMean = l
# ---------------------------------------------------------------------------
yMean = [statistics.mean(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
ySD = [stats.sem(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])] 
# ---------------------------------------------------------------------------
#plt.plot(xMean, yMean, c="#00ffff", label="GD - Squares world")
#plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="#00ffff", alpha=0.1)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# SIMULATION ON MODEL / MB OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp1_beta100/v1_TBMC_exp1_expert_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp2_beta100/v1_TBMC_exp2_expert_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp3_beta100/v1_TBMC_exp3_expert_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp4_beta100/v1_TBMC_exp4_expert_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp5_beta100/v1_TBMC_exp5_expert_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp6_beta100/v1_TBMC_exp6_expert_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp7_beta100/v1_TBMC_exp7_expert_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp8_beta100/v1_TBMC_exp8_expert_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp9_beta100/v1_TBMC_exp9_expert_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/alphaFilter0.6/short/MC/exp10_beta100/v1_TBMC_exp10_expert_log.dat"
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
y_all = list()
x_all = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	cumulatedReward = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		l = 0
		for line in file1:
			x.append(l)
			cumulatedReward += int(line.split(" ")[2].rstrip())
			y.append(cumulatedReward)
			l += 1
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c=color[i])
	y_all.append(y)
	x_all.append(x)
	# -----------------------------------------------------------------------
	i += 1
# ---------------------------------------------------------------------------
minLen = 1000000000000
# ---------------------------------------------------------------------------
for l in x_all:
	if len(l) < minLen:
		minLen = len(l)
		xMean = l
# ---------------------------------------------------------------------------
yMean = [statistics.mean(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
ySD = [stats.sem(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
# ---------------------------------------------------------------------------
#plt.plot(xMean, yMean, c="#9966ff", label="GD - Model of real world")
#plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="#9966ff", alpha=0.1)
plt.plot(xMean, yMean, c="blue", label="GD only")
plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="blue", alpha=0.1)
# ---------------------------------------------------------------------------














# ---------------------------------------------------------------------------
# SIMULATION ON MODEL / COMBOT RANDOM
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/random/alphaFilter0.6/short//MC/exp1_beta100/v1_TBMC_exp1_expert_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/random/alphaFilter0.6/short/MC/exp2_beta100/v1_TBMC_exp2_expert_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/random/alphaFilter0.6/short/MC/exp3_beta100/v1_TBMC_exp3_expert_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/random/alphaFilter0.6/short/MC/exp4_beta100/v1_TBMC_exp4_expert_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/random/alphaFilter0.6/short/MC/exp5_beta100/v1_TBMC_exp5_expert_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/random/alphaFilter0.6/short/MC/exp6_beta100/v1_TBMC_exp6_expert_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/random/alphaFilter0.6/short/MC/exp7_beta100/v1_TBMC_exp7_expert_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/random/alphaFilter0.6/short/MC/exp8_beta100/v1_TBMC_exp8_expert_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/random/alphaFilter0.6/short/MC/exp9_beta100/v1_TBMC_exp9_expert_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/random/alphaFilter0.6/short/MC/exp10_beta100/v1_TBMC_exp10_expert_log.dat"
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
y_all = list()
x_all = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	cumulatedReward = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		l = 0
		for line in file1:
			x.append(l)
			cumulatedReward += int(line.split(" ")[2].rstrip())
			y.append(cumulatedReward)
			l += 1
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c=color[i])
	y_all.append(y)
	x_all.append(x)
	# -----------------------------------------------------------------------
	i += 1
# ---------------------------------------------------------------------------
minLen = 1000000000000
# ---------------------------------------------------------------------------
for l in x_all:
	if len(l) < minLen:
		minLen = len(l)
		xMean = l
# ---------------------------------------------------------------------------
yMean = [statistics.mean(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
ySD = [stats.sem(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
# ---------------------------------------------------------------------------
plt.plot(xMean, yMean, c="green", label="Random criterion")
plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="green", alpha=0.1)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# SIMULATION ON MODEL / COMBOT TRADE-OFF ENTROPY
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp1_beta50/v1_TBMC_exp1_expert_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp2_beta50/v1_TBMC_exp2_expert_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp3_beta50/v1_TBMC_exp3_expert_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp4_beta50/v1_TBMC_exp4_expert_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp5_beta50/v1_TBMC_exp5_expert_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp6_beta50/v1_TBMC_exp6_expert_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp7_beta50/v1_TBMC_exp7_expert_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp8_beta50/v1_TBMC_exp8_expert_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp9_beta50/v1_TBMC_exp9_expert_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp10_beta50/v1_TBMC_exp10_expert_log.dat"
CR11 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp11_beta50/v1_TBMC_exp11_expert_log.dat"
CR12 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp12_beta50/v1_TBMC_exp12_expert_log.dat"
CR13 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp13_beta50/v1_TBMC_exp13_expert_log.dat"
CR14 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp14_beta50/v1_TBMC_exp14_expert_log.dat"
CR15 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp15_beta50/v1_TBMC_exp15_expert_log.dat"
CR16 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp16_beta50/v1_TBMC_exp16_expert_log.dat"
CR17 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp17_beta50/v1_TBMC_exp17_expert_log.dat"
CR18 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp18_beta50/v1_TBMC_exp18_expert_log.dat"
CR19 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp19_beta50/v1_TBMC_exp19_expert_log.dat"
CR20 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/entropy_and_time/expoEntropy/MC/exp20_beta50/v1_TBMC_exp20_expert_log.dat"
#experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10,CR11,CR12,CR13,CR14,CR15,CR16,CR17,CR18,CR19,CR20]
# ---------------------------------------------------------------------------
y_all = list()
x_all = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	cumulatedReward = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		l = 0
		for line in file1:
			x.append(l)
			cumulatedReward += int(line.split(" ")[2].rstrip())
			y.append(cumulatedReward)
			l += 1
	# -----------------------------------------------------------------------
	#plt.plot(x, y, label="Kappa = 0."+str(i), color=color[i])
	# -----------------------------------------------------------------------
	y_all.append(y)
	x_all.append(x)
	# -----------------------------------------------------------------------
	i += 1
# ---------------------------------------------------------------------------
minLen = 1000000000000
# ---------------------------------------------------------------------------
for l in x_all:
	if len(l) < minLen:
		minLen = len(l)
		xMean = l
# ---------------------------------------------------------------------------
yMean = [statistics.mean(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9],y_all[10],y_all[11],y_all[12],y_all[13],y_all[14],y_all[15],y_all[16],y_all[17],y_all[18],y_all[19])]
ySD = [stats.sem(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9],y_all[10],y_all[11],y_all[12],y_all[13],y_all[14],y_all[15],y_all[16],y_all[17],y_all[18],y_all[19])]
# ---------------------------------------------------------------------------
plt.plot(xMean, yMean, c="purple", label="Trade-off criterion - entropy and time")
plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="purple", alpha=0.1)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# EXPE ON REAL WORLD / MF OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/real/exp1_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/real/exp2_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/real/exp3_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/real/exp4_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/real/exp5_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/real/exp6_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/real/exp7_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/real/exp8_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/real/exp9_alpha0.6_gamma0.9_beta100/allReward_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/real/exp10_alpha0.6_gamma0.9_beta100/allReward_log.dat"
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
y_all = list()
x_all = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	cumulatedReward = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		l = 0
		for line in file1:
			x.append(l)
			cumulatedReward += int(line.split(" ")[2].rstrip())
			y.append(cumulatedReward)
			l += 1
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c=color[i], label="exp"+str(i+1))
	y_all.append(y)
	x_all.append(x)
	# -----------------------------------------------------------------------
	i += 1
# ---------------------------------------------------------------------------
minLen = 1000000000000
# ---------------------------------------------------------------------------
for l in x_all:
	if len(l) < minLen:
		minLen = len(l)
		xMean = l
# ---------------------------------------------------------------------------
yMean = [0] * minLen
# ---------------------------------------------------------------------------
yMean = [statistics.mean(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
ySD = [stats.sem(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
#-------------------------------------------------------------------c---------
#plt.plot(xMean, yMean, c="red", label="Hab - Real world")
#plt.plot(xMean, yMean, c="red", label="Hab")
#plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="red", alpha=0.1)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# EXPE ON REAL WORLD / MB OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/real/exp1_gamma0.9_beta100/allReward_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/real/exp2_gamma0.9_beta100/allReward_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/real/exp3_gamma0.9_beta100/allReward_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/real/exp4_gamma0.9_beta100/allReward_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/real/exp5_gamma0.9_beta100/allReward_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/real/exp6_gamma0.9_beta100/allReward_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/real/exp7_gamma0.9_beta100/allReward_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/real/exp8_gamma0.9_beta100/allReward_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/real/exp9_gamma0.9_beta100/allReward_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/real/exp10_gamma0.9_beta100/allReward_log.dat"
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
y_all = list()
x_all = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	cumulatedReward = 0
	y = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		l = 0
		for line in file1:
			x.append(l)
			cumulatedReward += int(line.split(" ")[2].rstrip())
			y.append(cumulatedReward)
			l += 1
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c=color[i], label="exp"+str(i+1))
	y_all.append(y)
	x_all.append(x)
	# -----------------------------------------------------------------------
	i += 1
# ---------------------------------------------------------------------------
minLen = 1000000000000
# ---------------------------------------------------------------------------
for l in x_all:
	if len(l) < minLen:
		minLen = len(l)
		xMean = l
# ---------------------------------------------------------------------------
yMean = [0] * minLen
# ---------------------------------------------------------------------------
yMean = [statistics.mean(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
ySD = [stats.sem(k) for k in zip(y_all[0],y_all[1],y_all[2],y_all[3],y_all[4],y_all[5],y_all[6],y_all[7],y_all[8],y_all[9])]
#----------------------------------------------------------------------------
#plt.plot(xMean, yMean, c="blue", label="GD - Real world")
#plt.plot(xMean, yMean, c="blue", label="GD")
#plt.fill_between(xMean, list(map(add,yMean,np.negative(ySD))), list(map(add,yMean,ySD)), color="blue", alpha=0.1)
#----------------------------------------------------------------------------







# ---------------------------------------------------------------------------
# SHOW
# ---------------------------------------------------------------------------
plt.grid(linestyle='--')
plt.xlabel("Number of actions")
plt.axvline(x = 1600, c = "black", linewidth = 2, label = "Switch of the reward's position")
#plt.ylabel("Cumulated reward")
plt.ylabel("Cumulated reward")
plt.xlim(0,3200)
plt.legend()
plt.show()
# ---------------------------------------------------------------------------














