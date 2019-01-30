library('stringi')

f <- file('stdin', open='r')

no_of_cases <- as.integer(readLines(f, n=1))

for (i in 1:no_of_cases){
  n <- as.integer(stri_reverse(as.character(sum(as.integer(stri_reverse(unlist(strsplit(readLines(f, n=1), ' '))))))))
  write(n, stdout())
}
