#!/usr/bin/env python3
#encoding: utf-8

# ---------------------------------------------------------------------------
import sys
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from PIL import Image
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
import matplotlib.colors
import matplotlib.patches as mpatches
import palettable
from palettable.colorbrewer.sequential import Greys_9, Greys_9_r, Reds_9, Reds_9_r, YlOrRd_9, YlOrRd_9_r, Greens_9 
from optparse import OptionParser
import json
import os
from os import listdir
from os.path import isfile, join
import re
import copy

INF = 100000000000000000
# ---------------------------------------------------------------------------

def voronoi_finite_polygons_2d(vor, radius=None):
    """
    Reconstruct infinite voronoi regions in a 2D diagram to finite
    regions.

    Parameters
    ----------
    vor : Voronoi
        Input diagram
    radius : float, optional
        Distance to 'points at infinity'.

    Returns
    -------
    regions : list of tuples
        Indices of vertices in each revised Voronoi regions.
    vertices : list of tuples
        Coordinates for revised Voronoi vertices. Same as coordinates
        of input vertices, with 'points at infinity' appended to the
        end.

    """
    #--------------------------------------------------------------------
    if vor.points.shape[1] != 2:
        raise ValueError("Requires 2D input")
    #--------------------------------------------------------------------
    new_regions = []
    new_vertices = vor.vertices.tolist()
    #--------------------------------------------------------------------
    center = vor.points.mean(axis=0)
    if radius is None:
        radius = vor.points.ptp().max()
    #--------------------------------------------------------------------
    # Construct a map containing all ridges for a given point
    all_ridges = {}
    for (p1, p2), (v1, v2) in list(zip(vor.ridge_points, vor.ridge_vertices)):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))
    #--------------------------------------------------------------------
    # Reconstruct infinite regions
    for p1, region in enumerate(vor.point_region):
        vertices = vor.regions[region]
        #----------------------------------------------------------------
        if all(v >= 0 for v in vertices):
            # finite region
            new_regions.append(vertices)
            continue
        #----------------------------------------------------------------
        # reconstruct a non-finite region
        ridges = all_ridges[p1]
        new_region = [v for v in vertices if v >= 0]
        #----------------------------------------------------------------
        for p2, v1, v2 in ridges:
            #------------------------------------------------------------
            if v2 < 0:
                v1, v2 = v2, v1
            #------------------------------------------------------------
            if v1 >= 0:
                # finite ridge: already in the region
                continue
            #------------------------------------------------------------
            # Compute the missing endpoint of an infinite ridge
            t = vor.points[p2] - vor.points[p1] # tangent
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])  # normal
            #------------------------------------------------------------
            midpoint = vor.points[[p1, p2]].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[v2] + direction * radius
            #------------------------------------------------------------
            new_region.append(len(new_vertices))
            new_vertices.append(far_point.tolist())
        #----------------------------------------------------------------
        # sort region counterclockwise
        vs = np.asarray([new_vertices[v] for v in new_region])
        c = vs.mean(axis=0)
        angles = np.arctan2(vs[:,1] - c[1], vs[:,0] - c[0])
        new_region = np.array(new_region)[np.argsort(angles)]
        #----------------------------------------------------------------
        # finish
        new_regions.append(new_region.tolist())
    #--------------------------------------------------------------------
    return new_regions, np.asarray(new_vertices)
    #--------------------------------------------------------------------


def create_map(img, offset, resolution, file1, file2, keystates, experts, iteration, num):
    """
    Create the map with color code according to deltaQ value of state
    """
    # ------------------------------------------------------------------
    #print("Iteration --> "+str(iteration))
    clk_file = file1[:,0]   
    x_file = file1[:,1]
    y_file = file1[:,2]
    # ------------------------------------------------------------------
    # make up data points
    x = x_file
    y = y_file
    xmin = (x.min() - offset[0]) / resolution
    xmax = (x.max() - offset[0]) / resolution
    ymin = (y.min() - offset[1]) / resolution
    ymax = (y.max() - offset[1]) / resolution
    xc = (file2[:,1] - offset[0]) / resolution
    yc = (file2[:,2] - offset[1]) / resolution
    pointsForVoronoi = list(zip(xc, yc))
    # ------------------------------------------------------------------
    # compute Voronoi tesselation
    vor = Voronoi(pointsForVoronoi)
    # ------------------------------------------------------------------
    # reconstruct infnit voronoi
    regions, vertices = voronoi_finite_polygons_2d(vor)
    # ------------------------------------------------------------------
    fig, ax = plt.subplots()
    # ------------------------------------------------------------------
    # Change the goal after a certain iteration
    if iteration < keystates[2]:
        goal = keystates[1]
    else:
        goal = keystates[3]
    # ------------------------------------------------------------------
    # colorize polygon according to the expert who choose the action to do
    #cmap = plt.cm.YlOrRd
    #norm = matplotlib.colors.Normalize(vmin = 0, vmax = 40)
    #norm = matplotlib.colors.Normalize(vmin = 0, vmax = 10)
    state = 0
    for region in regions:
        polygon = vertices[region]
        if str(state) in experts.keys():
            if experts[str(state)] == "Hab":
                colorState = (1,0.0,0.0,1.0)
            elif experts[str(state)] == "GD":
                colorState = (0.0,0.0,1.0,1.0)
            if state == goal:
                colorState = (1.0,1.0,1.0,1.0)
        else:
            colorState = (0.0,0.0,0.0,1.0)
        plt.fill(*list(zip(*polygon)), color = colorState, alpha = 1, zorder = 1)
        state = state + 1
    #sm = plt.cm.ScalarMappable(cmap = cmap, norm = norm)
    #sm.set_array([])
    #cbar = fig.colorbar(sm, orientation = 'horizontal')
    #cbar.ax.set_xticklabels(['0', '0.05', '0.1', '0.15', '0.2', '0.25', '0.3', '0.35', '0.4'])
    #cbar.ax.set_xticklabels(['0', '0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07','0.08','0.09', '0.1'])
    # ------------------------------------------------------------------
    # Create the map
    for s in np.arange(len(xc)):
        if s in keystates[0]:
            color = 'green'
            label = 'Initial states'
        elif s == goal:
            color = 'purple'
            label = 'Goal'
        else:
            color = 'grey'
            label = 'States'
        ax.plot(xc[s], yc[s], c = color, marker = 'o', markersize = 10, label = label, zorder = 3)
        ax.text(xc[s]+4, yc[s]-1, str(s), color = 'k' , fontsize = 12, zorder = 3)
    handles, labels = ax.get_legend_handles_labels()
    handle_list, label_list = [], []
    for handle, label in zip(handles, labels):
        if label not in label_list:
            handle_list.append(handle)
            label_list.append(label)
    margin = 30
    ax.axis([xmin-margin, xmax+margin, ymin-margin, ymax+margin])
    ax.legend(handle_list, label_list, loc = 1)
    if iteration == "END":
        ax.set_title('Map of the deltaQ values for the last iteration ')
    else:
        ax.set_title('Map of the deltaQ values for the iteration ' + str(iteration))
    ax.imshow(img, zorder = 2)
    plt.savefig('map'+str(num)+'.png')
    plt.close()
    # ------------------------------------------------------------------


def manage_experts_file(expertsFile, firstLastStep):
    """
    Manage the file that contains the dynamics of the expert
    """
    # ------------------------------------------------------------------
    start = firstLastStep[0]
    end = firstLastStep[1] 
    step = firstLastStep[2]
    # ------------------------------------------------------------------
    dict_expert = dict()
    dict_it = dict()
    # ------------------------------------------------------------------
    it = start
    # ------------------------------------------------------------------
    lastIt = sum(1 for line in open(expertsFile, 'r'))
    # ------------------------------------------------------------------
    with open(expertsFile,'r') as file4:
        # --------------------------------------------------------------
        if step == INF:
            step = lastIt-1
        # --------------------------------------------------------------
        for line in file4:
            # ----------------------------------------------------------
            l = int(line.split(" ")[0].rstrip())
            state = line.split(" ")[1].rstrip()
            expert = line.split(" ")[4].rstrip()
            dict_it[state] = expert
            # ----------------------------------------------------------
            if l == it or l == lastIt-1:
                # ------------------------------------------------------
                if l == lastIt-1:
                    it = lastIt-1
                # ------------------------------------------------------
                dict_expert[it] = dict_it
                # ------------------------------------------------------
                it = it + step
                dict_it = copy.deepcopy(dict_it)
            # ----------------------------------------------------------
            if l == end:
                break
        # --------------------------------------------------------------
    #print(dict_expert)
    return dict_expert
    # ------------------------------------------------------------------


def manage_keystates_file(keyStatesFile):
    """
    Manage the file that contains the key states
    """
    # ------------------------------------------------------------------
    init = list()
    with open(keyStatesFile,'r') as file3:
        for line in file3:
            if line.split(" ")[0] == "goal":
                goal = int(line.split(" ")[1])
            elif line.split(" ")[0] == "new_goal":
                switch = int(line.split(" ")[1])
                new_goal = int(line.split(" ")[2])
            elif line.split(" ")[0] == "init":
                init = init + list(map(int, line.split(" ")[1:]))
    # ------------------------------------------------------------------
    keystates = [init, goal, switch, new_goal]
    return keystates
    # ------------------------------------------------------------------


def manage_map_files(path):
    """
    Manage the files requisite for construct the map
    """
    # ------------------------------------------------------------------
    onlyfiles = [f for f in listdir(mapDataPath) if isfile(join(mapDataPath,f))]
    # ------------------------------------------------------------------
    poseOverTime = [s for s in onlyfiles if "poseCell_log" in s][0]
    statePositions = [s for s in onlyfiles if "voronoiCenters_exp" in s][0]
    expGlobalParam = [s for s in onlyfiles if "param_exp" in s][0]
    mapsOverTime = sorted([s for s in onlyfiles if ".yaml" in s])
    # ------------------------------------------------------------------
    runData = mapDataPath + "/" + poseOverTime
    file1 = np.genfromtxt(runData)
    # ------------------------------------------------------------------
    stateData = mapDataPath + "/" + statePositions
    file2 = np.genfromtxt(stateData)
    # ------------------------------------------------------------------
    paramDict = {}
    with open(mapDataPath + "/" + mapsOverTime[-1]) as f:
        for line in f:
            try:
                (key, val) = line.split(":")
            except ValueError:
                break
            paramDict[key] = val[1:].strip('\n')
    # ------------------------------------------------------------------
    paramGlobalDict = {}
    with open(mapDataPath + "/" + expGlobalParam) as f:
        for line in f:
            try:
                (key, val) = line.split(":")
            except ValueError:
                break
            paramGlobalDict[key] = val[1:].strip('\n')
    # ------------------------------------------------------------------
    # apply transparency on image
    img = Image.open(mapDataPath +"/"+ paramDict['image'])
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if (0 <= item[0] <= 150) and (0 <= item[1] <= 150) and (0 <= item[2] <= 150):
             # draw the border in grey
            newData.append((100, 100, 100, 255))
        else:
            # just apply the transparency, don't care about the color
            newData.append((0, 0, 0, 0)) 

    img.putdata(newData)
    # ------------------------------------------------------------------
    resolution = float(paramDict['resolution'])
    offset = ((paramDict['origin'][1:(len(paramDict['origin'])-1)]).replace(" ","")).split(',')
    offset = [float(i) for i in offset]
    # ------------------------------------------------------------------
    return img, offset, resolution, file1, file2
    # ------------------------------------------------------------------


if __name__ == "__main__":
    # ----------------------------------------------------------------------
    # MANAGE ARGUMENTS
    # ----------------------------------------------------------------------
    usage = "usage: plotColoredMapAccordingToDeltaQ.py [options] [path toward map files] [file that contains the key states] [file that contains the dynamics of the experts] [name of output file without the extension]"
    parser = OptionParser(usage)
    parser.add_option('-f', '--firstAction', 
        type = "int", 
        dest = "firstAction", 
        help = "This option is the first iteration/action that we want to vizualise. By default, the first iteration is 1.")
    parser.add_option('-l', '--lastAction', 
        type = "int", 
        dest = "lastAction",
        help = "This option is the last iteration/action that we want to vizualise. By default, the last iteration is the real last iteration.") 
    parser.add_option('-s', '--steps', 
        type = "int", 
        dest = "steps", 
        help = "This option is the step used to print the iteration betwen the firt and the last. By default, the step is the last iteration.")
    # ----------------------------------------------------------------------
    (options, args) = parser.parse_args()
    # ----------------------------------------------------------------------
    # Check arguments validity
    if len(args) != 4:
        parser.error("Wrong number of arguments.")
    else:
        mapDataPath = sys.argv[1]
        keyStatesFile = sys.argv[2]
        expertsFile = sys.argv[3]
        outputFile = sys.argv[4]
    # ----------------------------------------------------------------------
    # Check options validity
    if not options.firstAction: 
        options.firstAction = 0
    elif type(options.firstAction) != int:
        parser.error("Option -f must be a integer.")
    elif options.firstAction < 0:
        parser.error("Option -f must be positiv.")
    if not options.lastAction: 
        options.lastAction = INF
    elif type(options.lastAction) != int:
        parser.error("Option -l must be a integer.")
    elif options.firstAction < 0:
        parser.error("Option -f must be positiv.")
    if not options.steps: 
        options.steps = INF
    elif type(options.steps) != int:
        parser.error("Option -s must be a integer.")
    elif options.firstAction < 0:
        parser.error("Option -f must be positiv.")
    # ----------------------------------------------------------------------

    firstLastStep = [options.firstAction, options.lastAction, options.steps]
    # ----------------------------------------------------------------------
    print(options, args)
    # ----------------------------------------------------------------------
    params = {
    'axes.labelsize': 16,
    'axes.titlesize': 18,
    'legend.fontsize': 16,
    'xtick.labelsize': 14,
    'ytick.labelsize': 14,
    'text.usetex': False,
    'figure.figsize': [10.0, 10.0]
    }
    mpl.rcParams.update(params)
    # ----------------------------------------------------------------------
    img, offset, resolution, file1, file2 = manage_map_files(mapDataPath)
    # ----------------------------------------------------------------------
    keystates = manage_keystates_file(keyStatesFile)
    # ----------------------------------------------------------------------
    dict_expert = manage_experts_file(expertsFile, firstLastStep)
    # ----------------------------------------------------------------------
    num = 0
    for it in dict_expert:
        create_map(img, offset, resolution, file1, file2, keystates, dict_expert[it], it, num)
        num = num + 1
    # ----------------------------------------------------------------------
    # Make a gif with images
    files = ['map{}.png'.format(i) for i in range(num)]
    newmov = ImageSequenceClip(files, fps = 4)
    newmov.write_gif(outputFile+'.gif')
    # ----------------------------------------------------------------------
    # Delete images
    folder = os.getcwd()
    expression = r"map[0-9]+.png"
    for the_file in listdir(folder):
        if re.match(expression, the_file):
            os.remove(the_file)
    # ----------------------------------------------------------------------



