#!/bin/bash
# GMT modern mode bash template
# Date:    2019-11-13T11:03:39
# User:    root
# Draw timeseries of three components
# Example:ts.sh XZAR

tenv_gmt ${1}_0_clean.tenv
tenv_gmt ${1}_1_clean.tenv
tenv_gmt ${1}_2_clean.tenv
e_file=${1}_0_clean_0.gmt
n_file=${1}_1_clean_1.gmt
u_file=${1}_2_clean_2.gmt


export GMT_SESSION_NAME=$$	# Set a unique session name
    gmt begin $1_clean png E1000

    gmt subplot begin 3x1 -Fs16c/4c  -SCb -M0.5c/0.5c -T"$1_Timeseries" -A+jTL+o0.3c/0.3c
#
    gmt subplot set 0,0 -AE
    resu=(`tenv_gmt_cal.py $e_file`)
    ymin=${resu[0]}
    ymax=${resu[1]}
    yemin=${resu[2]}
    yemax=${resu[3]}
    gmt basemap  -R${yemin}/${yemax}/${ymin}/${ymax}   -Bxf1g1 -Byaf -BWSrt
    cat  >zeroline<< EOF
${yemin} 0
${yemax} 0
EOF
    gmt plot zeroline  -W1p,black,-  
    gmt plot  $e_file -Sc1p -Ey+w2p -W1p,blue -Gblack
#
    gmt subplot set 1,0 -AN
    resu=(`tenv_gmt_cal.py $n_file`)
    ymin=${resu[0]}
    ymax=${resu[1]}
    yemin=${resu[2]}
    yemax=${resu[3]}
    gmt basemap  -R${yemin}/${yemax}/${ymin}/${ymax}   -Bxf1g1 -Byaf -BWSrt
    cat  >zeroline<< EOF
${yemin} 0
${yemax} 0
EOF
    gmt plot zeroline  -W1p,black,-  
    gmt plot  $n_file -Sc1p -Ey+w2p -W1p,green  -Gblack

#
    gmt subplot set 2,0 -AU
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
