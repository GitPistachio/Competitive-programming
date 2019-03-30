/*
* Project name : SPOJ: BINARYIO - Binary Input and Output
* Author       : Wojciech Raszka
* Date created : 2019-03-10
* Description  :
* Status       : Accepted (23379855)
* Comment      :
*/

#include <stdio.h>
#include <math.h>

int main(){
  const int MAX_SIZE = 1000000;
  double x[MAX_SIZE];

  size_t no_of_ret = fread(x, sizeof *x, MAX_SIZE, stdin);
  for (int i = 0; i < no_of_ret; i++){
      x[i] = log(x[i]);
  }

  fwrite(x, sizeof *x, no_of_ret, stdout);

  return 0;
}
