#!/usr/bin/env python3
#encoding: utf-8

# ---------------------------------------------------------------------------
# IMPORT
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
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
nb_iterations = 1600+1
nb_states = 37
xAll = list()
yAll = list()
dictOutput = dict()
dictOutput["states"] = list()
# ---------------------------------------------------------------------------
for state in range(0,nb_states+1):
	dictStateValues = dict()
	dictStateValues["state"] = str(state)
	dictStateValues["values"] = [{"expert": "MF", "values": dict()}, {"expert": "MB", "values": dict()}]
	# -----------------------------------------------------------------------
	for dictExpertValues in dictStateValues["values"]:
		# -------------------------------------------------------------------
		if dictExpertValues["expert"] == "MF":
			dictExpertValues["values"]["plan_time"] = [0.0]*nb_iterations
			dictExpertValues["values"]["deltaQ"] = [0.0]*nb_iterations
			dictExpertValues["values"]["RPE"] = [0.0]*nb_iterations
		# -------------------------------------------------------------------
		elif dictExpertValues["expert"] == "MB":
			dictExpertValues["values"]["plan_time"] = [0.0]*nb_iterations
			dictExpertValues["values"]["deltaQ"] = [0.0]*nb_iterations
			dictExpertValues["values"]["delta_prob"] = [0.0]*nb_iterations
	# -----------------------------------------------------------------------
	dictOutput["states"].append(dictStateValues)
# ---------------------------------------------------------------------------
#print(dictOutput)


# ---------------------------------------------------------------------------
# DATA OF SIMULATION ON MODEL / MF OPTIMISTIC
# ---------------------------------------------------------------------------
file1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/simu/onModel/optimisticQ1/exp1_param_0.6_0.9_100.0/v0_TBMF_exp1_monitoring_values_log.dat"
file2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/simu/onModel/optimisticQ1/exp2_param_0.6_0.9_100.0/v0_TBMF_exp2_monitoring_values_log.dat"
file3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/simu/onModel/optimisticQ1/exp3_param_0.6_0.9_100.0/v0_TBMF_exp3_monitoring_values_log.dat"
file4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/simu/onModel/optimisticQ1/exp4_param_0.6_0.9_100.0/v0_TBMF_exp4_monitoring_values_log.dat"
file5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/simu/onModel/optimisticQ1/exp5_param_0.6_0.9_100.0/v0_TBMF_exp5_monitoring_values_log.dat"
file6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/simu/onModel/optimisticQ1/exp6_param_0.6_0.9_100.0/v0_TBMF_exp6_monitoring_values_log.dat"
file7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/simu/onModel/optimisticQ1/exp7_param_0.6_0.9_100.0/v0_TBMF_exp7_monitoring_values_log.dat"
file8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/simu/onModel/optimisticQ1/exp8_param_0.6_0.9_100.0/v0_TBMF_exp8_monitoring_values_log.dat"
file9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/simu/onModel/optimisticQ1/exp9_param_0.6_0.9_100.0/v0_TBMF_exp9_monitoring_values_log.dat"
file10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/simu/onModel/optimisticQ1/exp10_param_0.6_0.9_100.0/v0_TBMF_exp10_monitoring_values_log.dat"
experiences = [file1,file2,file3,file4,file5,file6,file7,file8,file9,file10]
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	# -----------------------------------------------------------------------
	with open(expe,'r') as file:
		# -------------------------------------------------------------------
		for line in file:
			it = int(line.split(" ")[0].rstrip())
			x.append(it)
			previous_state = str(line.split(" ")[1].rstrip())
			plan_time = str(line.split(" ")[2].rstrip())
			RPE = str(line.split(" ")[3].rstrip())
			deltaQ = str(line.split(" ")[4].rstrip())
			# ---------------------------------------------------------------
			for dictStateValues in dictOutput["states"]:
				if dictStateValues["state"] == previous_state:
					for dictExpertValues in dictStateValues["values"]:
						if dictExpertValues["expert"] == "MF":
							for key, value in dictExpertValues["values"].items():
								if key == "plan_time":
									value[it] = plan_time
								elif key == "RPE":
									value[it] = RPE
								elif key == "deltaQ":
									value[it] = deltaQ

							break
					break
		# -------------------------------------------------------------------
		listStates = list()
		for state in range(0, nb_states+1):
			for dictStateValues in dictOutput["states"]:
				if dictStateValues["state"] == str(state):
					for dictExpertValues in dictStateValues["values"]:
						if dictExpertValues["expert"] == "MF":
							y_plan_time = dictExpertValues["values"]["plan_time"]
							y_deltaQ = dictExpertValues["values"]["deltaQ"]
							y_RPE = dictExpertValues["values"]["RPE"]
							listStates.append({"plan_time_MF": y_plan_time, "deltaQ_MF": y_deltaQ, "RPE": y_RPE})
							break
					break		
		# -------------------------------------------------------------------
		yAll.append(listStates)
		xAll.append(x)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# DATA OF SIMULATION ON MODEL / MB OPTIMISTIC
# ---------------------------------------------------------------------------
file1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/simu/onModel/exp1_param_0.9_100.0/v0_TBMB_exp1_monitoring_values_log.dat"
file2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/simu/onModel/exp2_param_0.9_100.0/v0_TBMB_exp2_monitoring_values_log.dat"
file3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/simu/onModel/exp3_param_0.9_100.0/v0_TBMB_exp3_monitoring_values_log.dat"
file4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/simu/onModel/exp4_param_0.9_100.0/v0_TBMB_exp4_monitoring_values_log.dat"
file5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/simu/onModel/exp5_param_0.9_100.0/v0_TBMB_exp5_monitoring_values_log.dat"
file6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/simu/onModel/exp6_param_0.9_100.0/v0_TBMB_exp6_monitoring_values_log.dat"
file7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/simu/onModel/exp7_param_0.9_100.0/v0_TBMB_exp7_monitoring_values_log.dat"
file8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/simu/onModel/exp8_param_0.9_100.0/v0_TBMB_exp8_monitoring_values_log.dat"
file9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/simu/onModel/exp9_param_0.9_100.0/v0_TBMB_exp9_monitoring_values_log.dat"
file10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/simu/onModel/exp10_param_0.9_100.0/v0_TBMB_exp10_monitoring_values_log.dat"
experiences = [file1,file2,file3,file4,file5,file6,file7,file8,file9,file10]
# ---------------------------------------------------------------------------
f = 0
for expe in experiences:
	# -----------------------------------------------------------------------
	with open(expe,'r') as file:
		# -------------------------------------------------------------------
		for line in file:
			it = int(line.split(" ")[0].rstrip())
			previous_state = str(line.split(" ")[1].rstrip())
			plan_time = str(line.split(" ")[2].rstrip())
			delta_prob = str(line.split(" ")[3].rstrip())
			deltaQ = str(line.split(" ")[4].rstrip())
			# ---------------------------------------------------------------
			for dictStateValues in dictOutput["states"]:
				if dictStateValues["state"] == previous_state:
					for dictExpertValues in dictStateValues["values"]:
						if dictExpertValues["expert"] == "MB":
							for key, value in dictExpertValues["values"].items():
								if key == "plan_time":
									value[it] = plan_time
								elif key == "delta_prob":
									value[it] = delta_prob
								elif key == "deltaQ":
									value[it] = deltaQ
							break
					break
		# -------------------------------------------------------------------
		listStates = list()
		for state in range(0, nb_states+1):
			for dictStateValues in dictOutput["states"]:
				if dictStateValues["state"] == str(state):
					for dictExpertValues in dictStateValues["values"]:
						if dictExpertValues["expert"] == "MB":
							yAll[f][state]["plan_time_MB"] = dictExpertValues["values"]["plan_time"]
							yAll[f][state]["deltaQ_MB"] = dictExpertValues["values"]["deltaQ"]
							yAll[f][state]["delta_prob"] = dictExpertValues["values"]["delta_prob"]
							break
	# -----------------------------------------------------------------------
	f += 1
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# PLOT DATA
# ---------------------------------------------------------------------------
for expe in range(0, len(experiences)):
	print("Expe: "+str(expe))
	# -----------------------------------------------------------------------
	fig = plt.figure()
	i = 1
	for state in range(0, 16):
		print("State: "+str(state))
		ax = fig.add_subplot(4,4,i)
		#ax.plot(xAll[expe], yAll[expe][state]["deltaQ_MF"], c = "blue", label = ("MF, S" + str(state)))
		ax.plot(xAll[expe], yAll[expe][state]["deltaQ_MB"], c = "red", label = ("MB, S" + str(state)))
		#ax.plot(xAll[expe], yAll[expe][state]["plan_time_MF"], c = "blue", label = ("MF, S" + str(state)))
		#ax.plot(xAll[expe], yAll[expe][state]["plan_time_MB"], c = "red", label = ("MB, S" + str(state)))
		#ax.plot(xAll[expe], yAll[expe][state]["RPE"], c = "blue", label = ("MF, S" + str(state)))
		#ax.plot(xAll[expe], yAll[expe][state]["delta_prob"], c = "red", label = ("MB, S" + str(state)))
		ax.set_ylim(0,10)
		ax.legend(prop={'size': 6})
		i += 1
	# -----------------------------------------------------------------------
	fig.text(0.5, 0.04, 'Iterations', ha='center', va='center')
	fig.text(0.06, 0.5, 'DeltaQ', ha='center', va='center', rotation='vertical')
	#fig.text(0.06, 0.5, 'Time of planification', ha='center', va='center', rotation='vertical')
	#fig.text(0.06, 0.5, 'RPE / delta of probabilities of transition', ha='center', va='center', rotation='vertical')
	fig.subplots_adjust(wspace=0.4, hspace=0.4)
	plt.show()
	plt.savefig('deltaQ_exp'+str(expe+1)+'_part1.png')
	#plt.savefig('plan_time_exp'+str(expe+1)+'_part1.png')
	#plt.savefig('RPE_delta_prob_exp'+str(expe+1)+'_part1.png')
	# -----------------------------------------------------------------------
	fig = plt.figure()
	i = 1
	for state in range(16, 32):
		ax = fig.add_subplot(4,4,i)
		ax.plot(xAll[expe], yAll[expe][state]["deltaQ_MF"], c = "blue", label = ("MF, S" + str(state)))
		ax.plot(xAll[expe], yAll[expe][state]["deltaQ_MB"], c = "red", label = ("MB, S" + str(state)))
		#ax.plot(xAll[expe], yAll[expe][state]["plan_time_MF"], c = "blue", label = ("MF, S" + str(state)))
		#ax.plot(xAll[expe], yAll[expe][state]["plan_time_MB"], c = "red", label = ("MB, S" + str(state)))
		#ax.plot(xAll[expe], yAll[expe][state]["RPE"], c = "blue", label = ("MF, S" + str(state)))
		#ax.plot(xAll[expe], yAll[expe][state]["delta_prob"], c = "red", label = ("MB, S" + str(state)))
		ax.set_ylim(0,10)
		ax.legend(prop={'size': 6})
		i += 1
	# -----------------------------------------------------------------------
	fig.text(0.5, 0.04, 'Iterations', ha='center', va='center')
	fig.text(0.06, 0.5, 'DeltaQ', ha='center', va='center', rotation='vertical')
	#fig.text(0.06, 0.5, 'Time of planification', ha='center', va='center', rotation='vertical')
	#fig.text(0.06, 0.5, 'RPE / delta of probabilities of transition', ha='center', va='center', rotation='vertical')
	fig.subplots_adjust(wspace=0.4, hspace=0.4)
	plt.show()
	plt.savefig('deltaQ_exp'+str(expe+1)+'_part2.png')
	#plt.savefig('plan_time_exp'+str(expe+1)+'_part1.png')
	#plt.savefig('RPE_delta_prob_exp'+str(expe+1)+'_part1.png')
	# -----------------------------------------------------------------------
	fig = plt.figure()
	i = 1
	for state in range(32, 38):
		ax = fig.add_subplot(2,c3,i)
		ax.plot(xAll[expe], yAll[expe][state]["deltaQ_MF"], c = "blue", label = ("MF, S" + str(state)))
		ax.plot(xAll[expe], yAll[expe][state]["deltaQ_MB"], c = "red", label = ("MB, S" + str(state)))
		#ax.plot(xAll[expe], yAll[expe][state]["plan_time_MF"], c = "blue", label = ("MF, S" + str(state)))
		#ax.plot(xAll[expe], yAll[expe][state]["plan_time_MB"], c = "red", label = ("MB, S" + str(state)))
		#ax.plot(xAll[expe], yAll[expe][state]["RPE"], c = "blue", label = ("MF, S" + str(state)))
		#ax.plot(xAll[expe], yAll[expe][state]["delta_prob"], c = "red", label = ("MB, S" + str(state)))
		ax.set_ylim(0,10)
		ax.legend(prop={'size': 6})
		i += 1
	# -----------------------------------------------------------------------
	fig.text(0.5, 0.04, 'Iterations', ha='center', va='center')
	fig.text(0.06, 0.5, 'DeltaQ', ha='center', va='center', rotation='vertical')
	#fig.text(0.06, 0.5, 'Time of planification', ha='center', va='center', rotation='vertical')
	#fig.text(0.06, 0.5, 'RPE / delta of probabilities of transition', ha='center', va='center', rotation='vertical')
	fig.subplots_adjust(wspace=0.4, hspace=0.4)
	plt.show()
	plt.savefig('deltaQ_exp'+str(expe+1)+'_part3.png')
	#plt.savefig('plan_time_exp'+str(expe+1)+'_part1.png')
	#plt.savefig('RPE_delta_prob_exp'+str(expe+1)+'_part1.png')
# ---------------------------------------------------------------------------






