#include <iostream>
using namespace std;

int addTwo(const int num) {
	num += 2;
	return num;
}

int main() {
	addTwo(4);
	return 0;
}

/* const_param.cpp:5:6: error: cannot assign to variable 'num' with const-qualified type 'const int'
        num += 2;
        ~~~ ^
const_param.cpp:4:22: note: variable 'num' declared const here
int addTwo(const int num) {
           ~~~~~~~~~~^~~
1 error generated. */
