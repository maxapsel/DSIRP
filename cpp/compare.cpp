#include <iostream>
using namespace std;

void compare(int a, int b) {
	if (a > b) {
		cout << "a is greater than b" << endl;
	} else if (b > a) {
		cout << "b is greater than a" << endl;
	} else {
		cout << "a is equal to b" << endl;
	}
}

int main() {
	compare(3, 1);
	return 0;
}
