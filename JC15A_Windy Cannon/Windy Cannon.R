# Project name : SPOJ: JC15A - Windy Cannon
# Author       : Wojciech Raszka
# Date created : 2019-02-20
# Description  :
# Status       : Accepted (23267897)
# Comment      :

options(digits=10)

timeToHitTarget <- function(CP, TP, CBS, WS, WD){
  if (TP == CP){
    return (0)
  }

  CS = "L"
  if (TP < CP){
    CS = "R"
  }

  if (CS == "L"){
    s <- TP - CP
  } else {
    s <- CP - TP
  }

  if (WD == "L" && CS == "L"){
    v <- CBS - WS
  } else if (WD == "R" && CS == "R"){
    v <- WS - CBS
  } else {
    v <- WS + CBS
  }

  if (v <= 0){
    return (-1)
  } else {
    return (s/v)
  }
}

f <- file('stdin', open='r')

inp <- unlist(strsplit(readLines(f, n=1), ' '))

CP = as.integer(inp[1])
TP = as.integer(inp[2])
CBS = as.integer(inp[3])
WS = as.integer(inp[4])
WD = inp[5]

t <- format(round(timeToHitTarget(CP, TP, CBS, WS, WD), 6), nsmall=6)

if (t < 0){
  write('Impossible', stdout())
} else{
    write(t, stdout())
}
