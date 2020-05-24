/*
* Project name : SPOJ: CLOPPAIR - Closest point pair
* Link         : https://www.spoj.com/problems/CLOPPAIR/
* Author       : Wojciech Raszka
* E-mail       : spoj@gitpistachio.site
* Date created : 2019-02-09
* Description  :
* Status       : Accepted (23201679)
* Tags         : c++, closest pair of points
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
	/* Compare points by its x coordinate. */
	return x.x < y.x;
}

long long dist(long long x1,long long y1,long long x2,long long y2){
	/* Calculate square of Euclidean distance between points (x1, y1) and (x2, y2). */
	return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
}

int main(){
  int a, b, n;
  long long d, h;
  Point P[50000];
  scanf("%lld",&n); // number of points

  for(int i=0; i < n;i++){ // reads points to table P
		scanf("%lld%lld",&P[i].x,&P[i].y);
		P[i].idx=i;
	}
	sort(P,P + n); // sort points by its x coordinate
	h = 10000000000000; // initial minimum distance between points

  for(int i=0; i < n - 1; i++) // find the minimum distance between points, check distances of all points pairs
		for(int j=i+1; j < n; j++){
			if (P[j].x - P[i].x > h) // points are sorted by x coordinate, thus if distance between x coordinate of j-point and i-point is greater than h so the j+1, j+2, ... points is greater
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
