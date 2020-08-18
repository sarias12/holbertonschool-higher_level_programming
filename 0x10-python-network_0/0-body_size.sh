#!/bin/bash
#this script displays the size of the body of the response of a request url.
curl 0.0.0.0:5000 -sI | grep "Length" | cut -d " " -f2
