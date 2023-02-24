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


def create_map(img, offset, resolution, file1, file2, init, goal, vValues, iteration, num):
    """
    Create the map with color code according to V-values of state
    """
    # ------------------------------------------------------------------
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
    # colorize polygon according to Vvalues
    cmap = plt.cm.YlOrRd
    #norm = matplotlib.colors.Normalize(vmin = 0, vmax = 400)
    #norm = matplotlib.colors.Normalize(vmin = 0, vmax = 100)
    #norm = matplotlib.colors.Normalize(vmin = 0, vmax = 200)
    norm = matplotlib.colors.Normalize(vmin = 0, vmax = 300)

    state = 0
    for region in regions:
        polygon = vertices[region]
        if not str(state) in vValues.keys():
            colorState = cmap(norm(100))
        else:
            colorState = cmap(norm(vValues[str(state)]*100))
        plt.fill(*list(zip(*polygon)), color = colorState, alpha = 1, zorder = 1)
        state = state + 1
    sm = plt.cm.ScalarMappable(cmap = cmap, norm = norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, orientation = 'horizontal')
    #cbar.ax.set_xticklabels(['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4'])
    #cbar.ax.set_xticklabels(['0', '0.2', '0.4', '0.6', '0.8', '1'])
    #cbar.ax.set_xticklabels(['0', '0.25', '0.5', '0.75', '1', '1.25', '1.5', '1.75', '2'])
    cbar.ax.set_xticklabels(['0', '0.5', '1', '1.5', '2', '2.5', '3'])
    # ------------------------------------------------------------------
    # plot 
    for s in np.arange(len(xc)):
        if s in init:
            color = 'purple'
            label = 'Initial states'
        elif s == goal:
            color = 'blue'
            label = 'Goal'
        else:
            color = 'green'
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
        ax.set_title('Map of V-values for the last iteration ')
    else:
        ax.set_title('Map of V-values for the iteration ' + str(iteration))
    ax.imshow(img, zorder = 2)
    plt.savefig('map'+str(num)+'.png')
    plt.close()
    # ------------------------------------------------------------------


def manage_qvalues_file_MB(qvaluesFile, firstLastStep):
    """
    Manage the file that contains the evolution of q-values
    """
    # ------------------------------------------------------------------
    start = firstLastStep[0]
    end = firstLastStep[1] 
    step = firstLastStep[2]
    # ------------------------------------------------------------------
    vValuesDict = dict()
    # ------------------------------------------------------------------
    it = start
    # ------------------------------------------------------------------
    with open(qvaluesFile,'r') as file4:
        # --------------------------------------------------------------
        data = file4.read()
        data = re.sub(r'\n|\t', '' , data)
        listIterations = data.split("<>")
        lastIt = len(listIterations)
        # --------------------------------------------------------------
        if step == INF:
            step = lastIt-1
        # --------------------------------------------------------------
        for iteration in listIterations:
            # ----------------------------------------------------------
            dictIteration = json.loads(iteration)
            #print(dictIteration["actioncount"])
            # ----------------------------------------------------------
            if dictIteration["actioncount"] == it or dictIteration["actioncount"] == lastIt-1:
                # ------------------------------------------------------
                if dictIteration["actioncount"] == lastIt-1:
                        it = lastIt-1
                # ------------------------------------------------------
                vValuesDict[it] = dict()
                # ------------------------------------------------------
                for dictStateValues in dictIteration["states"]:
                    listQvalues = list()
                    # --------------------------------------------------
                    for dictActionValue in dictStateValues["actionQual"]:
                        listQvalues.append(dictActionValue["Qvalue"])
                    # --------------------------------------------------
                    vValuesDict[it][str(dictStateValues["state"])] = max(listQvalues)
                 # -----------------------------------------------------
                it = it + step
            # ----------------------------------------------------------
            if dictIteration["actioncount"] == end:
                break
        
        # --------------------------------------------------------------
    return vValuesDict
    # ------------------------------------------------------------------


def manage_qvalues_file_MF(qvaluesFile, firstLastStep):
    """
    Manage the file that contains the evolution of q-values
    """
    # ------------------------------------------------------------------
    start = firstLastStep[0]
    end = firstLastStep[1] 
    step = firstLastStep[2]
    # ------------------------------------------------------------------
    vValuesDict = dict()
    # ------------------------------------------------------------------
    it = start
    # ------------------------------------------------------------------
    with open(qvaluesFile,'r') as file4:
        # --------------------------------------------------------------
        datas = json.load(file4)
        listIterations = datas["logs"]
        lastIt = len(listIterations)
        # --------------------------------------------------------------
        if step == INF:
            step = lastIt-1
        # --------------------------------------------------------------
        for dictIteration in listIterations:
            # ----------------------------------------------------------
            if dictIteration["actioncount"] == it or dictIteration["actioncount"] == lastIt-1:
                # ------------------------------------------------------
                if dictIteration["actioncount"] == lastIt-1:
                        it = lastIt-1
                # ------------------------------------------------------
                vValuesDict[it] = dict()
                # ------------------------------------------------------
                for dictStateValues in dictIteration["values"]:
                    listQvalues = list()
                    # --------------------------------------------------
                    for dictActionValue in dictStateValues["values"]:
                        listQvalues.append(dictActionValue["value"])
                    # --------------------------------------------------
                    vValuesDict[it][dictStateValues["state"]] = max(listQvalues)
                 # -----------------------------------------------------
                it = it + step
            # ----------------------------------------------------------
            if dictIteration["actioncount"] == end:
                break
        # --------------------------------------------------------------
    print(vValuesDict)
    return vValuesDict
    # ------------------------------------------------------------------


def manage_keystates_file(statesFile):
    """
    Manage the file that contains the key states
    """
    # ------------------------------------------------------------------
    init = list()
    goal = 0
    with open(statesFile,'r') as file3:
        for line in file3:
            if line.split(" ")[0] == "goal":
                goal = int(line.split(" ")[1])
            elif line.split(" ")[0] == "init":
                init = init + list(map(int, line.split(" ")[1:]))
    # ------------------------------------------------------------------
    return init, goal
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
    usage = "usage: plotColoredMapAccordingToQvalues.py [options] [path toward map files] [file that contains the key states] [file that contains a succesion of json format of the evolution of qvalues] [name of output file without the extension]"
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
    if len(args) != 5:
        parser.error("Wrong number of arguments.")
    else:
        mapDataPath = sys.argv[1]
        keyStates = sys.argv[2]
        qValuesFile = sys.argv[3]
        outputFile = sys.argv[4]
        controller = sys.argv[5]
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
    init, goal = manage_keystates_file(keyStates)
    # ----------------------------------------------------------------------
    if controller == "MF":
        vValuesDict = manage_qvalues_file_MF(qValuesFile, firstLastStep)
    elif controller == "MB":
        vValuesDict = manage_qvalues_file_MB(qValuesFile, firstLastStep)
    # ----------------------------------------------------------------------
    num = 0
    for it in vValuesDict:
        create_map(img, offset, resolution, file1, file2, init, goal, vValuesDict[it], it, num)
        num = num + 1
    # ----------------------------------------------------------------------
    # Make a gif with images
    files = ['map{}.png'.format(i) for i in range(num)]
    newmov = ImageSequenceClip(files, fps = 2)
    newmov.write_gif(outputFile+'.gif')
    # ----------------------------------------------------------------------
    # Delete images
    folder = os.getcwd()
    expression = r"map[0-9]+.png"
    for the_file in listdir(folder):
        if re.match(expression, the_file):
            os.remove(the_file)
    # ----------------------------------------------------------------------



