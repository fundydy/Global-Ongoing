#! /bin/bash
function read_dir(){
	mkdir $2
	cd $2
for file in `ls ../$1` #注意此处这是两个反引号，表示运行系统命令
  do
	name=${file:0:4}
	#echo $name
 	if [ -d $name ]
	then
		cp ../$1/$file ./$name/$file
		compress -d $name/$file
	else
		mkdir $name
		cp ../$1/$file ./$name/$file
		compress -d $name/$file
	fi
#在此处处理文件即可
  done

cd ..
} 

#读取第一个参数
read_dir $1 $2
