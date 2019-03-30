# Project name : SPOJ: TEST - Life, the Universe, and Everything
# Author       : Wojciech Raszka
# Date created :
# Description  :
# Status       : Accepted (???)
# Tags         : R
# Comment      :

f <- file('stdin', open='r')

for(ans in readLines(f)){
  if (ans == '42') break
  write(ans, stdout())
}
