#!/bin/sh

#########################################################################################
# Author: Mino Cha									
# Date: 2024-Feb-24									
# Description: This script takes in input for FILENAME and DURATION to capture packets.
#			   Also automatically opens and closes Spotify application.
#########################################################################################

##########################
# HOW TO USE THIS SCRIPT:	
##########################################################################################
# 1. on the terminal, type:								 
# 	source capture_packets.sh							 
# 2. After running the command above, it will ask for the parameters:			 
# 	3. Type FILENAME without .pcap							 
# 	4. Type DURATION in seconds (if 0, you choose to manually stop)			  
##########################################################################################


echo "Output .pcap filename:"
read FILENAME

echo "Duration (in seconds):"
read DURATION

sudo tcpdump -i en0 -w "$FILENAME.pcap" &
TCPDUMP_PID=$!

# open spotify
echo "Open Spotify application..."
open -a Spotify


if [ "$DURATION" -eq 0 ]; then
	echo "Ctrl+C to stop manually"
	trap "echo Stopping tcpdump and Spotify...; osascript -e 'tell application \"Spotify\" to quit'; sudo kill $TCPDUMP_PID;" SIGINT
	wait
else
	echo "Stopping after $DURATION seconds..."
	sleep $DURATION
	echo "Close Spotify application..."
	osascript -e 'tell application "Spotify" to quit'
	sudo kill $TCPDUMP_PID	
fi

# open .pcap
# sudo tcpdump -nnttr "$FILENAME.pcap"
