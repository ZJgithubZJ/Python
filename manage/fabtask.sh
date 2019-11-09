#!/bin/bash
for webip in `cat iplist.txt | awk '{print $2}'`
do
	name=`cat iplist.txt | grep $webip | awk '{print $1}'`
	#-H $webip默认是以当前登录用户登录的，如果你是非root用户执行指令，需要添加当前用户的公钥内容到目标主机认证，且这里需要修改为'-H root@$webip'
	fab -H $webip webtask	
	if [[ $? -eq 0 ]]; then
		echo $name done!
	else
		echo $name error!
	fi
done
