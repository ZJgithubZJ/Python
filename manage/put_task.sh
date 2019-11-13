#!/bin/bash
for webip in `cat iplist.txt | awk '{print $2}'`
do
	line=`cat iplist.txt | grep $webip`
	echo '----------------split line ------------------'
	fab -H $webip put-task
	echo $line done!
	echo -e "\n"
done
