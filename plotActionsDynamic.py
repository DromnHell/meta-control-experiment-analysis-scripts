#!/usr/bin/env python3
#encoding: utf-8

# ---------------------------------------------------------------------------
# IMPORT
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import statistics
import json
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
# SIMULATION ON MODEL / MF OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.2/MF/exp1_alpha0.6_gamma0.9_beta100/v1_TBMF_exp1_actions_evolution_log.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.2/MF/exp2_alpha0.6_gamma0.9_beta100/v1_TBMF_exp2_actions_evolution_log.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.2/MF/exp3_alpha0.6_gamma0.9_beta100/v1_TBMF_exp3_actions_evolution_log.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.2/MF/exp4_alpha0.6_gamma0.9_beta100/v1_TBMF_exp4_actions_evolution_log.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.2/MF/exp5_alpha0.6_gamma0.9_beta100/v1_TBMF_exp5_actions_evolution_log.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.2/MF/exp6_alpha0.6_gamma0.9_beta100/v1_TBMF_exp6_actions_evolution_log.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.2/MF/exp7_alpha0.6_gamma0.9_beta100/v1_TBMF_exp7_actions_evolution_log.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.2/MF/exp8_alpha0.6_gamma0.9_beta100/v1_TBMF_exp8_actions_evolution_log.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.2/MF/exp9_alpha0.6_gamma0.9_beta100/v1_TBMF_exp9_actions_evolution_log.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/changePositionOfReward/Hab_only/simu/onModel/optimisticQ1/alphaFilter0.2/MF/exp10_alpha0.6_gamma0.9_beta100/v1_TBMF_exp10_actions_evolution_log.dat"
experiences = [CR1]#,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
nb_experiments = len(experiences)
nb_states = 38
nb_actions = 8
# ---------------------------------------------------------------------------
yAll = list()
xAll = list()
i = 0
# ---------------------------------------------------------------------------
for expe in experiences:
	x = list()
	dict_states = dict()
	for state in range(0,nb_states):
		dict_states[str(state)] = [list(),list(),list(),list(),list(),list(),list(),list()]
	# -----------------------------------------------------------------------
	with open(expe) as file:
		dict_actions_prob = json.load(file)
		it = 0
		for dictValues in dict_actions_prob["logs"]:
			x.append(it)
			for dictStateActionsProbs in dictValues["values"]:
				for state in range(0,nb_states):
					if dictStateActionsProbs["state"] == str(state):
						decided_action = dictStateActionsProbs["decided_action"]
						list_probs = dictStateActionsProbs["actions_prob"]
						for action in range(0,nb_actions):
							dict_states[str(state)][action].append(list_probs[action])
			it += 1
	# -----------------------------------------------------------------------
	#plt.plot(x, y, c=color[i])c
	yAll.append(dict_states)
	xAll.append(x)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# PLOT ALL DATA
# ---------------------------------------------------------------------------
fig = plt.figure()
for expe in range(0, nb_experiments):
	i = expe+1
	for state in range(0,nb_states):
		for action in range(0,nb_actions):
			plt.plot(xAll[expe], yAll[expe][str(state)][action], c = color[action], label = "Action "+str(action))
		plt.grid(linestyle='--')
		plt.axvline(x = 1600, c = "black", linewidth = 2, label = "Switch of the reward's position")
		plt.xlabel("Number of actions")
		plt.ylabel("Probabilities of action")
		plt.xlim(0,3200)
		plt.title("State "+str(state))
		plt.legend()
		plt.show()
# ---------------------------------------------------------------------------















