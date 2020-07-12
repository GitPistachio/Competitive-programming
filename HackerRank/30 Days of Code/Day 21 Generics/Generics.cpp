/*
* Project name : HackerRank: Day 21: Generics
* Link         : https://www.hackerrank.com/challenges/30-generics/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2020-07-10
* Description  :
* Status       : Accepted (168243218)
* Tags         : c++
* Comment      : 
*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/


template <class T>
void printArray(vector<T> v){
    for(int i = 0; i != v.size(); ++i){
        cout << v[i] << endl;
    }
}

int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}