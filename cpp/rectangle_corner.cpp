#include <iostream>
using namespace std;

struct Point {
    double x, y;
};

struct Rectangle {
    Point corner;
    double width, height;
};

Point lowerRight(Rectangle& rect) {
	double x = rect.corner.x + rect.width;
	double y = rect.corner.y - rect.height;
	Point result = {x,y};
	return result;
}

int main() {
	Rectangle rect = {{10, 10}, 10, 10};
	Point p = lowerRight(rect);	
	cout << "(" << p.x << ", " << p.y << ")" << endl;
	return 0;
}
