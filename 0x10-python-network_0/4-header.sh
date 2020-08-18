#!/bin/bash
#This script takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sX GET -sH 'X-HolbertonSchool-User-Id: 98' "$1"
