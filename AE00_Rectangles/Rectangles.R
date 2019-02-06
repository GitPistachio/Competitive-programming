f <- file('stdin', open='r')

N = as.integer(readLines(f, n=1))

no_of_rectangles = N

root_of_N = as.integer(sqrt(N))
i = 2
while (i <= root_of_N){
    for (j in i:as.integer(N/i)){
      no_of_rectangles = no_of_rectangles + 1
    }
  i = i + 1
}

write(no_of_rectangles, stdout())
