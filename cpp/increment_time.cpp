#include <iostream>
using namespace std;

struct Time {
    int hour, minute;
    double second;
    void print();
    void increment(double secs);
};

void Time::to_string()
{
    Time time = *this;
    string output = time.hour + ":" + time.minute + ":" + time.second;
    return output;
}

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

void Time::increment(double secs)
{
    second += secs;
    int minutes = hour * 60 + minute;
    double seconds = minutes * 60 + second;

    hour = int(seconds / 3600.0);
    seconds -= hour * 3600.0;
    minute = int(seconds / 60.0);
    seconds -= minute * 60;
    second = seconds;
}

int main () {
	Time time = {11, 59, 3.14159};
	increment(time, 142.2);
	cout << time.hour << "hr" << time.minute << "min" << time.second << "s" << endl;
	time.increment(500.2);
	cout << time.hour << "hr" << time.minute << "min" << time.second << "s" << endl;

	return 0;
}
