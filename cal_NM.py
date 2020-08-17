#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#===============================================================================
#Main program
#Generate time: 2020年 07月 31日 星期五 16:16:46 CST
#===============================================================================
import math
import sys


lat=float(sys.argv[1])
lat=lat/180*math.pi
sinB2=math.pow(math.sin(lat),2)

a = 6378137.0
f = 298.257223563
alpha=1/f
b=6356752.3142
c=6399593.6258
e2=0.00669437999013

W=math.pow((1-e2*sinB2),0.5)
# Meridian circle radius
M=a*(1-e2)/math.pow(W,3)

# The prime vertical radius
N=a/W

print('%-11.4f %-11.4f' %(M,N))
