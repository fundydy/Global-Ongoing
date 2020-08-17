#!/bin/tcsh -f
#runing under poscov dir
#USAGE: tm.sh
#generate $site_original.ps and $site_corrected.ps to ps dir
set path0=`pwd`
cd $path0
#rm *.pfiles
rm *.ps
set length=`wc -l site`
set k=0
rm tslog
foreach site0 (`cat ./site`)
	set site = `echo $site0 | tr "[a-z]" "[A-Z]"`
	timeseries_fang -d -s $site>>tslog
	cp $site.pfiles ${site}_original.pfiles
#all para
	#list_pfile_outliers_fang -station $site -limits -200 200 -sr 1500 -rf>>tslog	
	list_pfile_outliers_fang -station $site -limits -200 200 -sr 1500 -rf>>tslog	
#lhas para1
	#list_pfile_outliers_fang -station $site -limits -250000 250000 -sr 250000 -rf>>tslog	
	#list_pfile_outliers_fang -station $site -limits -60 60 -sr 1000 -rf>>tslog	
	mv $site.pfilescorrected $site.pfiles
	timeseries_fang -d -co -final -s $site>>tslog
	paste -s *.vel>allsite.vel
	@ k = $k + 1
	echo $site"["$k"/"$length"]"
	cp *.ps ../ps
end

