#include <iostream>
#include <sstream>

using namespace std;

int main() {
    string line;
    int total = 0;
    while(getline(cin, line)) {
        istringstream iss(line);
        int curr_num, mn=99999, mx=0;
        while(iss >> curr_num) {
            mn = min(mn, curr_num);
            mx = max(mx, curr_num);
        }
        total += mx - mn;
    }
    cout << total << endl;
}
