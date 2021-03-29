/*
* Project name : SPOJ: BUET19 - Map
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 
* Description  :
* Status       : 
* Tags         : c++
* Comment      : 
*/

#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

int main() {
	int N;

  cin >> N;
  set<int> IDs;
  if (N == 1) {
  	cout << 1 << endl;
  }
  else{
  	bool display;
  	int no_of_unique_id = 0;
  	int id;
  	for (int i=0; i<N; i++){
  		display = true;
  		cin >> id;

  		IDs.insert(id);
  	}
  	cout << IDs.size() << endl;
  }

  return 0;
}
