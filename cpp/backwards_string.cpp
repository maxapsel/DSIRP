#include <iostream>
#include <string>
using namespace std;

string backwards(string x) {
	string word;
	for (int i = x.length() - 1; i >= 0; i--) {
		word += x[i];
	}
	return word;
}

int main() {
	string word;
	cout << "Enter a string: ";
	cin >> word;
	string result = backwards(word);
	cout << result << endl;
	return 0;
}
