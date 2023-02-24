#!/usr/bin/env python3
#encoding: utf-8

# ---------------------------------------------------------------------------
# IMPORT
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics
from scipy.interpolate import spline
from operator import add
import sys
import os
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# BUILD DATA TO PLOT / COMBO
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/nav1/MC/exp1_beta100/v1_TBMC_exp1_expert_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/nav1/MC/exp2_beta100/v1_TBMC_exp2_expert_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/nav1/MC/exp3_beta100/v1_TBMC_exp3_expert_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/nav1/MC/exp4_beta100/v1_TBMC_exp4_expert_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/nav1/MC/exp5_beta100/v1_TBMC_exp5_expert_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/nav1/MC/exp6_beta100/v1_TBMC_exp6_expert_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/nav1/MC/exp7_beta100/v1_TBMC_exp7_expert_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/nav1/MC/exp8_beta100/v1_TBMC_exp8_expert_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/nav1/MC/exp9_beta100/v1_TBMC_exp9_expert_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Combo/simu/nav1/MC/exp10_beta100/v1_TBMC_exp10_expert_log.dat"
# ---------------------------------------------------------------------------
experiences = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
nb_experiments = len(experiences)
nb_iterations = 3200
# ---------------------------------------------------------------------------
x = list(range(0, nb_iterations+1))
yAll = list()
xAll = list()
e = 1
# ---------------------------------------------------------------------------
for expe in experiences:
	expert = list()
	color = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		for line in file1:
			if line.split(" ")[2].rstrip() == "Hab":
				expert.append(0)
				color.append("r")
			elif line.split(" ")[2].rstrip() == "GD":
				expert.append(0)
				color.append("b")
			else:
				expert.append(0)
				color.append("b")
	# -----------------------------------------------------------------------
		dictExpert = dict()
		dictExpert["expert"] = expert
		dictExpert["color"] = color
	# -----------------------------------------------------------------------
	yAll.append(dictExpert.copy())
	xAll.append(x)
	# -----------------------------------------------------------------------
	plt.scatter(x[1:], expert[1:], c = color[1:])
	plt.plot(0, 0, "ro", label = "Hab expert")
	plt.plot(0, 0, "bo", label = "GD expert")
	plt.xlim(1, nb_iterations)
	#plt.ylim(-1,1)
	plt.axvline(x = 1600, c = "black", linewidth = 2, label = "Switch of the reward's position")
	plt.xlabel("Number of actions")
	plt.ylabel("Expert")
	plt.grid(linestyle='--')
	plt.xticks(np.arange(0, nb_iterations+1, 100))
	plt.gca().set_yticks([0])
	plt.gca().set_yticklabels(["Expert"])
	plt.legend()
	plt.title("Exp "+str(e)+" - Dynamics of the experts over time")
	plt.show()
	# -----------------------------------------------------------------------
	e += 1
	# -----------------------------------------------------------------------



# ---------------------------------------------------------------------------
# PLOT ALL DATA
# ---------------------------------------------------------------------------
# fig = plt.figure()
# for expe in range(0, nb_experiments):
# 	ax = fig.add_subplot(3,4,expe+1)
# 	ax.scatter(xAll[expe], yAll[expe]["expert"], c = yAll[expe]["color"])
# 	ax.plot(0, 0, "ro", label = "Hab expert")
# 	ax.plot(0, 0, "bo", label = "GD expert")
# 	ax.axvline(x = 1600, c = "black", linewidth = 2, label = "Switch of the reward's position")
# 	ax.title.set_text('Exp '+str(expe+1))
# 	ax.legend(prop={'size': 6})
# # ---------------------------------------------------------------------------
# fig.text(0.5, 0.04, 'Number of actions', ha = 'center', va = 'center', fontsize = 14, fontweight = 'bold')
# fig.text(0.06, 0.5, 'Expert', ha = 'center', va = 'center', rotation = 'vertical', fontsize=  14, fontweight = 'bold')
# fig.subplots_adjust(wspace = 0.4, hspace = 0.4)
# plt.show()
# ---------------------------------------------------------------------------
