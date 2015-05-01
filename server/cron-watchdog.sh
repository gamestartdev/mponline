#!/bin/sh
#install with crontab -e
#*/1 * * * * /home/ubuntu/mponline/server/cron-watchdog.sh

ps auxw | grep java | grep -v grep > /dev/null

if [ $? != 0 ]
then
	cd ~/mponline/server
	touch cron-was-here.txt
	python start-server.py
fi
