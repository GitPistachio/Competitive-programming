/*
* Project name : SPOJ: MATCHSTR - Tìm xâu 01
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2019-04-10
* Description  :
* Status       : Accepted (23614796)
* Tags         : c++, string pattern, sliding window technique, pattern match, substring in a string
* Comment      : 100 score
*/

#include <iostream>
using namespace std;

int main() {
  string s, t;
  int no_of_occ = 0;
  bool occured;

  cin >> s;
  cin >> t;

  for (int i = 0; i < s.length(); i++){
    occured = true;
    if (s.length() - i >= t.length()){
      for (int j = 0; j < t.length(); j++){
        if (t[j] != s[i + j]){
          occured = false;
          break;
        }
      }
    } else {
      occured = false;
    }
    if (occured == true){
        no_of_occ++;
    }
  }
  cout << no_of_occ << endl;
	return 0;
}
