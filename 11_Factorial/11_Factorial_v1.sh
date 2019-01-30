#!/bin/bash
#This is to slow for SPOJ but works on Ideone.com nicely.

Z()
{
  d=5
  no_of_zeros=0
  while [ $d -le $1 ]
  do
	no_of_zeros=$(($no_of_zeros + $1/$d))
	d=$(($d*5))
  done
  echo $no_of_zeros
}

read T
for  ((i=1; i<=$T; i++))
do
  read n
  Z $n
done
