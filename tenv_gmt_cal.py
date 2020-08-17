#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import numpy as np
import sys
#===============================================================================
def madmethod(gmt):
#estimate trend and rm
	trend=np.polyfit(gmt[:,0],gmt[:,1],1)
	p=np.poly1d(trend)
#	print(p)
	gmt[:,1]=gmt[:,1]-p(gmt[:,0])
#	print(np.size(gmt))
#mad
	array=gmt[:,1]
	med=np.median(array)
	b=1.4826
	mad=b*np.median(np.abs(array-med))
#	print(mad)
	low=med-(3*mad)
	up=med+(3*mad)
	arr=gmt[(gmt[:,1]>low) & (gmt[:,1]<up),:]
#	print(np.size(arr))
#add trend
	arr[:,1]=arr[:,1]+p(arr[:,0])
	arr[:,1]=arr[:,1]-np.mean(arr[:,1])
	return arr
# Main program
#===============================================================================

gmtfn=sys.argv[1]
gmt=np.loadtxt(gmtfn)
gmtf=madmethod(gmt)
np.savetxt(gmtfn,gmtf,fmt="%9.4f",delimiter=" ")

minvalue=np.min(gmtf,axis=0)
maxvalue=np.max(gmtf,axis=0)
minyear=np.floor(minvalue[0])
maxyear=np.ceil(maxvalue[0])
y=np.array([np.absolute(minvalue[1]),np.absolute(maxvalue[1])])
meany=np.mean(gmtf[:,1])


gmtf[:,1]=gmtf[:,1]-meany
ylength=np.max(y,axis=0)
yl=np.ceil(ylength/10)*10*1.2
ym=-yl
print('%d %d %d %d' %(ym,yl,minyear,maxyear))
