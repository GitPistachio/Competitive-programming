# Project name : SPOJ: Transform the expression
# Author       : Wojciech Raszka
# Date created : 2019-02-10
# Description  :
# Status       : Accepted (23205239)
# Comment      :

PNToRPN <- function(exp){
  cout <- character(length(exp))
  s <- character(length(exp))

  j = 1
  i = 1
  for (e in unlist(strsplit(exp, ""))){
    if (e %in% letters){
      cout[i] = e
      i = i + 1
    } else if (e == "-" || e == "+") {
      while (j > 1 && s[j - 1] != "("){
        j = j - 1
        cout[i] = s[j]
        i = i + 1
      }
      s[j] = e
      j = j + 1
    } else if (e == "*" || e == "/") {
      while (j > 1 && !(s[j - 1] %in% c("(", "+", "-"))){
        j = j - 1
        cout[i] = s[j]
        i = i + 1
      }
      s[j] = e
      j = j + 1
    } else if (e == "^") {
      while (j > 1 && s[j - 1] == "^"){
        j = j - 1
        cout[i] = s[j]
        i = i + 1
      }
      s[j] = e
      j = j + 1
    } else if (e == "(") {
      s[j] = e
      j = j + 1
    } else if (e == ")") {
      while (j > 1 && s[j - 1] != "("){
        j = j - 1
        cout[i] = s[j]
        i = i + 1
      }
      j = j - 1
    }
  }
  write(paste(cout, collapse=""), stdout())
}

f <- file('stdin', open='r')

no_of_exp <- as.integer(readLines(f, n=1))

for (i in 1:no_of_exp){
  PNToRPN(readLines(f, n=1))
}
