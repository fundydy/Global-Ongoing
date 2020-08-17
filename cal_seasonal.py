#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#===============================================================================
#Generate time: 2020年 08月 10日 星期一 17:19:24 CST
from math import cos,sin,pi
import sys
import numpy as np
import pandas as pd
import os

#===============================================================================
#Main program
#Add seasonal signal(seasonal.csv) to XZAR.tenv and generate XZAR_seasonal.tenv
#Usage: cal_seasonal.py 
#input sitename


np.set_printoptions(precision=6, suppress=True)

sea=pd.read_csv('./seasonal.csv',header=None)
sea.columns=["st","cy","sy","scy","ssy","chy","shy","schy","sshy"]
st=sea["st"]
st=np.array(st)
X=sea[["cy","sy","scy","ssy","chy","shy","schy","sshy"]]
X=np.array(X)

out=np.empty((len(st[:]),))

for i in range(len(st[:])):
	site=st[i][0:4]
	cy=X[i,0]
	sy=X[i,1]
	chy=X[i,4]
	shy=X[i,5]
	tenvfile='./'+site + '.tenv'
	outfile=site + '_seasonal.tenv'
	tenv=pd.read_csv(tenvfile,header=None,sep='\s+')
	tenv.columns=["st","ymd","dyr","mjd","gw","gd","e","n","u","zero","de","dn","du","ce","cn","cu"]
	dyru=tenv[["dyr","u"]]
	dyru=np.array(dyru)
	#print(dyru[0:8,:])
	Y=dyru[:,:]
	for i in range(len(Y[:,0])):
		Y[i,1]=Y[i,1]-(cy*cos(2*pi*Y[i,0])+sy*sin(2*pi*Y[i,0])+chy*cos(4*pi*Y[i,0])+shy*sin(4*pi*Y[i,0]))/1000.0
	#print(Y[0:8,:])
	tenv["u"]=Y[:,1]
	tenv.to_csv(outfile,header=None,sep='\t',index=False,float_format='%.6f')
	print(site+"--done")
