/*
* Project name : SPOJ: BINARYIO - Binary Input and Output
* Author       : Wojciech Raszka
* Date created : 2019-03-10
* Description  :
* Status       : Accepted (23379792)
* Comment      :
*/

#include <stdio.h>
#include <math.h>

int main(){
  double x;

  while (fread(&x, sizeof(x), 1, stdin) == 1){
    x = log(x);
    fwrite(&x, sizeof(x), 1, stdout);
  }

  return 0;
}
