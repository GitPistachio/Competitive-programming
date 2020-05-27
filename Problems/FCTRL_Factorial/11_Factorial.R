Z <- function(n){
  d <- 5
  no_of_zeros <- 0
  while (d <= n){
    no_of_zeros = no_of_zeros + n%/%d
    d = d*5
  }
  return (as.integer(no_of_zeros))
}

f <- file('stdin', open='r')

T = as.integer(readLines(f, n=1))
N = integer(T)
for (n in 1:T){
  write(Z(as.integer(readLines(f, n=1))), stdout())
}
