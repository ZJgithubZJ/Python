#!/bin/bash
for webip in `cat iplist.txt | awk '{print $2}'`
do
	line=`cat iplist.txt | grep $webip`
	echo '----------------split line ------------------'
	fab -H $webip all-task
	echo $line done!
	echo -e "\n"
done
