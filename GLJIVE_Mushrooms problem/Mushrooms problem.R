# Project name : SPOJ: Triple fat ladies
# Author       : Wojciech Raszka
# Date created : 2019-02-06
# Description  :
# Status       : Accepted (23186730)
# Comment      :


f <- file('stdin', open='r')

sum_of_points = 0
last_no_of_points = 0
for (i in 1:10){
  no_of_points = as.integer(readLines(f, n=1))

  if (abs(100 - sum_of_points - no_of_points) <= abs(100 - sum_of_points)){
    sum_of_points = sum_of_points + no_of_points
    last_no_of_points = no_of_points
    if (100 < sum_of_points) break;
  }
  else break;
}

write(sum_of_points, stdout())
