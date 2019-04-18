#!/bin/bash

# Project name : SPOJ: Test 1
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-13
# Description  :
# Status       : Accepted (23629481)
# Tags         : bash
# Comment      :

DONE=false
until $DONE; do

    read item || DONE=true

    if [ $item != "" ]; then
        if [[ $item = *i* ]]; then
            echo N
        else
            echo S
        fi
    fi
done
