/*
* Project name : SPOJ: HAMSTER1 - Hamster flight
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-04-05
* Description  :
* Status       : Accepted (23579542)
* Tags         : c++, physics, projectile motion, ternary search, unimodal function
* Comment      : Hmax = v^2*sin(2*alpha)/(2*g); Z = v^2*sin(2*alpha)/g
*/

#include <stdio.h>
#include <math.h>

inline double getMaxDistance(double v_0, double alpha, double g){
  return v_0*v_0*sin(2*alpha)/g;
}

inline double getMaxHeight(double v_0, double alpha, double g){
  double t = sin(alpha);
  return v_0*v_0*t*t/(2*g);
}

inline double getScore(double v_0, double alpha, double g, double k1, double k2){
  return k1*getMaxDistance(v_0, alpha, g) + k2*getMaxHeight(v_0, alpha, g);
}

inline double solveTernary(double v_0, double g, double k1, double k2){
  double m1, m2, l = 0.7853981633, r = 1.57079632;
  double m1_score, m2_score, alpha;

  if (k1 == 0.0)
    return r;
  if (k2 == 0.0)
    return l;

  while (abs(r - l) > 0.0002){
    m1 = l + (r - l)/3;
    m2 = r - (r - l)/3;
    m1_score = getScore(v_0, m1, g, k1, k2);
    m2_score = getScore(v_0, m2, g, k1, k2);

    if (m1_score < m2_score){
      l = m1;
    } else {
      r = m2;
    }
  }
  return (l + r)/2;
}

int main(){
    int T;
    double alpha, score;
    double v_0, k1, k2, g = 10;
    scanf("%d", &T);

    while (T-- > 0){
      scanf("%lf %lf %lf", &v_0, &k1, &k2);
      alpha = solveTernary(v_0, g, k1, k2);
      printf("%.3lf %.3lf\n", alpha, getScore(v_0, alpha, g, k1, k2));
    }
    return 0;
}
