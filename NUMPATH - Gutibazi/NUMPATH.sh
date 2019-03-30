#!/bin/bash

# Project name : SPOJ: NUMPATH - Gutibazi
# Author       : Wojciech Raszka
# Date created : 2019-03-22
# Description  :
# Status       : Accepted (23476899)
# Tags         : bash, game theory, dynamic programming
# Comment      :

MAX_N=7

for ((i=0; i<2*$MAX_N; i++))
do
	arr[i*2*$MAX_N]=1
	arr[i]=1
done

for ((i=1; i<2*MAX_N; i++))
do
	for ((j=1; j<2*$MAX_N-i; j++))
	do
		arr[i*2*MAX_N+j]=$((${arr[i*2*MAX_N+j - 1]} + ${arr[(i-1)*2*MAX_N+j]}))
	done
done


read T

for ((i=0; i<$T; i++))
do
	read r c
	echo ${arr[(r-1)*2*MAX_N+c-1]}
done
