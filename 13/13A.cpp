#include <iostream>
#include <sstream>

using namespace std;

int main() {
    int scanner_ranges[100];
    for(int i = 0; i<100; ++i) {
        scanner_ranges[i] = 0;
    }
    string line;
    while(getline(cin, line)) {
        istringstream iss;
        cout << line << endl;
        string first, second;
        iss >> first >> second;
        cout << first << second << endl;
        // okay I don't know how to do this input in C++
        // rip
    }

    int total = 0;
    for(int time = 0; time < 100; ++time) {
        if(scanner_ranges[time] != 0 && time % scanner_ranges[time] != 0) {
            total++;
        }
    }
    cout << total << endl;
}
