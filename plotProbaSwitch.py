#!/usr/bin/env python3
#encoding: utf-8

# ---------------------------------------------------------------------------
# IMPORT
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics
from scipy import stats
from scipy.interpolate import spline
from operator import add
import sys
import os
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
nb_experiments = len(experiences)
nb_iterations = 5001#3201
# ---------------------------------------------------------------------------
x = list(range(0, nb_iterations))
x_all = list()
y_all = list()
rewarded_it_all = list()
frustration_it_all = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	y_Hab = list()
	y_GD = list()
	rewarded_it = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file1:
		# -------------------------------------------------------------------
		flag_rwrd = True
		flag_frustration = False 
		it = 0
		for line in file1:
			#print(line)
			proba = float(line.split(" ")[5].rstrip())
			reward = int(line.split(" ")[2].rstrip())
			state = line.split(" ")[1].rstrip()
			if line.split(" ")[4].rstrip() == "Hab":
				y_Hab.append(proba)
				y_GD.append(1-proba)
			elif line.split(" ")[4].rstrip() == "GD":
				y_Hab.append(1-proba)
				y_GD.append(proba)
			# ---------------------------------------------------------------
			if flag_rwrd == True and reward:
				rewarded_it.append(it)
				flag_rwrd = False
			if it == 1601:
				flag_rwrd = True
			# ---------------------------------------------------------------
			if it > 1602 and state == "18" and flag_frustration == False:
				frustration_it = it 
				flag_frustration = True
			# ---------------------------------------------------------------
			it += 1
		# -------------------------------------------------------------------
		dictExpert = dict()
		dictExpert["GD"] = y_GD
		dictExpert["Hab"] = y_Hab
	# -----------------------------------------------------------------------
	y_all.append(dictExpert.copy())
	x_all.append(x)
	rewarded_it_all.append(rewarded_it)
	frustration_it_all.append(frustration_it)
# ---------------------------------------------------------------------------
xMean = x_all[0]
# ---------------------------------------------------------------------------
yMean_Hab = [statistics.mean(k) for k in zip(y_all[0]["Hab"],y_all[1]["Hab"],y_all[2]["Hab"],y_all[3]["Hab"],y_all[4]["Hab"],y_all[5]["Hab"],y_all[6]["Hab"],y_all[7]["Hab"],y_all[8]["Hab"],y_all[9]["Hab"],y_all[10]["Hab"],y_all[11]["Hab"],y_all[12]["Hab"],y_all[13]["Hab"],y_all[14]["Hab"],y_all[15]["Hab"],y_all[16]["Hab"],y_all[17]["Hab"],y_all[18]["Hab"],y_all[19]["Hab"])]
ySD_Hab = [stats.sem(k) for k in zip(y_all[0]["Hab"],y_all[1]["Hab"],y_all[2]["Hab"],y_all[3]["Hab"],y_all[4]["Hab"],y_all[5]["Hab"],y_all[6]["Hab"],y_all[7]["Hab"],y_all[8]["Hab"],y_all[9]["Hab"],y_all[10]["Hab"],y_all[11]["Hab"],y_all[12]["Hab"],y_all[13]["Hab"],y_all[14]["Hab"],y_all[15]["Hab"],y_all[16]["Hab"],y_all[17]["Hab"],y_all[18]["Hab"],y_all[19]["Hab"])]
dict_yHab = {"mean": yMean_Hab, "SD": ySD_Hab}
df_yHab = pd.DataFrame(data = dict_yHab)
df_yHab["moving_mean"] = df_yHab["mean"].rolling(100).mean()
df_yHab["moving_SD"] = df_yHab["SD"].rolling(100).mean()
for it in range(0,100):
	df_yHab["moving_mean"][it] = df_yHab["mean"].rolling(it+1).mean()[it]
	df_yHab["moving_SD"][it] = df_yHab["SD"].rolling(it+1).mean()[it]
# ---------------------------------------------------------------------------
yMean_GD = [statistics.mean(k) for k in zip(y_all[0]["GD"],y_all[1]["GD"],y_all[2]["GD"],y_all[3]["GD"],y_all[4]["GD"],y_all[5]["GD"],y_all[6]["GD"],y_all[7]["GD"],y_all[8]["GD"],y_all[9]["GD"],y_all[10]["GD"],y_all[11]["GD"],y_all[12]["GD"],y_all[13]["GD"],y_all[14]["GD"],y_all[15]["GD"],y_all[16]["GD"],y_all[17]["GD"],y_all[18]["GD"],y_all[19]["GD"])]
ySD_GD = [stats.sem(k) for k in zip(y_all[0]["GD"],y_all[1]["GD"],y_all[2]["GD"],y_all[3]["GD"],y_all[4]["GD"],y_all[5]["GD"],y_all[6]["GD"],y_all[7]["GD"],y_all[8]["GD"],y_all[9]["GD"],y_all[10]["GD"],y_all[11]["GD"],y_all[12]["GD"],y_all[13]["GD"],y_all[14]["GD"],y_all[15]["GD"],y_all[16]["GD"],y_all[17]["GD"],y_all[18]["GD"],y_all[19]["GD"])]
dict_yGD = {"mean": yMean_GD, "SD": ySD_GD}
df_yGD = pd.DataFrame(data = dict_yGD)
df_yGD["moving_mean"] = df_yGD["mean"].rolling(100).mean()
df_yGD["moving_SD"] = df_yGD["SD"].rolling(100).mean()
for it in range(0,100):
	df_yGD["moving_mean"][it] = df_yGD["mean"].rolling(it+1).mean()[it]
	df_yGD["moving_SD"][it] = df_yGD["SD"].rolling(it+1).mean()[it]
# ---------------------------------------------------------------------------
rewarded_it_mean_1 = np.mean([rewarded_it_all[0][0],rewarded_it_all[1][0],rewarded_it_all[2][0],rewarded_it_all[3][0],rewarded_it_all[4][0],rewarded_it_all[5][0],rewarded_it_all[6][0],rewarded_it_all[7][0],rewarded_it_all[8][0],rewarded_it_all[9][0],rewarded_it_all[10][0],rewarded_it_all[11][0],rewarded_it_all[12][0],rewarded_it_all[13][0],rewarded_it_all[14][0],rewarded_it_all[15][0],rewarded_it_all[16][0],rewarded_it_all[17][0],rewarded_it_all[18][0],rewarded_it_all[19][0]])
rewarded_it_mean_2 = np.mean([rewarded_it_all[0][1],rewarded_it_all[1][1],rewarded_it_all[2][1],rewarded_it_all[3][1],rewarded_it_all[4][1],rewarded_it_all[5][1],rewarded_it_all[6][1],rewarded_it_all[7][1],rewarded_it_all[8][1],rewarded_it_all[9][1],rewarded_it_all[10][1],rewarded_it_all[11][1],rewarded_it_all[12][1],rewarded_it_all[13][1],rewarded_it_all[14][1],rewarded_it_all[15][1],rewarded_it_all[16][1],rewarded_it_all[17][1],rewarded_it_all[18][1],rewarded_it_all[19][1]])
# ---------------------------------------------------------------------------

# # ---------------------------------------------------------------------------
# # PLOT ALL DATA IN TOGETHER
# # ---------------------------------------------------------------------------
# fig = plt.figure()
# for expe in range(0, nb_experiments):
# 	ax = fig.add_subplot(3,4,expe+1)
# 	ax.plot(x_all[expe], y_all[expe]["Hab"], c = "red", label = "Hab")
# 	ax.plot(x_all[expe], y_all[expe]["GD"], c = "blue", label = "GD")
# 	plt.axvline(x = 1600, c = "black", linewidth = 2, label = "Switch of the reward's position")
# 	ax.title.set_text('Exp '+str(expe+1))
# 	#ax.legend(prop={'size': 6})
# 	plt.grid(linestyle='--')
# 	plt.yticks(np.arange(0, 1, 0.1))
# 	plt.xticks(np.arange(0, nb_iterations+1, 800))
# # ---------------------------------------------------------------------------
# fig.text(0.5, 0.04, 'Number of actions', ha = 'center', va = 'center', fontsize = 14, fontweight = 'bold')
# fig.text(0.06, 0.5, 'Probabilities of selection', ha = 'center', va = 'center', rotation = 'vertical', fontsize=  14, fontweight = 'bold')
# fig.subplots_adjust(wspace = 0.4, hspace = 0.4)
# plt.show()
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# PLOT ALL DATA SEPARATALY
# ---------------------------------------------------------------------------
fig = plt.figure()
for expe in range(0, nb_experiments):
	# -----------------------------------------------------------------------
	dict_y = {"Hab": y_all[expe]["Hab"], "GD": y_all[expe]["GD"]}
	df_y = pd.DataFrame(data = dict_y)
	df_y["smooth_Hab"] = df_y["Hab"].rolling(100).mean()
	df_y["smooth_GD"] = df_y["GD"].rolling(100).mean()
	for it in range(0,100):
		df_y["smooth_Hab"][it] = df_y["Hab"].rolling(it+1).mean()[it]
		df_y["smooth_GD"][it] = df_y["GD"].rolling(it+1).mean()[it]
	# -----------------------------------------------------------------------
	plt.plot(x_all[expe], df_y["smooth_Hab"], linewidth = 2, c = "red", label = "Hab")
	plt.plot(x_all[expe], df_y["smooth_GD"], linewidth = 2, c = "blue", label = "GD")
	plt.axvline(x = 1600, c = "black", linewidth = 2, label = "Switch of the reward's position")
	plt.axvline(x = rewarded_it_all[expe][0], c = "purple", linewidth = 2, label = "First reward obtained")
	plt.axvline(x = rewarded_it_all[expe][1], c = "orange", linewidth = 2, label = "First reward obtained after switch")
	plt.axvline(x = frustration_it_all[expe], c = "grey", linewidth = 2, label = "Switch discovery")
	plt.legend()
	plt.title('Exp '+str(expe+1))
	plt.grid(linestyle='--')
	plt.yticks(np.arange(0, 1.1, 0.1))
	plt.xticks(np.arange(0, nb_iterations+1, 200))
	plt.xlabel("Number of actions")
	plt.ylabel("Probabilities of selection")
	plt.show()
# ---------------------------------------------------------------------------



# ---------------------------------------------------------------------------
# PLOT MEAN DATA
# ---------------------------------------------------------------------------
fig = plt.figure()
plt.plot(xMean[0:], df_yHab["moving_mean"][0:], "red", label = "Hab")
plt.fill_between(xMean[1:], list(map(add,df_yHab["moving_mean"][1:],np.negative(df_yHab["moving_SD"][1:]))), list(map(add,df_yHab["moving_mean"][1:],df_yHab["moving_SD"][1:])), color = "red", alpha = 0.2)
plt.plot(xMean[0:], df_yGD["moving_mean"][0:], "blue", label = "GD")
plt.fill_between(xMean[1:], list(map(add,df_yGD["moving_mean"][1:],np.negative(df_yGD["moving_SD"][1:]))), list(map(add,df_yGD["moving_mean"][1:],df_yGD["moving_SD"][1:])), color = "blue", alpha = 0.2)
plt.axvline(x = 1600, c = "black", linewidth = 2, label = "Switch of the reward's position")
plt.axvline(x = rewarded_it_mean_1, c = "purple", linewidth = 2, label = "First reward obtained")
plt.axvline(x = rewarded_it_mean_2, c = "orange", linewidth = 2, label = "First reward obtained after switch")
plt.legend()
plt.grid(linestyle='--')
plt.xlim(0.0,5000)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.xticks(np.arange(0, nb_iterations+1, 200))
plt.xlabel("Number of actions")
plt.ylabel("Probabilities of selection")
plt.show()
# ---------------------------------------------------------------------------
