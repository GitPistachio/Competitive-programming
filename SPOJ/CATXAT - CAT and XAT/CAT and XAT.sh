#!/bin/bash

# Project name : SPOJ: CATXAT - CAT and XAT
# Author       : Wojciech Raszka
# Date created : 2019-03-31
# Description  :
# Status       : Accepted (23537643)
# Tags         : bash
# Comment      :

LETTERS=(A B C D E F G H I J K L M N O P Q R S T U V W X Y Z)

function getCode(){
	if [ $1 == " " ]; then
		echo ""
	else
		j=0
		while [ ${LETTERS[j]} != $1 ]
		do
		  ((j++))
		done
		echo ${LETTERS[(j+23)%26]}${LETTERS[(j+4)%26]}
	fi
}

read T

for ((t = 0; t < T; t++))
do
  read s
  ts=""
  for ((i = 0; i < ${#s}; i++ ))
  do
	ts=$ts$(getCode "${s:$i:1}")
  done
  echo $ts
done
