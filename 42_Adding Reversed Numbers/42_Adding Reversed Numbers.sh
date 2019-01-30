#This is to slow for SPOJ but works on Ideone.com nicely.

read no_of_cases

for ((i=1; i<=$no_of_cases; i++))
do
  read pair_of_numbers

  z=$(echo $pair_of_numbers | rev)

  a=$(cut -d' ' -f1 <<< $z)
  b=$(cut -d' ' -f2 <<< $z)
  rs=$(echo $(($a+$b)) | rev)

  echo $rs | sed 's/^0*//'
done
