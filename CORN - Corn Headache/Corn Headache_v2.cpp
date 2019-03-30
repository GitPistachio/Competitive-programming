/*
* Project name : SPOJ: CORN - Corn Headache
* Author       : Wojciech Raszka
* Date created : 2019-03-11
* Description  :
* Status       : Accepted (23385820)
* Comment      : More c-like style and shoud be slighly faster than previous solution
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
  int T;
  char buffer[100];
  char delim[] = "e";
  double R, S, H;
  const double PI = 3.1415;
  double P;

  scanf("%d", &T);

  for (int t = 0; t < T; t++){
    scanf("%s", buffer);
    R = atof(strtok(buffer, delim));
    S = atof(strtok(NULL, delim));
    H = atof(strtok(NULL, delim));

    P = PI*R*sqrt(R*R + H*H);
    printf("%i\n", int(ceil(P*S)));
  }

  return 0;
}
