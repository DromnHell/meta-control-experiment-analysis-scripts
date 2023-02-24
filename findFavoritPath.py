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
dictMiddleMF = {"path": "middle", "values": list()}
dictDownMF = {"path": "down", "values": list()}
dictMiddleMB = {"path": "middle", "values": list()}
dictDownMB = {"path": "down", "values": list()}
dictMF = {"expert": "MF", "paths": [dictMiddleMF, dictDownMF]}
dictMB = {"expert": "MB", "paths": [dictMiddleMB, dictDownMB]}
dict_paths = {"paths": [dictMF, dictMB]}
# ---------------------------------------------------------------------------
# EXPE ON REAL WORLD / MF OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp1_alpha0.6_gamma0.9_beta100_optimistic/allStatesEvolution.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp2_alpha0.6_gamma0.9_beta100_optimistic/allStatesEvolution.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp3_alpha0.6_gamma0.9_beta100_optimistic/allStatesEvolution.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp4_alpha0.6_gamma0.9_beta100_optimistic/allStatesEvolution.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp5_alpha0.6_gamma0.9_beta100_optimistic/allStatesEvolution.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp6_alpha0.6_gamma0.9_beta100_optimistic/allStatesEvolution.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp7_alpha0.6_gamma0.9_beta100_optimistic/allStatesEvolution.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp8_alpha0.6_gamma0.9_beta100_optimistic/allStatesEvolution.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp9_alpha0.6_gamma0.9_beta100_optimistic/allStatesEvolution.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp10_alpha0.6_gamma0.9_beta100_optimistic/allStatesEvolution.dat"
experiences_MF = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
for exp in experiences_MF:
	l = 0
	middle = 0
	down = 0
	# -----------------------------------------------------------------------
	with open(exp,'r') as file1:
		l = 0
		for line in file1:
			l += 1
			if l > 1200:
				if line.split(" ")[2].rstrip() == "7":
					middle += 1
				elif line.split(" ")[2].rstrip() == "19":
					down += 1
	# -----------------------------------------------------------------------				
	for expert in dict_paths["paths"]:
		if expert["expert"] == "MF":
			for path in expert["paths"]:
				if path["path"] == "middle":
					path["values"].append(middle)
				elif path["path"] == "down":
					path["values"].append(down)
			break
# ---------------------------------------------------------------------------
# EXPE ON REAL WORLD / MB OPTIMISTIC
# ---------------------------------------------------------------------------
CR1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/real/exp1_gamma0.95_beta100_optimistic/allStatesEvolution.dat"
CR2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/real/exp2_gamma0.95_beta100_optimistic/allStatesEvolution.dat"
CR3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/real/exp3_gamma0.95_beta100_optimistic/allStatesEvolution.dat"
CR4 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/real/exp4_gamma0.95_beta100_optimistic/allStatesEvolution.dat"
CR5 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/real/exp5_gamma0.95_beta100_optimistic/allStatesEvolution.dat"
CR6 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/real/exp6_gamma0.95_beta100_optimistic/allStatesEvolution.dat"
CR7 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/real/exp7_gamma0.95_beta100_optimistic/allStatesEvolution.dat"
CR8 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/real/exp8_gamma0.95_beta100_optimistic/allStatesEvolution.dat"
CR9 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/real/exp9_gamma0.95_beta100_optimistic/allStatesEvolution.dat"
CR10 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MB/real/exp10_gamma0.95_beta100_optimistic/allStatesEvolution.dat"
experiences_MB = [CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8,CR9,CR10]
# ---------------------------------------------------------------------------
for exp in experiences_MB:
	l = 0
	middle = 0
	down = 0
	# -----------------------------------------------------------------------
	with open(exp,'r') as file1:
		for line in file1:
			l += 1
			if l > 1200:
				if line.split(" ")[2].rstrip() == "7":
					middle += 1
				elif line.split(" ")[2].rstrip() == "19":
					down += 1
	# -----------------------------------------------------------------------				
	for expert in dict_paths["paths"]:
		if expert["expert"] == "MB":
			for path in expert["paths"]:
				if path["path"] == "middle":
					path["values"].append(middle)
				elif path["path"] == "down":
					path["values"].append(down)
			break
# ---------------------------------------------------------------------------
# PRINT
# ---------------------------------------------------------------------------
print(dict_paths)
