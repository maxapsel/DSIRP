#include <iostream>
#include <string>
using namespace std;

void countLetters(string word, char letter) {
	int count = 0;
	int index = 0;

	while (index < word.length()) {
    		if (word[index] == letter) {
        		count = count + 1;
    		}
    		index = index + 1;
	}
	cout << count << endl;
}

int main() {
	string word;
	char letter;
	
	cout << "Enter a word: ";
	cin >> word;
	cout << "Enter a letter: ";
	cin >> letter;
	countLetters(word, letter);
	return 0;
}
