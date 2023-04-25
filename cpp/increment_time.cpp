#include <iostream>
using namespace std;

struct Time {
    int hour, minute;
    double second;
};

double convert_to_seconds(const Time& t)
{
    int minutes = t.hour * 60 + t.minute;
    double seconds = minutes * 60 + t.second;

    return seconds;
}

Time make_time(double secs)
{
    Time time;
    time.hour = int(secs / 3600.0);
    secs -= time.hour * 3600.0;
    time.minute = int(secs / 60.0);
    secs -= time.minute * 60;
    time.second = secs;

    return time;
}

void increment(Time& time, double secs)
{
    time.second += secs;
    time = make_time(convert_to_seconds(time));
}

int main () {
	Time time = {11, 59, 3.14159};
	increment(time, 142.2);
	cout << time.hour << "hr" << time.minute << "min" << time.second << "s" << endl;
	return 0;
}
