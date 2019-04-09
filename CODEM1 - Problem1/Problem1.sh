#!/bin/bash

# Project name : SPOJ: CODEM1 - Problem1
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-03-09
# Description  :
# Status       : Accepted (23370367)
# Tags         : bash
# Comment      : The question should be: Is it possible to determine if sum of given three numbers is positive, negative or 0

function NVL {
    if [ $1 == '$' ] && [ $2 == '$' ]; then
      echo $3
    elif [ $1 == '$' ]; then
      echo $2
    else
      echo $1
    fi
}

read T

for ((t = 0; t < $T; t++))
do
  read l
  a=$(echo $l | cut -c1)
  b=$(echo $l | cut -c2)
  c=$(echo $l | cut -c3)

  ma=$(NVL $a $b $c)
  mb=$(NVL $b $c $a)
  mc=$(NVL $c $a $b)

  if [ $ma == $mb ] && [ $mb == $mc ]; then
    echo possible
  else
    echo trivial
  fi
done
