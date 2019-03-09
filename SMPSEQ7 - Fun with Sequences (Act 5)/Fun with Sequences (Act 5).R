# Project name : SPOJ: SMPSEQ7 - Fun with Sequences (Act 5)
# Author       : Wojciech Raszka
# Date created : 2019-02-24
# Description  :
# Status       : Accepted (23291817)
# Comment      :

f <- file('stdin', open='r')

n <- as.integer(readLines(f, n=1))
S <- as.integer(unlist(strsplit(readLines(f, n=1), ' ')))

descending_order = TRUE
request_order = TRUE
for (i in 2:n){
  if (S[i] < S[i - 1] && !descending_order){
    request_order = FALSE
    break
  } else if (S[i] == S[i - 1]){
    if (descending_order){
      descending_order = !descending_order
    } else {
      request_order = FALSE
      break
    }
  } else if (S[i] > S[i - 1] && descending_order){
    descending_order = !descending_order
  }
}

if (request_order && !descending_order){
  write("Yes", stdout())
} else {
  write("No", stdout())
}
