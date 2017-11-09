#!/bin/bash

if [ $# -eq 0 ]
  then
      echo "No arguments supplied"
else
    if [ -d $1 ]; then
	echo "Directory exists"
    else 
	mkdir $1
        cd $1
        touch $1.py
        mkdir templates
        mkdir static
        mkdir utils
        mkdir data
        cd utils
        touch __init__.py
        cd ..
    fi
fi
