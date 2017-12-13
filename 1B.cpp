#include <iostream>

using namespace std;

int main() {
    string in; cin >> in;
    int n = in.length();
    int total = 0;
    for(int i = 0; i<n; ++i) {
        if(in[i] == in[(i+n/2) % n]) {
            total += in[i]-'0';
        }
    }
    cout << total << endl;
}
