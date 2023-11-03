# Meraki-API-Examples
This repository contains some example on how to use the API calls in an actual Python script.

# How to run
Run the Meraki_API_Calls.py file
You'll be asked for your API key generated from the Meraki dashboard. Enter it.  
A list of all your available organizations will be displayed. Enter the index for the one you wish to run the script against.  
A similar list with all the networks available in the selected organization will be displayed. Enter the index for one of them.  
All of the API calls available in this script will be run for that network.  

# Notes
If you do not want to run all of the API calls, just locate the lines where they are called in the main script and comment them.  
Depending on what devices are in the selected network and its config, some of the API calls might return with no information.  
