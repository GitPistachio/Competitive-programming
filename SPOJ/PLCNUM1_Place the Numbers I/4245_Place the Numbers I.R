# Project name : SPOJ: PLCNUM1 - Place the Numbers I
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 
# Description  :
# Status       : 
# Tags         : R
# Comment      :

f <- file('stdin', open='r')

N <- as.integer(readLines(f, n=1))

board <- matrix(, nrow=N, ncol=N)

board[1,] <- 1:N

if (N > 1){
  if ((N %% 2) == 0){
    rb <- N
  } else{
    rb <- N - 2
  }

  for (j in 1:rb){
    u <- j*(N - 1) + N
    l <- u - N + 2
    board[2:N, N - j + 1] <- if ((j %% 2) == 1) l:u else u:l
  }
}

if ((N %% 2) == 1){
  if (N > 3){
    board[seq(2, N, 2), 1] <- seq(N*N - 1, N*(N - 2) + 4, -4)
    board[seq(3, N, 2), 1] <- seq(N*N - 2, N*(N - 2) + 4, -4)
    board[seq(2, N, 2), 2] <- seq(N*N, N*(N - 2) + 3, -4)
    board[seq(3, N, 2), 2] <- seq(N*N - 3, N*(N - 2) + 3, -4)
  } else if (N == 3){
    board[2, 1] <- 8
    board[2, 2] <- 9
    board[3, 1] <- 7
    board[3, 2] <- 6
  }
}

write.table(board, file=stdout(), quote=FALSE, row.names=FALSE, col.names=FALSE)
