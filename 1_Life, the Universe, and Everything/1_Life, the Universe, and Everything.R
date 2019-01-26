f <- file('stdin', open='r')

for(ans in readLines(f)){
  if (ans == '42') break
  write(ans, stdout())
}