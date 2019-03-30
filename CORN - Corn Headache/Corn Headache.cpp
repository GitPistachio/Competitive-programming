/*
* Project name : SPOJ: CORN - Corn Headache
* Author       : Wojciech Raszka
* Date created : 2019-03-09
* Description  :
* Status       : Accepted (23375635)
* Comment      :
*/

#include <iostream>
#include <bits/stdc++.h>
#include <boost/algorithm/string.hpp>
#include <string>
#include <cmath>

using namespace std;

int main(){
  int T;
  string RSH;
  vector<string> sRSH;
  double R, S, H;
  const double PI = 3.1415;
  double P;

  scanf("%d", &T);

  for (int t = 0; t < T; t++){
    cin >> RSH;
    boost::split(sRSH, RSH, boost::is_any_of("e"));
    R = strtod(sRSH[0].c_str(), 0);
    S = strtod(sRSH[1].c_str(), 0);
    H = strtod(sRSH[2].c_str(), 0);
    P = PI*R*sqrt(R*R + H*H);
    cout << int(ceil(P*S)) << endl;
  }

  return 0;
}
