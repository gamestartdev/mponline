#!/bin/sh
#install with "crontab crontab-entry.txt"

ps auxw | grep java | grep -v grep > /dev/null

if [ $? != 0 ]
then
	cd ~/mponline/server
	touch cron-was-here.txt
	screen -dmS minecraft-server java -jar CanaryMod-1.2.0.jar
else
	echo "detected java running. not starting server."
fi
