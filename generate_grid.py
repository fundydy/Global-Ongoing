#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#===============================================================================
#Usage: 
#Description: generate seasonalparameter gridfile from seasonal.csv
#Generate time: 2020年 08月 17日 星期一 15:32:34 CST
from math import cos,sin,pi
from scipy.interpolate import griddata
import sys
import numpy as np
import pandas as pd
import os

#Main program
#===============================================================================
sea=pd.read_csv('./seasonal.csv',header=None)
sea.columns=["st","cy","sy","scy","ssy","chy","shy","schy","sshy"]
st=sea["st"]
st=np.array(st)
X=sea[["cy","sy","chy","shy"]]
X=np.array(X)
cy=X[:,0]
sy=X[:,1]
chy=X[:,2]
shy=X[:,3]

