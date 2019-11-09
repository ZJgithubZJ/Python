#!/bin/bash
for webip in `cat iplist.txt | awk '{print $2}'`
do
	name=`cat iplist.txt | grep $webip | awk '{print $1}'`
	fab -H $webip webtask
	echo $name done!
done
