#include <iostream>
using namespace std;

void loop_forever(int n) {
    while (true) {
        cout << "n is now " << n << "." << endl;
        n = n + 1;
    }
}

void recurse_forever(int n) {
    cout << "n is now " << n << "." << endl;
    recurse_forever(n + 1);
}

int main() {
	/*
	loop_forever(1);
	with loop forever, the program looped continuously and needed to be terminated for it to stop. */
	/*
	recurse_forever(1);
	with recurse forever, the program recursed 262020 times before reaching a segmentation fault because it tried to access memory that the program was not allowed to access, beyond its limits. */
	return 0;
}

