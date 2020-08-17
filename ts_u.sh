#!/bin/bash
# -*- coding: UTF-8 -*-
#===============================================================================
#Generate time: 2020年 08月 03日 星期一 20:49:39 CST
#===============================================================================
#Main program
#Usage: 
tenv_gmt ${1}.tenv
e_file=${1}_0.gmt
n_file=${1}_1.gmt
u_file=${1}_2.gmt


export GMT_SESSION_NAME=$$	# Set a unique session name
    gmt begin ${1}_u png E1000

    gmt subplot begin 1x1 -Fs16c/4c  -SCb -M0.5c/0.5c -T"$1_U_Timeseries" -A+jTL+o0.3c/0.3c

#
    gmt subplot set 0,0 -AU
    resu=(`tenv_gmt_cal.py $u_file`)
    ymin=${resu[0]}
    ymax=${resu[1]}
    yemin=${resu[2]}
    yemax=${resu[3]}
    gmt basemap  -R${yemin}/${yemax}/${ymin}/${ymax}   -Bxa1f1g1 -Byaf -BWSrt
    cat  >zeroline<< EOF
${yemin} 0
${yemax} 0
EOF
    gmt plot zeroline  -W1p,black,-  
    gmt plot  $u_file -Sc1p -Ey+w2p -W1p,orange -Gblack
    gmt subplot end

    gmt end 

rm zeroline
rm *.gmt
