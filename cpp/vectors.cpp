#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

vector<int> random_vector(int n, int upper_bound)
{
    vector<int> vec(n);

    for (int i = 0; i < vec.size(); i++) {
        vec[i] = rand() % upper_bound + 1;
    }

    return vec;
}

void print_vector(const vector<int>& vec)
{
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }
}

int main () {
	print_vector(random_vector(10, 10));	
	return 0;
}
