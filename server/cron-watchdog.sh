#!/bin/sh
#install with crontab -e
#*/10 * * * * /home/ubuntu/mponline/server/cron-watchdog.sh


export CANARY_ROOT="/home/ubuntu/mponline/server/"

ps auxw | grep CanaryMod | grep -v grep > /dev/null


if [ $? != 0 ]
then
	cd $CANARY_ROOT
        python start-server.py
fi
