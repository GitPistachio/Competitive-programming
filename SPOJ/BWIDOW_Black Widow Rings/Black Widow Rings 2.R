# Project name : SPOJ: BWIDOW - Black widow rings
# Author       : Wojciech Raszka
# Date created : 2019-02-08
# Description  :
# Status       : 
# Comment      : It's solve more complicated problem. When for each ring one ring have to be in another one. Think of it as filling gaps in half-line where the ring r R fill inverval [r, R].


f <- file('stdin', open='r')

T = as.integer(readLines(f, n=1))

for (t in 1:T){
  N = as.integer(readLines(f, n=1))
  half_line = logical(10000000)
  distraction_ring = -1
  max_inner_radius = 1

  for (n in 1:N){
    ring <- as.integer(unlist(strsplit(readLines(f, n=1), ' ')))
    inv <- seq(ring[1], ring[2] - 1, by=1)
    if (any(half_line[inv])){
      write(-1, stdout())
      distraction_ring = -1
      break
    } else {
      half_line[inv] = TRUE
      if (ring[1] > max_inner_radius){
        max_inner_radius = ring[1]
        distraction_ring = n
      }
    }
  }
  if (distraction_ring > 0){
    write(distraction_ring, stdout())
  }
}
