/*
* Project name : SPOJ: MINSTACK - Smallest on the Stack
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-16
* Description  :
* Status       : Accepted (23927580)
* Tags         : c++, stack, minimum value on stack
* Comment      :
*/

#include <iostream>
#include <cstdio>
#include <stack>

using namespace std;

int main(void) {
    int n;
    int val;
    char type_of_operation[10];
    stack<int> st;

    scanf("%d", &n);
    while (n--) {
        scanf("%s", type_of_operation);
        if (type_of_operation[1] == 'U') {
            scanf("%d", &val);
            st.push(st.empty() ? val: min(st.top(), val));
        } else if (type_of_operation[1] == 'O') {
            if (st.empty()) {
                puts("EMPTY");
            } else {
                st.pop();
            }
        }
        else {
            if (st.empty()) {
                puts("EMPTY");
            } else {
                printf("%d\n", st.top());
            }
        }
    }

    return 0;
}
