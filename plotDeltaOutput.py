#!/usr/bin/env python3
#encoding: utf-8

# ---------------------------------------------------------------------------
# IMPORT
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patheffects as pe
import numpy as np
import pandas as pd
import math
import statistics
from scipy.interpolate import spline
from operator import add
import sys
import os
import json
import copy
import re
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# CREATE DATA STRUCTURE
# ---------------------------------------------------------------------------
nb_experiments = 10
nb_iterations = 10000+1#2400+1#1600+1
nb_states = 37
xAll = list()
yAll = list()
listExperiments = [[]]*nb_experiments
# ---------------------------------------------------------------------------
for expe in range(0,nb_experiments):
	listExperiments[expe].append({"expert": "MF", "values": dict()})
	listExperiments[expe].append({"expert": "MB", "values": dict()})
	listExperiments[expe].append({"expert": "SuperMF", "values": dict()})
	for dictExpertValues in listExperiments[expe]:
		if dictExpertValues["expert"] == "MF":
			dictExpertValues["values"]["plan_time"] = [0.0]*nb_iterations
			dictExpertValues["values"]["deltaQ"] = [0.0]*nb_iterations
			dictExpertValues["values"]["RPE"] = [0.0]*nb_iterations
		# -------------------------------------------------------------------
		elif dictExpertValues["expert"] == "MB":
			dictExpertValues["values"]["plan_time"] = [0.0]*nb_iterations
			dictExpertValues["values"]["deltaQ"] = [0.0]*nb_iterations
			dictExpertValues["values"]["delta_prob"] = [0.0]*nb_iterations
			# -------------------------------------------------------------------
		elif dictExpertValues["expert"] == "SuperMF":
			dictExpertValues["values"]["plan_time"] = [0.0]*nb_iterations
			dictExpertValues["values"]["deltaQ"] = [0.0]*nb_iterations
			dictExpertValues["values"]["RPE"] = [0.0]*nb_iterations
	# -----------------------------------------------------------------------


# ---------------------------------------------------------------------------
# DATA OF SIMULATION ON MODEL / MF OPTIMISTIC
# ---------------------------------------------------------------------------
file1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/long/MF/exp1_alpha0.2_gamma0.9_beta100/v1_TBMF_exp1_monitoring_values_log.dat"
file2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/long/MF/exp2_alpha0.2_gamma0.9_beta100/v1_TBMF_exp2_monitoring_values_log.dat"
file3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/long/MF/exp3_alpha0.2_gamma0.9_beta100/v1_TBMF_exp3_monitoring_values_log.dat"
file4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/long/MF/exp4_alpha0.2_gamma0.9_beta100/v1_TBMF_exp4_monitoring_values_log.dat"
file5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/long/MF/exp5_alpha0.2_gamma0.9_beta100/v1_TBMF_exp5_monitoring_values_log.dat"
file6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/long/MF/exp6_alpha0.2_gamma0.9_beta100/v1_TBMF_exp6_monitoring_values_log.dat"
file7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/long/MF/exp7_alpha0.2_gamma0.9_beta100/v1_TBMF_exp7_monitoring_values_log.dat"
file8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/long/MF/exp8_alpha0.2_gamma0.9_beta100/v1_TBMF_exp8_monitoring_values_log.dat"
file9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/long/MF/exp9_alpha0.2_gamma0.9_beta100/v1_TBMF_exp9_monitoring_values_log.dat"
file10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.6/long/MF/exp10_alpha0.2_gamma0.9_beta100/v1_TBMF_exp10_monitoring_values_log.dat"
experiments_MF = [file1,file2,file3,file4,file5,file6,file7,file8,file9,file10]
# ---------------------------------------------------------------------------
for expe in experiments_MF:
	x = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file:
		# -------------------------------------------------------------------
		for line in file:
			it = int(line.split(" ")[0].rstrip())
			x.append(it)
			plan_time = float(line.split(" ")[1].rstrip())
			RPE = float(line.split(" ")[2].rstrip())
			deltaQ = float(line.split(" ")[3].rstrip())
			# ---------------------------------------------------------------
			for listExperts in listExperiments:
				for dictExpertValues in listExperts:
					if dictExpertValues["expert"] == "MF":
						for key, value in dictExpertValues["values"].items():
							if key == "plan_time":
								value[it] = plan_time
							elif key == "RPE":
								value[it] = RPE
							elif key == "deltaQ":
								value[it] = deltaQ
						break
		# -------------------------------------------------------------------
		for listExperts in listExperiments:
			for dictExpertValues in listExperts:
				if dictExpertValues["expert"] == "MF":
					y_plan_time = dictExpertValues["values"]["plan_time"]
					y_deltaQ = dictExpertValues["values"]["deltaQ"]
					y_RPE = dictExpertValues["values"]["RPE"]
					dictDelta = {"plan_time_MF": y_plan_time, "deltaQ_MF": y_deltaQ, "RPE": y_RPE}
					break
		# -------------------------------------------------------------------
		yAll.append(copy.deepcopy(dictDelta))
		xAll.append(x)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# DATA OF SIMULATION ON MODEL / MB OPTIMISTIC
# ---------------------------------------------------------------------------
file1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/long/MB/exp1_gamma0.9_beta100/v1_TBMB_exp1_monitoring_values_log.dat"
file2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/long/MB/exp2_gamma0.9_beta100/v1_TBMB_exp2_monitoring_values_log.dat"
file3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/long/MB/exp3_gamma0.9_beta100/v1_TBMB_exp3_monitoring_values_log.dat"
file4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/long/MB/exp4_gamma0.9_beta100/v1_TBMB_exp4_monitoring_values_log.dat"
file5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/long/MB/exp5_gamma0.9_beta100/v1_TBMB_exp5_monitoring_values_log.dat"
file6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/long/MB/exp6_gamma0.9_beta100/v1_TBMB_exp6_monitoring_values_log.dat"
file7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/long/MB/exp7_gamma0.9_beta100/v1_TBMB_exp7_monitoring_values_log.dat"
file8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/long/MB/exp8_gamma0.9_beta100/v1_TBMB_exp8_monitoring_values_log.dat"
file9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/long/MB/exp9_gamma0.9_beta100/v1_TBMB_exp9_monitoring_values_log.dat"
file10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/long/MB/exp10_gamma0.9_beta100/v1_TBMB_exp10_monitoring_values_log.dat"
experiments_MB = [file1,file2,file3,file4,file5,file6,file7,file8,file9,file10]
# ---------------------------------------------------------------------------
f = 0
for expe in experiments_MB:
	# -----------------------------------------------------------------------
	with open(expe,'r') as file:
		# -------------------------------------------------------------------
		for line in file:
			it = int(line.split(" ")[0].rstrip())
			plan_time = float(line.split(" ")[1].rstrip())
			delta_prob = float(line.split(" ")[2].rstrip())
			deltaQ = float(line.split(" ")[3].rstrip())
			# ---------------------------------------------------------------
			for listExperts in listExperiments:
				for dictExpertValues in listExperts:
					if dictExpertValues["expert"] == "MB":
						for key, value in dictExpertValues["values"].items():
							if key == "plan_time":
								value[it] = plan_time
							elif key == "delta_prob":
								value[it] = delta_prob
							elif key == "deltaQ":
								value[it] = deltaQ
						break
		# -------------------------------------------------------------------
		for listExperts in listExperiments:
			for dictExpertValues in listExperts:
				if dictExpertValues["expert"] == "MB":
					y_plan_time = dictExpertValues["values"]["plan_time"]
					y_deltaQ = dictExpertValues["values"]["deltaQ"]
					y_delta_prob = dictExpertValues["values"]["delta_prob"]
					dictDelta = {"plan_time_MB": y_plan_time, "deltaQ_MB": y_deltaQ, "delta_prob": y_delta_prob}
					break
	# -----------------------------------------------------------------------
		yAll[f]["plan_time_MB"] = y_plan_time.copy()
		yAll[f]["deltaQ_MB"] = y_deltaQ.copy()
		yAll[f]["delta_prob"] = y_delta_prob.copy()
		f += 1
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# DATA OF SIMULATION ON MODEL / BOOSTED hab
# ---------------------------------------------------------------------------
# file1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/MF/exp1_alpha0.2_gamma0.9_beta100/v1_TBMF_exp1_monitoring_values_log.dat"
# file2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/MF/exp2_alpha0.2_gamma0.9_beta100/v1_TBMF_exp2_monitoring_values_log.dat"
# file3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/MF/exp3_alpha0.2_gamma0.9_beta100/v1_TBMF_exp3_monitoring_values_log.dat"
# file4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/MF/exp4_alpha0.2_gamma0.9_beta100/v1_TBMF_exp4_monitoring_values_log.dat"
# file5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/MF/exp5_alpha0.2_gamma0.9_beta100/v1_TBMF_exp5_monitoring_values_log.dat"
# file6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/MF/exp6_alpha0.2_gamma0.9_beta100/v1_TBMF_exp6_monitoring_values_log.dat"
# file7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/MF/exp7_alpha0.2_gamma0.9_beta100/v1_TBMF_exp7_monitoring_values_log.dat"
# file8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/MF/exp8_alpha0.2_gamma0.9_beta100/v1_TBMF_exp8_monitoring_values_log.dat"
# file9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/MF/exp9_alpha0.2_gamma0.9_beta100/v1_TBMF_exp9_monitoring_values_log.dat"
# file10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/GD_only/simu/onModel/optimisticQ1/MF/exp10_alpha0.2_gamma0.9_beta100/v1_TBMF_exp10_monitoring_values_log.dat"
# experiments_SuperMF = [file1,file2,file3,file4,file5,file6,file7,file8,file9,file10]
# # ---------------------------------------------------------------------------
# f = 0
# for expe in experiments_SuperMF:
# 	# -----------------------------------------------------------------------
# 	with open(expe,'r') as file:
# 		# -------------------------------------------------------------------
# 		for line in file:
# 			it = int(line.split(" ")[0].rstrip())
# 			plan_time = float(line.split(" ")[2].rstrip())
# 			RPE = float(line.split(" ")[3].rstrip())
# 			deltaQ = float(line.split(" ")[4].rstrip())
# 			# ---------------------------------------------------------------
# 			for listExperts in listExperiments:
# 				for dictExpertValues in listExperts:
# 					if dictExpertValues["expert"] == "SuperMF":
# 						for key, value in dictExpertValues["values"].items():
# 							if key == "plan_time":
# 								value[it] = plan_time
# 							elif key == "RPE":
# 								value[it] = RPE
# 							elif key == "deltaQ":
# 								value[it] = deltaQ
# 						break
# 		# -------------------------------------------------------------------
# 		for listExperts in listExperiments:
# 			for dictExpertValues in listExperts:
# 				if dictExpertValues["expert"] == "SuperMF":
# 					y_plan_time = dictExpertValues["values"]["plan_time"]
# 					y_deltaQ = dictExpertValues["values"]["deltaQ"]
# 					y_RPE = dictExpertValues["values"]["RPE"]
# 					dictDelta = {"plan_time_SuperMF": y_plan_time, "deltaQ_SuperMF": y_deltaQ, "RPE_SuperMF": y_RPE}
# 					break
# 	# -----------------------------------------------------------------------
# 		yAll[f]["plan_time_SuperMF"] = y_plan_time.copy()
# 		yAll[f]["deltaQ_SuperMF"] = y_deltaQ.copy()
# 		yAll[f]["RPE_SuperMF"] = y_RPE.copy()
# 		f += 1
# # ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# PLOT ALL DATA
# ---------------------------------------------------------------------------
#fig = plt.figure()
for expe in range(0, nb_experiments):
	i = expe+1
	#ax = fig.add_subplot(3,4,i)
	#ax.plot(xAll[expe], yAll[expe]["deltaQ_MB"], c = "blue", label = "GD", alpha = 0.6)
	#ax.plot(xAll[expe], yAll[expe]["deltaQ_MF"], c = "red", label = "Hab", alpha = 0.6)
	#ax.plot(xAll[expe], yAll[expe]["plan_time_MB"], c = "red", label = "MB")
	#ax.plot(xAll[expe], yAll[expe]["plan_time_MF"], c = "blue", label = "MF")
	#ax.plot(xAll[expe], yAll[expe]["delta_prob"], c = "red", label = "MB")
	#ax.plot(xAll[expe], yAll[expe]["RPE"], c = "blue", label = "MF")
	#ax.set_ylim(0,0.5)
	#ax.title.set_text('Exp '+str(i))
	#ax.legend(prop={'size': 6})
	i += 1

# -----------------------------------------------------------------------
#fig.text(0.5, 0.04, 'Iterations', ha = 'center', va = 'center', fontsize = 14, fontweight = 'bold')
#fig.text(0.06, 0.5, 'DeltaQ', ha = 'center', va = 'center', rotation = 'vertical', fontsize=  14, fontweight = 'bold')
#fig.text(0.06, 0.5, 'Time of planification', ha='center', va='center', rotation='vertical', fontsize = 14, fontweight = 'bold')
#fig.text(0.06, 0.5, 'RPE / delta of probabilities of transitions', ha='center', va='center', rotation='vertical', fontsize = 14, fontweight = 'bold')
#fig.subplots_adjust(wspace = 0.4, hspace = 0.4)
#plt.show()
#plt.savefig('time_planif_sim.png')
#plt.savefig('plan_time_exp'+str(expe+1)+'_part1.png')
#plt.savefig('RPE_delta_prob_exp'+str(expe+1)+'_part1.png')
# ---------------------------------------------------------------------------



# ---------------------------------------------------------------------------
# PLOT MEAN DATA
# ---------------------------------------------------------------------------
xMean = xAll[0]
# ---------------------------------------------------------------------------
yMean_MF = [statistics.mean(k) for k in zip(yAll[0]["deltaQ_MF"],yAll[1]["deltaQ_MF"],yAll[2]["deltaQ_MF"],yAll[3]["deltaQ_MF"],yAll[4]["deltaQ_MF"],yAll[5]["deltaQ_MF"],yAll[6]["deltaQ_MF"],yAll[7]["deltaQ_MF"],yAll[8]["deltaQ_MF"],yAll[9]["deltaQ_MF"])]
ySD_MF = [statistics.pstdev(k) for k in zip(yAll[0]["deltaQ_MF"],yAll[1]["deltaQ_MF"],yAll[2]["deltaQ_MF"],yAll[3]["deltaQ_MF"],yAll[4]["deltaQ_MF"],yAll[5]["deltaQ_MF"],yAll[6]["deltaQ_MF"],yAll[7]["deltaQ_MF"],yAll[8]["deltaQ_MF"],yAll[9]["deltaQ_MF"])]
dict_yMF = {"mean": yMean_MF, "SD": ySD_MF}
df_yMF = pd.DataFrame(data = dict_yMF)
df_yMF["moving_mean"] = df_yMF["mean"].rolling(1).mean()
df_yMF["moving_SD"] = df_yMF["SD"].rolling(1).mean()
# ---------------------------------------------------------------------------
yMean_MB = [statistics.mean(k) for k in zip(yAll[0]["deltaQ_MB"],yAll[1]["deltaQ_MB"],yAll[2]["deltaQ_MB"],yAll[3]["deltaQ_MB"],yAll[4]["deltaQ_MB"],yAll[5]["deltaQ_MB"],yAll[6]["deltaQ_MB"],yAll[7]["deltaQ_MB"],yAll[8]["deltaQ_MB"],yAll[9]["deltaQ_MB"])]
ySD_MB = [statistics.pstdev(k) for k in zip(yAll[0]["deltaQ_MB"],yAll[1]["deltaQ_MB"],yAll[2]["deltaQ_MB"],yAll[3]["deltaQ_MB"],yAll[4]["deltaQ_MB"],yAll[5]["deltaQ_MB"],yAll[6]["deltaQ_MB"],yAll[7]["deltaQ_MB"],yAll[8]["deltaQ_MB"],yAll[9]["deltaQ_MB"])]
dict_yMB = {"mean": yMean_MB, "SD": ySD_MB}
df_yMB = pd.DataFrame(data = dict_yMB)
df_yMB["moving_mean"] = df_yMB["mean"].rolling(1).mean()
df_yMB["moving_SD"] = df_yMB["SD"].rolling(1).mean()
# ---------------------------------------------------------------------------
#yMean_SuperMF = [statistics.mean(k) for k in zip(yAll[0]["deltaQ_SuperMF"],yAll[1]["deltaQ_SuperMF"],yAll[2]["deltaQ_SuperMF"])]#,yAll[3]["deltaQ_SuperMF"],yAll[4]["deltaQ_SuperMF"],yAll[5]["deltaQ_SuperMF"],yAll[6]["deltaQ_SuperMF"],yAll[7]["deltaQ_SuperMF"],yAll[8]["deltaQ_SuperMF"],yAll[9]["deltaQ_SuperMF"])]
#ySD_SuperMF = [statistics.pstdev(k) for k in zip(yAll[0]["deltaQ_SuperMF"],yAll[1]["deltaQ_SuperMF"],yAll[2]["deltaQ_SuperMF"])]#,yAll[3]["deltaQ_SuperMF"],yAll[4]["deltaQ_SuperMF"],yAll[5]["deltaQ_SuperMF"],yAll[6]["deltaQ_SuperMF"],yAll[7]["deltaQ_SuperMF"],yAll[8]["deltaQ_SuperMF"],yAll[9]["deltaQ_SuperMF"])]
#dict_ySuperMF = {"mean": yMean_SuperMF, "SD": ySD_SuperMF}
#df_ySuperMF = pd.DataFrame(data = dict_ySuperMF)
#df_ySuperMF["moving_mean"] = df_ySuperMF["mean"].rolling(100).mean()
#df_ySuperMF["moving_SD"] = df_ySuperMF["SD"].rolling(100).mean()
# ---------------------------------------------------------------------------
#yMean_MF = [statistics.mean(k) for k in zip(yAll[0]["plan_time_MF"],yAll[1]["plan_time_MF"],yAll[2]["plan_time_MF"],yAll[3]["plan_time_MF"],yAll[4]["plan_time_MF"],yAll[5]["plan_time_MF"],yAll[6]["plan_time_MF"],yAll[7]["plan_time_MF"],yAll[8]["plan_time_MF"],yAll[9]["plan_time_MF"])]
#ySD_MF = [statistics.pstdev(k) for k in zip(yAll[0]["plan_time_MF"],yAll[1]["plan_time_MF"],yAll[2]["plan_time_MF"],yAll[3]["plan_time_MF"],yAll[4]["plan_time_MF"],yAll[5]["plan_time_MF"],yAll[6]["plan_time_MF"],yAll[7]["plan_time_MF"],yAll[8]["plan_time_MF"],yAll[9]["plan_time_MF"])]
# ---------------------------------------------------------------------------
#yMean_MB = [statistics.mean(k) for k in zip(yAll[0]["plan_time_MB"],yAll[1]["plan_time_MB"],yAll[2]["plan_time_MB"],yAll[3]["plan_time_MB"],yAll[4]["plan_time_MB"],yAll[5]["plan_time_MB"],yAll[6]["plan_time_MB"],yAll[7]["plan_time_MB"],yAll[8]["plan_time_MB"],yAll[9]["plan_time_MB"])]
#ySD_MB = [statistics.pstdev(k) for k in zip(yAll[0]["plan_time_MB"],yAll[1]["plan_time_MB"],yAll[2]["plan_time_MB"],yAll[3]["plan_time_MB"],yAll[4]["plan_time_MB"],yAll[5]["plan_time_MB"],yAll[6]["plan_time_MB"],yAll[7]["plan_time_MB"],yAll[8]["plan_time_MB"],yAll[9]["plan_time_MB"])]
# ---------------------------------------------------------------------------
#yMean_MB = [statistics.mean(k) for k in zip(yAll[0]["delta_prob"],yAll[1]["delta_prob"],yAll[2]["delta_prob"],yAll[3]["delta_prob"],yAll[4]["delta_prob"],yAll[5]["delta_prob"],yAll[6]["delta_prob"],yAll[7]["delta_prob"],yAll[8]["delta_prob"],yAll[9]["delta_prob"])]
#ySD_MB = [statistics.pstdev(k) for k in zip(yAll[0]["delta_prob"],yAll[1]["delta_prob"],yAll[2]["delta_prob"],yAll[3]["delta_prob"],yAll[4]["delta_prob"],yAll[5]["delta_prob"],yAll[6]["delta_prob"],yAll[7]["delta_prob"],yAll[8]["delta_prob"],yAll[9]["delta_prob"])]
# ---------------------------------------------------------------------------
#yMean_MF = [statistics.mean(k) for k in zip(yAll[0]["RPE"],yAll[1]["RPE"],yAll[2]["RPE"],yAll[3]["RPE"],yAll[4]["RPE"],yAll[5]["RPE"],yAll[6]["RPE"],yAll[7]["RPE"],yAll[8]["RPE"],yAll[9]["RPE"])]
#ySD_MF = [statistics.pstdev(k) for k in zip(yAll[0]["RPE"],yAll[1]["RPE"],yAll[2]["RPE"],yAll[3]["RPE"],yAll[4]["RPE"],yAll[5]["RPE"],yAll[6]["RPE"],yAll[7]["RPE"],yAll[8]["RPE"],yAll[9]["RPE"])]
# ---------------------------------------------------------------------------
plt.plot(xMean[1:], df_yMF["moving_mean"][1:], c = "red", linewidth = 2, label = "Hab", alpha = 1)
plt.fill_between(xMean[1:], list(map(add,df_yMF["moving_mean"][1:],np.negative(df_yMF["moving_SD"][1:]))), list(map(add,df_yMF["moving_mean"][1:],df_yMF["moving_SD"][1:])), color = "red", alpha = 0.2)
plt.plot(xMean[1:], df_yMB["moving_mean"][1:], c = "blue", linewidth = 2, label = "GD", alpha = 1)
plt.fill_between(xMean[1:], list(map(add,df_yMB["moving_mean"][1:],np.negative(df_yMB["moving_SD"][1:]))), list(map(add,df_yMB["moving_mean"][1:],df_yMB["moving_SD"][1:])), color = "blue", alpha = 0.2)
#plt.plot(xMean, df_ySuperMF["moving_mean"], c = "green", linewidth = 2, label = "Boosted hab", alpha = 1)
#plt.fill_between(xMean, list(map(add,df_ySuperMF["moving_mean"],np.negative(df_ySuperMF["moving_SD"]))), list(map(add,df_ySuperMF["moving_mean"],df_ySuperMF["moving_SD"])), color = "green", alpha = 0.2)
# ---------------------------------------------------------------------------
plt.axvline(x = 5000, c = "black", linewidth = 2, label = "Switch of the reward's position")
plt.axhline(y = 0.01, c = "purple", linewidth = 1, label = "Epsilon")
plt.grid(linestyle='--')
plt.xlabel("Number of actions")
plt.ylabel("Mean DeltaQ")
#plt.ylabel("Mean time of planification")
#plt.ylabel("Mean RPE / delta of probabilities of transitions")
plt.yticks(np.arange(0, 1, 0.01))
plt.xticks(np.arange(0, nb_iterations, 200))
plt.ylim(-0.01,0.31)
plt.legend()
plt.show()
# ---------------------------------------------------------------------------





