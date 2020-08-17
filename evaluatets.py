#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from math import cos,sin,pi
import sys
import numpy as np
import pandas as pd
import os

def trend(x):
	trend=np.polyfit(x[:,0],x[:,1],1,cov=True)
	p=np.poly1d(trend[0])
	covm=trend[1]
	cov=covm[0,1]
	timestd=np.std(x[:,0],ddof=1)
	ustd=np.std(x[:,1],ddof=1)
	r=cov/(timestd*ustd)
	unc=np.absolute(p[1]*np.sqrt((1/(r*r)-1)/(len(x[:,0])-2)))
	
	result=np.array([p[1],unc])
	return result

def res(x):
	trend=np.polyfit(x[:,0],x[:,1],1)
	p=np.poly1d(trend)
	res=x[:,1]-p(x[:,0])
	return res
#   RMS
def resrms(x):
    n=len(x)
    rms=(sum(x*x)/(n-1))**0.5
    return rms

#   WRMS
def wrms(x,sig):
    lam=np.reciprocal(sig*sig)
    xlam=sum(x*lam)/sum(lam)
    wrms=(sum(lam*(x-xlam)*(x-xlam))/sum(lam))**0.5
    return wrms


#===============================================================================
#Main program
#===============================================================================

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
	
	tenvfile='./'+site + '.tenv'
	tenv=pd.read_csv(tenvfile,header=None,sep='\s+')
	tenv.columns=["st","ymd","dyr","mjd","gw","gd","e","n","u","zero","de","dn","du","ce","cn","cu"]	
	u0=tenv[["dyr","u"]]
	u0=np.array(u0)
	du=tenv[["du"]]
	du=np.array(du)
	resu0=res(u0)
	std0=np.std(resu0,ddof=1)*1000
	rms0=resrms(resu0)*1000
	wrms0=wrms(u0[:,1],du[:,0])*1000
	
	tr0=trend(u0)*1000
	print('{0}_origin	{1:5.3f} ± {5:4.2f} mm/yr	res_RMS={2:5.3f} mm	WRMS={3:5.3f} mm	res_STD={4:5.3f} mm'.format(site,tr0[0],rms0,wrms0,std0,tr0[1]))

	corfile='./'+site + '_seasonal.tenv'
	cor=pd.read_csv(corfile,header=None,sep='\s+')
	cor.columns=["st","ymd","dyr","mjd","gw","gd","e","n","u","zero","de","dn","du","ce","cn","cu"]
	u=cor[["dyr","u"]]
	u=np.array(u)
	du=cor[["du"]]
	du=np.array(du)
	resu=res(u)
	std=np.std(resu,ddof=1)*1000
	rms=resrms(resu)*1000
	wrms=wrms(u[:,1],du[:,0])*1000
	tr=trend(u)*1000
	print('{0}_seasonal	{1:5.3f} ± {5:4.2f} mm/yr	res_RMS={2:5.3f} mm	WRMS={3:5.3f} mm	res_STD={4:5.3f} mm'.format(site,tr[0],rms,wrms,std,tr[1]))
	
	decr=(rms-rms0)/rms0*100
	decw=(wrms-wrms0)/wrms0*100
	print("decrease rate:	{0:4.2f}%	{1:4.2f}%".format(decr,decw))

