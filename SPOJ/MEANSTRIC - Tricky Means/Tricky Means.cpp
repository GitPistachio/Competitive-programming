/*
* Project name : SPOJ: MEANSTRIC - Tricky Means
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2023-04-21
* Description  :
* Status       : Accepted (31240034)
* Tags         : c++, math, arithmetic mean, harmonic mean, geometric mean
* Comment      :
*/

#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double arithmeticMean(double A[], int n){
  double sum_of_elements = 0;
  
  for(int i = 0; i < n; i++){
  	sum_of_elements += A[i];
  }

  return sum_of_elements/n;
}

double geometricMean(double A[], int n){
  double product_of_elements = 1;
  
  for(int i = 0; i < n; i++){
  	product_of_elements *= A[i];
  }

  return pow(product_of_elements, 1./n);
}

double harmonicMean(double A[], int n){
  double sum_of_reciprocals = 0;
  
  for(int i = 0; i < n; i++){
  	sum_of_reciprocals += 1/A[i];
  }
  
  return n/sum_of_reciprocals;
}

int main() {
  int no_of_tests;
  int n;
  double am, ag, ah;
  double A[100];

  cout << fixed << setprecision(9);
  
  cin >> no_of_tests;
  
  for (int i = 0; i < no_of_tests; i++){
  	cin >> n;
  	
  	for (int j = 0; j < n; j++){
  		cin >> A[j];
  	}
  	
  	am = arithmeticMean(A, n);
  	ag = geometricMean(A, n);
  	ah = harmonicMean(A, n);
  	
  	
  	cout << am << ' ' << ag << ' ' << ah << endl;
  }
  
  return 0;
}