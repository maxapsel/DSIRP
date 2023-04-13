#include <iostream>
using namespace std;

void work_age(int age) {
	if (age > 16 && age < 65) {
        	cout << "age is within the normal working age." << endl;
    	}
}

int main() {
	work_age(18);
	return 0;
}
