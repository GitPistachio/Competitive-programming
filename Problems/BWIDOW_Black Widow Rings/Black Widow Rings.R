# Project name : SPOJ: Black widow rings
# Author       : Wojciech Raszka
# Date created : 2019-02-09
# Description  :
# Status       : Accepted (23197915)
# Comment      :


f <- file('stdin', open='r')

T = as.integer(readLines(f, n=1))

for (t in 1:T){
  N = as.integer(readLines(f, n=1))
  dr = -1
  dr_ir = 1
  dr_or = 2
  slr_or = 2

  for (n in 1:N){
    ring <- as.integer(unlist(strsplit(readLines(f, n=1), ' ')))
    if (ring[1] > dr_ir){
      dr = n
      dr_ir = ring[1]
      if (dr_or > slr_or){
        slr_or = dr_or
      }
      dr_or = ring[2]
    } else if(ring[2] > slr_or){
      slr_or = ring[2]
    }
  }
  if (slr_or <= dr_ir){
    write(dr, stdout())
  } else {
    write(-1, stdout())
  }
}
