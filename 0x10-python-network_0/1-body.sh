#!/bin/bash
#this script sends a GET request to the URL, and displays the body of the response.
curl -sLX GET "$1"
