#!/bin/bash
#this script displays the size of the body of the response of a request url.
curl "$1" -sI | grep "Length" | cut -d " " -f2
