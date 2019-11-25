#!/bin/csh
set a = 0
mkdir namelist
foreach aa (`cat site`)
	cd ./$aa 
	ls|sort -n -k 2 -t'.' > ../namelist/$aa.nl	
  	awk '{print substr($0,10,2)}' ../namelist/$aa.nl > ../namelist/$aa.nl1
	awk -F: '{if($0>=80)printf "%d\n",$0-100;else print $0}' ../namelist/$aa.nl1 > ../namelist/$aa.nl2
	sort -n ../namelist/$aa.nl2	> ../namelist/$aa.yl
	#awk -v name=$aa -F: 'FNR==1{tmp=$0}END{printf("%4s %d %d %d\n",name,$tmp,$0,$0-$tmp)}' ../namelist/$aa.yl >> ../namelist/station.year
	awk -v name=$aa -F: 'FNR==1{tmp=$0}END{printf("%4s %d %d %d\n",name,tmp,$0,$0-tmp)}' ../namelist/$aa.yl >> ../namelist/station.year
	@ a = $a + 1
	echo $a
	cd ..
end 
