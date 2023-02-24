#!/usr/bin/env python3
#encoding: utf-8

# ---------------------------------------------------------------------------
# IMPORT
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
import sys
import os
# ---------------------------------------------------------------------------
qvalFile1 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp4_alpha0.6_gamma0.9_beta100_optimistic/v60_exp12_MF2_allActionValues_log.dat"
qvalFile2 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp4_alpha0.6_gamma0.9_beta100_optimistic/v60_exp13_MF2_allActionValues_log.dat"
qvalFile3 = "/Users/dromnelle/Documents/thèse/experiences/turtlebot/control/MF/real/exp4_alpha0.6_gamma0.9_beta100_optimistic/v60_exp31_MF2_allActionValues_log.dat"
qvalFiles = [qvalFile1,qvalFile2,qvalFile3]
# ---------------------------------------------------------------------------
starCount = [0]
string = '"actioncount":'
# ---------------------------------------------------------------------------
with open("allActionValues_log.dat","w") as fileW:
	# -----------------------------------------------------------------------
	for idx, qvalFile in enumerate(qvalFiles):
		act = 0
		# -------------------------------------------------------------------
		with open(qvalFile, "r") as fileR:
			# ---------------------------------------------------------------
			for line in fileR : 
				# -----------------------------------------------------------
				if string in line :
					act += 1
					actioncount = line.split(":")[1].rstrip()[:-1]
					# -------------------------------------------------------
					if idx > 0 :
						old = actioncount
						new = str(starCount[idx] + act)
						line = line.replace(old, new)
				# -----------------------------------------------------------
				fileW.write(line)
			# ---------------------------------------------------------------
			starCount.append(starCount[idx] + int(actioncount))
# ---------------------------------------------------------------------------








