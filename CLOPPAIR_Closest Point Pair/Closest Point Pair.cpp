/*
* Project name : SPOJ: Closest point pair
* Author       : Wojciech Raszka
* Date created : 2019-02-09
* Description  :
* Status       : Accepted (23201679)
* Comment      : O(N^2)
*/

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;
struct Point{
	long long x;
	long long y;
	long long idx;
};

bool operator <(const Point& x,const Point& y){
	return x.x < y.x;
}

long long dist(long long x1,long long y1,long long x2,long long y2){
	return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
}

int main(){
  int a, b, n;
	long long d, h;
  Point P[50000];
	scanf("%lld",&n);

  for(int i=0; i < n;i++){
		scanf("%lld%lld",&P[i].x,&P[i].y);
		P[i].idx=i;
	}
	sort(P,P + n);
	h = 10000000000000;

  for(int i=0; i < n - 1; i++)
		for(int j=i+1; j < n; j++){
			if (P[j].x - P[i].x > h)
				break;
			d = dist(P[i].x, P[i].y, P[j].x, P[j].y);
			if(d < h)
			{
				a = P[i].idx;
				b = P[j].idx;
				h = d;
			}
		}
	if(a > b)
		swap(a, b);

	printf("%lld %lld %.6f", a, b,sqrt((double)h));
	return 0;
}
